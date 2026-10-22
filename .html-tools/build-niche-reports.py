#!/usr/bin/env python3
"""
Generate customer-facing DOCX, HTML, and PDF reports for the framework
runbooks that are Markdown-first in this repository.

The DOCX and HTML outputs use pandoc. The PDF output intentionally uses a small
stdlib-only writer so the repo does not require LaTeX, wkhtmltopdf, or reportlab.

Each framework entry carries an explicit topic-to-CSW-capability map and an
evidence-collection table so the report mirrors what an SE / assessor would
actually need rather than a generic bullet list. Specific CSW UI navigation is
intentionally not included; framework-specific CSW UI paths are on the Cisco
product roadmap, and this report references CSW capabilities and the evidence
artifacts they produce.
"""

from __future__ import annotations

import re
import subprocess
import tempfile
import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / ".html-tools"
CSS = TOOLS / "style.css"


# Per-framework metadata.
#
# Field reference:
#   folder            : sub-directory under the repo root
#   title             : title used by pandoc and on the rendered title page
#   stem              : filename stem for the three generated outputs
#   standard          : full framework name (with version where applicable)
#   version_note      : explicit version / publication caveat shown in the report
#   audience          : who this report is for
#   driver            : one-line description of CSW positioning for this framework
#   scope_pattern     : suggested CSW root-scope tree (rendered as a fenced block)
#   in_scope          : framework topic areas where CSW produces evidence
#   out_of_scope      : framework topic areas CSW does not address (transparency)
#   topic_map         : list of (framework_topic, csw_capability, evidence_artifact)
#   evidence_collection: list of (topic, what_to_collect, csw_source, cadence)
#   boundaries        : prose paragraph summarising what CSW does not replace
#   runbook_filename  : technical runbook filename in the same folder
#
# All control IDs / paragraph references / section numbers in topic_map and
# evidence_collection are written against the framework version stated in
# version_note. If the customer is assessed against a different version, validate
# before using these references for formal evidence.
FRAMEWORKS = [
    {
        "folder": "MAS-TRM",
        "title": "Cisco Secure Workload - MAS TRM Compliance Report",
        "stem": "CSW-MAS-TRM-Compliance-Report",
        "standard": "Monetary Authority of Singapore (MAS) Technology Risk Management Guidelines",
        "version_note": "References the MAS TRM Guidelines published January 2021 (current published version at the time of writing). Validate against the latest MAS publication before use in a supervisory or audit context.",
        "audience": "Singapore-licensed financial institutions (banks, finance companies, insurers, capital markets services licensees, payment services licensees) using MAS TRM as the technology risk baseline.",
        "driver": "Critical-system segmentation, technology-asset evidence, outsourcing visibility, vulnerability context, monitoring, and incident scoping.",
        "scope_pattern": "MAS-TRM\n├── Critical-Systems (Digital-Banking, Payments, Trading, Core-Platforms)\n├── Customer-Data (Data-Stores, Analytics)\n├── Security-Services (Identity-Adjacent, Monitoring, Patch-Management)\n└── Outsourced-Third-Parties",
        "in_scope": [
            "Technology Risk Management Framework (asset inventory, classification)",
            "Access Control (workload-to-workload allowlist)",
            "Data and Infrastructure Security (segmentation, plaintext-flow detection)",
            "Cyber Security Operations (telemetry, alerts, forensic search)",
            "Cyber Security Assessment (CVE + reachability)",
            "Management of IT Services / Outsourcing (third-party egress visibility)",
            "IT Audit (evidence pack inputs)",
        ],
        "out_of_scope": [
            "Governance and board oversight",
            "Cryptography module assurance",
            "Identity / privileged-access lifecycle",
            "Business continuity / disaster recovery testing",
            "Outsourcing due diligence and supplier assurance contracts",
            "MAS reporting / notification decisions",
        ],
        "topic_map": [
            ("Technology asset inventory", "Workload inventory; scope + label export", "Inventory export reconciled to institution CMDB"),
            ("Information security risk assessment", "Vulnerability + reachability report", "Reachability-weighted exposure summary scoped to MAS-TRM"),
            ("Access control (network access layer)", "Policy workspace + enforcement log", "Workspace snapshot and violation/exception register"),
            ("Data security", "Plaintext-flow detection from observed flows", "List of unencrypted flows on customer-data paths"),
            ("Vulnerability management", "Reachability-weighted CVE evidence", "Prioritised remediation list with compensating-control register"),
            ("Security monitoring", "Continuous flow + process telemetry", "Alert and anomaly log scoped to Critical-Systems"),
            ("Cyber security operations / incident", "Forensic flow + process search", "Investigation pack covering affected workloads and time window"),
            ("Management of IT services / outsourcing", "Outbound flow summary to third-party endpoints", "Vendor-edge flow report reconciled against outsourcing register"),
            ("IT audit", "Periodic evidence pack", "Quarterly inventory, policy, vulnerability, incident-sample bundle"),
        ],
        "evidence_collection": [
            ("Critical-system inventory", "Inventory export with scope, labels, and lifecycle", "Workload inventory + scope membership export", "Monthly"),
            ("Approved vs. observed flows", "ADM output vs. enforced policy", "ADM workspace export", "Quarterly"),
            ("Policy enforcement evidence", "Workspace snapshot + violation log", "Policy workspace export and policy analysis output", "Quarterly + after each change"),
            ("Vulnerability + reachability", "CVE list weighted by reach into Critical-Systems", "Vulnerability report scoped to MAS-TRM", "Monthly"),
            ("Third-party egress reconciliation", "Outbound flow to vendor endpoints", "Flow search filtered to outsourced endpoints", "Monthly"),
            ("Incident sample", "Workload-level timeline for one representative incident", "Flow + process search", "Per incident; one representative sample per audit cycle"),
        ],
        "boundaries": "CSW does not replace MAS-level governance, board / senior-management accountability, the technology risk management framework, BCP/DR, IAM/PAM, cryptography programme decisions, outsourcing due diligence, or regulatory notification decisions.",
        "runbook_filename": "CSW-MAS-TRM-Reference-Design.md",
    },
    {
        "folder": "APRA-CPS-234",
        "title": "Cisco Secure Workload - APRA CPS 234 Compliance Report",
        "stem": "CSW-APRA-CPS234-Compliance-Report",
        "standard": "APRA Prudential Standard CPS 234 - Information Security",
        "version_note": "References CPS 234 as published in 2019. Paragraph numbers in this report are well-known and stable for CPS 234; if APRA has issued amendments or related standards in scope (e.g. CPS 230 Operational Risk Management), validate the applicable text.",
        "audience": "Australian banks, insurers, superannuation trustees, and other APRA-regulated entities; CISO function, technology risk, internal audit, and information asset owners.",
        "driver": "Information asset segmentation, control-implementation evidence, control-testing inputs, incident management, and third-party service-provider visibility.",
        "scope_pattern": "CPS-234\n├── Critical-Information-Assets (Customer-Records, Payments-and-Ledger, Trading-Settlement, Policy-and-Claims)\n├── Material-Operations (Online-Channels, Operational-Core)\n├── Service-Providers (Outsourced-Connectivity)\n└── Incident-Evidence",
        "in_scope": [
            "Para. 20 - Information asset identification and classification",
            "Para. 21-23 - Implementation of controls (network access layer)",
            "Para. 24-28 - Incident management (technical scoping)",
            "Para. 29-33 - Testing of control effectiveness (continuous, not point-in-time)",
            "Para. 34-35 - Internal audit (evidence pack inputs)",
        ],
        "out_of_scope": [
            "Para. 13-15 - Information security capability (governance)",
            "Para. 16-19 - Policy framework",
            "Para. 36-37 - APRA notification decision (CSW provides scoping inputs only)",
            "IAM/PAM, cryptography assurance, BCP/DR, supplier contractual arrangements",
        ],
        "topic_map": [
            ("Para. 20 - Asset identification and classification", "Workload inventory; scope + label export", "Inventory and scope membership export reconciled to information asset register"),
            ("Para. 21-23 - Controls implementation", "Policy workspace; ADM-derived allowlist", "Workspace snapshot and observed-vs-approved flow comparison"),
            ("Para. 21-23 - Third-party paths", "Outbound flow summary to service-provider endpoints", "Service-provider egress report"),
            ("Para. 24-28 - Incident management", "Forensic flow + process telemetry", "Investigation pack with timeline and impact scope"),
            ("Para. 29-33 - Control effectiveness testing", "Continuous flow data; policy-violation log; drift report", "Continuous control-testing evidence (replaces point-in-time samples)"),
            ("Para. 34-35 - Internal audit", "Periodic evidence pack", "Quarterly evidence bundle for audit work-papers"),
        ],
        "evidence_collection": [
            ("Information asset register reconciliation", "Workloads supporting each critical information asset", "Inventory + scope membership", "Quarterly"),
            ("Controls-implementation evidence", "Workspace snapshot and observed-vs-approved flow comparison", "Policy workspace export + ADM export", "Quarterly + after each change"),
            ("Control-effectiveness testing", "Continuous policy-violation and drift evidence", "Policy analysis output (continuous)", "Continuous, reviewed quarterly"),
            ("Third-party service-provider paths", "Outbound flow to vendor endpoints", "Flow search filtered to vendor endpoints", "Monthly"),
            ("Incident management sample", "One representative incident timeline", "Flow + process search", "Per incident; one representative sample per audit cycle"),
        ],
        "boundaries": "CSW does not replace board accountability for information security (Para. 13-14), the policy framework (Para. 16-19), related-party assurance, IAM/PAM lifecycle, cryptography programme decisions, BCP/DR test outcomes, or the APRA notification decision (Para. 36-37).",
        "runbook_filename": "CSW-APRA-CPS234-Reference-Design.md",
    },
    {
        "folder": "NY-DFS-23-NYCRR-500",
        "title": "Cisco Secure Workload - NY DFS Part 500 Compliance Report",
        "stem": "CSW-NYDFS-Compliance-Report",
        "standard": "NY DFS 23 NYCRR Part 500 (Second Amendment, effective 1 November 2023)",
        "version_note": "References 23 NYCRR Part 500 as amended in November 2023. Several requirements have phased transition dates through 2024-2025 (e.g. Sections 500.7, 500.13, 500.14, 500.15, 500.17). Validate the applicable effective date for each requirement against the DFS published rule.",
        "audience": "Covered entities under 23 NYCRR Part 500 (banks, insurance companies, licensed lenders, money transmitters, virtual-currency businesses, etc.); the CISO designated under Section 500.4, risk and audit leaders, and compliance teams preparing the annual notice of compliance.",
        "driver": "Covered workload visibility, NPI segmentation, access privilege evidence, monitoring, vulnerability management, audit trail, and incident scoping.",
        "scope_pattern": "NYDFS-500\n├── Covered-Systems (Customer-Channels, Account-and-Ledger, Payments-and-Settlement, Underwriting-Claims)\n├── NPI-Applications (Customer-Data-Stores, Analytics-on-NPI)\n├── Critical-Operations (Identity-Adjacent, Monitoring, Patch-Management)\n└── Third-Party-Service-Providers",
        "in_scope": [
            "Section 500.2 - Cybersecurity Program (technical inputs)",
            "Section 500.5 - Vulnerability Management (CVE + reachability)",
            "Section 500.6 - Audit Trail (workload network layer)",
            "Section 500.7 - Access Privileges and Management (workload-to-workload)",
            "Section 500.13 - Asset Management and Data Retention (workload inventory)",
            "Section 500.14 - Monitoring and Training (technical monitoring)",
            "Section 500.16 - Incident Response (forensic timeline)",
        ],
        "out_of_scope": [
            "Section 500.3 - Cybersecurity Policy (governance)",
            "Section 500.4 - CISO role",
            "Section 500.12 - MFA (identity layer)",
            "Section 500.15 - Encryption (CSW detects plaintext flows but does not enforce encryption)",
            "Section 500.17(a) - 72-hour notification decision (CSW provides scoping inputs only)",
            "Section 500.17(b) - Annual notice of compliance / senior officer certification (governance)",
        ],
        "topic_map": [
            ("Section 500.2 - Program operation", "Continuous workload telemetry + periodic evidence pack", "Quarterly evidence bundle demonstrating program operating across covered workloads"),
            ("Section 500.5 - Vulnerability management", "Reachability-weighted CVE evidence", "Prioritised remediation list with compensating controls"),
            ("Section 500.6 - Audit trail", "Workload flow + process telemetry retained per retention policy", "Retained flow telemetry for audit-trail purposes"),
            ("Section 500.7 - Access privileges", "Policy workspace + enforcement / violation log", "Workspace snapshot and least-privilege evidence at workload-to-workload layer"),
            ("Section 500.13 - Asset management", "Workload inventory; scope + label export", "Inventory and classification evidence"),
            ("Section 500.14 - Monitoring", "Continuous flow + process telemetry; alerts", "Monitoring evidence at network and process layer"),
            ("Section 500.15 - Encryption (detection)", "Plaintext-flow detection on regulated paths", "Detection input only - encryption itself is enforced elsewhere"),
            ("Section 500.16 - Incident response", "Forensic flow + process search", "Incident timeline and impact scope"),
            ("Section 500.17(a) - Notification scoping", "Affected-systems list with time windows and paths", "Scoping input to the 72-hour notification decision"),
        ],
        "evidence_collection": [
            ("Covered workload inventory", "Information systems in scope of Part 500", "Inventory + scope membership export", "Monthly"),
            ("NPI scope evidence", "Workloads handling nonpublic information", "Scope + label export filtered by data_class=npi", "Monthly"),
            ("Audit-trail retention", "Workload flow + process telemetry for the required window", "Retained telemetry export", "Continuous, validated quarterly"),
            ("Least-privilege evidence", "Workspace snapshot and policy violation log", "Policy workspace export and policy analysis output", "Quarterly + after each change"),
            ("Vulnerability + reachability", "CVE list weighted by reach into NPI-Applications and Covered-Systems", "Vulnerability report scoped to NYDFS-500", "Monthly"),
            ("Third-party egress reconciliation", "Outbound flow to vendor endpoints", "Flow search filtered to vendor endpoints", "Monthly"),
            ("Incident timeline sample", "One representative incident", "Flow + process search", "Per incident; one representative sample per audit cycle"),
        ],
        "boundaries": "CSW does not replace the CISO function, written policies, MFA / IAM enforcement, encryption programmes, the risk assessment itself, the 72-hour notification decision under Section 500.17(a), or the senior officer / board-of-directors annual notice of compliance under Section 500.17(b).",
        "runbook_filename": "CSW-NYDFS-Reference-Design.md",
    },
    {
        "folder": "TISAX",
        "title": "Cisco Secure Workload - TISAX / VDA ISA Compliance Report",
        "stem": "CSW-TISAX-Compliance-Report",
        "standard": "TISAX (Trusted Information Security Assessment Exchange) - assessment of the VDA ISA (Information Security Assessment) catalogue",
        "version_note": "TISAX is the assessment label operated by the ENX Association; VDA ISA is the underlying control catalogue. VDA ISA has multiple published versions (5.x at time of writing). This report references VDA ISA topic areas by name, not specific control numbers, because control numbering may vary across catalogue versions. Validate against the VDA ISA workbook version applicable to your assessment scope and assessment objectives (AL 1 / AL 2 / AL 3 / AL High / AL Very High).",
        "audience": "Automotive suppliers, OEM partners, and engineering / development service providers preparing for, maintaining, or renewing a TISAX assessment.",
        "driver": "Information security level evidence, prototype-protection segmentation, data-protection segmentation, and supplier readiness for the ENX/TISAX assessment.",
        "scope_pattern": "TISAX\n├── Information-Security-Scope (Production-Workloads, Engineering-Workloads, Corporate-Adjacent)\n├── Prototype-Protection-Scope (only when in assessment scope)\n├── Data-Protection-Scope (only when in assessment scope)\n├── Security-Services\n└── Supplier-Edges",
        "in_scope": [
            "Asset Management (workload inventory, labels, reachability)",
            "Communication Security (workload-level segmentation)",
            "Operations Security (continuous monitoring, vulnerability + reachability)",
            "Identity and Access Management (workload-to-workload layer)",
            "Information Security Incident Management (forensic flow / process telemetry)",
            "Prototype Protection (when in scope - isolation evidence)",
            "Data Protection (when in scope - isolation evidence)",
            "Supplier Relationships (outbound flow visibility)",
            "Compliance (evidence pack inputs)",
        ],
        "out_of_scope": [
            "Information Security Policies and Organisation (governance)",
            "Personnel / HR controls",
            "Physical Security (including prototype physical handling)",
            "System Acquisition, Development, Maintenance (code-level controls)",
            "Cryptography (CSW detects plaintext flows but does not enforce encryption)",
            "Portability and Interoperability",
        ],
        "topic_map": [
            ("Asset Management", "Workload inventory; scope + label export", "Inventory and classification evidence at workload layer"),
            ("Communication Security", "Policy workspace; ADM-derived allowlist; observed flows", "Segmentation evidence (workspace snapshot + observed-vs-approved flow comparison)"),
            ("Operations Security", "Continuous monitoring; vulnerability + reachability; configuration baseline on policy", "Operations control evidence"),
            ("Identity and Access Management (workload-to-workload)", "Policy workspace + enforcement / violation log", "Workload-to-workload privilege evidence (complements identity layer)"),
            ("Cryptography (detection)", "Plaintext-flow detection on regulated paths", "Detection input only"),
            ("Supplier Relationships", "Outbound flow summary to supplier endpoints", "Supplier-edge flow report reconciled against supplier register"),
            ("Incident Management", "Forensic flow + process telemetry", "Investigation pack with timeline and impact scope"),
            ("Prototype Protection (if in scope)", "Isolation evidence for the Prototype-Protection scope", "Inbound/outbound reachability summary for prototype workloads"),
            ("Data Protection (if in scope)", "Isolation evidence for the Personal-Data scope", "Inbound/outbound reachability summary for personal-data workloads"),
        ],
        "evidence_collection": [
            ("Information asset and prototype/data scope mapping", "Workloads in the assessment scope by label", "Inventory + scope membership export filtered by assessment_objective, prototype, data_class", "Monthly"),
            ("Segmentation evidence", "Workspace snapshot and ADM-derived allowlist", "Policy workspace export + ADM export", "Quarterly + after each change"),
            ("Supplier egress reconciliation", "Outbound flow to supplier endpoints", "Flow search filtered to supplier endpoints", "Monthly"),
            ("Operations evidence", "Continuous monitoring and vulnerability data", "Vulnerability report + alert log scoped to TISAX", "Monthly"),
            ("Prototype-Protection isolation (if in scope)", "Reachability into the prototype scope", "Reach summary for the Prototype-Protection scope", "Quarterly"),
            ("Data-Protection isolation (if in scope)", "Reachability into the personal-data scope", "Reach summary for the Data-Protection scope", "Quarterly"),
            ("Incident sample", "One representative incident timeline", "Flow + process search", "Per incident; one representative sample per surveillance cycle"),
        ],
        "boundaries": "CSW does not replace organisational policy, training, supplier assurance contracts, physical security and prototype physical handling, identity lifecycle, cryptography assurance, or the TISAX assessment itself.",
        "runbook_filename": "CSW-TISAX-Reference-Design.md",
    },
    {
        "folder": "NIST-800-82",
        "title": "Cisco Secure Workload - NIST SP 800-82 Compliance Report",
        "stem": "CSW-NIST-800-82-Compliance-Report",
        "standard": "NIST SP 800-82 Revision 3 - Guide to Operational Technology (OT) Security (September 2023)",
        "version_note": "NIST SP 800-82 Rev. 3 is guidance, not a separate control catalogue. It uses NIST SP 800-53 Rev. 5 as its underlying control framework and provides an OT-tailored overlay. This report references 800-82 topic areas and the 800-53 control families they align to; the customer's OT cybersecurity programme determines the actual control tailoring.",
        "audience": "Industrial / critical-infrastructure operators (manufacturing, energy, water, transportation, pharma, food production) and any organisation with an OT estate whose IT-side boundary must demonstrate segmentation hygiene.",
        "driver": "IT-side segmentation adjacent to OT zones; the OT device layer is addressed by an OT-native product (Cyber Vision, Claroty, Nozomi). CSW focuses on the IT-side workloads (historians, engineering workstations, jump hosts, IT/OT DMZ, monitoring, patch / asset servers).",
        "scope_pattern": "NIST-800-82\n├── OT-Adjacent-IT (Historians, Patch-Servers-OT-Direction, Engineering-Workstations, Jump-Hosts-to-OT)\n├── OT-Monitoring-IT-Side\n├── Enterprise-IT\n└── OT-Zones (NOT instrumented by CSW; observed via flow visibility only)",
        "in_scope": [
            "Network architecture and segmentation (IT side of the IT/OT boundary) - 800-53 SC-7, AC-4",
            "Monitoring (IT side) - 800-53 SI-4, AU family",
            "Access control (workload-to-workload, IT side) - 800-53 AC-3, AC-4, AC-6",
            "Vulnerability management (reachability-weighted, OT-aware) - 800-53 RA-5, SI-2",
            "Incident response (IT-side forensic input) - 800-53 IR family",
            "Configuration / change management (IT-side workspace baseline) - 800-53 CM family",
        ],
        "out_of_scope": [
            "OT device-layer policy and protocol inspection (use an OT-native product)",
            "OT change management and OT-side cybersecurity programme governance",
            "Identity management and physical security",
            "Cryptography for OT protocols",
            "BCP/DR for OT operations",
        ],
        "topic_map": [
            ("Network architecture / segmentation (IT side)", "Policy workspace; observed IT-OT flows; ADM-derived allowlist", "Workspace snapshot + observed IT-OT flow report"),
            ("Monitoring (IT side)", "Continuous flow / process telemetry; alerts on unauthorised IT-OT flow", "Alert and anomaly log scoped to OT-Adjacent-IT"),
            ("Access control (IT side)", "Workload-to-workload allowlist + enforcement log", "Workspace snapshot and violation/exception register"),
            ("Vulnerability management (OT-aware)", "Reachability-weighted CVE on OT-adjacent IT workloads", "Prioritised remediation list with compensating-control register"),
            ("Incident response (IT side)", "Forensic flow / process search across the incident window", "Investigation pack with timeline and impact scope"),
            ("Configuration management", "Workspace snapshot before/after each change", "Change-controlled policy workspace export"),
        ],
        "evidence_collection": [
            ("OT-adjacent IT inventory", "Workloads adjacent to OT zones with isa_level and it_or_ot labels", "Inventory + scope membership export", "Monthly"),
            ("IT-OT boundary flow evidence", "Approved vs. observed IT-OT flow comparison", "ADM workspace export + policy workspace export", "Quarterly"),
            ("Jump-host activity", "Jump-host flows to OT-Zones with timing", "Flow search on Jump-Hosts-to-OT", "Continuous; reviewed monthly"),
            ("Vulnerability + reachability", "CVE list weighted by reach into OT-Zones", "Vulnerability report scoped to NIST-800-82", "Monthly"),
            ("Incident sample (IT side)", "One representative IT-side incident timeline", "Flow + process search", "Per incident; one representative sample per audit cycle"),
        ],
        "boundaries": "CSW does not enforce policy on OT devices, parse OT protocols (Modbus, DNP3, S7, OPC UA, etc.), manage OT change windows, replace an OT-native product (Cyber Vision, Claroty, Nozomi), or replace the OT cybersecurity programme.",
        "runbook_filename": "CSW-NIST-800-82-Reference-Design.md",
    },
    {
        "folder": "BSI-C5",
        "title": "Cisco Secure Workload - BSI C5 Compliance Report",
        "stem": "CSW-BSI-C5-Compliance-Report",
        "standard": "BSI Cloud Computing Compliance Criteria Catalogue (C5:2020)",
        "version_note": "References C5:2020. BSI may publish revisions; validate the catalogue version against the customer's assessment scope. C5 distinguishes Basic Criteria from Additional Criteria (the latter expanding evidence requirements). Topic areas in this report are referenced by name and area abbreviation; specific criterion numbering may vary across catalogue revisions.",
        "audience": "Cloud service providers (CSPs) and cloud-hosted workload owners serving German federal / public-sector customers or any customer that contractually requires C5 evidence.",
        "driver": "Cloud workload segmentation, operations security (OPS), communication security (KOS), workload-to-workload identity and access management (IDM), asset management (AM), and security incident management (SIM) evidence.",
        "scope_pattern": "BSI-C5\n├── Customer-Tenants (Tenant-A, Tenant-B, Tenant-C ...)\n├── Shared-Infrastructure (Identity-Layer, Logging-Telemetry, Patch-Configuration, Backup-Layer)\n├── Management-Plane (Operator-Jump-Hosts, Admin-Consoles)\n└── External-Service-Providers",
        "in_scope": [
            "Asset Management (AM)",
            "Communication Security (KOS) - tenant separation and segmentation",
            "Operations Security (OPS) - monitoring, vulnerability + reachability, configuration baseline",
            "Identity and Access Management (IDM) - workload-to-workload layer",
            "Cryptography (KRY) - plaintext-flow detection only",
            "Supplier / Sub-Service Provider Control (SP)",
            "Security Incident Management (SIM)",
            "Business Continuity (BCM) - approved flow baseline as input to recoverability",
            "Compliance (COM) and Investigation (INQ) - evidence pack inputs",
        ],
        "out_of_scope": [
            "Organisation of Information Security (OIS)",
            "Personnel (HR)",
            "Physical Security (PS)",
            "Portability and Interoperability (PI)",
            "Procurement, Development, and Modification (DEV) - code-level controls",
            "Cryptography enforcement and key management (KRY enforcement)",
        ],
        "topic_map": [
            ("Asset Management (AM)", "Workload inventory; scope + label export", "Inventory + classification evidence"),
            ("Communication Security (KOS) - tenant separation", "Policy workspace + cross-tenant deny enforcement", "Workspace snapshot + cross-tenant violation log (the heart of multi-tenant KOS evidence)"),
            ("Operations Security (OPS)", "Continuous monitoring; vulnerability + reachability; configuration drift on policy", "Operations evidence pack"),
            ("Identity and Access Management (IDM)", "Policy workspace + enforcement / violation log", "Workload-to-workload privilege evidence"),
            ("Cryptography (KRY) - detection", "Plaintext-flow detection on regulated paths", "Detection input only"),
            ("Sub-Service Provider Control (SP)", "Outbound flow summary to service-provider endpoints", "Service-provider egress report"),
            ("Security Incident Management (SIM)", "Forensic flow + process telemetry", "Investigation pack with timeline and tenant-impact scope"),
            ("Business Continuity (BCM)", "Approved flow baseline", "Recoverability input only"),
            ("Compliance (COM)", "Periodic evidence pack", "Auditor work-paper input"),
        ],
        "evidence_collection": [
            ("Cloud workload inventory across tenants", "Workloads grouped by tenant and service offering", "Inventory + scope membership export filtered by tenant, customer, service_offering", "Monthly"),
            ("Tenant separation evidence", "Cross-tenant deny enforcement and violation log", "Policy workspace export + policy analysis output", "Continuous; reviewed quarterly"),
            ("Operations evidence", "Continuous monitoring + reachability-weighted vulnerability data", "Vulnerability report scoped to BSI-C5 + alert log", "Monthly"),
            ("Sub-service-provider egress", "Outbound flow to External-Service-Providers", "Flow search filtered to external service-provider endpoints", "Monthly"),
            ("Incident sample (per tenant)", "Workload-level timeline including tenant identification", "Flow + process search", "Per incident; one representative sample per audit cycle"),
        ],
        "boundaries": "CSW does not replace BSI C5 attestation, CSP organisational and physical controls, supplier contractual arrangements, identity lifecycle, key management / cryptography enforcement, backup/DR, portability and interoperability assurance, or shared-responsibility model decisions.",
        "runbook_filename": "CSW-BSI-C5-Reference-Design.md",
    },
    {
        "folder": "IEC-62443",
        "title": "Cisco Secure Workload - IEC 62443 Compliance Report",
        "stem": "CSW-IEC62443-Compliance-Report",
        "standard": "IEC 62443 - Industrial Automation and Control Systems Security",
        "version_note": "IEC 62443 is a multi-part series (e.g. 62443-2-1 for IACS security programmes, 62443-3-2 for zones and conduits / risk assessment, 62443-3-3 for system security requirements, 62443-4-2 for component requirements). This report focuses on the zones-and-conduits and system-security-requirement themes; cite the specific part and edition relevant to the customer's certification scope.",
        "audience": "Industrial, manufacturing, energy, utilities, transportation, and pharmaceutical operators and integrators applying IEC 62443 zones and conduits architecture.",
        "driver": "IT-side workload segmentation that aligns with zones and conduits architecture; the OT device-layer SR controls are addressed by an OT-native product (Cyber Vision, Claroty, Nozomi).",
        "scope_pattern": "IEC-62443\n├── IT-Side-Zones (Enterprise-Zone, Operations-Zone-IT-Side)\n├── IT-OT-DMZ-IT-Side (Historians, Engineering-Workstations, Jump-Hosts, Patch-Servers, Asset-Servers)\n├── Conduits (observed IT-side endpoints of every IT-OT conduit)\n└── OT-Side-Zones (NOT instrumented; observed via conduit endpoints)",
        "in_scope": [
            "Zone definition (IT side) and IT-side conduit endpoints",
            "Foundational Requirement-aligned themes on the IT side: Identification and Authentication Control (FR1), Use Control (FR2), System Integrity / monitoring (FR3 / FR6), Data Confidentiality (detection, FR4), Restricted Data Flow (FR5)",
            "Network architecture evidence on the IT side",
            "Vulnerability management with reachability context",
            "Incident response - IT-side forensic input",
        ],
        "out_of_scope": [
            "Component-level (FR / SR) requirements on OT devices (PLC, RTU, IED, HMI)",
            "OT protocol inspection and OT change management",
            "Physical security and personnel controls",
            "Cryptography enforcement on OT links",
            "Safety system controls",
        ],
        "topic_map": [
            ("Zone and conduit architecture (IT side)", "Scope architecture mirroring zones; policy workspace as conduit allowlist", "Workspace snapshot + observed conduit flow report"),
            ("Restricted Data Flow (FR5, IT side)", "Workload-to-workload allowlist between zones; cross-zone deny enforcement", "Policy workspace + cross-zone violation log"),
            ("System Integrity / Monitoring (FR3 / FR6)", "Continuous flow + process telemetry; alerts on unauthorised conduit flow", "Alert and anomaly log scoped to IEC-62443"),
            ("Use Control (FR2) workload layer", "Policy workspace + enforcement / violation log", "Workload-to-workload use-control evidence"),
            ("Data Confidentiality (FR4) detection", "Plaintext-flow detection on regulated paths", "Detection input only"),
            ("Vulnerability handling", "Reachability-weighted CVE on IT-side zone members", "Prioritised remediation list with compensating-control register"),
            ("Incident response (IT side)", "Forensic flow + process telemetry", "Investigation pack with timeline and impact scope"),
        ],
        "evidence_collection": [
            ("Zone inventory (IT side)", "Workloads grouped by zone and conduit endpoint", "Inventory + scope membership export with iec62443_zone label", "Monthly"),
            ("Conduit evidence", "Observed and approved IT-side conduit flows", "ADM workspace export + policy workspace export", "Quarterly"),
            ("Cross-zone deny evidence", "Cross-zone violation log", "Policy analysis output", "Continuous; reviewed quarterly"),
            ("Vulnerability + reachability", "CVE list weighted by reach into OT-side zones", "Vulnerability report scoped to IEC-62443", "Monthly"),
            ("Incident sample", "One representative IT-side incident timeline", "Flow + process search", "Per incident; one representative sample per audit cycle"),
        ],
        "boundaries": "CSW does not certify against IEC 62443, parse OT protocols, enforce SR controls on OT components, manage OT change windows, or replace an OT-native product (Cyber Vision, Claroty, Nozomi, Dragos) for OT device discovery and protocol inspection.",
        "runbook_filename": "CSW-IEC-62443-Reference-Design.md",
    },
    {
        "folder": "GDPR",
        "title": "Cisco Secure Workload - GDPR Compliance Report",
        "stem": "CSW-GDPR-Compliance-Report",
        "standard": "EU General Data Protection Regulation 2016/679 (GDPR)",
        "version_note": "References GDPR as published (Regulation (EU) 2016/679). Article references in this report are well-known and stable. The UK GDPR (post-Brexit) is similar but separate; validate against the applicable text.",
        "audience": "EU and EEA data controllers and processors and any organisation processing personal data of EU/EEA data subjects; DPO, privacy office, security, and application teams.",
        "driver": "Security of processing evidence (Article 32), data-flow inputs for the Record of Processing Activities (Article 30), breach timeline inputs (Articles 33-34), and processor-egress reconciliation (Article 28).",
        "scope_pattern": "GDPR\n├── Personal-Data-Systems (Customer-Data-Stores, Application-Tier, Identity-Adjacent)\n├── Special-Category-Data-Systems (when applicable)\n├── Processors (Outsourced-Connectivity)\n└── Breach-Investigation",
        "in_scope": [
            "Article 32 - Security of processing (segmentation, monitoring, vulnerability management)",
            "Article 30 - Records of processing (data-flow inputs only)",
            "Article 33 / 34 - Notification of breach (technical scoping inputs)",
            "Article 28 - Processor egress visibility",
        ],
        "out_of_scope": [
            "Article 6 / 9 - Lawful basis and special-category processing conditions",
            "Article 13-14 - Information to data subjects",
            "Article 15-22 - Data subject rights handling",
            "Article 35 - Data Protection Impact Assessment (CSW provides technical inputs only)",
            "Article 37-39 - DPO role and responsibilities",
            "International transfer mechanisms (Chapter V)",
        ],
        "topic_map": [
            ("Article 32 - Security of processing (segmentation)", "Policy workspace + ADM-derived allowlist", "Workspace snapshot + observed-vs-approved flow comparison"),
            ("Article 32 - Security of processing (monitoring)", "Continuous flow + process telemetry; alerts", "Alert and anomaly log scoped to personal-data systems"),
            ("Article 32 - Security of processing (encryption detection)", "Plaintext-flow detection on regulated paths", "Detection input only"),
            ("Article 30 - Records of processing", "Observed application data flows", "Data-flow report by application owner (input to RoPA)"),
            ("Article 28 - Processor egress", "Outbound flow summary to processor endpoints", "Processor-egress report reconciled against processor register"),
            ("Article 33 / 34 - Breach timeline", "Forensic flow + process telemetry", "Investigation pack with timeline and data-subject-impact scoping inputs"),
            ("Vulnerability handling", "Reachability-weighted CVE on personal-data systems", "Prioritised remediation list with compensating-control register"),
        ],
        "evidence_collection": [
            ("Personal-data system inventory", "Workloads with data_class=personal or special-category", "Inventory + scope membership export", "Monthly"),
            ("Data-flow evidence (RoPA support)", "Observed application data flows", "ADM workspace export filtered by personal-data scope", "Quarterly + on RoPA review"),
            ("Segmentation evidence", "Workspace snapshot + observed-vs-approved flow comparison", "Policy workspace export + ADM export", "Quarterly + after each change"),
            ("Processor egress reconciliation", "Outbound flow to processor endpoints", "Flow search filtered to processor endpoints", "Monthly"),
            ("Vulnerability + reachability", "CVE list weighted by reach into personal-data systems", "Vulnerability report scoped to GDPR", "Monthly"),
            ("Breach timeline sample", "Workload-level timeline for one representative incident", "Flow + process search", "Per breach; supports the 72-hour Article 33 timeline"),
        ],
        "boundaries": "CSW does not determine lawful basis or consent, conduct Data Protection Impact Assessments, fulfil data-subject rights requests, manage international transfer mechanisms, replace the DPO function, or make the Article 33 / 34 notification decisions.",
        "runbook_filename": "CSW-GDPR-Reference-Design.md",
    },
    {
        "folder": "MITRE-ATTACK",
        "title": "Cisco Secure Workload - MITRE ATT&CK Compliance Report",
        "stem": "CSW-MITRE-ATTACK-Compliance-Report",
        "standard": "MITRE ATT&CK Enterprise (https://attack.mitre.org)",
        "version_note": "MITRE ATT&CK is a living knowledge base; the version evolves periodically (current version at time of writing is v15). This report references the high-level tactics (TA0001 through TA0040 / TA0011 family). Validate technique-level mappings against the ATT&CK version your detection-engineering team is using.",
        "audience": "Security architects, detection engineers, threat hunters, SOC analysts, and red-team / purple-team functions using ATT&CK as the common reference for adversary behaviour.",
        "driver": "ATT&CK is not a compliance framework. CSW supports a subset of ATT&CK tactics with workload-level prevention and detection evidence, primarily Lateral Movement (TA0008), Discovery (TA0007), Command and Control (TA0011) detection of egress, Exfiltration (TA0010) detection, and Initial Access (TA0001) reduction by reducing reachable surface.",
        "scope_pattern": "MITRE-ATTACK\n(no fixed scope tree; ATT&CK is a tactic / technique cross-cut applied to any CSW-instrumented scope)",
        "in_scope": [
            "Initial Access (TA0001) - reachable-surface reduction",
            "Discovery (TA0007) - lateral discovery flow detection",
            "Lateral Movement (TA0008) - east-west flow detection and prevention",
            "Command and Control (TA0011) - egress flow detection",
            "Exfiltration (TA0010) - egress flow detection",
            "Impact (TA0040) - workload reach scoping during impact analysis",
        ],
        "out_of_scope": [
            "Execution (TA0002) - endpoint behaviour (EDR domain)",
            "Persistence (TA0003) - host-level (EDR domain)",
            "Privilege Escalation (TA0004) - host-level (EDR domain)",
            "Defense Evasion (TA0005) - many techniques are host-level (EDR domain)",
            "Credential Access (TA0006) - identity layer (IAM / EDR)",
            "Collection (TA0009) - host-level (EDR / DLP)",
        ],
        "topic_map": [
            ("Initial Access (TA0001) - reduce reachable surface", "Reachability-weighted vulnerability evidence; policy workspace deny by default", "Vulnerability report + workspace snapshot showing reduced ingress paths"),
            ("Discovery (TA0007) - detect lateral discovery flows", "Process + flow telemetry; alerts on unexpected scanning patterns", "Alert log for unauthorised east-west reconnaissance"),
            ("Lateral Movement (TA0008) - east-west enforcement and detection", "Policy workspace + enforcement / violation log", "Workspace snapshot + violation log showing east-west allowlist enforcement"),
            ("Command and Control (TA0011) - egress detection", "Outbound flow telemetry with destination context", "Egress flow report and anomaly alerts"),
            ("Exfiltration (TA0010) - egress detection", "Outbound flow telemetry with destination context and volume context", "Egress flow report with volume anomalies"),
            ("Impact (TA0040) - reach scoping", "Forensic flow + process search", "Investigation pack showing reach from the impacted workload"),
        ],
        "evidence_collection": [
            ("Reachable-surface reduction", "Reduced ingress paths to high-value workloads", "Policy workspace export + reachability summary", "Quarterly + after each major workspace change"),
            ("Lateral-movement enforcement", "East-west allowlist enforcement and violation log", "Policy workspace export + policy analysis output", "Continuous; reviewed quarterly"),
            ("Egress monitoring", "Outbound flow telemetry to external destinations", "Flow search filtered to external destinations", "Continuous; reviewed daily for high-value scopes"),
            ("Detection content (joint with SOC)", "ATT&CK-mapped detection rules using CSW telemetry", "SOC integration (CSW telemetry exported to SIEM)", "Continuous; rule sets reviewed monthly"),
        ],
        "boundaries": "ATT&CK is not a compliance standard. CSW does not replace EDR, SIEM, identity telemetry, malware analysis, endpoint response, threat intelligence, or the full detection engineering function. CSW is one telemetry source among many for an ATT&CK-aligned SOC.",
        "runbook_filename": "CSW-MITRE-ATTACK-Reference-Design.md",
    },
    {
        "folder": "FedRAMP",
        "title": "Cisco Secure Workload - FedRAMP Compliance Report",
        "stem": "CSW-FedRAMP-Compliance-Report",
        "standard": "FedRAMP (Moderate baseline) - Federal Risk and Authorization Management Program",
        "version_note": "FedRAMP baselines are aligned to NIST SP 800-53 Rev. 5 (Low, Moderate, High). This report assumes the Moderate baseline as the most common cloud-service scope. Control IDs referenced (e.g. AC-4, SC-7, SI-4, CA-7) are stable in 800-53 Rev. 5. Validate the customer's authorisation level and parameter tailoring against the SSP.",
        "audience": "Cloud service providers seeking or maintaining FedRAMP authorisation, federal agency customers, and 3PAOs preparing assessment evidence.",
        "driver": "Information-flow enforcement (AC-4), boundary protection (SC-7), continuous monitoring evidence (CA-7), and system monitoring (SI-4) at the workload layer.",
        "scope_pattern": "FedRAMP\n├── Authorisation-Boundary (in-scope workloads inside the SSP boundary)\n├── External-Connections (external systems and interconnections)\n├── Privileged-Operations (jump hosts, admin paths)\n└── ConMon-Telemetry-Sources",
        "in_scope": [
            "AC-4 - Information Flow Enforcement (workload-to-workload)",
            "SC-7 - Boundary Protection (workload-to-workload)",
            "AU family - Audit and Accountability (workload telemetry)",
            "SI-4 - System Monitoring (workload telemetry)",
            "CA-7 - Continuous Monitoring (technical telemetry)",
            "RA-5 / SI-2 - Vulnerability Scanning and Flaw Remediation (reachability-weighted)",
        ],
        "out_of_scope": [
            "AC-1 through AC-3 - Identity-layer access enforcement",
            "Encryption controls (SC-8 / SC-13) - CSW detects plaintext flows but does not enforce encryption",
            "Personnel security (PS family), physical security (PE family)",
            "FedRAMP 3PAO judgement, agency ATO decisions, POA&M ownership",
            "SSP authorship and control parameter selection",
        ],
        "topic_map": [
            ("AC-4 - Information Flow Enforcement", "Policy workspace + workload-to-workload allowlist", "Workspace snapshot + observed-vs-approved flow comparison"),
            ("SC-7 - Boundary Protection (workload layer)", "Default-deny policy at the workload boundary", "Workspace snapshot showing boundary deny rules"),
            ("AU family - Audit", "Workload flow + process telemetry retained per retention policy", "Retained telemetry export"),
            ("SI-4 - System Monitoring", "Continuous flow + process telemetry; alerts", "Alert and anomaly log scoped to FedRAMP boundary"),
            ("CA-7 - Continuous Monitoring", "Continuous workspace + ADM + vulnerability evidence", "Monthly evidence pack for ConMon submission"),
            ("RA-5 / SI-2 - Vulnerability handling", "Reachability-weighted CVE evidence", "Prioritised remediation list with POA&M inputs"),
        ],
        "evidence_collection": [
            ("Authorisation boundary inventory", "Workloads inside the SSP boundary", "Inventory + scope membership export", "Monthly"),
            ("Information-flow enforcement evidence", "Workspace snapshot + violation log", "Policy workspace export + policy analysis output", "Monthly (ConMon cadence)"),
            ("Continuous monitoring evidence", "Workspace, ADM, and vulnerability inputs to ConMon", "Aggregated monthly evidence pack", "Monthly"),
            ("Vulnerability + reachability", "CVE list weighted by reach inside the boundary", "Vulnerability report scoped to FedRAMP boundary", "Monthly (per FedRAMP scanning cadence)"),
            ("Incident sample", "One representative incident timeline for IR drills or actual incidents", "Flow + process search", "Per incident"),
        ],
        "boundaries": "CSW does not replace FedRAMP authorisation, SSP ownership, 3PAO assessment, CSP platform controls, identity layer (IAM / MFA), encryption (FIPS-validated modules), audit-log retention infrastructure, or agency ATO decisions.",
        "runbook_filename": "CSW-FedRAMP-Reference-Design.md",
    },
    {
        "folder": "SWIFT-CSCF",
        "title": "Cisco Secure Workload - SWIFT CSCF Compliance Report",
        "stem": "CSW-SWIFT-CSCF-Compliance-Report",
        "standard": "SWIFT Customer Security Controls Framework (CSCF) v2024",
        "version_note": "References CSCF v2024. SWIFT publishes a new CSCF version yearly; verify against the version applicable to the customer's attestation cycle. Control codes (e.g. 1.1, 1.4, 2.1, etc.) are stable across recent versions for mandatory controls but advisory controls evolve.",
        "audience": "SWIFT users (financial institutions and service bureaus) subject to the SWIFT Customer Security Programme (CSP) and required to attest annually.",
        "driver": "SWIFT secure-zone segmentation, restricted Internet access from the secure zone, restricted access between the secure zone and the general enterprise IT estate, monitoring, and SWIFT-specific logging support.",
        "scope_pattern": "SWIFT-CSCF\n├── SWIFT-Secure-Zone (Messaging-Interfaces, Communication-Interfaces, Local-Authentication)\n├── Operator-Workstations (dedicated and general-purpose)\n├── Jump-Hosts-to-Secure-Zone\n├── Internet-Restricted-Systems\n└── Third-Party-Connectivity",
        "in_scope": [
            "1.1 SWIFT Environment Protection (secure-zone isolation evidence)",
            "1.4 Internet Access Restriction (egress monitoring from secure zone)",
            "2.x System Integrity (workload monitoring, vulnerability handling on secure-zone components)",
            "5.x Access Controls (workload-to-workload layer)",
            "6.x Detect Anomalous Activity (continuous flow + process telemetry)",
        ],
        "out_of_scope": [
            "3.x Physically Secure the Environment",
            "4.x Prevent Compromise of Credentials (identity layer)",
            "5.4 Physical and Logical Password Storage",
            "6.4 Logging and Monitoring (CSW is one log source; SWIFT-specific logging requires the messaging interface logs)",
            "7.x Plan for Incident Response and Information Sharing (governance)",
            "SWIFT CSP attestation submission itself",
        ],
        "topic_map": [
            ("1.1 Secure-zone isolation", "Policy workspace + default-deny at secure-zone boundary", "Workspace snapshot showing secure-zone boundary deny rules"),
            ("1.4 Internet access restriction", "Outbound flow telemetry from secure zone", "Egress flow report from SWIFT-Secure-Zone"),
            ("2.x System integrity (vulnerability)", "Reachability-weighted CVE on secure-zone components", "Prioritised remediation list"),
            ("5.x Access controls (workload layer)", "Policy workspace + enforcement / violation log", "Workspace snapshot + violation log"),
            ("6.x Anomalous activity detection", "Continuous flow + process telemetry; alerts", "Alert and anomaly log scoped to SWIFT-CSCF"),
            ("Operator path evidence", "Flow telemetry for operator workstations and jump hosts", "Operator-workstation flow report"),
        ],
        "evidence_collection": [
            ("Secure-zone inventory", "Workloads in SWIFT-Secure-Zone", "Inventory + scope membership export", "Monthly"),
            ("Secure-zone boundary evidence", "Workspace snapshot and policy violation log", "Policy workspace export + policy analysis output", "Quarterly + after each change"),
            ("Internet access restriction evidence", "Outbound flow from secure zone with destination context", "Flow search filtered to SWIFT-Secure-Zone egress", "Monthly"),
            ("Vulnerability + reachability", "CVE list weighted by reach into secure-zone components", "Vulnerability report scoped to SWIFT-CSCF", "Monthly"),
            ("Operator workstation activity", "Operator and jump-host flow telemetry", "Flow search on Operator-Workstations and Jump-Hosts", "Continuous; reviewed monthly"),
            ("Incident sample", "Workload-level timeline for one representative incident", "Flow + process search", "Per incident"),
        ],
        "boundaries": "CSW does not replace the SWIFT CSP attestation, the messaging interface itself, SWIFT-specific application controls (logging, message integrity, operator authentication), physical security of the SWIFT environment, or the operator credential lifecycle.",
        "runbook_filename": "CSW-SWIFT-CSCF-Reference-Design.md",
    },
    {
        "folder": "HITRUST-CSF",
        "title": "Cisco Secure Workload - HITRUST CSF Compliance Report",
        "stem": "CSW-HITRUST-Compliance-Report",
        "standard": "HITRUST CSF v11",
        "version_note": "References HITRUST CSF v11. HITRUST evolves the CSF periodically; assessment levels (e1, i1, r2) have different evidence requirements. Validate the version, assessment level, and authoritative-source mappings against the customer's HITRUST authoritative-sources list.",
        "audience": "Healthcare covered entities, payers, providers, life-sciences organisations, and service providers preparing for or maintaining HITRUST CSF certification.",
        "driver": "Network segregation, vulnerability management with reachability, monitoring, and incident response evidence harmonised against the HIPAA / ISO 27001 / NIST 800-53 / PCI authoritative sources HITRUST CSF integrates.",
        "scope_pattern": "HITRUST-CSF\n├── Regulated-Data-Systems (ePHI, PCI-CDE if applicable, PII)\n├── Network-Segmentation-Boundary\n├── Vulnerability-Management-Scope\n├── Incident-Evidence\n└── Third-Party-Egress",
        "in_scope": [
            "Network Protection / Segregation (HITRUST 09.m / 09.s; HIPAA Security Rule technical safeguards; ISO 27001 A.13; 800-53 SC-7 / AC-4)",
            "Vulnerability Management (HITRUST 06; 800-53 RA-5 / SI-2)",
            "Monitoring (HITRUST 09; 800-53 SI-4 / AU family)",
            "Incident Response (HITRUST 11; 800-53 IR family)",
            "Third-party / business-associate egress (HIPAA business-associate context)",
        ],
        "out_of_scope": [
            "Organisational policy, training, and governance domains",
            "Physical and environmental controls",
            "Identity lifecycle and access management beyond workload-to-workload",
            "Cryptography enforcement",
            "Business continuity testing",
            "HITRUST assessor scoring and certification decisions",
        ],
        "topic_map": [
            ("Network segregation", "Policy workspace + workload-to-workload allowlist", "Workspace snapshot + observed-vs-approved flow comparison"),
            ("Vulnerability management", "Reachability-weighted CVE on regulated workloads", "Prioritised remediation list with compensating-control register"),
            ("Monitoring", "Continuous flow + process telemetry; alerts", "Alert and anomaly log scoped to HITRUST-CSF"),
            ("Incident response", "Forensic flow + process search across the incident window", "Investigation pack with timeline and impact scope"),
            ("Business-associate / third-party egress", "Outbound flow summary to BA / vendor endpoints", "BA-edge flow report"),
            ("Audit support", "Periodic evidence pack", "Quarterly evidence bundle aligned to HITRUST authoritative-source mappings"),
        ],
        "evidence_collection": [
            ("Regulated-data system inventory", "Workloads with ePHI / PCI / PII labels", "Inventory + scope membership export", "Monthly"),
            ("Segmentation evidence", "Workspace snapshot + observed-vs-approved flow comparison", "Policy workspace export + ADM export", "Quarterly + after each change"),
            ("Vulnerability + reachability", "CVE list weighted by reach into regulated-data systems", "Vulnerability report scoped to HITRUST-CSF", "Monthly"),
            ("Third-party egress reconciliation", "Outbound flow to BA / vendor endpoints", "Flow search filtered to BA / vendor endpoints", "Monthly"),
            ("Incident timeline sample", "One representative incident", "Flow + process search", "Per incident"),
        ],
        "boundaries": "CSW does not replace HITRUST authoritative-source policy, training, governance, the HITRUST assessor's scoring, identity lifecycle, encryption, physical and environmental controls, or HITRUST certification submission.",
        "runbook_filename": "CSW-HITRUST-Reference-Design.md",
    },
    {
        "folder": "NIST-800-171",
        "title": "Cisco Secure Workload - NIST SP 800-171 Compliance Report",
        "stem": "CSW-NIST-800-171-Compliance-Report",
        "standard": "NIST SP 800-171 Revision 3 - Protecting Controlled Unclassified Information (CUI)",
        "version_note": "References NIST SP 800-171 Rev. 3 (published May 2024). Rev. 3 restructured the families; common family abbreviations used here (e.g. 03.01 Access Control, 03.13 System and Communications Protection) follow the Rev. 3 numbering. Validate against the version applicable to the customer's contract (Rev. 2 numbering may still be referenced in legacy contracts).",
        "audience": "Defense industrial base contractors, federal contractors and subcontractors, and any organisation processing or storing CUI on non-federal systems.",
        "driver": "CUI enclave isolation, access enforcement, system and communications protection (03.01 and 03.13 families), and CMMC Level 2 underpinning evidence.",
        "scope_pattern": "NIST-800-171\n├── CUI-Enclave (workloads processing or storing CUI)\n├── CUI-Adjacent-Services (identity, logging, patching adjacent to CUI)\n├── Admin-Paths (jump hosts)\n└── External-Connections (CUI-related external paths)",
        "in_scope": [
            "03.01 Access Control (workload-to-workload allowlist)",
            "03.13 System and Communications Protection (workload-to-workload segmentation)",
            "03.04 Configuration Management (workspace baseline)",
            "03.11 Risk Assessment (reachability-weighted vulnerability evidence)",
            "03.14 System and Information Integrity (monitoring)",
            "03.06 Incident Response (forensic input)",
        ],
        "out_of_scope": [
            "03.05 Identification and Authentication (identity layer)",
            "03.09 Personnel Security",
            "03.10 Physical Protection",
            "03.08 Media Protection",
            "03.13 Cryptography enforcement (CSW detects plaintext flows but does not enforce encryption)",
            "CMMC assessment scoring",
        ],
        "topic_map": [
            ("03.01 Access Control (workload layer)", "Policy workspace + enforcement / violation log", "Workspace snapshot + violation log"),
            ("03.13 System and Communications Protection", "Default-deny at CUI enclave boundary", "Workspace snapshot showing boundary deny rules"),
            ("03.04 Configuration Management", "Workspace baseline and change log", "Change-controlled policy workspace export"),
            ("03.11 Risk Assessment (reachability)", "Reachability-weighted CVE evidence", "Prioritised remediation list"),
            ("03.14 System and Information Integrity", "Continuous flow + process telemetry; alerts", "Alert and anomaly log scoped to CUI-Enclave"),
            ("03.06 Incident Response", "Forensic flow + process search", "Investigation pack with timeline and impact scope"),
        ],
        "evidence_collection": [
            ("CUI enclave inventory", "Workloads processing or storing CUI", "Inventory + scope membership export filtered by data_class=cui", "Monthly"),
            ("Enclave boundary evidence", "Workspace snapshot + observed-vs-approved flow comparison", "Policy workspace export + ADM export", "Quarterly + after each change"),
            ("External connection summary", "Outbound flow from CUI-Enclave", "Flow search filtered to CUI-Enclave egress", "Monthly"),
            ("Vulnerability + reachability", "CVE list weighted by reach into CUI-Enclave", "Vulnerability report scoped to NIST-800-171", "Monthly"),
            ("Incident sample", "One representative incident timeline", "Flow + process search", "Per incident"),
        ],
        "boundaries": "CSW does not replace CUI marking, federal contract requirements (DFARS 252.204-7012, FAR 52.204-21, etc.), System Security Plan ownership, POA&M ownership, identity governance, media protection, encryption (FIPS-validated modules), personnel security, or CMMC assessment.",
        "runbook_filename": "CSW-NIST-800-171-Reference-Design.md",
    },
    {
        "folder": "CSA-CCM",
        "title": "Cisco Secure Workload - CSA CCM Compliance Report",
        "stem": "CSW-CSA-CCM-Compliance-Report",
        "standard": "Cloud Security Alliance Cloud Controls Matrix (CCM) v4",
        "version_note": "References CCM v4. The CCM is updated periodically; validate the version applicable to the customer's STAR (Security, Trust, Assurance, and Risk) submission. CCM domain abbreviations used here (e.g. IVS Infrastructure & Virtualization Security, DSP Data Security and Privacy Lifecycle Management, TVM Threat & Vulnerability Management) are stable in v4.",
        "audience": "Cloud service providers preparing CSA STAR submissions (self-assessment, STAR Level 1) or CSA STAR Certification / Attestation (Level 2), and cloud customers using CCM as a control reference.",
        "driver": "Infrastructure and Virtualization Security (IVS), Data Security and Privacy Lifecycle (DSP), and Threat and Vulnerability Management (TVM) evidence at the cloud workload layer.",
        "scope_pattern": "CSA-CCM\n├── Cloud-Workloads (Customer-Tenants and Shared-Infrastructure)\n├── Tenant-Boundaries\n├── Data-Protection-Scope\n└── Management-Plane",
        "in_scope": [
            "IVS - Infrastructure and Virtualization Security (segmentation, tenant boundary)",
            "DSP - Data Security and Privacy Lifecycle (data-flow visibility, segmentation)",
            "TVM - Threat and Vulnerability Management (reachability-weighted CVE)",
            "LOG - Logging and Monitoring (workload telemetry as one log source)",
            "SEF - Security Incident Management, E-Discovery, and Cloud Forensics (forensic input)",
        ],
        "out_of_scope": [
            "AAA - Audit Assurance and Compliance (governance)",
            "BCR - Business Continuity Management and Operational Resilience",
            "CCC - Change Control and Configuration Management beyond CSW workspace",
            "DCS - Datacenter Security (physical)",
            "GRC - Governance, Risk Management, and Compliance",
            "HRS - Human Resources",
            "IAM - Identity and Access Management lifecycle",
            "STA - Supply Chain Management beyond CSW egress visibility",
        ],
        "topic_map": [
            ("IVS - Infrastructure and Virtualization Security", "Policy workspace + tenant-boundary deny enforcement", "Workspace snapshot + cross-tenant violation log"),
            ("DSP - Data Security (segmentation)", "Workload-to-workload allowlist between data-protection scopes", "Workspace snapshot + observed-vs-approved flow comparison"),
            ("TVM - Threat and Vulnerability Management", "Reachability-weighted CVE on cloud workloads", "Prioritised remediation list with compensating-control register"),
            ("LOG - Logging and Monitoring", "Continuous flow + process telemetry; alerts", "Alert and anomaly log scoped to CSA-CCM"),
            ("SEF - Incident Management / Forensics", "Forensic flow + process search", "Investigation pack with timeline and tenant-impact scoping"),
        ],
        "evidence_collection": [
            ("Cloud workload inventory across tenants", "Workloads grouped by tenant / service offering", "Inventory + scope membership export filtered by tenant and service_offering", "Monthly"),
            ("Tenant separation evidence", "Cross-tenant deny enforcement and violation log", "Policy workspace export + policy analysis output", "Continuous; reviewed quarterly"),
            ("Vulnerability + reachability", "CVE list weighted by reach into tenant data scopes", "Vulnerability report scoped to CSA-CCM", "Monthly"),
            ("Monitoring evidence", "Continuous flow + process telemetry; alerts", "Alert and anomaly log export", "Continuous"),
            ("Forensic sample", "Workload-level timeline for one representative incident", "Flow + process search", "Per incident"),
        ],
        "boundaries": "CSW does not replace CSA STAR submission / attestation, CSP organisational and physical controls, identity lifecycle (IAM), key management (KMS), backup and DR, portability and interoperability, or shared-responsibility model decisions.",
        "runbook_filename": "CSW-CSA-CCM-Reference-Design.md",
    },
    {
        "folder": "COBIT-2019",
        "title": "Cisco Secure Workload - COBIT 2019 Compliance Report",
        "stem": "CSW-COBIT-Compliance-Report",
        "standard": "ISACA COBIT 2019 - Framework for the Governance and Management of Enterprise IT",
        "version_note": "References COBIT 2019. Objective codes (e.g. APO13 Managed Security, DSS05 Managed Security Services, MEA01 Managed Performance and Conformance Monitoring, BAI06 Managed IT Changes) are stable in COBIT 2019. Validate scope tailoring against the customer's design factors and goals cascade.",
        "audience": "IT governance, internal audit, risk management, and assurance teams using COBIT 2019 as the governance and management framework.",
        "driver": "Workload-level evidence inputs to COBIT objectives where the practice is technical: DSS05 (security services), APO13 (managed security), MEA01 (performance and conformance monitoring), and BAI06 / BAI10 (change and configuration evidence).",
        "scope_pattern": "COBIT-2019\n(no fixed scope tree; COBIT objective evidence is mapped across whichever CSW-instrumented scopes are in audit scope)",
        "in_scope": [
            "DSS05.02 - Manage network and connectivity security (workload segmentation and policy enforcement)",
            "DSS05.03 - Manage endpoint security (workload-level allowlist input)",
            "DSS05.07 - Manage vulnerabilities (reachability-weighted CVE)",
            "APO13.01 - Establish and maintain an information security management system (workload-level inputs)",
            "MEA01.04 / MEA01.05 - Performance and conformance monitoring (continuous evidence)",
            "BAI06.01 - Evaluate, prioritise, and authorise change requests (workspace change log)",
            "BAI10.01 - Establish and maintain a configuration model (workspace baseline)",
        ],
        "out_of_scope": [
            "Governance objectives (EDM family)",
            "APO01-12 (organisational alignment, enterprise architecture, portfolio, financials, HR, relationships, service agreements, suppliers, quality, risk, security beyond technical, data, projects)",
            "BAI01-05 / BAI07-09 / BAI11 (organisational change, requirements definition, identification of solutions, availability, capacity, ITSM, organisational change enablement, knowledge, assets)",
            "DSS01 / DSS03 / DSS04 / DSS06 (managed operations, problems, continuity, business process controls)",
            "MEA02-04 (system of internal control, compliance with external requirements, assurance)",
        ],
        "topic_map": [
            ("DSS05.02 - Network and connectivity security", "Policy workspace + workload-to-workload allowlist", "Workspace snapshot + observed-vs-approved flow comparison"),
            ("DSS05.07 - Vulnerability management", "Reachability-weighted CVE evidence", "Prioritised remediation list"),
            ("APO13 - Managed security (technical inputs)", "Continuous workload telemetry + periodic evidence pack", "Quarterly evidence bundle"),
            ("MEA01.04 - Performance and conformance monitoring", "Policy-violation log; drift evidence", "Continuous evidence (replaces point-in-time samples)"),
            ("BAI06 - Managed changes", "Workspace change log (snapshots before/after each change)", "Change-controlled policy workspace export"),
            ("BAI10 - Managed configuration", "Workspace baseline snapshots", "Baseline configuration evidence"),
        ],
        "evidence_collection": [
            ("Workload scope inventory", "Workloads in COBIT audit scope by business function", "Inventory + scope membership export", "Monthly"),
            ("Policy and change evidence", "Workspace snapshot before/after each authorised change", "Policy workspace export + change log", "Per change + quarterly bundle"),
            ("Conformance monitoring evidence", "Continuous policy-violation and drift evidence", "Policy analysis output", "Continuous; reviewed quarterly"),
            ("Vulnerability + reachability", "CVE list weighted by reach across in-scope workloads", "Vulnerability report scoped to COBIT-2019", "Monthly"),
            ("Management review pack", "Aggregated quarterly evidence bundle", "Inventory + workspace + policy violation + vulnerability extracts", "Quarterly"),
        ],
        "boundaries": "CSW does not replace COBIT governance design, design-factor analysis, goals cascade, process ownership, risk appetite decisions, enterprise metrics ownership, audit judgement, or GRC workflow.",
        "runbook_filename": "CSW-COBIT-2019-Reference-Design.md",
    },
    {
        "folder": "AU-Essential-Eight",
        "title": "Cisco Secure Workload - ACSC Essential Eight Compliance Report",
        "stem": "CSW-Essential-Eight-Compliance-Report",
        "standard": "Australian Cyber Security Centre (ACSC) Essential Eight Maturity Model",
        "version_note": "References the Essential Eight Maturity Model as published by ACSC. The model uses three Maturity Levels (ML1, ML2, ML3). The eight mitigation strategies are: Application Control, Patch Applications, Configure Microsoft Office Macro Settings, User Application Hardening, Restrict Administrative Privileges, Patch Operating Systems, Multi-Factor Authentication, Regular Backups. CSW only supports a subset of these; the others are out of scope. Validate maturity-level requirements against the current ACSC publication.",
        "audience": "Australian Commonwealth, state, and territory government agencies and the broader Australian public and private sector using Essential Eight as the baseline maturity reference.",
        "driver": "Patch prioritisation using CVE + reachability, administrative-path restriction at the workload-to-workload layer, and supporting evidence for application control through observed process telemetry.",
        "scope_pattern": "Essential-Eight\n├── Critical-Applications\n├── Admin-Paths (Jump-Hosts, Admin-Workstations)\n├── Patch-Priority-Targets\n└── Application-Control-Support",
        "in_scope": [
            "E2 / E6 - Patch Applications and Patch Operating Systems (reachability-weighted prioritisation)",
            "E5 - Restrict Administrative Privileges (workload-to-workload admin path restriction)",
            "E1 - Application Control (supporting evidence via observed process telemetry; CSW does not enforce application control)",
        ],
        "out_of_scope": [
            "E3 - Configure Microsoft Office Macro Settings (endpoint configuration)",
            "E4 - User Application Hardening (endpoint configuration)",
            "E7 - Multi-Factor Authentication (identity layer)",
            "E8 - Regular Backups (backup / recovery)",
            "Essential Eight maturity-level scoring decisions",
        ],
        "topic_map": [
            ("E2 - Patch Applications (prioritisation)", "Reachability-weighted CVE on application workloads", "Prioritised remediation list with compensating-control register"),
            ("E6 - Patch Operating Systems (prioritisation)", "Reachability-weighted CVE on OS layer", "Prioritised remediation list"),
            ("E5 - Restrict Administrative Privileges (workload layer)", "Policy workspace + admin-path allowlist", "Workspace snapshot showing admin-path restrictions + jump-host flow report"),
            ("E1 - Application Control (supporting)", "Observed process telemetry", "Process inventory and unexpected-process anomalies as input to application control content"),
            ("Maturity-level evidence (across the above)", "Periodic evidence pack", "Quarterly evidence bundle covering the three CSW-supported strategies"),
        ],
        "evidence_collection": [
            ("Critical workload inventory", "Workloads in scope of Essential Eight uplift", "Inventory + scope membership export", "Monthly"),
            ("Patch prioritisation", "CVE list weighted by reach and exploitability", "Vulnerability report scoped to Essential-Eight", "Monthly"),
            ("Admin path restriction", "Jump-host and admin-workstation flow telemetry", "Flow search on Admin-Paths + policy workspace export", "Continuous; reviewed monthly"),
            ("Application control input", "Observed process telemetry on critical workloads", "Process inventory and anomaly report", "Quarterly"),
        ],
        "boundaries": "CSW does not enforce application control on endpoints, harden user applications, configure Office macro settings, enforce MFA, perform backups, or replace ACSC maturity-level assessment ownership.",
        "runbook_filename": "CSW-Essential-Eight-Reference-Design.md",
    },
    {
        "folder": "UK-Cyber-Essentials",
        "title": "Cisco Secure Workload - UK Cyber Essentials Plus Compliance Report",
        "stem": "CSW-Cyber-Essentials-Compliance-Report",
        "standard": "UK NCSC Cyber Essentials Plus",
        "version_note": "References Cyber Essentials (CE) and Cyber Essentials Plus (CE+) as operated by IASME on behalf of NCSC. The five control categories are: Firewalls, Secure Configuration, Security Update Management, User Access Control, and Malware Protection. CE / CE+ requirements are updated periodically; validate against the current published requirements document.",
        "audience": "UK organisations preparing for Cyber Essentials or Cyber Essentials Plus certification.",
        "driver": "Workload-level firewall evidence (control category 1), secure configuration baseline (category 2), patch / vulnerability prioritisation (category 3 - Security Update Management), and supporting evidence for technical verification (CE+ component).",
        "scope_pattern": "UK-Cyber-Essentials\n├── Internet-Facing-Systems\n├── Workload-Firewall-Scope\n├── Secure-Configuration-Baseline\n├── Patch-Evidence-Scope\n└── Verification-Sample",
        "in_scope": [
            "Category 1 - Firewalls (workload-level allowlist and default-deny)",
            "Category 2 - Secure Configuration (workspace baseline)",
            "Category 3 - Security Update Management (CVE + reachability)",
            "Technical Verification (CE+) - workload sample selection support",
        ],
        "out_of_scope": [
            "Category 4 - User Access Control (identity layer)",
            "Category 5 - Malware Protection (endpoint)",
            "Cyber Essentials questionnaire submission",
            "IASME certification body decisions",
        ],
        "topic_map": [
            ("Category 1 - Firewalls (workload layer)", "Policy workspace + default-deny + workload-to-workload allowlist", "Workspace snapshot showing firewall posture per workload"),
            ("Category 2 - Secure Configuration", "Workspace baseline + change log", "Baseline policy workspace export + change-controlled exports"),
            ("Category 3 - Security Update Management", "Reachability-weighted CVE evidence", "Prioritised remediation list with patch-due-date evidence"),
            ("Technical Verification (CE+) sampling", "Workload inventory + reach summary for sampled hosts", "Sample-pack export for assessor"),
        ],
        "evidence_collection": [
            ("Workload inventory", "Workloads in CE / CE+ certification scope", "Inventory + scope membership export", "Monthly"),
            ("Firewall posture per workload", "Default-deny and allowlist evidence", "Policy workspace export", "Quarterly + after each change"),
            ("Vulnerability + reachability", "CVE list weighted by reach across CE scope", "Vulnerability report scoped to UK-Cyber-Essentials", "Monthly (CE expects 14-day patching for critical/high)"),
            ("Verification sample pack", "Per-workload posture for assessor-selected sample", "Per-workload inventory, policy, and vulnerability extracts", "Per certification cycle"),
        ],
        "boundaries": "CSW does not replace the Cyber Essentials questionnaire submission, endpoint malware protection, user access control / identity governance, unsupported-software governance, the assessor's CE+ verification testing, or the IASME certification body decision.",
        "runbook_filename": "CSW-Cyber-Essentials-Reference-Design.md",
    },
    {
        "folder": "HIPAA-2025-NPRM",
        "title": "Cisco Secure Workload - HIPAA 2025 NPRM Compliance Report",
        "stem": "CSW-HIPAA-NPRM-Compliance-Report",
        "standard": "HIPAA Security Rule - 2025 Notice of Proposed Rulemaking (NPRM)",
        "version_note": "This report references the HIPAA Security Rule 2025 NPRM published by HHS / OCR. The NPRM is a PROPOSED rule. Final rule text, effective dates, and implementation expectations may differ from the NPRM. Revalidate this mapping after final rulemaking. Specific section references (e.g. proposed 45 CFR 164.312(a)(2)(vi) network segmentation; 24-month audit trail retention; 72-hour breach timeline) reflect the proposed-rule language at the time of writing.",
        "audience": "Healthcare covered entities, business associates, compliance leaders, and security architects preparing for the 2025 NPRM and tracking implementation expectations.",
        "driver": "Proposed mandatory network segmentation, technology asset inventory expansion, longer audit-trail retention architecture, 72-hour breach timeline support, and annual technical assessment evidence.",
        "scope_pattern": "HIPAA-2025-NPRM\n├── ePHI-Systems\n├── Network-Segmentation-Boundary\n├── Technology-Asset-Inventory\n├── Audit-Trail-Sources\n└── Incident-Timeline",
        "in_scope": [
            "Proposed network segmentation requirement (workload-to-workload allowlist)",
            "Proposed expanded technology asset inventory (workload + software inventory)",
            "Proposed longer audit-trail retention (architecture / evidence inputs)",
            "Proposed 72-hour breach timeline (forensic input)",
            "Proposed annual technical assessment (continuous evidence)",
        ],
        "out_of_scope": [
            "Privacy Rule provisions",
            "Business Associate Agreement (BAA) lifecycle",
            "Identity and access management beyond workload-to-workload",
            "Encryption enforcement (CSW detects plaintext but does not enforce encryption)",
            "Final OCR / HHS interpretive guidance and enforcement decisions",
        ],
        "topic_map": [
            ("Proposed mandatory network segmentation", "Policy workspace + workload-to-workload allowlist", "Workspace snapshot + observed-vs-approved flow comparison"),
            ("Proposed expanded technology asset inventory", "Workload inventory + software / package inventory", "Inventory and software-package extract reconciled to CMDB"),
            ("Proposed audit-trail retention", "Workload flow + process telemetry retained per longer retention window", "Retained telemetry export with retention attestation"),
            ("Proposed 72-hour breach timeline", "Forensic flow + process search across the incident window", "Investigation pack with timeline and ePHI-system-impact scope"),
            ("Proposed annual technical assessment", "Continuous policy + ADM + vulnerability evidence", "Annual evidence bundle"),
        ],
        "evidence_collection": [
            ("ePHI system inventory", "Workloads handling ePHI", "Inventory + scope membership export filtered by data_class=ephi", "Monthly"),
            ("Segmentation evidence", "Workspace snapshot + observed-vs-approved flow comparison", "Policy workspace export + ADM export", "Quarterly + after each change"),
            ("Technology asset inventory", "Workload + software inventory aligned to proposed inventory expansion", "Inventory + software/package extract", "Monthly"),
            ("Audit-trail retention", "Workload flow + process telemetry over the proposed retention window", "Retained telemetry export with retention attestation", "Continuous; validated annually"),
            ("Vulnerability + reachability", "CVE list weighted by reach into ePHI systems", "Vulnerability report scoped to HIPAA-2025-NPRM", "Monthly"),
            ("Breach timeline sample", "Workload-level timeline for one representative incident", "Flow + process search", "Per breach"),
            ("Annual technical assessment pack", "Aggregated annual evidence bundle", "Inventory + workspace + ADM + vulnerability + incident-sample extracts", "Annually"),
        ],
        "boundaries": "This mapping reflects a PROPOSED rule and must be revalidated against the final rule. CSW does not replace legal analysis, HIPAA policies, the risk analysis itself, BAA management, identity / authentication, encryption enforcement, breach-notification decisions, or OCR enforcement engagement.",
        "runbook_filename": "CSW-HIPAA-NPRM-Reference-Design.md",
    },
]


def render_table(headers: list[str], rows: list[tuple[str, ...]]) -> str:
    """Render a GitHub-flavored Markdown table."""
    header_line = "| " + " | ".join(headers) + " |"
    sep_line = "| " + " | ".join(["---"] * len(headers)) + " |"
    body_lines = ["| " + " | ".join(cell for cell in row) + " |" for row in rows]
    return "\n".join([header_line, sep_line, *body_lines])


def derive_coverage(capability: str, artifact: str) -> str:
    """Heuristic coverage rating for a topic row, derived from the row text.

    These ratings are machine-derived from each row's capability/artifact wording
    and are FLAGGED FOR SE REVIEW. Rule of thumb:
      - "Supporting" when CSW evidence feeds/complements another control or tool
        (detection-only, input-to, reconciled-against-register, one-log-source,
        does-not-deploy/install, recoverability input).
      - "Direct" otherwise (CSW produces the primary artifact: segmentation,
        policy, flow/process telemetry, inventory, vulnerability+reachability,
        forensic reconstruction).
    Coverage never means "the control is passed" — only that CSW produces evidence.
    """
    s = f"{capability} {artifact}".lower()
    supporting_markers = (
        "detection input only", "input only", "input to", "feeds the", "feeds ",
        "complements", "reconciled against", "recoverability", "one log source",
        "does not deploy", "does not install", "scoping input", "register reconcil",
        "not the recovery", "layered with", "complement",
    )
    if any(m in s for m in supporting_markers):
        return "Supporting"
    return "Direct"


def report_markdown(item: dict) -> str:
    in_scope_md = "\n".join(f"- {entry}" for entry in item["in_scope"])
    out_of_scope_md = "\n".join(f"- {entry}" for entry in item["out_of_scope"])
    topic_rows = [
        (topic, derive_coverage(cap, art), cap, art)
        for (topic, cap, art) in item["topic_map"]
    ]
    topic_table = render_table(
        ["Framework topic", "Coverage", "CSW capability", "Evidence artifact"],
        topic_rows,
    )
    evidence_table = render_table(
        ["Topic", "What to collect", "CSW source", "Suggested cadence"],
        item["evidence_collection"],
    )

    return f"""# {item['title']}

## Customer-Facing Compliance Report

**Framework:** {item['standard']}  
**Primary audience:** {item['audience']}  
**CSW positioning:** {item['driver']}

---

## Framework Version Note

{item['version_note']}

## CSW UI Navigation Note

Cisco does not yet publish framework-specific CSW UI navigation for this standard; framework-specific navigation is on the product roadmap. This report references CSW *capabilities* and the *evidence artifacts* they produce. The technical runbook (`{item['runbook_filename']}`) in this folder contains the deeper engineering detail.

---

## How to read the Coverage column

Every report in this set uses the same three coverage words. Coverage describes **what evidence CSW produces** for a topic — it never means the control is passed.

**Direct** — Secure Workload produces the primary evidence artifact for that topic (segmentation, policy, flow/process telemetry, inventory, vulnerability + reachability, forensic reconstruction). Direct is still evidence, not an attestation.

**Supporting** — Secure Workload contributes an input that feeds or complements another control, tool, or process (e.g. detection input only, reconciled against an external register, one log source among several).

**Evidence Required** — Secure Workload has no record for this topic. The customer supplies the contract, the analysis, or the HR / physical-security evidence from another control.

> The Coverage ratings in the topic map below are machine-derived from each row's wording and are flagged for SE review before customer use.

## Executive Summary

Cisco Secure Workload (CSW) supports a defined subset of this framework. The strongest customer story is not that CSW "certifies" compliance; it is that CSW turns workload communication and inventory into evidence that the customer, the customer's compliance team, and the customer's assessor can review. This report describes which framework topics CSW supports, which it does not, what evidence artifacts CSW produces, and how often the customer should collect them. CSW does **not** replace the customer's governance, policy, or assessor judgement, and this report is **not** a control attestation.

## Suggested CSW Scope Pattern

```
{item['scope_pattern']}
```

This scope pattern should be validated with the customer's architecture, application owners, compliance team, and assessor before it is used for formal evidence.

## In Scope for CSW Evidence

{in_scope_md}

## Out of Scope (Must Be Evidenced by Other Controls / Tools / Processes)

{out_of_scope_md}

## Framework Topic → CSW Capability Map

{topic_table}

## Evidence Collection Approach

The table below describes per-topic evidence collection - what to collect, the CSW source area, and a suggested cadence. The cadence should be tuned to the customer's audit cycle, regulatory cadence, and risk appetite.

{evidence_table}

## POV / Workshop Approach

1. Confirm the framework version and assessment cycle with the customer's compliance team.
2. Select one business service, regulated boundary, or critical workload group to start with; do not attempt to instrument the entire estate in the POV.
3. Validate workload coverage and install sensors or configure supported connectors. Document the cannot-instrument register; this is itself evidence.
4. Apply labels for application, environment, owner, data class, criticality, compliance scope, and any framework-specific tags (e.g. `tenant`, `prototype`, `isa_level`, `npi`, `cui`, `ephi`).
5. Observe flows over a representative business window. Minimum two weeks; longer if the customer has month-end, quarterly, or seasonal cycles relevant to the scope.
6. Use ADM to generate a candidate policy. Review with the application owner. Run in Simulation mode for at least two weeks before any enforcement.
7. Package inventory, scope, flows, policy, exceptions, and known gaps as the evidence output. Cross-reference this report's evidence collection table with the customer's existing audit work-papers.

## Boundaries and Complementary Controls

{item['boundaries']}

## Assessor / Auditor Caveat

CSW provides technical evidence inputs. The customer's qualified assessor, auditor, certifying body, or regulator determines compliance status. Validate all framework-topic mappings, control IDs, paragraph references, and section numbers in this report against the current official framework text. If the customer is being assessed against a version other than the one referenced in the framework version note above, revalidate before use.

## Disclaimer

This report is for informational and planning purposes. It is not legal, regulatory, audit, or certification advice. Validate all mappings against the current official framework text, the customer's environment, and qualified compliance, legal, and audit professionals.
"""


def plain_text(markdown: str) -> str:
    text = re.sub(r"`([^`]+)`", r"\1", markdown)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"^- ", "• ", text, flags=re.MULTILINE)
    text = text.replace("---", "")
    return text


def write_simple_pdf(text: str, output_path: Path) -> None:
    """Write a simple multi-page PDF using Helvetica and ASCII-compatible text."""
    lines: list[str] = []
    for paragraph in text.splitlines():
        paragraph = paragraph.strip()
        if not paragraph:
            lines.append("")
            continue
        if paragraph.startswith("• "):
            wrapped = textwrap.wrap(paragraph, width=88, subsequent_indent="  ")
        else:
            wrapped = textwrap.wrap(paragraph, width=92)
        lines.extend(wrapped or [""])

    pages = [lines[i : i + 48] for i in range(0, len(lines), 48)] or [[]]
    objects: list[bytes] = []

    def pdf_escape(value: str) -> str:
        value = value.encode("latin-1", "replace").decode("latin-1")
        return value.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")

    kids = []
    for idx, page_lines in enumerate(pages):
        page_obj_num = 3 + idx * 2
        content_obj_num = page_obj_num + 1
        kids.append(f"{page_obj_num} 0 R")
        stream_lines = ["BT", "/F1 10 Tf", "50 760 Td", "14 TL"]
        for line in page_lines:
            stream_lines.append(f"({pdf_escape(line)}) Tj")
            stream_lines.append("T*")
        stream_lines.append("ET")
        stream = "\n".join(stream_lines).encode("latin-1", "replace")
        objects.append(
            f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
            f"/Resources << /Font << /F1 << /Type /Font /Subtype /Type1 /BaseFont /Helvetica >> >> >> "
            f"/Contents {content_obj_num} 0 R >>".encode("latin-1")
        )
        objects.append(b"<< /Length " + str(len(stream)).encode("ascii") + b" >>\nstream\n" + stream + b"\nendstream")

    all_objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        f"<< /Type /Pages /Kids [{' '.join(kids)}] /Count {len(pages)} >>".encode("latin-1"),
        *objects,
    ]

    output = bytearray(b"%PDF-1.4\n")
    offsets = [0]
    for number, obj in enumerate(all_objects, start=1):
        offsets.append(len(output))
        output.extend(f"{number} 0 obj\n".encode("ascii"))
        output.extend(obj)
        output.extend(b"\nendobj\n")
    xref_offset = len(output)
    output.extend(f"xref\n0 {len(all_objects) + 1}\n".encode("ascii"))
    output.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        output.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
    output.extend(
        f"trailer\n<< /Size {len(all_objects) + 1} /Root 1 0 R >>\n"
        f"startxref\n{xref_offset}\n%%EOF\n".encode("ascii")
    )
    output_path.write_bytes(bytes(output))


def run_pandoc(markdown: str, output_path: Path, to_format: str, title: str) -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".md", encoding="utf-8", delete=False) as tmp:
        tmp.write(markdown)
        tmp_path = Path(tmp.name)
    header_path: Path | None = None
    try:
        cmd = [
            "pandoc",
            "--standalone",
            "--from",
            "markdown",
            "--to",
            to_format,
            "--metadata",
            f"title={title}",
            "-o",
            str(output_path),
            str(tmp_path),
        ]
        if to_format == "html5":
            header = tempfile.NamedTemporaryFile("w", suffix=".html", encoding="utf-8", delete=False)
            header.write(f"<style>\n{CSS.read_text(encoding='utf-8')}\n</style>\n")
            header.close()
            header_path = Path(header.name)
            cmd[2:2] = ["--embed-resources", "--toc", "--toc-depth=2", "--include-in-header", header.name]
        subprocess.run(cmd, check=True)
    finally:
        tmp_path.unlink(missing_ok=True)
        if header_path is not None:
            header_path.unlink(missing_ok=True)


def main() -> int:
    for item in FRAMEWORKS:
        folder = ROOT / str(item["folder"])
        folder.mkdir(parents=True, exist_ok=True)
        markdown = report_markdown(item)
        stem = folder / str(item["stem"])
        print(f"report (docx source) -> {stem.relative_to(ROOT)}.docx")
        # DOCX is the source of truth. Table styling (standardize-reports.py),
        # PDF (LibreOffice) and HTML (build-html.py) are produced downstream so
        # every framework in the set is rendered through one consistent pipeline.
        run_pandoc(markdown, stem.with_suffix(".docx"), "docx", str(item["title"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
