# Cisco Secure Workload — UK NCSC CAF Mapping

**Framework:** UK NCSC Cyber Assessment Framework (CAF) v3.2
**Applies to:** NIS Regulations (OES) assessments conducted by UK Competent
Authorities, including Ofgem, Ofcom, DWI, CAA, DfT and DHSC, and GovAssure
assessments administered by the Cabinet Office / Government Security Group (GSG).
**Status:** Draft v1 — SME review required against the current CAF text
and your assessor's expectations.

> **Companion assets.** This file is the 14-principle crosswalk only. For
> engineering steps, see the
> [Reference Design](./CSW-UK-NCSC-CAF-Reference-Design.md). For the
> customer-facing narrative, see the
> [Compliance Report](./CSW-UK-NCSC-CAF-Compliance-Report.md). For maturity
> scoring, see the [IGP Maturity Scorer](./caf-igp-maturity-scorer.md). For
> what to export per principle, see the
> [Evidence Pack Template](./caf-evidence-pack-template.md).

---

## How to use this document

The CAF describes **outcomes** across 4 Objectives (A/B/C/D) and 14
Principles. Assessors score each principle against granular Indicators of
Good Practice (IGPs) using three statuses — **Achieved**,
**Partially Achieved**, or **Not Achieved**. CSW does not satisfy any
principle by itself; it is an **evidence source** for a subset of the
technical IGPs.

For each principle below, this document identifies:

1. **Applicability** — Direct evidence (material to one contributing
   outcome; here, B5.b only), Supporting evidence (CSW supplements other
   controls), or Out of scope. Direct evidence does not mean Achieved.
2. **Primary existing reference design** inside this repository that already contains
   the relevant engineering detail and control-ID mapping.
3. **Specific CSW evidence** that an assessor can inspect.
4. **Pairings needed** — other controls / tools that must sit alongside CSW
   to close the principle.

The goal is to reuse evidence already produced for sister frameworks
(NIS2, NIST CSF 2.0, ISO 27001:2022, CIS Controls v8.1, NIST 800-53,
IEC 62443) rather than duplicate it.

---

## Quick-scan table

| CAF | Objective / Principle | Applicability | Reuse primarily from |
|---|---|---|---|
| **A1** | Governance | Supporting evidence | [NIST CSF GV.OV / GV.SC](../NIST-CSF-2/), [COBIT APO13](../COBIT-2019/), [ISO 27001 A.5](../ISO-27001-2022/) |
| **A2** | Risk Management | Supporting evidence | [NIS2 Art. 21(2)(a)](../NIS2/), [NIST CSF ID.RA](../NIST-CSF-2/), [NIST 800-53 RA family](../NIST-800-53/) |
| **A3** | Asset Management | Supporting evidence | [CIS Controls 1, 2](../CIS-Controls-v8/), [NIST CSF ID.AM](../NIST-CSF-2/), [NIST 800-53 CM-8](../NIST-800-53/) |
| **A4** | Supply Chain | Supporting evidence | [NIS2 Art. 21(2)(d)](../NIS2/), [ISO A.5.19–A.5.22](../ISO-27001-2022/), [DORA Art. 28](../DORA/) |
| **B1** | Service protection policies, processes and procedures | Supporting evidence | [NIST 800-53 PL family](../NIST-800-53/), [NIST CSF PR.PS](../NIST-CSF-2/), [ISO A.5](../ISO-27001-2022/) |
| **B2** | Identity & Access | Out of scope | — (pair with an identity platform; ISE can supply the identity assertion) |
| **B3** | Data Security | Supporting evidence | [NIST CSF PR.DS](../NIST-CSF-2/), [NIST 800-53 SC family](../NIST-800-53/), [FIPS 140](../FIPS-140/) |
| **B4** | System Security | Supporting evidence | [CIS Controls 4, 7, 8](../CIS-Controls-v8/), [AU Essential Eight E2/E6](../AU-Essential-Eight/) |
| **B5** | Resilient Networks & Systems | Direct evidence for B5.b segregation only | [NIST 800-53 SC-7/AC-4](../NIST-800-53/), [NIST CSF PR.IR](../NIST-CSF-2/), [CIS Control 13](../CIS-Controls-v8/), [ISO A.8.20–A.8.22](../ISO-27001-2022/), [IEC 62443 zones and conduits](../IEC-62443/), [NIST 800-82](../NIST-800-82/) |
| **B6** | Staff Awareness & Training | Out of scope | — |
| **C1** | Security Monitoring | Supporting evidence | [NIST CSF DE.CM / DE.AE](../NIST-CSF-2/), [CIS Control 13](../CIS-Controls-v8/), [NIST 800-53 AU, SI-4](../NIST-800-53/) |
| **C2** | Proactive Security Event Discovery | Supporting evidence | [MITRE ATT&CK reference design](../MITRE-ATTACK/), [NIST CSF DE.AE](../NIST-CSF-2/), [NIST 800-53 SI-4, RA-5](../NIST-800-53/) |
| **D1** | Response and Recovery Planning | Supporting evidence | [NIST CSF RS / RC](../NIST-CSF-2/), [NIST 800-53 IR family](../NIST-800-53/), [DORA Art. 19](../DORA/) |
| **D2** | Lessons Learned | Supporting evidence | [NIST CSF ID.IM](../NIST-CSF-2/), [NIST 800-53 IR family](../NIST-800-53/) |

Direct evidence means CSW produces evidence that is material to that
contributing outcome. It does not mean the principle is Achieved. The only
direct contribution in this mapping is **B5.b** (segregation of the systems
that support essential functions). CAF v3.2 does not name microsegmentation,
eBPF, NetFlow, or IEC 62443. Those are ways to discuss CSW evidence, not
CAF requirements. Supporting evidence supplements a control owned elsewhere.
Out of scope means do not cite CSW for that principle.

---

## Deep crosswalk

### Objective A — Managing Security Risk

#### A1 Governance

> *The organisation has appropriate management policies, processes and
> procedures to govern the security of its network and information systems.*

- **Applicability:** Supporting evidence
- **CSW evidence:** A posture summary (enforcement coverage, open CVE
  count, and the change between snapshots) can be attached to a board or
  CISO pack. That is telemetry. It is not the governance structure, roles,
  or resourcing that A1 requires.
- **Primary reference design to cite:** [NIST CSF GV.OV / GV.SC](../NIST-CSF-2/) for
  outcomes-based governance language; [COBIT 2019 APO13](../COBIT-2019/)
  for managed-security governance structure.
- **Pairings needed:** Documented security roles & resourcing (HR/finance),
  board/exec reporting cadence, risk appetite statement.

#### A2 Risk Management

> *The organisation takes appropriate steps to identify, assess and understand
> security risks to the network and information systems supporting essential
> functions, including an overall organisational approach to risk management.*

- **Applicability:** Supporting evidence
- **CSW evidence:** Enforcement-gap trend, CVE counts tied to workloads,
  which workloads can reach an affected service, and the change between
  snapshots. These are inputs to a risk process. They are not the risk
  assessment.
- **Primary reference designs:** [NIS2 Art. 21(2)(a)](../NIS2/) risk-analysis mapping;
  [NIST CSF ID.RA](../NIST-CSF-2/); [NIST 800-53 RA family](../NIST-800-53/).
- **Pairings needed:** Threat intelligence feeds, risk register, risk-tolerance
  decisions, business-impact analysis.

#### A3 Asset Management

> *Everything required to deliver, maintain or support the systems necessary
> for essential functions is understood. That includes data, people and
> systems, and supporting infrastructure such as power or cooling.*

- **Applicability:** Supporting evidence
- **CSW evidence:** Real-time sensor census (hostname, OS, agent version,
  interfaces, scope membership); installed-package inventory per workload;
  cluster snapshot JSON retained as point-in-time attestation.
- **Primary reference designs:** [CIS Controls 1 & 2](../CIS-Controls-v8/);
  [NIST CSF ID.AM](../NIST-CSF-2/); [NIST 800-53 CM-8](../NIST-800-53/).
- **Pairings needed:** CMDB authoritative source (ServiceNow via
  [CSW ServiceNow Integration](https://github.com/chandrapati/csw-servicenow-integration));
  IPAM/DNS inventory ([Infoblox integration](https://github.com/chandrapati/csw-infoblox-integration));
  cloud-provider asset APIs ([AWS](https://github.com/chandrapati/csw-aws-connector) /
  [Azure](https://github.com/chandrapati/csw-azure-connector) /
  [GCP](https://github.com/chandrapati/csw-gcp-connector) connectors).

#### A4 Supply Chain

> *The organisation understands and manages security risks that arise
> because essential functions depend on suppliers and other third parties.*

- **Applicability:** Supporting evidence
- **CSW evidence:** Vendor-code presence (installed packages per workload
  filtered by vendor); vendor-tagged egress reconciliation using scope-based
  flow analysis (what *actually* talks to vendor endpoints vs what the
  contract allows).
- **Primary reference designs:** [NIS2 Art. 21(2)(d)](../NIS2/);
  [ISO 27001 A.5.19–A.5.22](../ISO-27001-2022/);
  [DORA Art. 28](../DORA/) ICT third-party risk;
  [NIST CSF GV.SC](../NIST-CSF-2/).
- **Pairings needed:** Third-party risk management (TPRM) programme,
  contractual security clauses, assurance questionnaires, SBOM pipeline.

### Objective B — Protecting Against Cyber Attack

#### B1 Service Protection Policies, Processes and Procedures

> *The organisation defines, implements, communicates and enforces appropriate
> policies, processes and procedures for securing the systems and data that
> support essential functions.*

- **Applicability:** Supporting evidence
- **CSW evidence:** Workspace policies defined and version-controlled in CSW;
  continuous enforcement at the host firewall (nftables on Linux, WFP on
  Windows); every flow decision is a de-facto policy test; ADM version
  history as change log.
- **Primary reference designs:** [NIST 800-53 PL family](../NIST-800-53/);
  [NIST CSF PR.PS](../NIST-CSF-2/); [ISO 27001 A.5](../ISO-27001-2022/).
- **Pairings needed:** Policy governance body, change-approval process,
  exception-management workflow.

#### B2 Identity & Access Control

> *Access to the systems that support essential functions is verified,
> authenticated and authorised. CAF v3.2 places particular weight on
> remote access, privileged operations, user access levels, and MFA.*

- **Applicability:** Out of scope
- **Reason:** CSW is not an identity platform. CSW does not authenticate
  users, enforce MFA, manage RBAC, or operate PAM.
- **Pair with:** Enterprise IdP (Entra ID / Okta / Ping) for MFA + lifecycle;
  PAM tool (CyberArk / Delinea / BeyondTrust); SSO.
- **Where CSW *touches* B2:** User-identity–aware microsegmentation via
  [Cisco ISE / pxGrid integration](https://github.com/chandrapati/csw-ise-integration)
  — the identity assertion comes from ISE, not from CSW.

#### B3 Data Security

> *Data stored or transmitted electronically is protected from unauthorised
> access, modification, or deletion.*

- **Applicability:** Supporting evidence (data in transit and exfiltration paths)
- **CSW evidence:** East-west flow visibility across every workload-to-workload
  pair; segmentation policy preventing unauthorised data paths; insecure-cipher
  agent count (TLS hygiene signal); plaintext-protocol deny policies (see
  [FIPS 140 reference design](../FIPS-140/)).
- **CSW does not do:** Data classification, data-at-rest encryption, key
  management (KMS/HSM), DLP content inspection.
- **Primary reference designs:** [NIST CSF PR.DS](../NIST-CSF-2/);
  [NIST 800-53 SC family](../NIST-800-53/);
  [NIS2 Art. 21(2)(h)](../NIS2/); [FIPS 140](../FIPS-140/).
- **Pairings needed:** DLP, KMS/HSM, data classification tool, database
  activity monitoring.

#### B4 System Security

> *Systems critical to essential functions are protected from cyber attack.
> They are secure by design, the attack surface is kept small, and the
> essential function should not be lost because one vulnerability is
> exploited.*

- **Applicability:** Supporting evidence (vulnerability and configuration visibility only)
- **CSW evidence:** Per-workload CVE and package inventory, and which
  workloads can reach an affected service. CSW does not patch systems,
  remove default credentials, or stop unauthorised code from running.
- **Primary reference designs:** [CIS Controls 4, 7, 8](../CIS-Controls-v8/);
  [NIST CSF PR.PS](../NIST-CSF-2/);
  [AU Essential Eight E2/E6](../AU-Essential-Eight/) for patch cadence.
- **Pairings needed:** Patch management platform (SCCM/BigFix/Red Hat
  Satellite); config-baseline tool (CIS Benchmarks via scanner); EDR for
  process-level allow-listing.

#### B5 Resilient Networks & Systems

> *Resilience against cyber attack and system failure is built into the
> design, implementation, operation and management of systems that support
> essential functions. Contributing outcome B5.b is segregation and
> resilience of design. B5.c is secured, tested backups.*

- **Applicability:** Direct evidence for B5.b segregation only
- **CSW evidence:**
  - Workload policy enforced on the host firewall (nftables on Linux, WFP
    on Windows) can show that systems supporting an essential function are
    separated from other business systems, and which flows were denied.
  - CAF's Achieved IGP for B5.b also expects separate infrastructure,
    independent administration, no internet services such as browsing and
    email from those systems, and mitigation of resource and geographic
    limits. CSW does not prove those.
  - B5.c backups are outside CSW.
  - Where an IT/OT boundary exists, CSW covers the IT tier only. Pair with
    an OT visibility product for the device tier. IEC 62443 is a useful
    sister mapping; CAF v3.2 does not cite it.
- **Primary reference designs:** [NIST 800-53 SC-7 / AC-4](../NIST-800-53/);
  [NIST CSF PR.IR](../NIST-CSF-2/); [CIS Control 13](../CIS-Controls-v8/);
  [ISO 27001 A.8.20–A.8.22](../ISO-27001-2022/);
  [IEC 62443 zones and conduits](../IEC-62443/); [NIST 800-82](../NIST-800-82/).
- **Pairings needed:** Perimeter / DDoS layer (not CSW); OT-aware DPI
  (Cyber Vision / Claroty / Nozomi / Dragos); HA / BCP architecture.

#### B6 Staff Awareness & Training

> *Staff have the awareness, knowledge and skills to carry out their roles
> and to support the security of the essential function.*

- **Applicability:** Out of scope
- **Pair with:** Security awareness platform (KnowBe4 / Proofpoint /
  SANS); role-based training programme.

### Objective C — Detecting Cyber Security Events

#### C1 Security Monitoring

> *The organisation monitors the security status of the systems supporting
> essential functions in order to detect potential security problems and to
> track whether protective measures are still effective. C1.a is monitoring
> coverage. C1.b is protecting the logs themselves.*

- **Applicability:** Supporting evidence
- **CSW evidence:** Where agents are installed, CSW records connections with
  process context and the policy decision. That can feed host-based
  monitoring under C1.a. CSW is not the log store: C1.b (integrity,
  retention, access control, and a common time source for the master logs)
  stays with the logging platform. Authentication monitoring stays with the
  identity platform.
- **Primary reference designs:** [NIST CSF DE.CM, DE.AE](../NIST-CSF-2/);
  [CIS Control 13](../CIS-Controls-v8/);
  [NIST 800-53 AU, SI-4](../NIST-800-53/);
  [NIS2 Art. 21(2)(b)](../NIS2/).
- **Pairings needed:** SIEM/SOAR, authentication log sources (IdP), firewall
  logs, UBA.

#### C2 Proactive Event Discovery

> *The organisation detects malicious activity that affects, or could affect,
> essential functions even when that activity evades standard signature-based
> prevent or detect solutions.*

- **Applicability:** Supporting evidence
- **CSW evidence:** Observed communication (which systems do and do not
  talk) and forensic events a detection team can review. CSW is not the
  hunt programme and is not a vulnerability scanner. See the
  [MITRE ATT&CK reference design](../MITRE-ATTACK/) when mapping events to techniques.
- **Primary reference designs:** [MITRE ATT&CK reference design](../MITRE-ATTACK/);
  [NIST CSF DE.AE](../NIST-CSF-2/);
  [NIST 800-53 SI-4, RA-5](../NIST-800-53/).
- **Pairings needed:** External threat-intel feeds, EDR / XDR for host-level
  behavioural analytics, SOC playbooks.

### Objective D — Minimising the Impact of Incidents

#### D1 Response and Recovery Planning

> *The organisation has well-defined and tested incident management,
> continuity, and containment so that an incident does not stop the
> essential function for longer than the organisation has planned.*

- **Applicability:** Supporting evidence
- **CSW evidence:** A forensic flow history can support an incident
  timeline, and a previous policy version can be restored. That is
  containment evidence. It is not the response plan, the exercise, or
  the restore.
- **CSW does not do:** Backup, restore, immutable storage, DR orchestration,
  BCP site switchover.
- **Primary reference designs:** [NIST CSF RS / RC pillars](../NIST-CSF-2/);
  [NIST 800-53 IR, CP families](../NIST-800-53/);
  [NIS2 Art. 21(2)(b)](../NIS2/); [DORA Art. 19](../DORA/).
- **Pairings needed:** Backup/DR platform (Veeam/Rubrik/Cohesity);
  IR orchestration (SOAR); reference design library; tabletop exercise cadence.

#### D2 Lessons Learned

> *When an incident occurs, the organisation understands the root causes
> and uses them to improve protective measures.*

- **Applicability:** Supporting evidence
- **CSW evidence:** The difference between snapshots can show what changed
  around an incident. The lessons-learned process itself sits outside CSW.
- **Primary reference designs:** [NIST CSF ID.IM](../NIST-CSF-2/);
  [NIST 800-53 IR family](../NIST-800-53/). PM-14 is testing, training and
  monitoring, not lessons learned, so it is not the D2 mapping.
- **Pairings needed:** Formal lessons-learned / post-incident-review process;
  risk-register integration; policy-update workflow.

---

## What this mapping does **not** cover

Honest about scope so assessors don't form false expectations:

| Area | Why not | Where to look instead |
|---|---|---|
| **B2 Identity & Access entirely** | CSW is not an IAM tool. | IdP + PAM. CSW can consume ISE identity assertions for policy via [ISE integration](https://github.com/chandrapati/csw-ise-integration), but the authentication/authorisation decision lives in ISE. |
| **B6 Staff training entirely** | Not applicable. | Security awareness platform. |
| **Data at rest + KMS (B3)** | CSW doesn't touch stored data or keys. | KMS/HSM + storage encryption. |
| **Backup and restore (B5.c, and the recovery part of D1)** | CSW does not operate backup. | Backup/DR platform. |
| **A1 Governance structure** | CSW produces metrics, not org charts or role definitions. | HR + CISO office. |
| **Perimeter / DDoS** | CSW is east-west, not north-south edge defence. | Secure Firewall / DDoS service. |
| **OT device tier of B5** | CSW agents run on servers, not PLCs/RTUs. | Cyber Vision / Claroty / Nozomi / Dragos. |

---

## Related documents in this folder

- **[CSW-UK-NCSC-CAF-Reference-Design.md](./CSW-UK-NCSC-CAF-Reference-Design.md)** —
  engineering view: scope design, labels, policy authoring per principle,
  evidence collection steps.
- **[CSW-UK-NCSC-CAF-Compliance-Report.md](./CSW-UK-NCSC-CAF-Compliance-Report.md)** —
  customer-facing narrative for CISO / exec audiences.
- **[caf-igp-maturity-scorer.md](./caf-igp-maturity-scorer.md)** — working
  checks for the CSW evidence slice. A check does not set the IGP score.
- **[caf-evidence-pack-template.md](./caf-evidence-pack-template.md)** — what
  to export from CSW per principle for a GovAssure / OES submission.

## Disclaimer

Draft v1. Mapping derived from the UK NCSC Cyber Assessment Framework v3.2
and cross-referenced against documented Cisco Secure Workload product
capabilities. Requires SME review against your Competent Authority's current
expectations before relied upon in a formal assessment. See the
[repository-level disclaimer](../README.md#disclaimer) for the full
informational-only clause.
