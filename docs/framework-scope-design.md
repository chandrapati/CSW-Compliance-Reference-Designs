# Cisco Secure Workload — Framework Scope Design Guide

<a id="top"></a>

Customer-facing scope and label patterns for Cisco Secure Workload (CSW)
compliance mapping workshops.

Use this guide before a proof-of-value, deployment planning workshop, or
evidence-readiness discussion. It helps teams translate framework language
into practical CSW scopes, labels, and evidence boundaries. These patterns
are starting points: validate final scope with the customer's architecture,
asset owners, compliance team, and assessor.

## Table of contents

- [Scope design principles](#scope-design-principles)
- [Framework scope design](#framework-scope-design-table)
  - [HIPAA Security Rule](#hipaa-security-rule)
  - [SOC 2 Type II](#soc-2-type-ii)
  - [PCI DSS v4.0](#pci-dss-v40)
  - [NIST SP 800-53 Rev. 5](#nist-sp-800-53-rev-5)
  - [ISO/IEC 27001:2022](#isoiec-270012022)
  - [CISA Zero Trust Maturity Model](#cisa-zero-trust-maturity-model)
  - [FIPS 140](#fips-140)
  - [NIST SP 800-207](#nist-sp-800-207)
  - [NIST SP 800-207A](#nist-sp-800-207a)
  - [DORA](#dora)
  - [NIS2](#nis2)
  - [NERC CIP](#nerc-cip)
  - [TSA Pipeline Security Directive](#tsa-pipeline-security-directive)
  - [CIS Controls v8.1](#cis-controls-v81)
  - [NIST CSF 2.0](#nist-csf-20)
  - [CMMC 2.0](#cmmc-20)
  - [IEC 62443](#iec-62443)
  - [GDPR](#gdpr)
  - [MITRE ATT&CK](#mitre-attck)
  - [FedRAMP](#fedramp)
  - [SWIFT CSCF](#swift-cscf)
  - [HITRUST CSF v11](#hitrust-csf-v11)
  - [NIST SP 800-171 Rev. 3](#nist-sp-800-171-rev-3)
  - [CSA CCM v4.0](#csa-ccm-v40)
  - [COBIT 2019](#cobit-2019)
  - [SOX ITGC](#sox-itgc)
  - [Australian Essential Eight](#australian-essential-eight)
  - [UK Cyber Essentials Plus](#uk-cyber-essentials-plus)
  - [HIPAA Security Rule — 2025 NPRM](#hipaa-security-rule--2025-nprm)
  - [MAS TRM](#mas-trm)
  - [APRA CPS 234](#apra-cps-234)
  - [NY DFS 23 NYCRR Part 500](#ny-dfs-23-nycrr-part-500)
  - [TISAX](#tisax)
  - [NIST SP 800-82](#nist-sp-800-82)
  - [BSI C5](#bsi-c5)
- [Label / tag recommendations](#label--tag-recommendations)
  - [Baseline labels for every customer](#baseline-labels-for-every-customer)
  - [Framework-specific labels](#framework-specific-labels)
- [Workshop output checklist](#workshop-output-checklist)
- [Customer conversation prompt](#customer-conversation-prompt)

## Scope Design Principles

1. **Start from the protected service, not the tool.** Define the system,
   business function, data boundary, or regulated environment first; then
   map CSW scopes to that boundary.
2. **Separate regulatory scope from operational ownership.** A PCI CDE,
   HIPAA ePHI zone, CUI enclave, or DORA important business function may
   cross teams, clouds, and platforms.
3. **Use labels for policy and evidence.** Scopes should be generated from
   stable labels where possible so inventory, ADM, flow search, policy
   workspaces, and reports use the same vocabulary.
4. **Reconcile CSW coverage.** CSW evidence covers instrumented workloads
   and supported connector visibility. Reconcile gaps with the CMDB, cloud
   inventory, OT inventory, IAM, SIEM, vulnerability scanner, and GRC tools.
5. **Keep out-of-scope explicit.** Physical controls, legal obligations,
   cryptographic module validation, IAM/MFA, endpoint malware controls, and
   OT device enforcement usually require complementary controls.

[↑ Back to top](#top)

<a id="framework-mappings"></a>

## Framework Scope Design Table

| Framework | Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|---|
| HIPAA Security Rule | ePHI applications, databases, clinical integrations, and business associate connections | `Healthcare-Org` > `ePHI-Zone` > app/service scopes such as `EHR`, `Billing`, `PACS`, `HL7`; separate `BAA-Partners` egress scope | ePHI workload isolation, access-path evidence, audit-control telemetry, risk-analysis inputs | HIPAA administrative, physical, legal, and BAA obligations remain outside CSW; validate PHI classification with privacy/compliance owners. **Epic sites:** see [CSW Epic EHR Microsegmentation Guide](https://github.com/chandrapati/CSW-Epic-Microsegmentation-Guide) for tier-by-tier rollout. |
| SOC 2 Type II | The service organization's system boundary and selected Trust Services Criteria | `SOC2-System` > `Production`, `Supporting-Infra`, `Admin-Access`, `Vendor-Integrations`; align scope to system description | Operating-effectiveness evidence for segmentation, monitoring, change drift, incident investigation | SOC 2 criteria depend on the auditor's system description and control design; CSW augments IAM, change management, SIEM, and availability controls |
| PCI DSS v4.0 | Cardholder Data Environment (CDE), CDE-connected systems, and security-impacting systems | `PCI-Environment` > `CDE`, `CDE-Connected`, `Security-Services`, `Third-Party-Processors`, `Out-of-Scope-Validation` | CDE flow documentation, segmentation simulation/enforcement, policy exceptions, vulnerability exposure context | CSW does not replace QSA judgment, ASV scans, penetration testing, network security controls, or PCI governance requirements |
| NIST SP 800-53 Rev. 5 | FISMA/FedRAMP system boundary and SSP control implementation | `System-Boundary` > impact-level or component scopes such as `Moderate`, `High`, `Data-Store`, `App-Tier`, `Management` | AC, AU, CM, IR, RA, SC, and SI evidence for covered workloads | Full 800-53 scope includes many controls outside CSW: identity, personnel, physical, contingency, privacy, and governance controls |
| ISO/IEC 27001:2022 | ISMS scope, information assets, and Annex A control applicability | `ISMS-Boundary` > `Confidential-Data`, `Business-Critical-Apps`, `Cloud-Services`, `Supplier-Connections` | Annex A.8 monitoring, network security, segregation, vulnerability, and supplier-egress evidence | Certification depends on ISMS design, SoA, risk treatment, internal audit, and management review; CSW is a technical evidence source |
| CISA Zero Trust Maturity Model | Agency/enterprise zero-trust initiative by pillar and use case | `ZT-Workloads` > `Sensitive-Apps`, `Privileged-Admin`, `Inter-App-Flows`, `External-Dependencies` | Workload-layer evidence for networks and applications/workloads pillars, plus visibility and analytics | ZTMM maturity is organizational; pair CSW with IdP, MFA, device posture, data governance, SIEM/SOAR, and policy orchestration |
| FIPS 140 | Systems handling regulated cryptographic use or plaintext-protocol risk | `Crypto-Review` > `Sensitive-Transport`, `Plaintext-Protocol-Candidates`, `FIPS-Required-Systems` | Detection/blocking of obvious plaintext transports and inventory support for cryptographic usage review | CSW is not a FIPS-validated cryptographic module; validation, key management, and module selection belong to FIPS-validated libraries/HSMs |
| NIST SP 800-207 | Zero Trust Architecture tenets for workload-to-workload access | `ZTA-Resources` > `Protected-Resources`, `Policy-Enforced-Flows`, `Observed-Dependencies`, `Exceptions` | Resource inventory, per-connection flow evidence, dynamic scoping, workload enforcement as one possible PEP placement | NIST ZTA also requires identity, device posture, policy decision architecture, and enterprise-wide telemetry beyond CSW |
| NIST SP 800-207A | PDP/PEP/PA/PIP component mapping for a cloud-native ZTA discussion | `ZTA-Components` > `PEP-Analogue`, `Policy-Workspace`, `Telemetry-PIP`, `SOAR-Integrated` | Illustrative traceability from CSW policy, enforcement, and telemetry to 207A-style logical components | Treat PDP/PEP/PA/PIP mapping as an analogue for workload segmentation, not a complete enterprise ZTA architecture |
| DORA | Important business functions (IBFs), supporting ICT assets, and third-party dependencies | `DORA-IBF` > one scope per IBF, with nested `Critical`, `Supporting`, `Third-Party-Egress`, `Incident-Dossier` scopes | Article 8 inventory inputs, Article 9 segmentation, Article 10 detection, Article 19 incident evidence, Article 28 technical egress | DORA governance, register of information, contracts, testing programme, and authority reporting remain customer-owned |
| NIS2 | Essential/important entity services and Article 21 risk-management measures | `NIS2-Service` > `Essential-Service`, `Important-Service`, `Supplier-Egress`, `Incident-Reporting`, `High-Risk-Workloads` | Risk-policy enforcement evidence, incident dossier, supply-chain egress, vulnerability exposure, secured workload paths | MFA, training, governance, cryptography, secured voice/video, and national transposition specifics require complementary programmes |
| NERC CIP | IT-side systems supporting BES Cyber System functions | `BES-Supporting-IT` > `EACMS`, `Jump-Hosts`, `Vendor-Access`, `BCSI-Hosts`, `Identity-PKI`, `Patch-Repos` | IT-side ESP boundary evidence, interactive remote access paths, ports/services baseline, vulnerability and change evidence | CSW is not an EAP and does not enforce on PLCs/RTUs/IEDs/HMIs; pair with boundary firewalls and OT-aware monitoring |
| TSA Pipeline Security Directive | IT-side systems supporting Critical Cyber Systems and IT/OT segmentation | `Pipeline-IT-Estate` > `OT-Facing-IT`, `CCS-Supporting-IT`, `Vendor-Access`, `Patch-Repositories`, `Corporate-IT` | IT-side segmentation, documented IT-to-OT flows, access control, monitoring, unpatched-system risk evidence | CSW does not replace the Cybersecurity Coordinator, CAP/CIRP, architecture review, boundary firewall, or OT DPI/monitoring tools |
| CIS Controls v8.1 | Enterprise assets and software in the customer's Implementation Group scope | `CIS-IG2` > `Enterprise-Assets`, `Software-Inventory`, `Secure-Config`, `Vuln-Exposure`, `Network-Monitoring` | Controls 1, 2, 4, 7, 8, 13, and 17 evidence for covered workloads | Reconcile CSW inventory with enterprise source of truth; endpoint, email, awareness, backup, and data controls are broader than CSW |
| NIST CSF 2.0 | CSF Profile outcomes, target tier, and management reporting needs | `CSF-Profile` > `Govern-Evidence`, `Identify-Assets`, `Protect-Segmentation`, `Detect-Monitoring`, `Respond-Dossier`, `Recover-Diff` | Technical evidence that feeds GV, ID, PR, DE, RS, and RC outcomes | CSF is an outcomes framework; CSW does not author the Profile or replace governance, risk appetite, or enterprise policy decisions |
| CMMC 2.0 | FCI/CUI enclave and CMMC assessment boundary | `CMMC-Scope` > `CUI-Enclave`, `FCI-Systems`, `CUI-Connected`, `Admin-Access`, `External-Services`, `Out-of-Scope-Validation` | AC, AU, CM, RA, SC, and SI technical evidence for CUI-scope workloads | CMMC requires SSP, POA&M, CUI scoping, and C3PAO/government assessment as applicable; CSW supports evidence but does not certify compliance |
| IEC 62443 | IT-side systems supporting IACS zones & conduits (engineering workstations, jump hosts, historians, brokers — not Level 0–2 OT devices) | `Industrial-IACS` > `Plant-OT-Support`, `Conduit-<id>`, `DMZ-Brokers`, `Vendor-Remote-Access` — labels mirror approved zone/conduit reference design | SR 5 restricted data flow; SR 1 access paths; SR 3 integrity baselines; SR 6–7 monitoring & availability signals for adjacent IT | CSW does not inspect ICS wire payloads on PLCs/RTUs/IEDs; pair with OT PAS (Cyber Vision, Claroty, Nozomi) and integrator-approved conduit tests |
| GDPR | Systems processing personal data, aligned to RoPA activity IDs and processor egress | `GDPR-In-Scope` > `ROPA-<activity>`, `Personal-Data-Tier`, `Sub-Processors-Egress` | Art. 25/32 technical measures (segmentation, monitoring, cleartext posture); Art. 30 flow corroboration; Art. 28 egress; breach forensics for Art. 33–34 (*legal owns filings*) | Lawful basis, DPIA sign-off, DSARs, records text fields, and Schrems II assessments remain legal/privacy-owned |
| MITRE ATT&CK | Enterprise detection & containment programme scoped to crown jewels and lateral choke points | `Enterprise-ATTCK` > `Tier0-Identity-Adjacent`, `Crown-Jewel-Apps`, `Jump-Host-Enclave`, `Internet-Facing-Entry` | Tactic-level evidence (TA0001–TA0011, TA0040) from flow/process telemetry plus segmentation containment | CSW is not full EDR/email/identity coverage — pair with SIEM, XDR/EDR, and hunting workflows |
| FedRAMP | FedRAMP Moderate (or agency) authorization boundary for a cloud system | `FedRAMP-InScope` > `Management-Plane`, `App-Tier`, `Data-Tier`, `Security-Monitoring` mapped to SSP components | AC-4 / SC-7 workload enforcement; CA-7 ConMon exports; CM/RA/SI/AU/IR technical attachments; POA&M-ready vuln rows | CSW the **product** is not itself FedRAMP-authorized; reconcile inheritance vs customer responsibility in the SSP; 3PAO validates |
| SWIFT CSCF | SWIFT secure zone & adjacent controlled interfaces per CSP architecture | `SWIFT-Program` > `SWIFT-Secure-Zone` (`Messaging-Interfaces`, `Operator-Jump-Hosts`) + `SWIFT-Adjacent` | CSCF 1.1 zone isolation; 1.4 internet egress restriction; 2.1 internal flows (ADM); 2.6 session confidentiality; 6.4 logging | Mandatory vs Advisory applicability follows **your** official CSCF v2024 matrix row; CSW does not complete CSP attestation |
| HITRUST CSF v11 | MyCSF assessment scope spanning harmonised baselines (HIPAA, ISO, NIST, PCI as cited in PRS) | `HITRUST-In-Scope` > `PHI-Production` (if applicable), `PCI-CDE-Connected`, `Enterprise-Critical` | 01.m/01.n/01.o segregation & connection control; 09.ab/09.ad monitoring & operator evidence; 10.a ADM; 10.m vuln; 11.a/11.c incident artefacts; e1/i1/r2 export depth per programme | Certification remains with HITRUST/assessor; confirm **exact PRS** keys in MyCSF |
| NIST SP 800-171 Rev. 3 | CUI systems and enclaves per SSP / CMMC assessment context | `CUI-Program` > `CUI-Enclave` > `CUI-Apps`, `CUI-Data`, `Security-Services`, `Non-CUI` | 03.01.03 information-flow enforcement; 03.13.06 deny-by-default; 03.03 audit telemetry; 03.04 baselines; 03.11 vuln reachability | Confirm **Rev. 2 vs. Rev. 3** baseline with PMO; administrative, physical, IdP, and FIPS modules remain complementary |
| CSA CCM v4 | Multicloud / hybrid services in CCM or CSA STAR scope | `CCM-STAR` > `Prod-Regulated`, `Shared-Services`, `Sandbox` (separate policy workspaces from prod) | IVS-09-style segmentation; DSP tier isolation; LOG / SIEM forwarding; TVM reachability; AIS interface inventory | Map each row to **shared responsibility** (customer vs CSP); HRS and pure programme attestations stay organisational |
| COBIT 2019 | IT governance assessments where technology evidence is required for DSS / BAI / MEA | `COBIT-Evidence` > `Production-Critical`, `Admin-Jump`, `Third-Party-Integration` | DSS05.02 connectivity security; APO13 managed security posture; MEA01/02 conformance exports; BAI06/10 change & configuration signals | Culture, HR, sourcing, and full SOx narratives remain outside CSW; attach evidence only to technology-addressable practices |
| SOX ITGC | Financially-relevant applications and the infrastructure supporting them, per the SOX scoping memo | `SOX-Relevant` > `Financial-Reporting-Core`, `Feeder-Systems`, `Supporting-Infrastructure`, `Admin-Access` + a deliberate `Non-SOX-Adjacent` scope for boundary proof | APD network-path restriction with Denied Connections across the period; production/non-production segregation; close-cycle ADM for AS 2201 flow of transactions; PC inventory deltas vs change tickets; CO batch and interface telemetry | **No official SOX control catalogue** — map to ITGC domains and COBIT, never invented SOX IDs. Baseline must span a **full month-end or quarter-end close**. Entitlement review, SoD in the application, MFA, change authorisation, SDLC, and attestation stay outside CSW |
| Australian Essential Eight | Organisations aligning to ACSC EEMM strategies E1–E8 | `E8-Scope` > `Crown-Jewels`, `Windows-Servers`, `Linux-Servers`, `Admins-Jump-Zone` | E2/E6 CVE+EPSS prioritisation; E5 admin-path restriction; E1/E4 complementary process telemetry | CSW does **not** replace allowlisting, Office macro policy, MFA, or backup programmes |
| UK Cyber Essentials Plus | UK organisations in Cyber Essentials **Plus** certification boundary | `UK-CE` > `CE-In-Scope-Production`, `Corporate-Standard`, `Partner-Connectivity` | CE1 workload-level firewall; CE2 inventory & drift; CE3 east-west least privilege; CE5 vuln backlog | Accredited assessor awards certification; CSW complements perimeter firewalls and AV/EDR |
| HIPAA Security Rule (2025 NPRM) | Covered entities / BAs planning for **proposed** Security Rule updates | `HIPAA-NPRM` > `PHI-Zone`, `Non-PHI-Enterprise`, `BA-Connectivity`, `SIEM-Archive` | §164.312(a)(2)(vi) segmentation (*proposed*); technology asset inventory; §164.308(a)(2) vuln programme; §164.312(b) 24-month log architecture (*proposed*) | **Proposed rule** only — reconcile with **final** FR text; maintain **current-rule** compliance until effective |
| MAS TRM | Singapore financial institution critical systems, customer-data systems, and outsourced/third-party dependencies | `MAS-TRM` > `Critical-Systems`, `Customer-Data`, `Security-Services`, `Outsourced-Third-Parties` | Critical-system inventory, network security, vulnerability, monitoring, incident, and outsourcing evidence | Board/senior management accountability, outsourcing due diligence, BCP/DR, IAM, and MAS reporting decisions remain customer-owned |
| APRA CPS 234 | Australian prudential information assets and material operations | `APRA-CPS234` > `Critical-Information-Assets`, `Material-Operations`, `Service-Providers`, `Incident-Evidence` | Information asset mapping, control testing, service-provider egress, and incident scoping evidence | CPS 234 governance, formal control testing, APRA notification, and supplier assurance remain risk/compliance-owned |
| NY DFS 23 NYCRR Part 500 | Covered systems, nonpublic-information applications, and third-party service-provider paths | `NYDFS-500` > `Covered-Systems`, `NPI-Applications`, `Critical-Operations`, `Third-Party-Service-Providers` | Covered-system inventory, least-privilege workload paths, vulnerability, monitoring/testing, and incident evidence | CISO governance, annual certification, written policies, encryption, MFA/IAM, and DFS notification decisions remain outside CSW |
| TISAX | Automotive prototype, engineering, customer-confidential, and supplier/customer connectivity scopes | `TISAX` > `Prototype-Protection`, `Engineering-Systems`, `Customer-Confidential`, `Supplier-Customer-Egress` | VDA ISA-aligned network segregation, supplier/customer egress, vulnerability, and logging evidence | Assessment objectives, physical prototype controls, DLP, IAM, supplier contracts, and TISAX assessment outcome remain complementary |
| NIST SP 800-82 | OT-adjacent IT systems that support industrial operations | `NIST-800-82` > `OT-Facing-IT`, `Industrial-DMZ`, `Jump-Hosts`, `Historians`, `Patch-Repositories`, `Vendor-Access` | OT-supporting IT segmentation, remote access paths, vulnerability, monitoring, and incident evidence | PLC/RTU/IED/HMI visibility and OT protocol inspection require Cyber Vision/Claroty/Nozomi/Dragos and plant change control |
| BSI C5 | Cloud service scope, tenant/shared services, customer-data stores, and supplier egress | `BSI-C5` > `Cloud-Service-Scope`, `Production-Service`, `Tenant-Shared-Services`, `Customer-Data-Stores`, `Supplier-Egress` | Cloud workload inventory, communication security, vulnerability handling, incident, and shared-service boundary evidence | C5 attestation, IAM/KMS, CSP controls, backup/DR, portability, and shared-responsibility decisions remain audit/customer-owned |

The following anchors match the framework links in the [table of contents](#table-of-contents) so you can jump directly to a row in the table above.

<h3 id="hipaa-security-rule">HIPAA Security Rule</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| ePHI applications, databases, clinical integrations, and business associate connections | `Healthcare-Org` > `ePHI-Zone` > app/service scopes such as `EHR`, `Billing`, `PACS`, `HL7`; separate `BAA-Partners` egress scope | ePHI workload isolation, access-path evidence, audit-control telemetry, risk-analysis inputs | HIPAA administrative, physical, legal, and BAA obligations remain outside CSW; validate PHI classification with privacy/compliance owners |

[↑ Back to top](#top)

<h3 id="soc-2-type-ii">SOC 2 Type II</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| The service organization's system boundary and selected Trust Services Criteria | `SOC2-System` > `Production`, `Supporting-Infra`, `Admin-Access`, `Vendor-Integrations`; align scope to system description | Operating-effectiveness evidence for segmentation, monitoring, change drift, incident investigation | SOC 2 criteria depend on the auditor's system description and control design; CSW augments IAM, change management, SIEM, and availability controls |

[↑ Back to top](#top)

<h3 id="pci-dss-v40">PCI DSS v4.0</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| Cardholder Data Environment (CDE), CDE-connected systems, and security-impacting systems | `PCI-Environment` > `CDE`, `CDE-Connected`, `Security-Services`, `Third-Party-Processors`, `Out-of-Scope-Validation` | CDE flow documentation, segmentation simulation/enforcement, policy exceptions, vulnerability exposure context | CSW does not replace QSA judgment, ASV scans, penetration testing, network security controls, or PCI governance requirements |

[↑ Back to top](#top)

<h3 id="nist-sp-800-53-rev-5">NIST SP 800-53 Rev. 5</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| FISMA/FedRAMP system boundary and SSP control implementation | `System-Boundary` > impact-level or component scopes such as `Moderate`, `High`, `Data-Store`, `App-Tier`, `Management` | AC, AU, CM, IR, RA, SC, and SI evidence for covered workloads | Full 800-53 scope includes many controls outside CSW: identity, personnel, physical, contingency, privacy, and governance controls |

[↑ Back to top](#top)

<h3 id="isoiec-270012022">ISO/IEC 27001:2022</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| ISMS scope, information assets, and Annex A control applicability | `ISMS-Boundary` > `Confidential-Data`, `Business-Critical-Apps`, `Cloud-Services`, `Supplier-Connections` | Annex A.8 monitoring, network security, segregation, vulnerability, and supplier-egress evidence | Certification depends on ISMS design, SoA, risk treatment, internal audit, and management review; CSW is a technical evidence source |

[↑ Back to top](#top)

<h3 id="cisa-zero-trust-maturity-model">CISA Zero Trust Maturity Model</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| Agency/enterprise zero-trust initiative by pillar and use case | `ZT-Workloads` > `Sensitive-Apps`, `Privileged-Admin`, `Inter-App-Flows`, `External-Dependencies` | Workload-layer evidence for networks and applications/workloads pillars, plus visibility and analytics | ZTMM maturity is organizational; pair CSW with IdP, MFA, device posture, data governance, SIEM/SOAR, and policy orchestration |

[↑ Back to top](#top)

<h3 id="fips-140">FIPS 140</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| Systems handling regulated cryptographic use or plaintext-protocol risk | `Crypto-Review` > `Sensitive-Transport`, `Plaintext-Protocol-Candidates`, `FIPS-Required-Systems` | Detection/blocking of obvious plaintext transports and inventory support for cryptographic usage review | CSW is not a FIPS-validated cryptographic module; validation, key management, and module selection belong to FIPS-validated libraries/HSMs |

[↑ Back to top](#top)

<h3 id="nist-sp-800-207">NIST SP 800-207</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| Zero Trust Architecture tenets for workload-to-workload access | `ZTA-Resources` > `Protected-Resources`, `Policy-Enforced-Flows`, `Observed-Dependencies`, `Exceptions` | Resource inventory, per-connection flow evidence, dynamic scoping, workload enforcement as one possible PEP placement | NIST ZTA also requires identity, device posture, policy decision architecture, and enterprise-wide telemetry beyond CSW |

[↑ Back to top](#top)

<h3 id="nist-sp-800-207a">NIST SP 800-207A</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| PDP/PEP/PA/PIP component mapping for a cloud-native ZTA discussion | `ZTA-Components` > `PEP-Analogue`, `Policy-Workspace`, `Telemetry-PIP`, `SOAR-Integrated` | Illustrative traceability from CSW policy, enforcement, and telemetry to 207A-style logical components | Treat PDP/PEP/PA/PIP mapping as an analogue for workload segmentation, not a complete enterprise ZTA architecture |

[↑ Back to top](#top)

<h3 id="dora">DORA</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| Important business functions (IBFs), supporting ICT assets, and third-party dependencies | `DORA-IBF` > one scope per IBF, with nested `Critical`, `Supporting`, `Third-Party-Egress`, `Incident-Dossier` scopes | Article 8 inventory inputs, Article 9 segmentation, Article 10 detection, Article 19 incident evidence, Article 28 technical egress | DORA governance, register of information, contracts, testing programme, and authority reporting remain customer-owned |

[↑ Back to top](#top)

<h3 id="nis2">NIS2</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| Essential/important entity services and Article 21 risk-management measures | `NIS2-Service` > `Essential-Service`, `Important-Service`, `Supplier-Egress`, `Incident-Reporting`, `High-Risk-Workloads` | Risk-policy enforcement evidence, incident dossier, supply-chain egress, vulnerability exposure, secured workload paths | MFA, training, governance, cryptography, secured voice/video, and national transposition specifics require complementary programmes |

[↑ Back to top](#top)

<h3 id="nerc-cip">NERC CIP</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| IT-side systems supporting BES Cyber System functions | `BES-Supporting-IT` > `EACMS`, `Jump-Hosts`, `Vendor-Access`, `BCSI-Hosts`, `Identity-PKI`, `Patch-Repos` | IT-side ESP boundary evidence, interactive remote access paths, ports/services baseline, vulnerability and change evidence | CSW is not an EAP and does not enforce on PLCs/RTUs/IEDs/HMIs; pair with boundary firewalls and OT-aware monitoring |

[↑ Back to top](#top)

<h3 id="tsa-pipeline-security-directive">TSA Pipeline Security Directive</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| IT-side systems supporting Critical Cyber Systems and IT/OT segmentation | `Pipeline-IT-Estate` > `OT-Facing-IT`, `CCS-Supporting-IT`, `Vendor-Access`, `Patch-Repositories`, `Corporate-IT` | IT-side segmentation, documented IT-to-OT flows, access control, monitoring, unpatched-system risk evidence | CSW does not replace the Cybersecurity Coordinator, CAP/CIRP, architecture review, boundary firewall, or OT DPI/monitoring tools |

[↑ Back to top](#top)

<h3 id="cis-controls-v81">CIS Controls v8.1</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | intersections and complementary controls |
|---|---|---|---|
| Enterprise assets and software in the customer's Implementation Group scope | `CIS-IG2` > `Enterprise-Assets`, `Software-Inventory`, `Secure-Config`, `Vuln-Exposure`, `Network-Monitoring` | Controls 1, 2, 4, 7, 8, 13, and 17 evidence for covered workloads | Reconcile CSW inventory with enterprise source of truth; endpoint, email, awareness, backup, and data controls are broader than CSW |

[↑ Back to top](#top)

<h3 id="nist-csf-20">NIST CSF 2.0</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| CSF Profile outcomes, target tier, and management reporting needs | `CSF-Profile` > `Govern-Evidence`, `Identify-Assets`, `Protect-Segmentation`, `Detect-Monitoring`, `Respond-Dossier`, `Recover-Diff` | Technical evidence that feeds GV, ID, PR, DE, RS, and RC outcomes | CSF is an outcomes framework; CSW does not author the Profile or replace governance, risk appetite, or enterprise policy decisions |

[↑ Back to top](#top)

<h3 id="cmmc-20">CMMC 2.0</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| FCI/CUI enclave and CMMC assessment boundary | `CMMC-Scope` > `CUI-Enclave`, `FCI-Systems`, `CUI-Connected`, `Admin-Access`, `External-Services`, `Out-of-Scope-Validation` | AC, AU, CM, RA, SC, and SI technical evidence for CUI-scope workloads | CMMC requires SSP, POA&M, CUI scoping, and C3PAO/government assessment as applicable; CSW supports evidence but does not certify compliance |

[↑ Back to top](#top)

<h3 id="iec-62443">IEC 62443</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| IT-side systems supporting IACS zones & conduits | `Industrial-IACS` > `Plant-OT-Support`, `Conduit-<id>`, `DMZ-Brokers`, `Vendor-Remote-Access` | SR 5 conduit enforcement; SR 1 access paths; SR 3 integrity; SR 6–7 monitoring signals on IACS-adjacent IT | OT device layer (PLCs/RTUs/IEDs) and safety systems require PAS/ICS tools and integrator lifecycle evidence; CSW does not replace them |

[↑ Back to top](#top)

<h3 id="gdpr">GDPR</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| Personal-data processing systems tied to RoPA activities & processor endpoints | `GDPR-In-Scope` > `ROPA-<activity>`, `Personal-Data-Tier`, `Sub-Processors-Egress` | Art. 25/32 technical measures; RoPA flow validation; processor egress monitoring; breach forensics inputs | Lawful basis, DPIA decisions, DSAR fulfilment, privacy notices, and supervisory filings require legal/privacy programme ownership |

[↑ Back to top](#top)

<h3 id="mitre-attck">MITRE ATT&CK</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| SOC / purple-team coverage for crown jewels and lateral movement choke points | `Enterprise-ATTCK` > `Tier0-Identity-Adjacent`, `Crown-Jewel-Apps`, `Jump-Host-Enclave`, `Internet-Facing-Entry` | TA0001–TA0011 & TA0040 tactic-aligned telemetry; segmentation containment; SIEM export discipline | Email, identity, kernel, and cloud-control-plane techniques require companion tooling (XDR/EDR, IdP logs, CSPM); publish a pairing matrix |

[↑ Back to top](#top)

<h3 id="fedramp">FedRAMP</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| FedRAMP authorization boundary components (Moderate emphasis) | `FedRAMP-InScope` > SSP-aligned `Management-Plane`, `App-Tier`, `Data-Tier`, `Security-Monitoring` | AC-4 / SC-7 workload enforcement narratives; CA-7 ConMon exports; CM/RA/SI families; POA&M-ready findings | Many Moderate controls are policy, personnel, physical, or IAM-console tasks; CSW product FedRAMP status is separate from **your** system ATO |

[↑ Back to top](#top)

<h3 id="swift-cscf">SWIFT CSCF</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| SWIFT secure zone messaging interfaces, operator paths, and adjacent collectors | `SWIFT-Program` > `SWIFT-Secure-Zone` > `Messaging-Interfaces`, `Operator-Jump-Hosts`, `Local-Logging-Forwarders` + `SWIFT-Adjacent` | Zone isolation (1.1); internet egress deny (1.4); internal flow evidence (2.1); cleartext controls (2.6); logging integrations (6.4) | Official Mandatory/Advisory/N/A comes from your CSCF v2024 applicability worksheet; password/MFA policy and CSP organisational tasks sit outside CSW |

[↑ Back to top](#top)

<h3 id="hitrust-csf-v11">HITRUST CSF v11</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| MyCSF in-scope systems with harmonised PRS references | `HITRUST-In-Scope` > `PHI-Production`, `PCI-CDE-Connected`, risk-tier labels | 01.m/01.n/01.o network segregation & routing visibility; 09.x monitoring & operator logs; 10.a ADM; 10.m vulnerabilities; 11.x incident evidence; assessment-level export cadence (e1/i1/r2) | HITRUST certification, SoA/risk register narratives, privacy legal controls, AV/EDR, authenticated scanning, and physical security remain complementary |

[↑ Back to top](#top)

<h3 id="nist-sp-800-171-rev-3">NIST SP 800-171 Rev. 3</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| CUI systems and enclaves per SSP / nonfederal organisation boundary | `CUI-Program` > `CUI-Enclave` > `CUI-Apps`, `CUI-Data`, `Security-Services`, `Non-CUI` | 03.01.03 CUI information-flow enforcement; 03.13.06 deny-by-default; 03.03 audit exports; 03.04 baseline drift; 03.11 reachability-aware risk inputs | Personnel, physical, training, formal assessments, IdP lifecycle, and crypto module validation stay outside CSW; confirm applicable **800-171 revision** |

[↑ Back to top](#top) · [↑ Framework mappings](#framework-mappings) · [↑ Table of contents](#table-of-contents)

<h3 id="csa-ccm-v40">CSA CCM v4.0</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| Hybrid / multicloud workloads under CCM or CSA STAR evidence | `CCM-STAR` > regulated prod tiers + segregated non-prod | IVS / IAM / DSP segmentation; LOG forwarding; TVM reachability exports; AIS dependency baselines | Classify **customer vs CSP** responsibility per row; STAR legal attestation and HR domains stay programme-owned |

[↑ Back to top](#top) · [↑ Framework mappings](#framework-mappings) · [↑ Table of contents](#table-of-contents)

<h3 id="cobit-2019">COBIT 2019</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| IT governance scope where DSS / BAI / MEA need technical artefacts | `COBIT-Evidence` > tiered production + admin jump + integrations | DSS05.02 network security; APO13 enforcement posture; MEA01/02 conformance views; BAI06/10 change & configuration diffs | Board culture, competencies, procurement contracts, and non-technical COBIT practices require other evidence |

[↑ Back to top](#top) · [↑ Framework mappings](#framework-mappings) · [↑ Table of contents](#table-of-contents)

<h3 id="australian-essential-eight">Australian Essential Eight</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| ACSC EEMM strategies with per-strategy ML targets | `E8-Scope` > crown jewels + server classes + admin jump zone | E2/E6 inventory & prioritisation; E5 admin-path enforcement; E1/E4 detection-oriented telemetry | Allowlisting (**E1**), macro policy (**E3**), MFA (**E7**), backups (**E8**) remain owned by dedicated tooling |

[↑ Back to top](#top) · [↑ Framework mappings](#framework-mappings) · [↑ Table of contents](#table-of-contents)

<h3 id="uk-cyber-essentials-plus">UK Cyber Essentials Plus</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| CE Plus in-scope production estate | `UK-CE` > `CE-In-Scope-Production` + corporate / partner scopes | CE1 workload firewall narrative; CE2 secure configuration drift; CE5 patch evidence | Accredited assessor certifies outcome; perimeter appliance config and AV/EDR still required |

[↑ Back to top](#top) · [↑ Framework mappings](#framework-mappings) · [↑ Table of contents](#table-of-contents)

<h3 id="hipaa-security-rule--2025-nprm">HIPAA Security Rule — 2025 NPRM</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| ePHI processing systems while planning for **proposed** rule changes | `HIPAA-NPRM` > `PHI-Zone` default deny vs `Non-PHI-Enterprise` + SIEM archive scope | §164.312(a)(2)(vi) microsegmentation (*proposed*); inventory & ADM map; vuln backlog; §164.312(b) SIEM/object-store retention (*proposed*) | **NPRM is not final law** — privacy office & counsel own interpretation; parallel **current** HIPAA compliance until effective |

[↑ Back to top](#top) · [↑ Framework mappings](#framework-mappings) · [↑ Table of contents](#table-of-contents)

<h3 id="mas-trm">MAS TRM</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| Singapore financial institution critical systems and outsourced service paths | `MAS-TRM` > `Critical-Systems`, `Customer-Data`, `Security-Services`, `Outsourced-Third-Parties` | Critical-system inventory, approved-flow baselines, third-party egress, vulnerability, monitoring, and incident evidence | MAS governance, outsourcing due diligence, BCP/DR, IAM, and reporting decisions remain outside CSW |

[↑ Back to top](#top) · [↑ Framework mappings](#framework-mappings) · [↑ Table of contents](#table-of-contents)

<h3 id="apra-cps-234">APRA CPS 234</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| Critical information assets and material operations for APRA-regulated entities | `APRA-CPS234` > `Critical-Information-Assets`, `Material-Operations`, `Service-Providers`, `Incident-Evidence` | Information asset mapping, control testing, service-provider egress, and incident scoping evidence | Formal control testing, APRA notification, supplier assurance, and governance remain customer-owned |

[↑ Back to top](#top) · [↑ Framework mappings](#framework-mappings) · [↑ Table of contents](#table-of-contents)

<h3 id="ny-dfs-23-nycrr-part-500">NY DFS 23 NYCRR Part 500</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| Covered systems, NPI applications, and third-party service-provider access | `NYDFS-500` > `Covered-Systems`, `NPI-Applications`, `Critical-Operations`, `Third-Party-Service-Providers` | Covered workload inventory, least-privilege paths, vulnerability, monitoring/testing, and incident evidence | CISO governance, annual certification, written policies, encryption, MFA/IAM, and DFS notifications remain complementary |

[↑ Back to top](#top) · [↑ Framework mappings](#framework-mappings) · [↑ Table of contents](#table-of-contents)

<h3 id="tisax">TISAX</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| Automotive prototype, engineering, customer-confidential, and supplier/customer connectivity scopes | `TISAX` > `Prototype-Protection`, `Engineering-Systems`, `Customer-Confidential`, `Supplier-Customer-Egress` | VDA ISA-aligned network segregation, supplier/customer egress, vulnerability, and logging evidence | TISAX assessment objectives, physical prototype controls, DLP, IAM, and supplier contracts remain complementary |

[↑ Back to top](#top) · [↑ Framework mappings](#framework-mappings) · [↑ Table of contents](#table-of-contents)

<h3 id="nist-sp-800-82">NIST SP 800-82</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| OT-adjacent IT systems that support industrial operations | `NIST-800-82` > `OT-Facing-IT`, `Industrial-DMZ`, `Jump-Hosts`, `Historians`, `Patch-Repositories`, `Vendor-Access` | OT-supporting IT segmentation, remote access, vulnerability, monitoring, and incident evidence | PLC/RTU/IED/HMI visibility and protocol inspection require OT-native tools and plant change controls |

[↑ Back to top](#top) · [↑ Framework mappings](#framework-mappings) · [↑ Table of contents](#table-of-contents)

<h3 id="bsi-c5">BSI C5</h3>

| Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|
| Cloud service scope, tenant/shared services, customer-data stores, and supplier egress | `BSI-C5` > `Cloud-Service-Scope`, `Production-Service`, `Tenant-Shared-Services`, `Customer-Data-Stores`, `Supplier-Egress` | Cloud workload inventory, communication security, vulnerability handling, incident, and shared-service boundary evidence | C5 attestation, IAM/KMS, CSP controls, backup/DR, portability, and shared-responsibility decisions remain outside CSW |

[↑ Back to top](#top) · [↑ Framework mappings](#framework-mappings) · [↑ Table of contents](#table-of-contents)

## Label / Tag Recommendations

### Baseline Labels for Every Customer

Use a small, consistent baseline across all frameworks. Keep values stable
and controlled; avoid free-form spelling differences that split evidence.

| Label key | Example values | Why it matters |
|---|---|---|
| `app` | `payments-api`, `ehr-core`, `identity` | Groups workloads into application scopes and ADM workspaces |
| `env` | `prod`, `stage`, `dev`, `test` | Separates production evidence from non-production noise |
| `owner` | `team-payments`, `clinical-apps`, `platform` | Connects policy exceptions and remediation to accountable teams |
| `data_class` | `public`, `internal`, `confidential`, `phi`, `pci`, `cui` | Drives regulated data boundaries and evidence queries |
| `compliance` | `hipaa`, `pci`, `soc2`, `dora`, `cmmc`, `none` | Enables framework-specific scopes without duplicating inventory |
| `criticality` | `critical`, `high`, `medium`, `low` | Supports prioritization, segmentation strictness, and incident response |
| `internet_exposed` | `true`, `false` | Helps identify boundary and attack-surface review candidates |
| `third_party` | `none`, `supplier-name`, `processor-name` | Supports supplier egress and business associate / processor reviews |
| `region` | `us-east`, `eu-west`, `site-001` | Supports residency, operational ownership, and sector/site reporting |
| `lifecycle` | `active`, `exception`, `decommissioning` | Keeps stale workloads and temporary exceptions visible |

[↑ Back to top](#top)

### Framework-Specific Labels

| Framework | Additional label keys | Example values | Scope-design use |
|---|---|---|---|
| HIPAA | `phi_scope`, `clinical_system`, `baa_partner`, `ehr_app` | `in-scope`, `epic`, `clearinghouse-a`, `true` | Build ePHI and partner-egress scopes |
| SOC 2 | `soc2_boundary`, `trust_service`, `system_component` | `in-scope`, `security`, `database` | Align workloads to the SOC 2 system description |
| PCI DSS v4.0 | `pci_scope`, `cde_zone`, `card_data_role`, `qsa_exception` | `cde`, `cde-connected`, `pan-storage`, `none` | Separate CDE, connected, and out-of-scope validation populations |
| NIST 800-53 | `system_id`, `impact_level`, `control_family`, `ssp_component` | `sys-001`, `moderate`, `ac`, `app-tier` | Tie workloads to SSP components and impact-level evidence |
| ISO 27001:2022 | `isms_scope`, `soa_control`, `asset_type`, `supplier_related` | `in-scope`, `a.8.22`, `database`, `true` | Align CSW evidence with the SoA and asset inventory |
| CISA ZTMM | `zt_pillar`, `zt_stage_target`, `zt_use_case` | `networks`, `advanced`, `east-west` | Organize evidence by maturity pillar and use case |
| FIPS 140 | `fips_required`, `crypto_review`, `plaintext_risk`, `module_owner` | `true`, `transport`, `high`, `platform` | Identify workloads needing crypto posture review |
| NIST 800-207 | `zta_resource`, `pep_candidate`, `policy_source`, `access_pattern` | `protected`, `csw-workload`, `adm`, `inter-app` | Trace workload resources and enforcement patterns |
| NIST 800-207A | `zta_component`, `pdp_analogue`, `pip_signal`, `pa_workspace` | `pep`, `csw-policy`, `vuln-context`, `zta-prod` | Support logical-component discussion and traceability |
| DORA | `dora_ibf`, `ibf_name`, `ibf_criticality`, `ict_third_party` | `true`, `sepa-transfer`, `critical`, `provider-a` | Build IBF and third-party exposure scopes |
| NIS2 | `nis2_entity_type`, `nis2_service`, `article21_measure`, `csirt_reportable` | `essential`, `health-service`, `21-2-b`, `true` | Structure service, measure, and incident evidence |
| NERC CIP | `cip_scope`, `bes_support_role`, `eacms`, `bcsi`, `ot_facing` | `it-side`, `jump-host`, `true`, `false`, `true` | Isolate IT-side BES-supporting systems and access paths |
| TSA Pipeline | `tsa_scope`, `ccs_function`, `site`, `ot_facing`, `vendor_access` | `it-side`, `historian`, `site-001`, `true`, `true` | Build site-specific IT/OT and vendor access scopes |
| CIS Controls v8.1 | `cis_control`, `implementation_group`, `asset_inventory_source` | `control-1`, `ig2`, `cmdb` | Organize evidence by Safeguard and Implementation Group |
| NIST CSF 2.0 | `csf_function`, `csf_category`, `profile_scope`, `target_tier` | `protect`, `pr.ir`, `core-platform`, `tier-3` | Align evidence with CSF Profile outcomes |
| CMMC 2.0 | `cmmc_level`, `cui_scope`, `fci_scope`, `assessment_boundary`, `poam_item` | `l2`, `in-scope`, `false`, `cui-enclave`, `poam-123` | Build CUI/FCI boundaries and C3PAO evidence sets |
| IEC 62443 | `zone`, `conduit`, `sl-target`, `ics-role` | `cell-a`, `c-ot-to-mes-01`, `SL2`, `historian` | Align policies to approved cyber zone / conduit drawings |
| GDPR | `ropa-id`, `data-class`, `processor`, `gdpr_scope` | `HR-001`, `personal`, `payroll-vendor`, `in` | Tie telemetry to RoPA activities and processor egress reviews |
| MITRE ATT&CK | `attack-surface`, `mitre_tactic_focus`, `crown_jewel` | `internet-facing`, `lateral-movement`, `true` | Scope detection baselines and containment narratives |
| FedRAMP | `ssp-component-id`, `data-impact`, `conmon_cadence` | `web-tier`, `moderate`, `monthly` | Map hosts to SSP attachments and ConMon rhythm |
| SWIFT CSCF | `swift_zone`, `swift_role`, `cscf_arch_type` | `secure`, `smc`, `A1` | Partition secure zone vs adjacent interfaces for CSP folders |
| HITRUST CSF | `hitrust_prs_ref`, `assessment_level`, `data-class` | `01.m`, `i1`, `phi` | Cross-walk exports to MyCSF requirement rows |
| NIST 800-171 Rev. 3 | `cui_scope`, `cui_role`, `enclave_id`, `data_class` | `in_scope`, `stores`, `ENCLAVE-A`, `cui` | Tie workloads to SSP components and CUI handling roles |
| CSA CCM v4 | `ccm_domain_focus`, `data_class`, `star_service` | `IVS,LOG`, `pci`, `SVC-042` | Align STAR services to CCM domain evidence |
| COBIT 2019 | `cobit_domain`, `service_tier`, `owner_team` | `DSS`, `tier1`, `platform-ops` | Route exports to objective owners |
| ACSC Essential Eight | `e8_strategy`, `admin_tier`, `internet_exposed` | `E5`, `tier0`, `true` | Build per-strategy ML evidence slices |
| UK Cyber Essentials Plus | `ce-scope`, `tier`, `owner` | `in`, `data`, `infra-team` | Maintain Plus assessment boundary labels |
| HIPAA 2025 NPRM | `nprm_scope`, `data_class`, `siem_retention_track` | `2025-planning`, `ephi`, `24-mo` | Track NPRM programme vs current-rule scopes |
| MAS TRM | `mas_critical_system`, `outsourcing_provider`, `customer_data_scope` | `true`, `provider-a`, `in-scope` | Build critical-system and third-party egress evidence |
| APRA CPS 234 | `critical_info_asset`, `material_operation`, `service_provider` | `customer-data`, `digital-channel`, `provider-a` | Tie workloads to critical assets and control-testing owners |
| NY DFS 23 NYCRR Part 500 | `nydfs_covered_system`, `npi_scope`, `third_party_provider` | `true`, `npi`, `processor-a` | Separate covered systems and nonpublic-information applications |
| TISAX | `tisax_scope`, `prototype_data`, `customer_confidential`, `supplier_link` | `in-scope`, `true`, `oem-a`, `supplier-b` | Support VDA ISA assessment slices and supplier/customer egress |
| NIST 800-82 | `ot_facing`, `purdue_level`, `site`, `ics_support_role` | `true`, `3.5`, `plant-01`, `historian` | Label OT-adjacent IT and plant-specific support paths |
| BSI C5 | `c5_scope`, `tenant_boundary`, `cloud_service`, `customer_data` | `in-scope`, `shared-service`, `svc-001`, `true` | Align cloud workload evidence to C5 service boundaries |

[↑ Back to top](#top)

## Workshop Output Checklist

By the end of a scope-design workshop, capture:

- The customer-owned authoritative inventory source and reconciliation owner.
- The CSW scope hierarchy for the selected framework.
- Required baseline labels and framework-specific labels.
- Initial values for regulated data, criticality, owner, and environment.
- Known gaps: unsupported workloads, missing connectors, uninstrumented OT,
  unmanaged SaaS, IAM-only controls, physical controls, or legal obligations.
- The first ADM / flow-search window and evidence export cadence.
- A named owner for label hygiene and exception review.

[↑ Back to top](#top)

## Customer Conversation Prompt

The practical question is not "can CSW map to this framework?" It is:

> Which workloads, flows, owners, and labels must be correct before the
> mapping becomes evidence a customer can validate with their assessor?

Use this guide to answer that question before building dashboards or
collecting audit packets.

[↑ Back to top](#top)
