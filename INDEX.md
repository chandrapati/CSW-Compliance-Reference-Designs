# Control-ID Index

A lookup index across all thirty-five frameworks in this repository.
Use it to jump from a specific control / requirement / article to the
reference design section that explains how Cisco Secure Workload (CSW)
supports evidence for it.

> **Linking convention.** Most links point to the reference design root rather
> than a specific anchor — section anchors aren't stable across
> renderers. Once on the page, your browser's *Find* (Ctrl/Cmd+F) on
> the control ID is the fastest way to land in the right paragraph.

> **Why no entries for some controls?** A blank cell or omission means
> the control is intentionally outside CSW's scope (e.g., physical
> access, training, cryptographic primitives). The relevant reference design
> calls these out explicitly.

---

## Quick start by question

| If you're asking… | Start here |
|---|---|
| "How do I prove my segmentation actually works?" | [PCI Req 1](./PCI-DSS-v4/CSW-PCI-DSS-Reference-Design.md), [HIPAA §164.312(a)(1)](./HIPAA/CSW-HIPAA-Reference-Design.md), [NIST AC-4](./NIST-800-53/CSW-NIST-800-53-Reference-Design.md), [DORA Art. 9](./DORA/CSW-DORA-Reference-Design.md), [NERC CIP-005 R1](./NERC-CIP/CSW-NERC-CIP-Reference-Design.md), [TSA SD Section III.A](./TSA-Pipeline/CSW-TSA-Pipeline-Reference-Design.md), [TSA Rail III.B](./TSA-Rail/CSW-TSA-Rail-Reference-Design.md), [IEC 62443 SR 5.1–5.4](./IEC-62443/CSW-IEC62443-Reference-Design.md), [GDPR Art. 25 / Art. 32](./GDPR/CSW-GDPR-Reference-Design.md), [FedRAMP AC-4 / SC-7](./FedRAMP/CSW-FedRAMP-Reference-Design.md), [SWIFT CSCF 1.1](./SWIFT-CSCF/CSW-SWIFT-CSCF-Reference-Design.md), [HITRUST 01.m](./HITRUST-CSF/CSW-HITRUST-Reference-Design.md), [CIS Safeguard 13.4](./CIS-Controls-v8/CSW-CIS-Reference-Design.md), [CSF PR.IR-01](./NIST-CSF-2/CSW-CSF-Reference-Design.md), [CMMC SC.L2-3.13.1 / 3.13.6](./CMMC-2/CSW-CMMC-Reference-Design.md), [NIST 800-171 03.01.03 / 03.13.06](./NIST-800-171/CSW-NIST-800-171-Reference-Design.md), [HIPAA NPRM §164.312(a)(2)(vi)](./HIPAA-2025-NPRM/CSW-HIPAA-NPRM-Reference-Design.md), [UK CE1](./UK-Cyber-Essentials/CSW-Cyber-Essentials-Reference-Design.md), [AU E5](./AU-Essential-Eight/CSW-Essential-Eight-Reference-Design.md), [CSA IVS-09](./CSA-CCM/CSW-CSA-CCM-Reference-Design.md) |
| "How do I demonstrate continuous monitoring?" | [NIST CA-7 / SI-4](./NIST-800-53/CSW-NIST-800-53-Reference-Design.md), [PCI Req 11](./PCI-DSS-v4/CSW-PCI-DSS-Reference-Design.md), [SOC 2 CC7.2](./SOC2/CSW-SOC2-Reference-Design.md), [NIS2 Art. 21(2)(b)](./NIS2/CSW-NIS2-Reference-Design.md), [NERC CIP-007 R4](./NERC-CIP/CSW-NERC-CIP-Reference-Design.md), [TSA SD Section III.C](./TSA-Pipeline/CSW-TSA-Pipeline-Reference-Design.md), [TSA Rail III.D](./TSA-Rail/CSW-TSA-Rail-Reference-Design.md), [FedRAMP CA-7 / SI-4](./FedRAMP/CSW-FedRAMP-Reference-Design.md), [IEC 62443 SR 6](./IEC-62443/CSW-IEC62443-Reference-Design.md), [SWIFT CSCF 6.4](./SWIFT-CSCF/CSW-SWIFT-CSCF-Reference-Design.md), [HITRUST 09.ab](./HITRUST-CSF/CSW-HITRUST-Reference-Design.md), [CIS Safeguards 13.1 / 13.6](./CIS-Controls-v8/CSW-CIS-Reference-Design.md), [CSF DE.CM-01 / DE.CM-09](./NIST-CSF-2/CSW-CSF-Reference-Design.md), [CMMC SI.L2-3.14.6](./CMMC-2/CSW-CMMC-Reference-Design.md), [COBIT MEA01 / MEA02](./COBIT-2019/CSW-COBIT-Reference-Design.md), [CSA LOG](./CSA-CCM/CSW-CSA-CCM-Reference-Design.md) |
| "How do I produce an incident-reporting evidence pack?" | [DORA Art. 19](./DORA/CSW-DORA-Reference-Design.md), [NIS2 Art. 23](./NIS2/CSW-NIS2-Reference-Design.md), [HIPAA §164.308(a)(6)](./HIPAA/CSW-HIPAA-Reference-Design.md), [GDPR Art. 33–34](./GDPR/CSW-GDPR-Reference-Design.md), [NERC CIP-008](./NERC-CIP/CSW-NERC-CIP-Reference-Design.md), [TSA CIRP / 24-hour CISA](./TSA-Pipeline/CSW-TSA-Pipeline-Reference-Design.md), [SWIFT CSCF 7.1](./SWIFT-CSCF/CSW-SWIFT-CSCF-Reference-Design.md), [HITRUST 11.a / 11.c](./HITRUST-CSF/CSW-HITRUST-Reference-Design.md), [CIS Control 17](./CIS-Controls-v8/CSW-CIS-Reference-Design.md), [CSF RS.AN-03 / RS.AN-07](./NIST-CSF-2/CSW-CSF-Reference-Design.md), [CMMC IR.L2-3.6.x](./CMMC-2/CSW-CMMC-Reference-Design.md), [HIPAA NPRM §164.308(a)(6)](./HIPAA-2025-NPRM/CSW-HIPAA-NPRM-Reference-Design.md) |
| "How do I show my supply chain / third-party exposure?" | [DORA Art. 28](./DORA/CSW-DORA-Reference-Design.md), [NIS2 Art. 21(2)(d)](./NIS2/CSW-NIS2-Reference-Design.md), [GDPR Art. 28](./GDPR/CSW-GDPR-Reference-Design.md), [ISO A.5.19–A.5.22](./ISO-27001-2022/CSW-ISO27001-Reference-Design.md), [NERC CIP-013](./NERC-CIP/CSW-NERC-CIP-Reference-Design.md), [CIS Control 15](./CIS-Controls-v8/CSW-CIS-Reference-Design.md), [CSF GV.SC-04 / GV.SC-07](./NIST-CSF-2/CSW-CSF-Reference-Design.md) |
| "Where does CSW fit in a Zero Trust architecture?" | [NIST 800-207 Tenets](./NIST-800-207/CSW-NIST-800-207-Reference-Design.md), [NIST 800-207A PDP/PEP/PA/PIP](./NIST-800-207A/CSW-NIST-800-207A-Reference-Design.md), [CISA ZTMM](./CISA-ZeroTrust/CSW-CISA-ZTMM-Reference-Design.md), [FedRAMP AC-4 / SC-7 (workload tier)](./FedRAMP/CSW-FedRAMP-Reference-Design.md), [CSF PR.IR / PR.AA](./NIST-CSF-2/CSW-CSF-Reference-Design.md) |
| "How do I evidence vulnerability management?" | [PCI Req 6, 11.3](./PCI-DSS-v4/CSW-PCI-DSS-Reference-Design.md), [NIST RA-5](./NIST-800-53/CSW-NIST-800-53-Reference-Design.md), [ISO A.8.8](./ISO-27001-2022/CSW-ISO27001-Reference-Design.md), [NIS2 Art. 21(2)(e)](./NIS2/CSW-NIS2-Reference-Design.md), [NERC CIP-010 R3](./NERC-CIP/CSW-NERC-CIP-Reference-Design.md), [TSA SD Section III.D](./TSA-Pipeline/CSW-TSA-Pipeline-Reference-Design.md), [FedRAMP RA-5](./FedRAMP/CSW-FedRAMP-Reference-Design.md), [HITRUST 10.m](./HITRUST-CSF/CSW-HITRUST-Reference-Design.md), [IEC 62443 SR 3](./IEC-62443/CSW-IEC62443-Reference-Design.md), [CIS Control 7](./CIS-Controls-v8/CSW-CIS-Reference-Design.md), [CSF ID.RA-01 / ID.RA-05](./NIST-CSF-2/CSW-CSF-Reference-Design.md), [CMMC RA.L2-3.11.2 / 3.11.3](./CMMC-2/CSW-CMMC-Reference-Design.md), [AU E2 / E6](./AU-Essential-Eight/CSW-Essential-Eight-Reference-Design.md), [UK CE5](./UK-Cyber-Essentials/CSW-Cyber-Essentials-Reference-Design.md), [CSA TVM](./CSA-CCM/CSW-CSA-CCM-Reference-Design.md), [HIPAA NPRM §164.308(a)(2)](./HIPAA-2025-NPRM/CSW-HIPAA-NPRM-Reference-Design.md) |
| "How do I evidence IT/OT segmentation on the IT side?" | [NERC CIP-005 R1 (IT-side ESP enclave)](./NERC-CIP/CSW-NERC-CIP-Reference-Design.md), [TSA SD Section III.A](./TSA-Pipeline/CSW-TSA-Pipeline-Reference-Design.md), [TSA Rail III.B](./TSA-Rail/CSW-TSA-Rail-Reference-Design.md), [IEC 62443 SR 5 (zones & conduits)](./IEC-62443/CSW-IEC62443-Reference-Design.md), [NIST AC-4 / SC-7](./NIST-800-53/CSW-NIST-800-53-Reference-Design.md) |
| "How do I map workload telemetry to MITRE ATT&CK?" | [TA0001–TA0011, TA0040](./MITRE-ATTACK/CSW-MITRE-ATTACK-Reference-Design.md) |
| "How do I evidence a SWIFT secure zone at the workload layer?" | [SWIFT CSCF 1.1 / 1.4 / 2.1](./SWIFT-CSCF/CSW-SWIFT-CSCF-Reference-Design.md) |
| "How do I evidence asset and software inventory?" | [CIS Controls 1 + 2](./CIS-Controls-v8/CSW-CIS-Reference-Design.md), [NIST CM-8](./NIST-800-53/CSW-NIST-800-53-Reference-Design.md), [CSF ID.AM-01 / ID.AM-02](./NIST-CSF-2/CSW-CSF-Reference-Design.md), [CMMC CM.L2-3.4.1 / 3.4.6](./CMMC-2/CSW-CMMC-Reference-Design.md), [HIPAA NPRM §164.308(a)(1)(ii)(A)](./HIPAA-2025-NPRM/CSW-HIPAA-NPRM-Reference-Design.md), [NIST 800-171 03.04.x](./NIST-800-171/CSW-NIST-800-171-Reference-Design.md) |
| "How do I evidence governance to my management body?" | [DORA Art. 5](./DORA/CSW-DORA-Reference-Design.md), [NIS2 Art. 20](./NIS2/CSW-NIS2-Reference-Design.md), [CSF GV.OV-01/02/03](./NIST-CSF-2/CSW-CSF-Reference-Design.md), [SOC 2 CC4.1](./SOC2/CSW-SOC2-Reference-Design.md), [COBIT EDM03 / MEA01 / MEA02](./COBIT-2019/CSW-COBIT-Reference-Design.md) |
| "What does CSW look like for a CMMC L2 (CUI) scope?" | [CMMC AC.L2-3.1.1 / 3.1.3](./CMMC-2/CSW-CMMC-Reference-Design.md), [CMMC SC.L2-3.13.1 / 3.13.6](./CMMC-2/CSW-CMMC-Reference-Design.md), [NIST 800-53 AC-4](./NIST-800-53/CSW-NIST-800-53-Reference-Design.md), [NIST 800-171 Rev. 3](./NIST-800-171/CSW-NIST-800-171-Reference-Design.md) |
| "How do I evidence CCM / STAR segmentation and cloud data flows?" | [CSA IVS / IAM / DSP / TVM](./CSA-CCM/CSW-CSA-CCM-Reference-Design.md) |
| "How do I discuss Singapore MAS TRM technology risk with CSW?" | [MAS TRM critical systems, outsourcing, monitoring, vulnerability, incident evidence](./MAS-TRM/CSW-MAS-TRM-Reference-Design.md) |
| "How do I map APRA CPS 234 critical information assets?" | [APRA CPS 234 critical information asset segmentation, control testing, service-provider visibility](./APRA-CPS-234/CSW-APRA-CPS234-Reference-Design.md) |
| "How do I support NY DFS 23 NYCRR Part 500 evidence?" | [NY DFS Part 500 covered systems, NPI applications, monitoring, vulnerability, incident support](./NY-DFS-23-NYCRR-500/CSW-NYDFS-Reference-Design.md) |
| "How do I position CSW for TISAX / automotive supplier assessments?" | [TISAX / VDA ISA prototype, engineering, customer-confidential workload segmentation](./TISAX/CSW-TISAX-Reference-Design.md) |
| "How do I evidence OT-adjacent IT segmentation under NIST 800-82?" | [NIST SP 800-82 OT-facing IT systems, jump hosts, historians, vendor access](./NIST-800-82/CSW-NIST-800-82-Reference-Design.md) |
| "How do I support BSI C5 cloud assurance?" | [BSI C5 cloud service scope, tenant/shared-service boundaries, cloud communication security](./BSI-C5/CSW-BSI-C5-Reference-Design.md) |
| "How do I evidence UK NCSC CAF for NIS OES or GovAssure?" | [CAF A1–D2 crosswalk](./UK-NCSC-CAF/caf-mapping.md), [Reference design](./UK-NCSC-CAF/CSW-UK-NCSC-CAF-Reference-Design.md), [IGP scorer](./UK-NCSC-CAF/caf-igp-maturity-scorer.md), [Evidence pack](./UK-NCSC-CAF/caf-evidence-pack-template.md) |
---

## HIPAA Security Rule

Source: [`HIPAA/CSW-HIPAA-Reference-Design.md`](./HIPAA/CSW-HIPAA-Reference-Design.md)

| Citation | Topic | CSW can support evidence for |
|---|---|---|
| §164.306(a) | General requirements (admin, physical, technical safeguards) | Workload inventory, segmentation, telemetry baseline |
| §164.308(a)(1)(ii)(A) | Risk analysis | Workload inventory + ADM dependency graph (where monitored) |
| §164.308(a)(1)(ii)(B) | Risk management | Label/scope segmentation + drift detection |
| §164.308(a)(1)(ii)(D) | Information system activity review | Flow + process telemetry (exported to SIEM where integrated) |
| §164.308(a)(4) | Information access management | Identity/label-based segmentation |
| §164.308(a)(6) | Security incident procedures | Forensic timeline reconstruction |
| §164.312(a)(1) | Access control | Workload-level enforcement, deny-by-default |
| §164.312(b) | Audit controls | Process + flow telemetry; SIEM export when configured |
| §164.312(c)(1) | Integrity | Process / package change detection |
| §164.312(e)(1) | Transmission security | Plaintext-protocol DENY enforcement |
| §164.314(a) | Business Associate Agreements (technical companion) | Egress observation to BA endpoints |

---

## SOC 2 — Trust Services Criteria

Source: [`SOC2/CSW-SOC2-Reference-Design.md`](./SOC2/CSW-SOC2-Reference-Design.md)

| Criterion | Topic | CSW can support evidence for |
|---|---|---|
| CC6.1 | Logical & physical access controls | Workload segmentation, deny-by-default policy |
| CC6.6 | Restricting access to system resources | Per-process / per-port enforcement |
| CC6.7 | Restricting movement of information | Egress allow-listing |
| CC6.8 | Detecting unauthorised software | Process inventory, anomaly rules |
| CC7.1 | System operations — vulnerability management | CVE / exposure backlog with prioritisation signals |
| CC7.2 | System monitoring | Flow + process telemetry, SIEM forwarding |
| CC7.3 | Incident response | Forensic export + quarantine policy |
| CC7.4 | Recovery from incidents | Containment evidence + post-recovery diff |
| CC8.1 | Change management (technical companion) | Policy diff history, ADM drift |

---

## PCI DSS v4.0

Source: [`PCI-DSS-v4/CSW-PCI-DSS-Reference-Design.md`](./PCI-DSS-v4/CSW-PCI-DSS-Reference-Design.md)

| Requirement | Topic | CSW can support evidence for |
|---|---|---|
| Req 1 | Network security controls | CDE segmentation, simulation→enforce |
| Req 1.2.1 | Documented & approved flows | ADM-derived approved flow inventory |
| Req 2 | Secure configurations | Process / package baseline, drift |
| Req 6 | Develop & maintain secure software | Vulnerability inventory, CI/CD gating |
| Req 6.3.3 | Address vulnerabilities per risk ranking | CVSS + EPSS + reachability prioritisation |
| Req 7 | Restrict access by need-to-know | Identity-based workload segmentation |
| Req 10 | Log and monitor all access | Flow + process telemetry, SIEM export |
| Req 10.7.2 | Detect failures of critical controls | Sensor offline + enforcement gap alerts |
| Req 11.3 | Vulnerability scanning | Exposure insight from CSW-supported assessments — align with the Req 11 internal / ASV modalities your QSA expects |
| Req 11.4 | Network intrusion detection | Behavioural rules + conversation-graph anomaly |
| Req 11.5 | Detect changes/alterations | Process / package / configuration drift |
| Req 12.3.2 | Targeted risk analysis | CSW vulnerability + ADM data feeds risk analysis |

---

## NIST SP 800-53 Rev 5

Source: [`NIST-800-53/CSW-NIST-800-53-Reference-Design.md`](./NIST-800-53/CSW-NIST-800-53-Reference-Design.md)

| Control | Topic | CSW can support evidence for |
|---|---|---|
| AC-3 | Access enforcement | Workload-level policy enforcement |
| AC-4 | Information flow enforcement | Segmentation by label/scope |
| AC-6 | Least privilege | Deny-by-default policy + minimal allow |
| AU-2 / AU-12 | Auditable events | Process + flow telemetry |
| CA-7 | Continuous monitoring | Inventory snapshots + ADM drift signalling on whatever cadence you operate |
| CM-2 | Baseline configuration | Process / package baseline |
| CM-3 | Configuration change control | Policy diff history |
| CM-7 | Least functionality | Process + port allow-listing |
| CM-8 | System component inventory | Workload inventory reconciled with authoritative CMDB / cloud registers |
| IR-4 | Incident handling | Quarantine policy + forensic export |
| RA-5 | Vulnerability monitoring & scanning | Exposure monitoring backlog for workloads CSW observes |
| SA-11 | Developer testing & evaluation (technical evidence) | Pre-deploy vulnerability gating |
| SC-7 | Boundary protection | Egress allow-listing, plaintext-protocol DENY |
| SC-13 | Cryptographic protection | Plaintext-protocol DENY (FIPS-validated modules out of scope) |
| SI-4 | System monitoring | Behavioural rules + SIEM forwarding |
| SI-5 | Security alerts, advisories, directives | Vulnerability dashboards, exploit indicators |
| SR-3 / SR-6 | Supply chain controls (technical companion) | Egress observation to supplier endpoints |

---

## ISO/IEC 27001:2022 — Annex A

Source: [`ISO-27001-2022/CSW-ISO27001-Reference-Design.md`](./ISO-27001-2022/CSW-ISO27001-Reference-Design.md)

| Annex A | Topic | CSW can support evidence for |
|---|---|---|
| A.5.7 | Threat intelligence | Vulnerability + EPSS feed, IOC ingestion |
| A.5.19–A.5.22 | Supplier relationships (technical) | Supplier egress reconciliation |
| A.5.23 | Information security for cloud services | Cloud-account inventory + segmentation |
| A.5.30 | ICT readiness for business continuity (technical) | Containment + segmentation evidence |
| A.8.1 | User endpoint devices (workload portion) | Server / workload inventory baseline |
| A.8.8 | Management of technical vulnerabilities | CVE remediation tracking for workloads under observation |
| A.8.9 | Configuration management | Process / package baseline |
| A.8.16 | Monitoring activities | Behavioural rules + SIEM forwarding |
| A.8.20 | Networks security | Workload-level segmentation |
| A.8.21 | Security of network services | Per-service allow-listing |
| A.8.22 | Segregation of networks | Per-scope segmentation workspaces |
| A.8.23 | Web filtering (egress portion) | Egress allow-listing for HTTP/HTTPS workloads |
| A.8.24 | Use of cryptography | Plaintext-protocol DENY (no crypto primitives) |

---

## CISA Zero Trust Maturity Model v2.0

Source: [`CISA-ZeroTrust/CSW-CISA-ZTMM-Reference-Design.md`](./CISA-ZeroTrust/CSW-CISA-ZTMM-Reference-Design.md)

| Pillar | Example maturity path (varies by deployment) | CSW can support evidence for |
|---|---|---|
| Identity | Initial → Advanced | Identity-aware labels; integration with IdP-fed scopes (where deployed) |
| Devices | Initial → Advanced | Process-level fingerprinting; anomaly detection (tuning-dependent) |
| Networks | Often Advanced → Optimal aspiration | Enforcement / simulation workflows; observability-heavy ADM cadence — not an automatic Optimal-tier outcome |
| Applications & Workloads | Traditional → Advanced | Workload-level policy; vulnerability management views |
| Data | Traditional → Advanced | Conversation visibility; plaintext-protocol posture (encryption primitives still elsewhere) |

Cross-cutting capabilities — Visibility & Analytics; Automation &
Orchestration; Governance — *may* map to dashboard, API, and policy-
as-code workflows **when** customers wire those programmes up; the
pillars describe outcomes, not a guarantee of maturity tier.

---

## FIPS 140 (140-2 / 140-3)

Source: [`FIPS-140/CSW-FIPS-Reference-Design.md`](./FIPS-140/CSW-FIPS-Reference-Design.md)

CSW is **not a FIPS-validated cryptographic module**. The reference design
describes how CSW can support elements of an organisation's posture
toward FIPS — for instance by restricting obvious plaintext transports
and aligning workload inventory evidence with cryptographic usage
reviews — alongside **validated libraries and HSMs** that actually claim
modules. Statements like *"every in-scope workload only uses validated
cryptography"* still require cryptographic architecture and key
custody disciplines outside CSW.

| Requirement | CSW position |
|---|---|
| Cryptographic module validation | Out of scope — use a FIPS-validated library (OpenSSL FIPS, BouncyCastle FIPS) |
| Algorithm implementation testing | Out of scope — handled by NIST CMVP testing laboratory |
| Key generation & storage | Out of scope — use a FIPS-validated HSM |
| Module self-tests | Out of scope — handled by the cryptographic library |
| Use of FIPS-validated modules across the estate (programme assurance) | **In scope** — workload inventory + plaintext-protocol DENY evidence |

---

## NIST SP 800-207 — Zero Trust Architecture (Seven Tenets)

Source: [`NIST-800-207/CSW-NIST-800-207-Reference-Design.md`](./NIST-800-207/CSW-NIST-800-207-Reference-Design.md)

| Tenet | CSW can support evidence for |
|---|---|
| Tenet 1 — All data sources & computing services are resources | Workload/asset inventory plus cloud-account context (configured per your rollout) |
| Tenet 2 — All communication is secured regardless of network location | Plaintext-protocol DENY as one layer — TLS validation / crypto still owned elsewhere |
| Tenet 3 — Access to individual resources is granted on a per-session basis | Identity- and label-based segmentation per scope |
| Tenet 4 — Access is determined by dynamic policy | ADM-informed policy intents + drift/change signals (with human approvals) |
| Tenet 5 — Enterprise monitors integrity & posture of all assets | Posture telemetry (packages, CVE, flows)—interpret coverage with judgment |
| Tenet 6 — All resource authentication & authorisation is dynamic & strictly enforced | Identity-aware segmentation and enforcement at the workload (authn stacks still complementary) |
| Tenet 7 — Enterprise collects posture information & uses it to improve security | Evidence feeds into SIEM / metrics packs on a cadence you configure |

---

## NIST SP 800-207A — Zero Trust Logical Components (PDP/PEP/PA/PIP)

Source: [`NIST-800-207A/CSW-NIST-800-207A-Reference-Design.md`](./NIST-800-207A/CSW-NIST-800-207A-Reference-Design.md)

| Component | CSW role |
|---|---|
| Policy Decision Point (PDP) — Policy Engine | CSW Defend segmentation plane evaluates authored policy intents *(logical PEP/PIP analogue — map to official ZTA artefacts per assessor guidance)* |
| Policy Decision Point (PDP) — Policy Administrator | CSW Workspace administration + change history |
| Policy Enforcement Point (PEP) | CSW agent enforces decisions at the workload |
| Policy Information Point (PIP) | CSW telemetry (vulnerability, process, flow, package) feeds the policy decision |

---

## DORA — Regulation (EU) 2022/2554

> **Incident timelines.** The hour-based shorthand in Article 19 is widely
> discussed, but operative deadlines and classifications depend on the
> **Regulatory Technical Standards** and supervisory guidance **in force
> when you report**. Confirm against those instruments (and competent
> authority instructions) rather than relying on this index alone.

Source: [`DORA/CSW-DORA-Reference-Design.md`](./DORA/CSW-DORA-Reference-Design.md)

| Article | Topic | CSW can support evidence for |
|---|---|---|
| Art. 5 | Management body accountability | Quarterly evidence pack to management body |
| Art. 6 | ICT risk management framework | Centralised inventory, policy and detection state |
| Art. 8(1)–(6) | ICT asset inventory | Workload inventory + ADM dependency graph reconciled with authoritative registers |
| Art. 9(2)(a) | Network segmentation | Important-business-function scopes, simulation→enforce |
| Art. 9(2)(b) | Identification of unauthorised activities | ADM drift, conversation-graph anomalies |
| Art. 9(4)(g) | Continuous review of segmentation | Policy diff reports on an agreed supervisory cadence |
| Art. 10 | Detection | Behavioural rules + SIEM forwarding |
| Art. 11 | Response and recovery | Quarantine policy + forensic export bundle |
| Art. 13 | Learning and evolving | Quarterly metrics pack |
| Art. 17 | Incident management process | Forensic timeline reconstruction |
| Art. 18 | Classification of incidents | IBF labels + flow context inform classification |
| Art. 19 | Incident reporting (timing per RTS / supervisory guidance) | Artefact-heavy dossier templates in reference design — separate from statutory filing clocks |
| Art. 24 | Testing programme | Vulnerability + scenario test evidence |
| Art. 25(1) | Baseline tests | CVE dashboard + reachability queries |
| Art. 26 | TLPT (every 3 years for significant entities) | Red-team activity reconstruction |
| Art. 28(3) | Register of Information | Third-party egress reconciliation |
| Art. 28(4) | Third-party risk monitoring | Monitored egress patterns reconciled against the Register (where integrations exist) |
| Art. 30(2)(c) | Contractual right to monitor | Technical evidence supporting contractual right |

---

## NIS2 — Directive (EU) 2022/2555

> **Incident timelines (national law).** NIS2 Article 23 phases (24 h /
> 72 h / ~one month narrative) inherit detail from delegated acts plus
> **your Member State’s transposing statute** — confirm operative wording with
> local counsel / competent authority / CSIRT.

Source: [`NIS2/CSW-NIS2-Reference-Design.md`](./NIS2/CSW-NIS2-Reference-Design.md)

| Provision | Topic | CSW can support evidence for |
|---|---|---|
| Art. 20(1) | Management body accountability | Quarterly NIS2 pack |
| Art. 20(2) | Management body training | Pack section commentary as reusable training input |
| Art. 21(2)(a) | Risk analysis & IS-security policies | Workspace Intents grounded in observed behaviour |
| Art. 21(2)(b) | Incident handling | Detection rules + SIEM forwarding + 6-artefact dossier |
| Art. 21(2)(c) | Business continuity / backup / crisis | Containment + forensic preservation only (backups out of scope) |
| Art. 21(2)(d) | Supply chain security | Supplier egress reconciliation |
| Art. 21(2)(e) | Security in acquisition / dev / maintenance, vuln handling | Vulnerability inventory + CI/CD gate + CVE-to-attack-path |
| Art. 21(2)(f) | Effectiveness assessment | Quarterly effectiveness pack |
| Art. 21(2)(g) | Cyber hygiene + training | Patch & process telemetry (training out of scope) |
| Art. 21(2)(h) | Cryptography / encryption | Plaintext-protocol DENY (no crypto primitives) |
| Art. 21(2)(i) | HR sec / access control / asset management | Inventory + label discipline supporting asset-management evidence |
| Art. 21(2)(j) | MFA / secured comms | MFA remains outside CSW; CSW supports authorised workload-to-workload segmentation separately |
| Art. 23(1) | 24-h early warning | 6-artefact dossier (initial pass) |
| Art. 23(2) | 72-h notification | Same dossier, progressively complete |
| Art. 23(3) | 1-month final report | Same dossier, plus root-cause and remediation |
| Art. 32 / 33 | Supervisory measures | On-demand exports customers can use as inputs to supervisory evidence packs |

---

## NERC CIP — North American Bulk Electric System (IT-side mapping)

> **Scope.** CSW addresses the **IT side** of the IT/OT boundary —
> EACMS, jump hosts, vendor-access servers, identity/PKI, BCSI hosts.
> CSW is **not** an Electronic Access Point (EAP) and does not enforce
> on PLCs / RTUs / IEDs / HMIs. Pair with your boundary firewall and
> your OT-aware monitoring stack (Cisco Cyber Vision, Claroty, Nozomi,
> Dragos) for end-to-end coverage. Draft v1 — apply SME judgment.

Source: [`NERC-CIP/CSW-NERC-CIP-Reference-Design.md`](./NERC-CIP/CSW-NERC-CIP-Reference-Design.md)

| Standard / Requirement | Topic | CSW can support evidence for (IT-side) |
|---|---|---|
| CIP-002 R1 | BES Cyber System identification | Inventory + scope labelling for the IT estate supporting BCS |
| CIP-003 R1 | Senior Manager accountability | Quarterly evidence pack covering CIP-005/007/010/013 IT-side outputs |
| CIP-005 R1 | Electronic Security Perimeter | IT-side enclave segmentation; deny-by-default to EAP-IP set; documented exception list |
| CIP-005 R1.5 | Boundary control review | Quarterly enforcement diff report |
| CIP-005 R2 | Interactive Remote Access (IRA) | Intermediate-system enforcement; per-session flow telemetry; weekly IRA-pattern report |
| CIP-007 R1 | Ports and services baseline | Per-workload listening-port inventory with last-flow timestamp |
| CIP-007 R2 | Patch management | Continuous CVE inventory feeding the patch programme |
| CIP-007 R3 | Malicious code prevention | Behavioural rules + simulation→enforcement progression |
| CIP-007 R4 | Security event monitoring | Process + flow telemetry to SIEM with retention |
| CIP-008 R1 | Incident response plan | Six-artefact reconstruction bundle |
| CIP-008 R4 | Reportable Cyber Security Incident notification | Containment evidence + dossier supporting E-ISAC notification |
| CIP-010 R1 | Configuration baseline | Daily software + listening-port baseline with diff and disposition |
| CIP-010 R1.5 | Unauthorised change monitoring | Daily diff vs. previous day with disposition column |
| CIP-010 R3.1 | Active vulnerability assessment (Highs) | Per-workload CVE list with CVSS / exploit / EPSS context |
| CIP-010 R3.2 | Pre-commissioning VA | First-sighting CVE inventory before ESP connection |
| CIP-011 R1.1 | BCSI access controls | Egress and access pattern monitoring on `bes_role=bcsi-host` workloads |
| CIP-013 R1.2.5 | Vendor remote access | EACMS egress allowlist scoped to vendor register |
| CIP-013 R1.2.6 | Vendor incident coordination | Vendor-egress flow record for the incident window |

---

## TSA Pipeline — Security Directive 2021-02 series (IT-side mapping)

> **Scope.** CSW addresses the **IT side** of the IT/OT boundary —
> SCADA jump servers, historians, MES/EAM, engineering workstations,
> vendor-access hosts, identity/PKI. CSW is **not** an OT-protocol
> deep-packet-inspection tool and does not enforce on RTUs / flow
> computers / PLCs / IEDs / HMIs. Pair with your IT/OT firewall and
> your OT-aware sensors. Draft v1 — apply SME judgment.

Source: [`TSA-Pipeline/CSW-TSA-Pipeline-Reference-Design.md`](./TSA-Pipeline/CSW-TSA-Pipeline-Reference-Design.md)

| SD provision | Topic | CSW can support evidence for (IT-side) |
|---|---|---|
| Section II | Critical Cyber System identification | Inventory + scope labelling for CSW-managed workloads supporting CCS |
| Section II | Cybersecurity Coordinator | Quarterly evidence pack to the Coordinator |
| Section III.A | Network segmentation (IT/OT) | Per-site IT-side enclave segmentation; deny-by-default to IT/OT boundary firewall |
| Section III.A | Documented data flows | Observed IT→OT flow inventory + reconciliation against architecture |
| Section III.A | New-flow change control | Continuous monitoring for new IT→OT edges |
| Section III.B | Access control measures | Workload-level least-privilege; quarterly access review with sunset log |
| Section III.C | Continuous monitoring & detection | Behavioural rules + flow telemetry to SIEM; conversation-graph anomalies |
| Section III.C | SIEM integration | Forwarding configuration to Splunk / QRadar / Sentinel / Cisco XDR |
| Section III.C | Detection latency | Per-CCS-function MTTD report |
| Section III.D | Unpatched-system risk reduction | Continuous CVE inventory + compensating-control register |
| Section III.D | Patch verification | Diff report showing patched version + automatic CVE drop |
| Cybersecurity Incident Response Plan | Detection, response, 24-hour CISA reporting | Six-artefact reconstruction bundle |
| Cybersecurity Assessment Plan (CAP) | Annual implementation assessment | Per-SD-section evidence pack with prior-period delta |
| Cybersecurity Architecture Design Review | Periodic architecture review | Workload inventory + dependency graph + observed flow inventory |

---

## CIS Critical Security Controls v8.1 (IG2 lead)

> **Scope.** CIS Controls v8.1, 18 Controls and ~153 Safeguards.
> Default depth is **Implementation Group 2 (IG2)**; IG1 and IG3
> deltas are called out where the work materially changes. CSW is
> direct on six Controls (1, 2, 4, 7, 8, 13) and supporting on
> seven; out of scope on Controls 5 (account mgmt), 9 (email/web),
> 11 (data recovery), 14 (training).

Source: [`CIS-Controls-v8/CSW-CIS-Reference-Design.md`](./CIS-Controls-v8/CSW-CIS-Reference-Design.md)

| Safeguard | Topic | CSW can support evidence for |
|---|---|---|
| 1.1 / 1.5 | Inventory of enterprise assets; passive discovery | Continuous workload inventory + cloud-orchestrator polling |
| 1.2 | Address unauthorised assets | Quarantine policy applied to net-new workloads |
| 2.1 | Software inventory | Per-workload package + version inventory |
| 2.3 / 2.5 / 2.6 | Address unauthorised software; allow-list | Allow-list deviation alerting + (IG3) behavioural block |
| 4.1 | Secure configuration process | Daily baseline + drift report tied to change ticket |
| 4.4 / 4.6 | Default deny on FW; secure software config | CSW segmentation enforcement + per-workload listening-port inventory |
| 7.1–7.7 | Continuous vulnerability management | Continuous CVE inventory + reachability prioritisation + patch SLA tracking |
| 8.2 / 8.5 | Collect audit logs; detailed audit logs | SIEM forwarding with per-flow + per-process detail |
| 8.7 / 8.10 | Retain audit logs (≥90 days IG2) | SIEM retention policy + CSW window |
| 8.11 | Audit log reviews | Quarterly review of CSW alert summary |
| 12.2 | Use secure protocols | Plaintext-flow detection + DENY enforcement |
| 12.4 | Architecture diagrams | ADM dependency export |
| 13.1 / 13.6 | Centralised monitoring; flow logs | CSW flow telemetry + SIEM forwarding |
| 13.2 / 13.3 | Host + network IDS | Behavioural rule catalogue + anomaly detection |
| 13.4 | Traffic filtering between segments | CSW segmentation policy + simulation→enforcement log |
| 13.5 | Remote-asset access control | Bastion-source-restricted mgmt protocol allow rules |
| 13.7–13.10 (IG3) | HIPS / NIPS / port-level / app-layer filtering | Behavioural rules + segmentation enforcement |
| 15.1 / 15.4 | Service provider mgmt (technical lens) | Vendor-egress observation + reconciliation |
| 17.1–17.8 | Incident response management | Six-artefact reconstruction bundle |
| 18.1 / 18.5 | Penetration testing | Pre/post reachability + activity reconstruction |

---

## NIST Cybersecurity Framework 2.0 (Govern + 5 Functions)

> **Scope.** CSF 2.0 (Feb 2024) added **Govern (GV)** above the
> existing Identify / Protect / Detect / Respond / Recover. CSF
> wraps control catalogues; this section maps the **technical
> Subcategories** where CSW supplies evidence. Direct on ID / PR
> / DE / RS technical Subcategories; supporting on GV (evidence
> pack) and RC (post-incident diff). Out of scope on physical/
> environmental, backup/recovery execution, and training/HR
> Subcategories.

Source: [`NIST-CSF-2/CSW-CSF-Reference-Design.md`](./NIST-CSF-2/CSW-CSF-Reference-Design.md)

| Subcategory | Topic | CSW can support evidence for |
|---|---|---|
| GV.OV-01 / 02 / 03 | Cybersecurity strategy oversight | Quarterly evidence pack to management body |
| GV.SC-04 / 07 / 09 / 10 | Cybersecurity supply chain (CSCRM) | Vendor-egress observation + reconciliation + EOL register |
| ID.AM-01 / 02 / 03 | Hardware / software / flow inventory | Continuous workload + ADM dependency + observed-flow inventory |
| ID.AM-04 | Supplier service inventory | Vendor-egress + register reconciliation |
| ID.AM-05 / 07 | Asset / data prioritisation and classification | `crit_band` + `data_class` labels per workload |
| ID.AM-08 | Asset lifecycle | Vendor-EOL flags in software inventory |
| ID.RA-01 / 05 / 06 | Vulnerabilities + risk + response | CVE inventory + reachability prioritisation + remediation tracking |
| ID.RA-07 | Changes & exceptions | Drift report + change-ticket attribution |
| PR.AA-01 / 05 | Identity-aware access enforcement | Workload-side enforcement (identity upstream) |
| PR.DS-02 | Data-in-transit | Plaintext-protocol DENY enforcement |
| PR.IR-01 | Network protected from unauthorised access | Workload-level deny-by-default segmentation |
| PR.IR-03 | Resilience requirements | Quarantine policy + segmentation under change control |
| PR.PS-01 | Configuration management | Daily baseline + drift detection |
| PR.PS-02 | Software maintained | Per-workload software inventory + EOL tagging |
| PR.PS-04 | Log records generated | Per-flow + per-process telemetry to SIEM |
| PR.PS-05 | Unauthorised software prevented | Behavioural rules + (IG3) block |
| PR.PS-06 | Secure software development | CVE inventory feeds SDLC |
| DE.CM-01 | Networks monitored | CSW flow telemetry + behavioural rules + SIEM |
| DE.CM-03 | Personnel activity monitored | Process telemetry + identity-aware policy |
| DE.CM-06 | External service provider activities monitored | Vendor-egress observation + drift alerting |
| DE.CM-09 | Computing hardware/software monitored | Per-workload telemetry retention |
| DE.AE-02 / 03 / 04 / 06 / 07 / 08 | Adverse event analysis | Forensic timeline + SIEM correlation + threat intel + impact + ticket routing |
| RS.MA-01 to 05 | Incident management | Six-artefact dossier + severity routing |
| RS.AN-03 / 06 / 07 / 08 | Incident analysis (root cause, magnitude, integrity) | Process + flow timeline + dossier with timestamped exports |
| RS.MI-01 / 02 | Incident mitigation | Quarantine policy + compensating-control register |
| RC.RP-04 / 05 / 06 | Recovery actions (evidence side) | Post-recovery segmentation diff + re-baseline |

---

## CMMC 2.0 (Cybersecurity Maturity Model Certification — DoD/DIB)

> **Scope.** Default depth is **Level 2** (110 controls = NIST SP
> 800-171 Rev 2). Level 1 (FAR 52.204-21, 15 safeguards) and Level
> 3 (Level 2 + selected NIST 800-172 enhancements) are called out
> in the reference design. CSW is direct on AC, AU, CM, RA, SC, SI families;
> supporting on CA, IA, IR (evidence), MA; out of scope on AT, MP,
> PE, PS. **CMMC L2 assessment is performed by a C3PAO** — nothing
> here substitutes for the SSP, POA&M, or the C3PAO engagement.

Source: [`CMMC-2/CSW-CMMC-Reference-Design.md`](./CMMC-2/CSW-CMMC-Reference-Design.md)

| Practice | Topic | CSW can support evidence for |
|---|---|---|
| AC.L1/L2-3.1.1 | Limit system access | Per-enclave deny-by-default segmentation |
| AC.L2-3.1.2 | Limit access to authorised functions | Allow-list per documented system function |
| AC.L2-3.1.3 | Control flow of CUI | Inter-enclave flow allow-list + reconciliation against SSP |
| AC.L2-3.1.20 | Verify external connections | Egress allowlist + alert on net-new external destinations |
| AC.L2-3.1.22 | CUI on publicly-accessible systems | Internet-reachability query + scope review |
| AU.L2-3.3.1 | Audit records | Per-flow + per-process telemetry to SIEM |
| AU.L2-3.3.2 | Action traceability to individual users | Process attribution + SIEM identity correlation |
| AU.L2-3.3.4 / 3.3.5 / 3.3.8 | Alert / correlate / protect logs | Forwarder health alert + SIEM correlation + RBAC |
| AU.L2-3.3.9 | Limit audit-log mgmt functionality | CSW RBAC for audit-management roles |
| CM.L2-3.4.1 | Establish baseline configurations | Daily snapshot per workload (OS, packages, ports, processes) |
| CM.L2-3.4.3 / 3.4.4 | Track and approve changes | Daily diff + change-ticket attribution |
| CM.L2-3.4.6 | Least functionality | Listening-port + service inventory + 90-day-no-flow review |
| CM.L2-3.4.7 | Restrict nonessential programs | Software allow-list + (L3) behavioural block |
| RA.L2-3.11.2 | Vulnerability scanning | Continuous CVE inventory per CUI workload |
| RA.L2-3.11.3 | Remediate vulnerabilities | Patch SLA + compensating-control register + POA&M linkage |
| SC.L2-3.13.1 | Boundary protection | Per-enclave segmentation enforcement |
| SC.L2-3.13.2 | Architectural designs | ADM-derived as-observed architecture |
| SC.L2-3.13.5 | Subnetworks for publicly-accessible components | Public-component scope isolation |
| SC.L2-3.13.6 | Deny by default; permit by exception | Workload-level deny-by-default (native CSW posture) |
| SC.L2-3.13.7 | Prevent split tunneling | Detective alert on split-tunnel patterns |
| SI.L2-3.14.1 | Identify, report, correct system flaws | CVE inventory + drift + SIEM routing |
| SI.L2-3.14.2 | Malicious code protection | Behavioural rules layered with endpoint AV |
| SI.L2-3.14.3 | Monitor security advisories | Threat-intel-enriched CVE prioritisation |
| SI.L2-3.14.6 | Monitor communications | Flow telemetry + behavioural rules + anomaly detection |
| SI.L2-3.14.7 | Identify unauthorised use | Process telemetry + identity-aware policy |
| IR.L2-3.6.1 / 3.6.2 / 3.6.3 | Incident response process | Six-artefact dossier per CUI-scope incident |

---

## IEC 62443 — Industrial Automation & Control Systems (IT-side mapping)

> **Scope.** CSW addresses **servers, VMs, containers, and cloud workloads**
> on the **IT side** of the IT/OT boundary and systems that **support** IACS
> (jump hosts, engineering workstations, historians, DMZ brokers). CSW does
> **not** replace OT visibility for Level 0–2 devices — pair with **Cisco
> Cyber Vision**, **Claroty**, or equivalent for device-layer evidence.

Source: [`IEC-62443/CSW-IEC62443-Reference-Design.md`](./IEC-62443/CSW-IEC62443-Reference-Design.md)

| Requirement | Topic | CSW can support evidence for (IT-side / IACS-adjacent) |
|---|---|---|
| SR 5.1 | Segmentation / zones | Scope hierarchy; workspaces; `zone` / `conduit` labels |
| SR 5.2 | Segmentation for zones of differing security requirements | Tiered scopes by SL labels; stricter workspaces for higher SL-T |
| SR 5.3 | Conduit control | Allowlist rules per conduit; default deny |
| SR 5.4 | Covert channel mitigation (IT layer) | Egress restrictions; flow-volume anomaly reports |
| SR 1.1–1.13 | Identification, authentication, access control | Identity-aware policies (where integrated); admin path lock-down; least-privilege allowlists |
| SR 3.1–3.9 | System integrity | Process/binary inventory; drift alerts; vulnerability data |
| SR 6.1 | Audit logging support | Flow + process retention; exports |
| SR 6.2 | Continuous monitoring | Alerts; SIEM forwarders |
| SR 7.1–7.8 | Resource availability (DoS awareness) | Flow volumetrics; session-rate anomalies |
| 62443-2-1 (technical contributors) | Security management system — monitoring / IR support | Dashboards; scheduled exports; forensic drill packages |

---

## GDPR — Regulation (EU) 2016/679 (technical measures)

> **Limitation.** GDPR is a **legal** framework — lawful basis, DPIA
> sign-off, and data-subject rights remain with the controller, DPO, and
> counsel. This section indexes **technical security-of-processing** and
> **flow-corroboration** artefacts only.

Source: [`GDPR/CSW-GDPR-Reference-Design.md`](./GDPR/CSW-GDPR-Reference-Design.md)

| Provision | Topic | CSW can support evidence for |
|---|---|---|
| Art. 5(1)(f) | Integrity & confidentiality | Segmentation; monitoring; cleartext-path detection; vuln visibility |
| Art. 25(1–2) | Data protection by design & by default | Scopes isolating processing activities; default deny; ADM-driven least privilege |
| Art. 30 | Records of processing — accuracy of systems & transfers | ADM & flow telemetry validating documented flows vs RoPA |
| Art. 32(1) | Security of processing (TOMs) | Path hygiene; segmentation; resilience signals (with complementary crypto tools) |
| Art. 32(1)(d) | Testing effectiveness of measures | Policy drills; simulation reruns |
| Art. 33–34 | Breach notification & communication | Flow + process forensics; scope membership proofs (*legal finalizes filing*) |
| Art. 35 | DPIA (technical annex) | ADM + flow history for necessity / proportionality |
| Art. 28 | Processor & sub-processor oversight | Egress allowlists; alerts on new destinations |

---

## MITRE ATT&CK — Enterprise tactics & techniques

> **Pairing.** CSW provides **workload network/process** telemetry and
> **segmentation** — not full EDR/email/identity coverage. Map tactics with
> **SIEM**, **XDR/EDR**, and identity tooling for end-to-end ATT&CK
> narratives.

Source: [`MITRE-ATTACK/CSW-MITRE-ATTACK-Reference-Design.md`](./MITRE-ATTACK/CSW-MITRE-ATTACK-Reference-Design.md)

| Tactic | Representative techniques (examples) | CSW can support evidence for |
|---|---|---|
| TA0001 Initial Access | T1190, T1133, T1566* | Inbound flow anomalies; policy deny logs |
| TA0002 Execution | T1059, T1204, T1047 | Process monitoring; unseen CLI; scripting lineage |
| TA0003 Persistence | T1543, T1547, T1574 | New listeners; package drift |
| TA0004 Privilege Escalation | T1068, T1055 | Privilege context + anomalous children (validate with EDR) |
| TA0005 Defense Evasion | T1027, T1562, T1070 | Baseline drift; new egress |
| TA0006 Credential Access | T1003, T1558, T1110** | Credential-tool patterns; supporting flow context |
| TA0007 Discovery | T1046, T1018, T1087** | Scanning / fan-out behaviour from flow telemetry |
| TA0008 Lateral Movement | T1021, T1550 | Microsegmentation blocks; east-west allowlists |
| TA0009 Collection | T1005, T1119 | Internal staging / bulk cross-scope flows |
| TA0010 Exfiltration | T1048, T1020 | Egress anomalies; novel destinations |
| TA0011 Command and Control | T1071, T1095, T1573 | Beaconing candidates (finalize in SIEM) |
| TA0040 Impact | T1486, T1490 | Process anomaly; containment via policy |

\*T1566 — post-landing workload evidence only. \*\*Heavy identity/directory detail requires IdP / AD / EDR logs.

| Technique | Name | CSW alignment |
|---|---|---|
| T1190 | Exploit Public-Facing Application | Strong — ingress-tier flow pivot |
| T1059.001 | PowerShell | Medium–strong — process forensics |
| T1059.003 | Windows Command Shell | Medium–strong |
| T1574.002 | DLL Side-Loading | Medium |
| T1543.003 | Windows Service | Medium |
| T1003.001 | LSASS Memory | Medium — corroborate with EDR |
| T1046 | Network Service Scanning | Strong |
| T1021.001 | Remote Desktop Protocol | Strong |
| T1021.002 | SMB/Windows Admin Shares | Strong |
| T1021.004 | SSH | Strong |
| T1048 | Exfiltration Over Alternative Protocol | Medium–strong |
| T1071.001 | Web Protocols | Medium |
| T1486 | Data Encrypted for Impact | Medium |

---

## FedRAMP — Moderate baseline (workload evidence)

> **Note.** CSW as a **product** is not itself FedRAMP-authorized — this
> mapping describes **customer-deployed** CSW evidence **inside your**
> authorization boundary. Cross-reference the [800-53](./NIST-800-53/)
> reference design for control-family depth.

Source: [`FedRAMP/CSW-FedRAMP-Reference-Design.md`](./FedRAMP/CSW-FedRAMP-Reference-Design.md)

| Control | Topic | CSW can support evidence for |
|---|---|---|
| AC-4 | Information flow enforcement | Microsegmentation; ADM-documented flows; policy exports |
| AC-3 | Access enforcement | Workload-level allow/deny |
| CA-7 | Continuous monitoring | Scheduled exports; ConMon attachments |
| CM-2 | Baseline configuration | ADM baseline workspace |
| CM-3 | Configuration change control | Drift alerts → tickets |
| CM-8 | System component inventory | CSW inventory export reconciliation |
| RA-5 | Vulnerability monitoring | CVE + CVSS + EPSS + reachability; POA&M rows |
| SC-7 | Boundary protection | Internal segmentation / host-level boundaries |
| SI-4 | System monitoring | Process + flow telemetry; SIEM ingest |
| AU-2 / 3 / 6 / 12 | Audit events & review | Flow/process records; field mapping |
| IR-4 | Incident handling | Forensic export bundles |

---

## SWIFT — Customer Security Controls Framework (CSCF v2024)

> **M/A labels.** Mandatory (**M**) vs Advisory (**A**) vs N/A follows **your**
> official CSCF v2024 applicability row — treat hints below as navigation
> aid only.

Source: [`SWIFT-CSCF/CSW-SWIFT-CSCF-Reference-Design.md`](./SWIFT-CSCF/CSW-SWIFT-CSCF-Reference-Design.md)

| CSCF Ref | Title (short) | CSW can support evidence for |
|---|---|---|
| 1.1 | SWIFT environment protection | Secure-zone segmentation; ADM-backed allowlists |
| 1.2 | OS privileged account control | Process + flow visibility for privileged sessions |
| 1.4 | Restriction of internet access | DENY secure-zone → Internet at workload layer |
| 2.1 | Internal data flow security | ADM + flow telemetry |
| 2.6 | Operator session confidentiality | Plaintext protocol detection/blocking |
| 4.1 | Password policy | **Out of scope** — IdP / directory controls |
| 5.1 | Logical access control | Identity-aware policy (where integrated); label-scoped rules |
| 6.1 | Malware protection | Process anomaly signals (complement AV/EDR) |
| 6.4 | Logging & monitoring | Flow + process telemetry; SIEM export |
| 7.1 | Cyber incident response planning | Forensic reconstruction; policy snapshots |

---

## HITRUST CSF — v11 (harmonised requirements)

> **Notation.** **01.m**-style IDs are common discussion shorthand — confirm exact
> **PRS** text in **MyCSF** for your assessment. **e1 / i1 / r2** depth varies
> by programme and assessor interpretation.

Source: [`HITRUST-CSF/CSW-HITRUST-Reference-Design.md`](./HITRUST-CSF/CSW-HITRUST-Reference-Design.md)

| HITRUST Ref | Statement theme (short) | CSW can support evidence for |
|---|---|---|
| 01.m | Segregation in networks | Microsegmentation; ADM isolation proofs |
| 01.n | Network connection control | Service/port allowlists; denial logs |
| 01.o | Network routing control | Flow visibility of effective paths |
| 06.d | Data protection & privacy (technical facets) | Workload-layer data-flow mapping; isolation |
| 09.ab | Monitoring system use | Continuous flow/process monitoring |
| 09.ad | Administrator & operator logs | Admin-path flow bundles; process context |
| 10.a | Security requirements analysis | ADM + change-review packs |
| 10.m | Control of technical vulnerabilities | CVE + reachability; compensating rules |
| 11.a | Reporting information security events | IR exports + ticketing |
| 11.c | Collection of evidence | Forensic snapshots; hash manifests |

---

## NIST SP 800-171 Rev. 3

Source: [`NIST-800-171/CSW-NIST-800-171-Reference-Design.md`](./NIST-800-171/CSW-NIST-800-171-Reference-Design.md)

| Requirement | Topic | CSW can support evidence for |
|---|---|---|
| 03.01.02 | Access enforcement | Scope-based micro-segmentation; deny default with explicit allow; policy exports |
| 03.01.03 | Information flow enforcement for CUI | Boundary policies CUI↔non-CUI; ADM-approved paths |
| 03.01.05 | Least privilege (incl. network) | Minimal allow-list; process-scoped visibility |
| 03.01.12 | Remote access | Policies for jump hosts / bastions; admin-port flow logs |
| 03.03.01–03.03.08 | Audit and accountability | Flow + process telemetry → SIEM; timestamped records; RBAC on console |
| 03.04.01 / 03.04.02 | Baseline configuration; configuration change | ADM as communication baseline; new flows / listeners flagged |
| 03.04.08 | Authorized software — allow by exception | Process / software inventory vs approved list |
| 03.11.x | Risk assessment inputs | CVE + reachability + EPSS-style prioritisation |
| 03.13.01 | Boundary protection | Enclave segmentation; internal boundary rules |
| 03.13.06 | Deny by default / allow by exception | Workload-level default deny |
| 03.13.08 | Transmission confidentiality (path hygiene) | Cleartext detection/blocking; protocol posture narratives |
| 03.14.01 / 03.14.02 / 03.14.06 | Flaw remediation; malicious code (complementary); system monitoring | Vulnerability exports; process signals + AV pairing; behavioural rules |
| 03.06.x | Incident handling (technical evidence) | Forensic export bundle |
| 03.12.03 / 03.12.05 | Continuous monitoring; information exchange agreements | Telemetry + policy effectiveness; ADM interface inventory + SSP references |

---

## CSA Cloud Controls Matrix v4.0

Source: [`CSA-CCM/CSW-CSA-CCM-Reference-Design.md`](./CSA-CCM/CSW-CSA-CCM-Reference-Design.md)

| Domain / objective | Topic | CSW can support evidence for |
|---|---|---|
| AIS | Application & interface security | ADM dependency map; constrained interfaces; approved listener inventory |
| BCR | Business continuity & resilience | Pre/post DR ADM & policy diff; connectivity baselines around tests |
| CCC | Change control & configuration management | Drift detection; inventory deltas; CAB-linked diffs |
| DSP | Data security & privacy lifecycle | Tier separation; monitored egress; data-flow boundaries |
| GRC | Governance / metrics | Coverage KPIs; violation trends |
| IAM | Identity & access (technical) | Identity-aware segmentation; admin-path controls |
| IVS (e.g. IVS-09) | Infrastructure & virtualization / network segmentation | Micro-segmentation; east-west enforcement reports |
| LOG | Logging & monitoring | Flow/process telemetry; SIEM feed health |
| SEF | Security incident & forensics | Timeline reconstruction; process trees |
| TVM | Threat & vulnerability management | CVE inventory; reachability / exposure context |

---

## COBIT 2019

Source: [`COBIT-2019/CSW-COBIT-Reference-Design.md`](./COBIT-2019/CSW-COBIT-Reference-Design.md)

| Objective / focus area | Topic | CSW can support evidence for |
|---|---|---|
| APO13 | Managed security | Segmentation workspaces; telemetry; vuln exposure views |
| DSS01 | Managed operations | Flow/process monitoring; inventory; operational dashboards |
| DSS02 | Managed service requests & incidents | Forensic search; process context for IR |
| DSS05 | Managed security services | Enforcement logs; segmentation coverage |
| DSS05.02 | Network and connectivity security | ADM snapshots; explicit allow/deny exports |
| DSS05.05 | Physical and logical access (logical network) | Admin-path restriction rules; observed admin flows *(IdP/MFA complementary)* |
| MEA01 | Managed performance and conformance monitoring | Conformance dashboards; scheduled exports |
| MEA02 | Managed system of internal control | Drift detection; policy versioning; audit bundles |
| BAI06 | Managed IT changes | Post-change package / listener deltas |
| BAI10 | Managed configuration | Baseline listeners & process sets |
| EDM03 | Ensured risk optimization (inputs) | CVE + reachability prioritisation for risk committees |

---

## Australian Essential Eight (ACSC EEMM)

Source: [`AU-Essential-Eight/CSW-Essential-Eight-Reference-Design.md`](./AU-Essential-Eight/CSW-Essential-Eight-Reference-Design.md)

| Strategy | Topic | CSW can support evidence for |
|---|---|---|
| E1 | Application control | Process visibility; execution telemetry; hunt exports *with* allowlist records from endpoint tool |
| E2 | Patch applications | Inventory; CVE + EPSS + exposure |
| E3 | Office macro settings | Limited — egress patterns from Office *(not macro policy config)* |
| E4 | User application hardening | Browser/Office network baselines; anomalies |
| E5 | Restrict administrative privileges | Admin-path segmentation; jump-host rules; process visibility |
| E6 | Patch operating systems | OS inventory; CVE mapping |
| E7 | Multi-factor authentication | **Out of scope** — IdP evidence |
| E8 | Regular backups | Peripheral flow telemetry only *(not immutability / restore testing)* |

---

## UK Cyber Essentials Plus

Source: [`UK-Cyber-Essentials/CSW-Cyber-Essentials-Reference-Design.md`](./UK-Cyber-Essentials/CSW-Cyber-Essentials-Reference-Design.md)

| Theme | Topic | CSW can support evidence for |
|---|---|---|
| CE1 | Firewalls & gateways | Workload micro-segmentation; deny-by-default; ADM-backed rules |
| CE2 | Secure configuration | Software inventory; drift; listener reports |
| CE3 | User access control | Identity-aware policies where integrated; east-west least privilege |
| CE4 | Malware protection | Complement AV/EDR — anomaly rules; lateral containment |
| CE5 | Security updates | CVE + EPSS; reachability-ranked backlog |

---

## UK NCSC CAF v3.2

> **Draft v1.** For UK NIS Regulations (OES) assessments and GovAssure
> (Cabinet Office Government Security Group). Confirm the current CAF text
> and the assessor's expectations before formal reliance. CSW is an evidence
> source for a subset of Indicators of Good Practice; it does not satisfy a
> principle by itself.

Source: [`UK-NCSC-CAF/caf-mapping.md`](./UK-NCSC-CAF/caf-mapping.md) · [Reference design](./UK-NCSC-CAF/CSW-UK-NCSC-CAF-Reference-Design.md) · [Compliance report](./UK-NCSC-CAF/CSW-UK-NCSC-CAF-Compliance-Report.md) · [IGP scorer](./UK-NCSC-CAF/caf-igp-maturity-scorer.md) · [Evidence pack](./UK-NCSC-CAF/caf-evidence-pack-template.md)

| Principle | Topic | CSW can support evidence for |
|---|---|---|
| A1 | Governance | Executive posture telemetry for board/CISO reporting (not governance structure) |
| A2 | Risk management | Blast-radius, enforcement-gap, and reachability trends between snapshots |
| A3 | Asset management | Sensor census, package inventory, point-in-time cluster snapshot |
| A4 | Supply chain | Vendor-tagged egress vs. what the contract allows |
| B1 | Service protection policies | Versioned workspace policies and host-firewall enforcement |
| B2 | Identity and access | Out of scope — pair with an identity platform; ISE can supply identity-aware policy |
| B3 | Data security | East-west path control and plaintext-protocol deny (not encryption or DLP) |
| B4 | System security | Per-workload CVE and package inventory; config-drift signals |
| B5 | Resilient networks and systems | Segregation evidence for B5.b. Not backups (B5.c), and CAF does not name eBPF or microsegmentation |
| B6 | Staff awareness and training | Out of scope |
| C1 | Security monitoring | Continuous flow telemetry with process context and policy decision |
| C2 | Proactive event discovery | Forensic events and vulnerability reachability, paired with detection content |
| D1 | Response and recovery | Forensic timeline and containment evidence (recovery programme stays outside CSW) |
| D2 | Lessons learned | Snapshot delta a root-cause review can use. Not NIST PM-14 |

---

## HIPAA Security Rule — 2025 NPRM (proposed)

> **Proposed rule.** This section indexes **discussed NPRM provisions** — confirm **final** regulatory text and effective dates with counsel before formal reliance. Parallel compliance with the **current** Security Rule applies until amendments are in force.

Source: [`HIPAA-2025-NPRM/CSW-HIPAA-NPRM-Reference-Design.md`](./HIPAA-2025-NPRM/CSW-HIPAA-NPRM-Reference-Design.md)

| Provision | Topic | CSW can support evidence for |
|---|---|---|
| §164.312(a)(2)(vi) | Network segmentation (*proposed mandatory*) | Deny-by-default between ePHI and non-ePHI; ADM-backed rules |
| §164.312(a)(1) | Access control (*strengthened*) | Identity-aware segmentation; process-level visibility |
| §164.308(a)(1)(ii)(A) | Technology asset inventory | Workload discovery; software inventory exports |
| §164.308(a)(1)(ii)(B) | Risk analysis — network map | ADM + flow topology |
| §164.308(a)(2) | Vulnerability management (*proposed*) | CVE + EPSS + reachability |
| §164.312(b) | Audit controls — *24-month retention (proposed)* | Flow/process telemetry to SIEM / durable archive |
| §164.312(e) / NPRM encryption (*verify final §*) | Encryption in transit / path hygiene | Plaintext detection & blocking narratives |
| §164.308(a)(6) | Security incident — timely notification themes | Forensic flow/process timelines |
| §164.306(e) | Annual compliance assessment (*proposed*) | Continuous monitoring artefact cadence |

---

## MAS Technology Risk Management Guidelines

Source: [`MAS-TRM/CSW-MAS-TRM-Reference-Design.md`](./MAS-TRM/CSW-MAS-TRM-Reference-Design.md)

| Topic | CSW can support evidence for |
|---|---|
| Critical system inventory | Workload inventory, labels, application scopes, cloud connector context |
| Network security | Workload-level segmentation, deny-by-default policies, approved-flow baselines |
| Vulnerability management | CVE/package exposure and reachability-informed prioritisation |
| Security monitoring | Flow/process telemetry and SIEM export |
| Incident response | Affected-workload scoping and flow/process timelines |
| Outsourcing / third-party risk | Supplier egress visibility and approved endpoint mapping |

---

## APRA CPS 234

Source: [`APRA-CPS-234/CSW-APRA-CPS234-Reference-Design.md`](./APRA-CPS-234/CSW-APRA-CPS234-Reference-Design.md)

| Topic | CSW can support evidence for |
|---|---|
| Information asset identification | Workload inventory, labels, scopes, and critical information asset mapping |
| Control implementation | Segmentation policy, deny-by-default allowlists, and scope-based enforcement |
| Control testing | Policy simulation, observed-vs-allowed flow review, and evidence exports |
| Incident management | Flow/process timeline and affected workload scoping |
| Service-provider management | Third-party dependency and egress visibility |

---

## NY DFS 23 NYCRR Part 500

Source: [`NY-DFS-23-NYCRR-500/CSW-NYDFS-Reference-Design.md`](./NY-DFS-23-NYCRR-500/CSW-NYDFS-Reference-Design.md)

| Part 500 topic | CSW can support evidence for |
|---|---|
| Cybersecurity program | Workload telemetry and segmentation evidence |
| Asset inventory | Covered workload and application-scope inventory |
| Access privileges | Workload communication allowlists and least-privilege policy |
| Vulnerability management | CVE/package exposure and reachability context |
| Monitoring and testing | Flow/process telemetry, policy simulation, and drift review |
| Incident response | Affected-workload and communication timeline |
| Third-party service providers | External dependency and service-provider egress summary |

---

## TISAX / VDA ISA

Source: [`TISAX/CSW-TISAX-Reference-Design.md`](./TISAX/CSW-TISAX-Reference-Design.md)

| Assessment topic | CSW can support evidence for |
|---|---|
| Information classification | Scope/label mapping to prototype, engineering, and customer-confidential workloads |
| Access control | Workload-level communication allowlists |
| Network segregation | Engineering/prototype enclave segmentation and supplier egress |
| Vulnerability management | Workload package/CVE context and reachability |
| Logging and monitoring | Flow/process telemetry and SIEM export |
| Supplier connectivity | Approved customer/supplier endpoints and egress tracking |

---

## NIST SP 800-82

Source: [`NIST-800-82/CSW-NIST-800-82-Reference-Design.md`](./NIST-800-82/CSW-NIST-800-82-Reference-Design.md)

| 800-82 topic | CSW can support evidence for |
|---|---|
| Network segmentation | Workload policy for OT-facing IT, DMZ brokers, jump hosts, historians |
| Remote access | Vendor/jump-host dependency mapping and allowlists |
| Asset inventory | OT-supporting Windows/Linux workload inventory |
| Vulnerability management | CVE/package context for IT workloads supporting OT |
| Monitoring and detection | Flow/process telemetry and SIEM export for OT-adjacent workloads |
| Incident response | Communication timeline and containment evidence for IT-side systems |

---

## BSI C5

Source: [`BSI-C5/CSW-BSI-C5-Reference-Design.md`](./BSI-C5/CSW-BSI-C5-Reference-Design.md)

| C5 topic | CSW can support evidence for |
|---|---|
| Asset management | Workload inventory, cloud connector context, and labels |
| Communication security | Workload segmentation and approved service paths |
| Operations | Baseline dependencies, drift detection, and policy reports |
| Vulnerability handling | Package/CVE exposure and reachability context |
| Incident management | Flow/process timelines and affected workload scoping |
| Supplier/customer boundaries | Tenant/service egress and shared-service communication |

---

## Reverse Lookup — common CSW capabilities → frameworks

| CSW capability | Frameworks it often supports (apply judgment per deployment) |
|---|---|
| Workload inventory views | HIPAA §164.308(a)(1)(ii)(A) · PCI Req 2 · NIST CM-8 · ISO A.8.1 · CISA ZTMM Devices · 800-207 Tenet 1 · DORA Art. 8 · NIS2 Art. 21(2)(i) · NERC CIP-002 R1 · TSA SD Section II · IEC 62443 SR 3 · FedRAMP CM-8 · CIS Safeguard 1.1 · CSF ID.AM-01 · CMMC CM.L2-3.4.1 · HIPAA NPRM §164.308(a)(1)(ii)(A) · NIST 800-171 03.04.x · MAS TRM critical systems · APRA CPS 234 information assets · NY DFS covered systems · BSI C5 asset management |
| Workload-level segmentation (allow-list / deny-by-default) | HIPAA §164.312(a)(1) · SOC 2 CC6.1 · PCI Req 1, 7 · NIST AC-3, AC-4, SC-7 · ISO A.8.20–A.8.22 · CISA ZTMM Networks · 800-207 Tenets 3, 6 · 800-207A PEP · DORA Art. 9 · NIS2 Art. 21(2)(a), (j) · NERC CIP-005 R1 · TSA SD Section III.A · IEC 62443 SR 5 · GDPR Art. 25 / 32 · FedRAMP AC-4 / SC-7 · SWIFT CSCF 1.1 · HITRUST 01.m–01.o · CIS Safeguards 4.4, 13.4 · CSF PR.IR-01 · CMMC AC.L2-3.1.1, SC.L2-3.13.1 / 3.13.6 · NIST 800-171 03.13.06 · HIPAA NPRM §164.312(a)(2)(vi) · UK CE1 · CSA IVS-09 · COBIT DSS05.02 · MAS TRM network security · APRA CPS 234 control implementation · NY DFS access privileges · TISAX network segregation · NIST 800-82 network segmentation · BSI C5 communication security |
| Identity-aware least-privilege between zones (e.g. IT-to-OT-adjacent) | NIST AC-3, AC-6 · 800-207 Tenets 3, 6 · NERC CIP-005 R1 (IT-side) · TSA SD Section III.A / III.B · IEC 62443 SR 1 · SWIFT CSCF 5.1 · CIS Safeguard 6.1 · CSF PR.AA-05 · CMMC AC.L2-3.1.2 / 3.1.3 · AU E5 · UK CE3 |
| Interactive remote access termination evidence | NERC CIP-005 R2 · NIST AC-17 · DORA Art. 9 (telework) · CIS Safeguard 13.5 · CMMC AC.L2-3.1.13 |
| ADM (application dependency mapping) | PCI Req 1.2.1 · NIST CA-7, CM-2 · ISO A.8.16 · DORA Art. 8(6) · NIS2 Art. 21(2)(a) · NERC CIP-010 R1.1 · TSA SD Section III.A (documented flows) · GDPR Art. 30 (RoPA corroboration) · IEC 62443 SR 5 · FedRAMP AC-4 · HITRUST 10.a · CIS Safeguard 12.4 · CSF ID.AM-03 · CMMC SC.L2-3.13.2 |
| Per-workload listening-port inventory + last-flow timestamp | PCI Req 1.2.6, 2.2.4 · NIST CM-7 · NERC CIP-007 R1 · TSA SD Section III.B · CIS Safeguards 4.6, 2.6 · CMMC CM.L2-3.4.6 · UK CE2 · AU E1/E4 (listener visibility) |
| Exposure / vulnerability views + conversational reachability | PCI Req 6.3.3, 11.3 · NIST RA-5, SI-5 · ISO A.8.8 · DORA Art. 25(1) · NIS2 Art. 21(2)(e) · NERC CIP-010 R3 · TSA SD Section III.D · FedRAMP RA-5 · IEC 62443 SR 3 · HITRUST 10.m · CIS Safeguards 7.1–7.7 · CSF ID.RA-01 / ID.RA-05 · CMMC RA.L2-3.11.2 / 3.11.3 · HIPAA NPRM §164.308(a)(2) · CSA TVM · AU E2/E6 · UK CE5 · MAS TRM vulnerability management · APRA CPS 234 control testing · NY DFS vulnerability management · TISAX vulnerability management · NIST 800-82 vulnerability management · BSI C5 vulnerability handling |
| Configuration baseline + unauthorised-change detection | NIST CM-2, CM-3, CM-6 · ISO A.8.9 · NERC CIP-010 R1, R1.5 · CIS Safeguard 4.1 · CSF PR.PS-01 / ID.RA-07 · CMMC CM.L2-3.4.1 / 3.4.3 · COBIT BAI06 / BAI10 · CSA CCC |
| Process + flow telemetry into SIEM | HIPAA §164.312(b) · SOC 2 CC7.2 · PCI Req 10 · NIST AU-2, AU-12, SI-4 · ISO A.8.16 · DORA Art. 10 · NIS2 Art. 21(2)(b) · NERC CIP-007 R4 · TSA SD Section III.C · FedRAMP SI-4 / AU-* · IEC 62443 SR 6 · SWIFT CSCF 6.4 · HITRUST 09.ab · CIS Safeguards 8.2 / 8.5 / 13.6 · CSF DE.CM-01 / DE.CM-09 / PR.PS-04 · CMMC AU.L2-3.3.1 / 3.3.2 / SI.L2-3.14.6 · NIST 800-171 03.03.x · HIPAA NPRM §164.312(b) (*proposed retention*) · CSA LOG · MAS TRM monitoring · NY DFS monitoring/testing · TISAX logging/monitoring · NIST 800-82 monitoring · BSI C5 incident management |
| Quarantine policy + forensic export | HIPAA §164.308(a)(6) · SOC 2 CC7.3, CC7.4 · NIST IR-4 · DORA Art. 11 · NIS2 Art. 21(2)(b) · NERC CIP-008 · TSA CIRP / 24-hour CISA · GDPR Art. 33–34 · SWIFT CSCF 7.1 · HITRUST 11.a / 11.c · CIS Control 17 · CSF RS.MI-01 / RS.AN-07 · CMMC IR.L2-3.6.x |
| Egress observation + supplier reconciliation | ISO A.5.19–A.5.22 · NIST SR-3, SR-6 · DORA Art. 28 · NIS2 Art. 21(2)(d) · GDPR Art. 28 · NERC CIP-013 R1 (vendor remote access on the IT side) · CIS Safeguards 15.1 / 15.4 · CSF GV.SC-04 / GV.SC-07 / GV.SC-09 · CMMC AC.L2-3.1.20 |
| Plaintext-protocol DENY enforcement | HIPAA §164.312(e)(1) · NIST SC-7, SC-13 (programme support) · ISO A.8.24 · 800-207 Tenet 2 · NIS2 Art. 21(2)(h) · GDPR Art. 32 · SWIFT CSCF 2.6 · FIPS 140 (programme support) · CIS Safeguard 12.2 · CSF PR.DS-02 |
| Quarterly evidence pack to management body / Senior Officer | DORA Art. 5 · NIS2 Art. 20 · ISO Clause 9.3 (management review input) · SOC 2 CC4.1 · NERC CIP-003 R1 · TSA Cybersecurity Coordinator role · CSF GV.OV-01 / 02 / 03 · CMMC supports the SSP/POA&M cycle · COBIT MEA01 / EDM03 (technical inputs) |
| Annual self-assessment evidence pack | NIST CA-2 · ISO Clause 9.2 · TSA Cybersecurity Assessment Plan (CAP) · CIS IG self-assessment · CMMC L2 self-assessment (where contract permits) · HIPAA NPRM §164.306(e) (*proposed*) |
| Behavioural detection + anomaly detection | NIST SI-4 · DORA Art. 10(2) · NIS2 Art. 21(2)(b) · MITRE ATT&CK TA0001–TA0040 · CIS Safeguards 13.2 / 13.3 · CSF DE.AE-02 / DE.AE-07 · CMMC SI.L2-3.14.2 / 3.14.6 · UK CE4 · AU E1/E4 |
| CUI / regulated-data scope labelling | HIPAA ePHI tagging · PCI CDE labelling · DORA ICT-asset criticality (Art. 8) · CSF ID.AM-05 · CMMC CUI scope (foundational) · NIST 800-171 `cui_scope` / enclave labels |

---

## Disclaimer

This index is curated for navigation, not certification. Listing a control
means that a properly scoped Cisco Secure Workload deployment may help you
assemble material artefacts aligned with that expectation — it does **not**
by itself constitute compliance with that control or satisfy supervisory filing
obligations.

Consult each framework reference design plus the disclaimer in [`README.md`](./README.md)
for supervisory reporting expectations, product coverage considerations,
and out-of-scope notes.

**Guidelines.** The tables above summarise typical ways teams discuss
Cisco Secure Workload alongside each control. They are reference points,
not prescriptions—use professional judgment in your environment and with
your assessors. Where mappings use language like *continuous*, *always-on*,
or similar shorthand, that reflects typical operating rhythm—calendar it
and prioritise refreshes using your team's judgment.
