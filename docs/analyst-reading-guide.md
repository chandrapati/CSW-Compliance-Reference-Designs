# Analyst reading guide — walking the compliance library

Use this when walking an industry analyst or reviewer through
[chandrapati/CSW-Compliance-Reference-Designs](https://github.com/chandrapati/CSW-Compliance-Reference-Designs).
It explains each report and reference design at the point a reader can misread the coverage label.

This library is a field mapping maintained for customer conversations. It is an evidence map, not a Cisco corporate attestation, not a certification, and not an analyst submission. Several older PDFs still say “Prepared by: Cisco Systems, Inc.” and “Cisco Confidential.” Say that those covers are templates. The current position is in the repository disclaimer: SME review is still required, and the mapping does not establish compliance.

## What to say first

Cisco Secure Workload watches workload-to-workload communication: which process talked to which host, on which port, whether policy permitted it, and what changed. The library takes that evidence and lines it up with a framework’s control language.

Two documents sit in every framework folder:

- The **report** is the narrative for a CISO, a GRC lead, or an assessor. It says which requirement the evidence can support and where another control still has to be filed.
- The **reference design** is the engineering view. It shows scope design, policy shape, and which export to pull. If a claim in the report is real, the steps are in the reference design.

Coverage in this library always means “evidence from instrumented workloads in the agreed scope.” It never means the organization is compliant, and it never means Secure Workload is the only control.

## Three labels, and they are not interchangeable

The library grew in three waves. The word on the page changes. The meaning below is the one to use in the room.

| What the page says | Where you will see it | What to say |
|---|---|---|
| **Full Coverage** | Older reports: HIPAA, SOC 2, PCI DSS, NIST 800-53, ISO 27001, FIPS 140, NIST 800-207, NIST 800-207A, parts of CISA ZTMM and NERC CIP | On workloads that have a reporting sensor and policy applied, Secure Workload can produce the artifact named for that row: policy, flows, inventory, or a forensic timeline. File that export against the control. The customer’s control owner and assessor still decide if it is enough. |
| **Partial Coverage** | Same older reports, plus NERC | Secure Workload covers one slice. File the export next to the other record (identity, firewall, patch install, written analysis, physical security, OT tool). |
| **Evidence Required** | HIPAA, PCI DSS, NERC CIP | Secure Workload does not produce the record. The customer files a contract, a written analysis, a test method, or an HR or physical-security file. |
| **Direct** | Newer narrative reports: DORA, NIS2, NERC, TSA, CIS, CSF 2.0, CMMC, and the CAF mapping | Secure Workload is a primary technical evidence source for that requirement on the IT side. Direct is still evidence, not a pass. |
| **Supporting** | Same newer reports | Another control owns the requirement. Secure Workload strengthens the file. |
| **Out of scope** | Same newer reports, and the “Out of Scope” section in the generated reports | The evidence lives in another programme. Secure Workload has nothing to export for that requirement. |
| **In scope / Out of scope** | Generated reports: FedRAMP, GDPR, HITRUST, SWIFT, 800-171, CSA CCM, COBIT, Essential Eight, Cyber Essentials, MAS TRM, APRA, NY DFS, TISAX, 800-82, IEC 62443, BSI C5, MITRE ATT&CK, HIPAA 2025 NPRM | The report already separates what can be collected from what must be evidenced elsewhere. Read the Out of Scope list before the capability map. |

When an older report says “Full Coverage” on a governance or identity row, use the Partial reading in this guide. The PDF has not been re-scored. Saying the accurate slice is better than letting “Full” stand as “the control is met.”

## Older reports — the label is the unclear part

### HIPAA Security Rule

- **Report.** Walks administrative, physical, technical, and organizational safeguards and names the export for each.
- **Reference design.** Builds the ePHI scope tree, the allowlist, and the quarterly evidence pack.
- **Unclear label.** Administrative safeguards and technical safeguards are marked Full Coverage. Physical is Partial. Organizational requirements and the business-associate contract are Evidence Required.
- **Say this.** Full on the technical side means workload allowlists, flow and process audit trails, and forensic timelines for systems that hold ePHI. The written risk analysis, sanctions, workforce training, and the business-associate agreement are still the covered entity’s. Physical safeguards stay with facilities. The Epic microsegmentation guide is the practitioner companion for EHR tier design. It is a product pattern, not a named-customer write-up.

### HIPAA 2025 NPRM

- **Report.** Maps the *proposed* Security Rule changes: mandatory segmentation, a wider asset inventory, longer audit retention, a 72-hour breach timeline, and an annual technical assessment.
- **Reference design.** Shows how to collect those inputs if the proposal is what the customer is planning against.
- **Unclear point.** A proposed rule is not the rule in force.
- **Say this.** Re-read this pair against the final rule before anyone relies on it. Secure Workload can supply segmentation, inventory, and timeline evidence. It does not make the breach-notification decision, write the risk analysis, or manage the BAA.

### SOC 2 Type II

- **Report.** Maps selected Trust Services Criteria, mainly CC6, CC7, CC8, CC9, A1, and C1. Every row in that table says Full Coverage.
- **Reference design.** Shows the operating-effectiveness exports an auditor can sample across the period: policy, denied flows, change diffs, and monitoring.
- **Unclear label.** “Full Coverage” on all ten rows reads as “SOC 2 is done.”
- **Say this.** Those rows are the workload evidence inside the system the service organization describes. The system description, the control design, and the auditor’s sample are still the organization’s. Availability in this table is sensor and telemetry continuity, not the business-continuity programme. Confidentiality is scope isolation and plaintext-path detection, not data classification.

### PCI DSS v4.0

- **Report.** Maps Requirements 1, 6.3.3, 7.2.1, 10, 11.3.1, 11.4.1, and 12.3.2.
- **Reference design.** Designs the CDE scope, default-deny in and out, and the QSA evidence pack.
- **Unclear label.** Most rows say Full Coverage. Penetration testing (11.4.1) is Partial. Targeted risk analysis (12.3.2) is Evidence Required. The executive summary says Secure Workload “directly satisfies” five requirements.
- **Say this.** The QSA can sample CDE segmentation, allowed flows, and workload logs from the exports. Secure Workload does not replace the QSA, the penetration test, or the written targeted risk analysis. Vulnerability “Full Coverage” is inventory and prioritization on instrumented systems. The patch install and the compensating-control write-up stay with the customer. Validate the defined or customized approach with the QSA.

### NIST SP 800-53 Rev 5

- **Report.** Maps 18 controls in AC, AU, CM, IR, RA, SC, and SI. The opening line says Full Coverage across all 18. The impact-level table marks Low / simulation-only as Partial.
- **Reference design.** Shows how those 18 are configured and which export feeds a POA&M or a continuous-monitoring package.
- **Unclear label.** “All 18” can be heard as “all of 800-53.”
- **Say this.** The 18 are the workload-relevant controls in those families: flow enforcement, least privilege on the network path, audit content, inventory, boundary protection, and monitoring. Simulation mode is design evidence, not enforcement proof. Identity, privacy, physical security, and the authorization package sit outside this table.

### ISO/IEC 27001:2022

- **Report.** Maps selected Annex A controls, mostly A.5 and A.8. Most rows say Full Coverage. Security testing (A.8.29), secure coding (A.8.28), and data masking (A.8.11) are Partial.
- **Reference design.** Turns network segregation, logging, and supplier egress into scope design and exports.
- **Unclear label.** Annex A coverage can be heard as ISMS certification.
- **Say this.** The Full rows are network security, segregation, logging, monitoring, and inventory-style evidence. Secure coding, security testing, and data masking need the SDLC, the test team, and data-protection controls beside the export. Clauses 4 through 10 — context, leadership, internal audit, management review, and the certificate — are not in the table.

### FIPS 140

- **Report.** Lists cleartext protocols Secure Workload can see and block, and a FIPS-boundary scope around cryptographic services. Almost every detection row says Full Coverage. TLS 1.0/1.1 is Partial.
- **Reference design.** Builds the plaintext-protocol deny rules and the boundary scope.
- **Unclear label.** “FIPS 140 compliance” can be heard as “the module is FIPS validated.”
- **Say this.** Secure Workload can show a cleartext flow and deny it, and it can restrict which workloads reach a crypto service. It is not the cryptographic module. Confirming TLS version and cipher suite still needs the module or endpoint configuration. Programme ownership of FIPS 140-3 transition stays with the customer.

### NIST SP 800-207

- **Report.** Scores the seven Zero Trust tenets. Tenets 1 through 5 and 7 say Full Coverage. Tenet 6 says Partial, and the report explains why.
- **Reference design.** Places the sensor as one policy-enforcement point and collects the tenet evidence.
- **Unclear label.** Six Full tenets can be heard as a complete zero-trust architecture.
- **Say this.** Full here is the workload tier: every instrumented host is a resource, communications can be held to an allowlist, and telemetry is continuous. Tenet 6 is partial because Secure Workload can force the path through LDAPS or Kerberos and can see a bypass. It does not evaluate the identity, the session, or step-up authentication. Pair identity with the IdP and a ZTNA control such as Cisco Secure Access.

### NIST SP 800-207A

- **Report.** Maps PDP, PEP, PA, and PIP, then three use cases. Most component rows say Full Coverage. The subject, agentless cloud coverage, and identity-aware partner access are Partial. Treat the component model as draft-derived and confirm the NIST text in force.
- **Reference design.** Traces one access decision through those components using workload policy.
- **Unclear label.** “Full Coverage” on the PDP can be heard as “Secure Workload is the enterprise policy decision point.”
- **Say this.** For workload-to-workload allow and deny, the policy engine decides, the sensor enforces, the workspace records the change, and telemetry informs the decision. The requesting user’s identity proof, and any partner identity proof, stay with the IdP. Agentless cloud connectors provide flow visibility. Enforcement on those workloads still needs a sensor or the cloud-native control.

### CISA Zero Trust Maturity Model

- **Report.** Scores five pillars and a path from Traditional toward Optimal. Networks and Applications & Workloads are marked Full. Data is marked Full in the summary table even though the role column says Supporting. Identity and Devices are Partial.
- **Reference design.** Stages the network pillar from visibility, to microsegmentation, to ongoing policy review, and says what the other pillars still need.
- **Unclear label.** “Advanced → Optimal” can be heard as Optimal on every pillar.
- **Say this.** The workload and network path is where Secure Workload can show progression. Identity, device health, and data governance remain other pillars. Optimal is a maturity description of that workload slice after enforcement and continuous review, not a score of the whole architecture.

## Narrative reports — Direct, Supporting, and out of scope

These reports already contain a posture table and an out-of-scope section. The unclear part is treating Direct as a pass, and treating the IT-side sentence as coverage of the OT device.

### DORA (EU 2022/2554)

- **Report.** Articles 8, 9, 10, and 19 for ICT inventory, segregation, detection, and the incident file, plus Article 28 egress to third parties.
- **Reference design.** Builds one scope per important business function and the dossier export.
- **Say this.** The register of information, contracts, the threat-led testing programme, and the report to the competent authority stay with the financial entity. Secure Workload fills the technical annex: what talked to what, and what was denied.

### NIS2 (EU 2022/2555)

- **Report.** Article 21(2) risk-management measures and Article 23 timelines. Monitoring evidence is Article 21(2)(b).
- **Reference design.** Collects the 24-hour, 72-hour, and one-month dossier inputs from flow and process history.
- **Say this.** Secure Workload can show segmentation, logging, vulnerability context, and supplier egress. It does not make the authority notification, and it does not transpose the directive. National law is what the entity is assessed against.

### UK NCSC CAF v3.2

- **Report.** Customer narrative for NIS operators of essential services and GovAssure.
- **Reference design.** How to collect the evidence. **caf-mapping.md** is the 14-principle crosswalk. The maturity scorer and the evidence-pack template sit beside them.
- **Unclear point.** CAF has 14 principles. Only one outcome is direct evidence.
- **Say this.** Direct evidence is B5.b only: segregation of essential-function systems from other business systems, shown with policy and denied connections. Achieved for B5.b still expects separate infrastructure, independent administration, and no browsing or email from those systems. A1, A2, A3, A4, B1, B3, B4, C1, C2, D1, and D2 are supporting. B2 identity and B6 staff awareness are out of scope. CAF v3.2 does not name eBPF, NetFlow, or IEC 62443. An export does not, by itself, move a principle to Achieved. This set is draft and needs SME review.

### UK Cyber Essentials Plus

- **Report.** Control themes for firewalls, secure configuration, security-update management, and what a Plus technical check can sample.
- **Reference design.** Produces the workload-firewall and patch-priority evidence.
- **Say this.** Secure Workload can show workload firewall policy, configuration drift, and which vulnerable software is reachable. Malware protection, user access control, the questionnaire, and the IASME certification decision stay outside it. Plus testing is the assessor’s.

### NERC CIP

- **Report.** Two tables. The posture table is Direct, Supporting, or out of scope. The control coverage summary is Full, Partial, or Evidence Required, and it includes CIP-007 R5, CIP-012, and CIP-015.
- **Reference design.** IT-side ESP approach, interactive remote access evidence, ports and baseline, and the same coverage column.
- **Say this.** Full Coverage is only CIP-007 R1 (listening ports) and CIP-010 R1 (baseline and change disposition) on instrumented IT-side hosts. CIP-012 shows paths between instrumented control-center workloads. The entity still files the CIP-012 plan and the protection on that link. Secure Workload is not an Electronic Access Point and does not enforce on PLCs, RTUs, IEDs, or HMIs. Evidence Required with no Secure Workload artifact: CIP-004, CIP-006, and CIP-014. Draft, pending a NERC CIP specialist review.

### TSA Pipeline Security Directive

- **Report.** IT-side reading of the 2021-02 series: segmentation, access, monitoring, unpatched-system risk, and incident and assessment packs.
- **Reference design.** Builds the IT-to-OT-facing scopes and the evidence for Sections III.A through III.D.
- **Say this.** The boundary firewall, the Cybersecurity Coordinator, the architecture review, the incident plan, and OT protocol inspection stay with the operator. Secure Workload hardens the IT side up to that boundary. It does not inspect DNP3, IEC 61850, Modbus, or OPC-UA, and it does not enforce on pipeline OT devices. Draft.

### IEC 62443

- **Report.** Zones and conduits as scope and policy for IT-side systems that face the industrial network.
- **Reference design.** Designs those zones and the evidence for the security requirements Secure Workload can actually record.
- **Say this.** This is not an IEC 62443 certification. OT device security requirements and OT protocol inspection belong with an OT product such as Cyber Vision, Claroty, Nozomi, or Dragos.

### NIST SP 800-82

- **Report.** OT-adjacent IT: historians, engineering workstations, jump hosts, patch servers, and vendor access.
- **Reference design.** Scopes that tier and records the flows across the IT/OT boundary from the IT side.
- **Say this.** Same boundary as IEC 62443. Secure Workload does not parse Modbus, DNP3, S7, or OPC UA, and it does not replace the OT programme.

## Generated reports — read Out of Scope before the map

Each of these reports already has an executive summary, a scope picture, an in-scope list, an out-of-scope list, a topic map, and a collection cadence. The reference design is the same folder’s engineering steps. The unclear part is leading with the topic map and skipping the boundary paragraph.

| Framework | Report argues | Reference design does | Say this when it is unclear |
|---|---|---|---|
| **NIST CSF 2.0** | Outcomes, not a control catalogue. Direct on asset, risk, protection, detection, and response subcategories that workload telemetry can evidence. Govern and Recover are supporting. | How to produce the evidence pack for those subcategories. | A subcategory mapping is not a Profile, and it is not an implementation of every Informative Reference. Draft. |
| **CIS Controls v8.1** | Direct on Controls 1, 2, 4, 7, 8, and 13 at the workload tier. Written at Implementation Group 2, with IG1 and IG3 called out. | Safeguard-level collection for those controls. | Controls 5, 9, 11, and 14, plus HR and physical safeguards, are out of scope. Secure Workload feeds a SIEM. It is not the SIEM. Draft. |
| **CMMC 2.0** | Level 2 lead, because Level 2 is NIST 800-171. Direct on AC, AU, CM, RA, SC, and SI. | CUI-scope labels and the evidence an assessor can sample. | Secure Workload does not write the SSP or POA&M and does not perform the C3PAO assessment. AT, MP, PE, and PS stay with HR, media, and physical security. Draft. |
| **NIST SP 800-171 Rev 3** | CUI enclave isolation and the 03.01 and 03.13 flow-enforcement requirements. | The enclave scope and the family evidence. | Marking, the contract clauses, the SSP, media protection, and FIPS-validated encryption stay with the contractor. This underpins CMMC Level 2. It is not the assessment. |
| **FedRAMP Moderate** | Workload evidence for AC-4, SC-7, CA-7, and SI-4 inside a Moderate baseline. | ConMon-style exports and POA&M inputs. | Secure Workload does not grant an authority to operate, replace the 3PAO, or own the SSP. |
| **GDPR** | Article 32 security-of-processing evidence, Article 30 flow inputs, Articles 33 and 34 timeline inputs, Article 28 processor egress. | How to export those four evidence sets. | Lawful basis, consent, data-subject rights, transfer tools, the DPO, and the notification decision stay with the controller. |
| **HITRUST CSF v11** | Segregation, vulnerability reachability, monitoring, and incident evidence that several authoritative sources ask for in similar words. | One collection path that can be shown against the harmonized control. | The assessor’s score and the certification submission are HITRUST’s and the customer’s. Identity, encryption, and physical controls stay outside. |
| **SWIFT CSCF v2024** | Secure-zone isolation, restricted internet and enterprise paths, and logging around the SWIFT zone. | The zone scope and the operator-session and egress evidence. | Secure Workload is not the SWIFT interface, not the attestation, and not operator credential management. |
| **CSA CCM v4** | Cloud workload evidence for infrastructure security, data isolation, and vulnerability reachability. | Scope and exports a STAR conversation can use as technical support. | STAR submission, key management, and the shared-responsibility split stay with the provider and the customer. |
| **COBIT 2019** | Technical inputs to DSS05, APO13, MEA01 and MEA02, and change and configuration objectives. | The exports a process owner can attach to those practices. | COBIT design factors, goals, risk appetite, and audit judgement stay with the enterprise. |
| **Australian Essential Eight** | Patch priority from exposure, and administrative-path restriction. Some support for application-control questions from observed processes. | ML1–ML3 evidence for the strategies Secure Workload can actually see. | Application control, macro hardening, MFA, and backups are not Secure Workload strategies. Maturity judgement stays with the customer against the ACSC model. |
| **MAS TRM** | Critical-system segmentation, asset evidence, outsourcing egress, and incident scope for a Singapore financial institution. | The scope tree and the supervisory evidence pack. | Board accountability, the technology-risk framework, IAM, cryptography decisions, and the MAS notification stay with the institution. |
| **APRA CPS 234** | Information-asset segmentation, control testing inputs, and service-provider visibility. | The evidence for implementation and for testing. | Board accountability, the policy framework, and the APRA notification decision stay with the APRA-regulated entity. |
| **NY DFS 23 NYCRR 500** | Covered-system visibility, nonpublic-information scope, vulnerability context, and third-party egress. | The monitoring and audit-trail exports. | The CISO function, MFA, the risk assessment, the 72-hour notice, and the annual certification stay with the covered entity. |
| **TISAX / VDA ISA** | Prototype and confidential engineering workloads segmented, with supplier and customer egress visible. | The assessment evidence for those network and data-flow questions. | TISAX labels, physical prototype handling, and the ENX assessment stay outside. |
| **BSI C5** | Tenant and shared-service boundaries, cloud communication security, and incident evidence a cloud provider can show. | The OPS, KOS, and asset exports. | C5 attestation, physical controls, key management, and portability claims stay with the cloud provider. |
| **MITRE ATT&CK** | A tactic map for workload-visible behavior, especially lateral movement, discovery, command-and-control egress, and exfiltration paths. | Which forensic rules and flow questions line up to which tactics. | ATT&CK is not a compliance framework. Secure Workload is one telemetry source. Email, identity, and endpoint malware analysis stay with the SOC’s other tools. |

## How to close

Offer one framework the analyst cares about, open the reference design, and show one export path from sensor to the artifact named in the report. Then show the out-of-scope or Partial row for that same framework. That pair is the argument: continuous workload evidence, with the rest of the control still owned by the customer and the assessor.
