# Cisco Secure Workload — UK NCSC CAF Compliance Report

**Framework:** UK NCSC Cyber Assessment Framework (CAF) v3.2
**Audience:** CISO, Head of Compliance, CAF Lead Assessor, Competent
Authority relationship owner.
**Status:** Draft v1 — SME review required.

---

## How to read the coverage words

**Full Coverage** on the older reports means Secure Workload can produce that row's artifact. It does not mean the control is met.

**Partial Coverage** means file that export next to another control.

**Evidence Required** means Secure Workload has no record. The customer files the contract, the analysis, or the HR or physical-security evidence.

**Direct**, **Supporting**, and **Out of scope** on the newer reports are the same idea in different words. Direct is still evidence, not a pass. In this CAF report, direct evidence is B5.b only. Direct evidence does not mean Achieved.

## Executive summary

The UK NCSC Cyber Assessment Framework (CAF) is the outcome-based security
assessment framework used by UK Competent Authorities, including Ofgem,
Ofcom, DWI, CAA, DfT and DHSC, under the NIS Regulations and by the Cabinet Office
Government Security Group under GovAssure. It evaluates an organisation
against **14 Principles** grouped under **4 Objectives**, scored against
Indicators of Good Practice (IGPs) as **Achieved**, **Partially Achieved**,
or **Not Achieved**.

Cisco Secure Workload (CSW) is a workload-visibility and east-west policy
platform. CSW does not satisfy any CAF principle on its own. The only
**direct evidence** contribution is **B5.b**, segregation of the systems
that support an essential function from other business systems. CSW can
**support** A1, A2, A3, A4, B1, B3, B4, C1, C2, D1 and D2. B2 and B6 are
out of scope. CAF v3.2 does not require microsegmentation, eBPF, or
NetFlow by name.

For a Competent Authority assessment, CSW output is continuously produced
evidence an assessor can inspect. It does not, by itself, move a principle
from Partially Achieved to Achieved.

---

## What CSW contributes per CAF Objective

### Objective A — Managing Security Risk

- **A2 Risk Management (Supporting).** CSW can feed exposure and
  enforcement-gap trends into a risk process. CAF A2 still requires the
  organisation's own risk method, decision-makers, and review. It does not
  say "replace the annual audit with threat modelling."
- **A3 Asset Management (Supporting).** Inventory of agented workloads,
  installed packages, interface addresses, scope membership, and agent
  posture. Pairs with CMDB/IPAM/cloud-provider sources via CSW connectors.
- **A1 Governance / A4 Supply Chain (Supporting).** CSW produces
  governance telemetry (board-ready posture summaries) and vendor-code
  presence signals; it does not substitute for governance structure or
  TPRM programmes.

### Objective B — Protecting Against Cyber Attack

- **B5 Resilient Networks & Systems (direct evidence for B5.b only).**
  Host-firewall policy can show segregation between essential-function
  systems and other business systems, and which connections were denied.
  CAF Achieved for B5.b also expects separate infrastructure, independent
  administration, no browsing or email from those systems, and mitigation
  of resource and geographic limits. B5.c backups are not a CSW control.
  CAF does not cite eBPF, microsegmentation, or IEC 62443.
- **B1 Service protection policies (Supporting).** Workspace-based policy authoring
  with ADM-suggested baselines, pre-enforcement simulation, in-kernel
  enforcement, and ADM version history as change log.
- **B4 System Security (Supporting).** Per-workload CVE inventory with
  exploit-intelligence prioritisation; package inventory for patch
  targeting; agent-version drift as config-baseline signal.
- **B3 Data Security (Supporting).** East-west segmentation prevents
  unauthorised data paths; insecure-cipher count flags TLS hygiene gaps.
  Pair with KMS, DLP, and data classification.
- **B2 Identity & Access (Out of scope).** CSW is not an IAM tool. Pair
  with your IdP and PAM; use ISE integration if identity-aware
  segmentation is required.
- **B6 Staff Awareness (Out of scope).**

### Objective C — Detecting Cyber Security Events

- **C1 Security Monitoring (Supporting).** Where agents are installed, CSW
  records connections with process context and the policy decision. That
  can feed C1.a host monitoring. CSW is not the log store (C1.b) and does
  not cover authentication events. CAF does not name NetFlow, IPFIX, or
  eBPF.
- **C2 Proactive Security Event Discovery (Supporting).** MITRE ATT&CK technique
  coverage through CSW forensics rules; vulnerability scanning with
  threat-intel enrichment; anomaly detection via policy-violation
  (rejected-flow) analysis.

### Objective D — Minimising the Impact of Incidents

- **D1 Response & Recovery (Supporting).** CSW contains blast radius
  (limits incident scope) and provides per-connection flow history for
  IR timeline reconstruction. CSW does not operate backup, restore, or
  DR orchestration — pair with your backup/DR platform.
- **D2 Lessons Learned (Supporting).** The difference between snapshots
  can show what changed. The root-cause review sits outside CSW.

---

## IGP maturity narrative (how CSW moves the needle)

A representative CAF journey, year-over-year:

| Principle | Year 0 (baseline) | Year 1 (CSW in place) | Year 2 (CSW evidence in use) |
|---|---|---|---|
| A2 | Risk register only | Posture snapshots exist | Snapshots are used in the risk review. A2 is still the organisation's risk process |
| A3 | Asset register only | Agent census exists | Census reconciled for workloads CSW can see. People, power, and cooling stay outside CSW |
| B1 | Policies on paper | Workload policy authored and simulated | Workload policy enforced where intended. The wider policy set stays outside CSW |
| B4 | Vulnerability list not tied to workloads | CVE list tied to workloads | Reachability used to prioritise patching. Patching itself stays outside CSW |
| B5.b | Essential-function systems not separated | Segregation designed or simulated | Denied connections show segregation. Physical separation, independent administration, and backups stay outside CSW |
| C1 | Gateway logs only | Host connection records exist | Monitoring team uses those records. The log store stays outside CSW |
| C2 | Signature detection only | Communication baseline exists | Unexpected paths are investigated. The hunt programme stays outside CSW |
| D1 | Response plan not tested with workload evidence | Flow history available | Timeline evidence used in an exercise. Restore stays outside CSW |

The maturity scorer document (see
[caf-igp-maturity-scorer.md](./caf-igp-maturity-scorer.md)) gives the
specific CSW observations behind each row. It does not set the IGP score.

---

## What CSW explicitly does **not** satisfy

Being honest about scope is itself CAF-aligned (Principle A1 wants clear
accountability). The following CAF obligations are **not** addressable
by CSW alone and must be evidenced through pairings:

- **B2 Identity & Access** — IdP + PAM (CSW consumes identity, doesn't
  issue it).
- **B6 Staff Awareness & Training** — security awareness platform.
- **B3 Data at rest + key management** — KMS/HSM + storage encryption.
- **D1 Backup / restore / BCP** — backup/DR platform.
- **A1 Governance structure** — org-chart, roles, resourcing decisions.
- **Perimeter / DDoS** — Secure Firewall + DDoS service.
- **OT device tier (B5)** — Cyber Vision / Claroty / Nozomi / Dragos.

A credible CAF submission must address these pairings explicitly rather
than ignore them.

---

## Suggested next steps

1. **Scope workshop.** Translate essential functions into the CSW scope
   pattern described in the
   [Reference Design](./CSW-UK-NCSC-CAF-Reference-Design.md) Phase 1.
2. **Baseline snapshot.** Run `cluster_snapshot.py` and
   `generate_executive_report.py` to capture the current posture — this
   becomes "Year 0" in the maturity narrative.
3. **Policy authoring.** Author B5 segmentation per essential function
   with the ADM-suggested baseline; simulate for two full business cycles.
4. **Quarterly evidence pack.** Pre-stage CSW artefacts into the pack
   structure described in
   [caf-evidence-pack-template.md](./caf-evidence-pack-template.md).
5. **Pair-up matrix.** Document which pairings (IdP, PAM, DLP, backup,
   training, OT visibility, perimeter) will supply the non-CSW evidence.
6. **Pre-assessment dry run.** Walk the pack with the CAF lead before the
   Competent Authority or GovAssure assessment. GovAssure is not a FedRAMP
   3PAO review.

---

## Disclaimer

Draft v1. Mapping derived from the UK NCSC CAF v3.2 and documented CSW
capabilities. For informational and reference purposes only — not legal,
regulatory, or audit advice. Requires SME review against the current CAF
text and your Competent Authority's expectations before relied upon in a
formal assessment. See the
[repository-level disclaimer](../README.md#disclaimer) for the full clause.
