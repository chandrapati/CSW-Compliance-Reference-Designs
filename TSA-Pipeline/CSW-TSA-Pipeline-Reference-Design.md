# Cisco Secure Workload — TSA Pipeline Security
## Reference Design | Owners and Operators of TSA-Designated Natural Gas / Hazardous Liquid Pipelines

**Version:** 1.0 (draft — pending SME review) | **Standard:** TSA Security Directive Pipeline-2021-02 series (current revision; the SD has been republished as 02A, 02B, 02C, and 02D as TSA has updated the requirements; this reference design is generic to the current effective version) and Security Directive Pipeline-2021-01 series for incident reporting | **Audience:** Pipeline owner/operators designated by TSA as Critical Pipeline owner/operators, and the cybersecurity teams supporting them | **Environment:** IT estate supporting OT (corporate IT, engineering workstations, SCADA jump servers, historian/MES, vendor-access servers — *not* the pipeline OT control devices themselves)

---

## Reader's Guide

**Who this is for.** TSA-designated owner/operators of natural gas
and oil/hazardous liquid pipelines and their cybersecurity, IT, and
OT operations teams. The reference design is also useful for pipeline
operators not currently TSA-designated who want to align proactively
with the SD framework.

**Scope boundary you must understand before reading further.** Cisco
Secure Workload (CSW) is a workload-protection and segmentation
platform for **IT estate** — servers, virtual machines, containers,
and cloud workloads. CSW does **not** enforce policy on RTUs,
flow computers, PLCs, valve actuators, or any other Level 0–2 OT
device on the pipeline itself. CSW's TSA SD contribution is at the
**IT-side of the IT/OT boundary** and within the IT systems that
support pipeline operations — engineering workstations, SCADA jump
servers, historian databases, MES/EAM systems, vendor remote-access
hosts, identity/PKI services, and the corporate IT systems that
interact with Critical Cyber Systems on the IT side.

**Questions this reference design helps you answer:**

- *Section II — Critical Cyber System identification: do I have a
  current inventory of every IT system that supports pipeline
  operations, with the supporting Critical Cyber System linkage
  documented and continuously refreshed?*
- *Section III.A — Network Segmentation (IT/OT separation): can I
  prove that segmentation between IT and OT is enforced at the
  workload level on the IT side, and that the documented
  IT-to-OT data flows are the only flows actually occurring?*
- *Section III.B — Access Control Measures: can I produce evidence
  that access to Critical Cyber Systems and to the IT systems that
  support them is least-privilege, monitored, and reviewed on a
  documented cadence?*
- *Section III.C — Continuous Monitoring and Detection: when an
  anomalous IT-side flow appears (e.g., a corporate workstation
  starts talking to a SCADA jump server it has never touched
  before), is it detected in time to investigate?*
- *Section III.D — Reduce Risk of Exploitation of Unpatched Systems:
  can I produce a per-IT-workload vulnerability inventory with
  remediation tracking, prioritised by which workloads support
  Critical Cyber Systems?*
- *Cybersecurity Incident Response Plan: when a Cybersecurity
  Incident occurs on the IT estate, can I reconstruct the process
  and flow context to support TSA's 24-hour reporting requirement?*
- *Cybersecurity Assessment Plan (CAP): can I produce evidence of
  annual implementation assessment for the IT-side controls, with
  measurable test outcomes?*

**What you'll need.** Your current Critical Cyber System inventory
(per Section II of the SD), your most recent Cybersecurity Incident
Response Plan, your Cybersecurity Architecture Design Review
documentation, and your current CAP. CSW will augment these
governance artefacts with workload-level evidence; it will not
replace them.

**Where to start.** Section 2 if you are scoping CSW relative to the
Critical Cyber System inventory; sections 3–4 if IT/OT segmentation
is the priority; section 5 if access control evidence is the gap;
section 6 if the CAP requires improved continuous monitoring
evidence; section 9 if vendor and third-party visibility is the
open item.

**Important.** TSA SDs are issued under TSA's regulatory authority;
designated owner/operators are required to comply. Nothing in this
reference design substitutes for the responsible Senior Cybersecurity
Officer's accountability under the SD or for the formal TSA
inspection response. CSW gives the responsible officer technical
evidence inputs for the operator's compliance programme; it does not
substitute for the designated security programme.

---

<!-- CSW-RUNBOOK-PRIMER:v1 -->

## CSW primer — if you are new to Cisco Secure Workload

Cisco Secure Workload (CSW) is a **workload protection platform**. A lightweight **agent** on each server/VM/container observes processes and network flows; **cloud connectors** add AWS/Azure/GCP inventory where agents are not deployed.

| CSW term | Meaning | Why compliance teams care |
|----------|---------|---------------------------|
| **Scope** | Logical boundary (CDE, PHI zone, CUI enclave) | Defines the systems you must prove are isolated |
| **Label / filter** | Tag or query assigning workloads to scopes | Automates scope membership — reduces drift |
| **ADM** | Application Dependency Mapping from observed traffic | **Live** network/data-flow diagram for assessors |
| **Workspace** | Policy container for one scope or application | Where allow/deny rules are authored |
| **Monitor → Simulation → Enforce** | Safe rollout sequence | Simulation = change-board evidence before blocking traffic |
| **Denied Connections** | Log of flows blocked by policy | Primary proof that enforcement **operates** |

**Console areas:** Investigate (inventory, flows, vulns) · Defend/Segmentation (policy) · Manage (agents) · Platform (connectors) · Administration (audit log)

**Read next:** [Compliance evidence playbook](../docs/compliance-evidence-playbook.md) (full step-by-step) · [About CSW](../docs/about-csw.md) (platform intro)

---

## Universal evidence workflow

Execute these phases for **this framework's** compliance boundary. Map exports to control IDs in the **Reporting & Evidence** section below.

| Phase | Goal | Key CSW actions | Typical duration |
|-------|------|-----------------|------------------|
| **1 — Coverage** | Every in-scope workload in CSW | Install agents/connectors; apply compliance labels; create scope | Days 1–10 |
| **2 — Baseline** | Machine-generated flow map | Run ADM ≥2 weeks; export clusters; app-owner signoff | Days 11–28 |
| **3 — Policy** | Designed isolation before enforce | Build workspace; Simulation mode; fix false positives | Days 29–45 |
| **4 — Operate** | Continuous proof between audits | Enforce; quarterly export pack; ADM refresh every 90 days | Ongoing |

### Phase 1 checklist (coverage)

- [ ] In-scope host list reconciled to CSW Inventory (100% or documented exceptions)
- [ ] Labels applied: `compliance:<framework>`, `data:<classification>`, `env:<tier>`
- [ ] CSW scope created matching compliance boundary
- [ ] **Export:** inventory CSV + agent status screenshot

### Phase 2 checklist (baseline)

- [ ] ADM running on compliance scope for full business cycle (≥2 weeks)
- [ ] Unexpected flows documented (shadow IT, vendor egress, scope creep)
- [ ] App owners signed cluster-to-application mapping
- [ ] **Export:** ADM diagram + flow samples with process context

### Phase 3 checklist (policy)

- [ ] Default-deny posture defined for sensitive scope
- [ ] ADM-imported rules refined; Simulation run ≥1 week
- [ ] Change tickets for false-positive fixes; exception register updated
- [ ] **Export:** policy export + simulation report

### Phase 4 checklist (operate)

- [ ] Enforcement enabled on pilot scope; negative test recorded in Denied Connections
- [ ] Quarterly pack: inventory, policy, denies, vulns, audit log (see playbook)
- [ ] SIEM integration verified (sample events)
- [ ] **Export:** enforcement screenshot + quarterly binder

### What CSW evidence does not replace

Physical access, HR/training records, encryption key management, signed BAAs/vendor contracts, formal pen tests, and assessor attestation still require separate programmes. CSW addresses the **workload-resident** slice: segmentation, flows, process context, vuln reachability, and change drift.

---

## CSW effectiveness for this framework

- IT/OT segmentation evidence (Section III.A) on IT workloads
- Access control + monitoring (III.B/C) at workload tier
- CIRP/CAP evidence packs from forensic flow export

**Compared to manual programmes:** static diagrams and annual firewall samples age immediately; CSW ties evidence to **live workload behaviour** and produces queryable exports on demand — supporting "operating effectively" language in PCI v4.0, SOC 2 CC7, and HIPAA risk analysis.

---

## 1. Overview

The TSA Pipeline Security Directive 2021-02 series (currently in
revision; consult the TSA web site for the active revision letter)
imposes mandatory cybersecurity requirements on TSA-designated
Critical Pipeline owner/operators in the United States. The directive
mirrors much of the CISA CPGs and NIST 800-53 control family in
content, but applies on a sector-specific basis with TSA enforcement.

The SD's substantive cybersecurity requirements fall under four broad
sections:

| Section | Topic | CSW relevance |
|---|---|---|
| Section II | Critical Cyber System identification + Cybersecurity Coordinator + governance | Inventory + scope labelling on the IT side |
| Section III.A | Network Segmentation (IT/OT separation) | **Direct** — IT-side segmentation up to the IT/OT boundary |
| Section III.B | Access Control Measures | **Direct** — workload-level least-privilege; deny-by-default for cross-zone access |
| Section III.C | Continuous Monitoring & Detection | **Direct** — behavioural detection + flow telemetry to SIEM |
| Section III.D | Reduce Risk of Exploitation of Unpatched Systems | **Direct** — continuous CVE inventory tied to workload context |
| Cybersecurity Incident Response Plan | Plan, test, report | Forensic flow + process telemetry for incident reconstruction |
| Cybersecurity Assessment Plan (CAP) | Annual implementation assessment | Evidence pack supporting the CAP self-assessment |
| Cybersecurity Architecture Design Review | Architecture + design assessment | Workload-level inventory and dependency graph as inputs |

**Where CSW fits — the short version.** TSA SDs explicitly call for
network segmentation between IT and OT, continuous monitoring,
access control, and reduction of unpatched-system risk. CSW is a
direct fit for the **IT side** of all four substantive III.A–III.D
requirements. CSW supplements (does not replace) your OT-aware
monitoring and your IT/OT firewall pair at the boundary.

**Where CSW does not fit.** CSW does not enforce policy on RTUs,
flow computers, PLCs, IEDs, HMIs at the OT layer; does not perform
deep packet inspection of OT protocols (DNP3, IEC 61850, Modbus,
OPC-UA); is not certified as a Cybersecurity Architecture Design
Review tool; and does not author the Cybersecurity Incident Response
Plan. Your OT-aware monitoring stack (Cisco Cyber Vision, Claroty,
Nozomi, Dragos, etc.) and your boundary firewall remain the
controlling artefacts at and below the IT/OT boundary.

---

## 2. Section II — Critical Cyber System Identification

The SD requires identification of every Critical Cyber System
(those that, if compromised or rendered unavailable, would result in
operational disruption). The inventory must be kept current and made
available to TSA on request.

**CSW does not perform Critical Cyber System designation.** That is
an engineering and risk decision driven by the operational impact
analysis your Senior Cybersecurity Officer signs off. CSW *does*
host the labels that downstream IT-side controls depend on.

**CSW Implementation:**
```
Step 1: Receive the Critical Cyber System list from the operations
        risk function
  → Per IT workload supporting a CCS:
      ccs_id:       [reference to your CCS register entry]
      ccs_function: [scada-jump | historian | mes | hmi-server-it |
                     vendor-access | engineering-workstation |
                     identity | patch-repo | other-it-supporting]
      ot_facing:    true | false   (does the workload reach into OT?)
      site:         [pipeline segment / facility name]

Step 2: Apply consistent labels to every CSW-managed workload
  CSW UI → Inventory → Bulk Label
  Mandatory labels:
    ccs_id, ccs_function, ot_facing, site, region, classification

Step 3: Build CSW Scopes per (region, site, ccs_function)
  CSW UI → Organize → Scopes → New
  → Recommended hierarchy:
        Root
        └── Pipeline-IT-Estate
            ├── OT-Facing (ot_facing=true)
            │   ├── SCADA-Jump-Hosts
            │   ├── Historians
            │   ├── HMI-Servers-IT
            │   ├── Engineering-Workstations
            │   └── Vendor-Access-Hosts
            ├── CCS-Supporting-IT (CCS but not ot-facing)
            │   ├── Identity-and-PKI
            │   ├── Patch-Repositories
            │   └── MES-and-EAM
            └── Corporate-IT (default-deny target)

Step 4: Validate scope membership against the CCS register
  → Cross-check CSW count vs. the CCS register; reconcile any delta
    with the CCS Asset Owner before formal sign-off
```

**Evidence:** Per-scope membership snapshot (CSV) with workload
identity, OS, owner, CCS reference, OT-facing flag, site, and last-
seen timestamp. This becomes the IT-side companion to your Section
II Critical Cyber System inventory.

---

## 3. Section III.A — Network Segmentation (IT/OT Separation)

TSA SD Section III.A is the foundational segmentation requirement.
The directive calls for network segmentation policies and controls
ensuring that the OT system can continue to safely operate in the
event of an IT system compromise, *and vice versa*.

**Architectural reality.** Your IT/OT boundary firewall(s) remain
the controlling artefact for the actual IT/OT boundary. CSW
contributes by ensuring *the IT-side itself is segmented*, so that a
compromised corporate-IT workload cannot reach the boundary firewall
from an undocumented direction.

**CSW Implementation — IT-side segmentation pattern:**
```
Step 1: Define the IT-side OT-adjacent enclave policy workspace
  CSW UI → Defend → Segmentation → New Workspace
  Name: tsa-pipeline-it-side-{site}
  Scope: site = {site} AND ot_facing = true OR ccs_function != null

Step 2: Compute the as-observed baseline via ADM
  Run ADM ≥ 14 days; capture maintenance and turnaround windows
  Reject "noise" clusters; rename clusters to operational roles

Step 3: Layer SD-aligned hardening rules on top of the baseline
  DENY:  Corporate-IT → OT-Facing-IT
         (only documented hosts may reach the OT-adjacent IT tier)
  DENY:  Corporate-IT → Boundary-Firewall-IPs
         (the IT/OT firewall itself only accessible from documented
          management network)
  DENY:  OT-Facing-IT → Internet
         (no direct internet from a SCADA jump host or historian)
  ALLOW: Vendor-Access-Hosts → vendor-allowlisted FQDNs only
         (vendor remote support path documented and bounded)
  ALLOW: Patch-Repositories → vendor patch URLs only
         (so patching can occur without broad internet)
  LOG:   Any unmatched flow inbound to OT-Facing-IT or CCS-Supporting-IT
         (becomes a Section III.C continuous-monitoring candidate)

Step 4: Run in Simulation for ≥ 30 days
  → Resolve every legitimate-but-blocked flow with the asset owner;
    document each exception in the workspace notes for the audit
    trail referenced from the SD.

Step 5: Promote to Enforce; gate by change-management approval
  → Each subsequent change captured in CSW change history; this is
    the IT-side complement to your Section III.A documentation.
```

**Evidence:** (a) workspace export per site; (b) simulation→
enforcement transition log; (c) quarterly enforcement diff report
delivered to the responsible Senior Cybersecurity Officer.

---

## 4. Section III.A continued — Documented Data Flows

The SD calls for documentation of permitted communication between IT
and OT systems, with denial of all other communication.

**CSW Implementation:**
```
Step 1: Enumerate observed IT→OT flows
  CSW UI → Investigate → Flow Search
  Filter: source_scope ⊂ Pipeline-IT-Estate AND
          destination_subnet ∈ OT-network-ranges
  → Output: observed IT→OT flow inventory per site for instrumented IT
    workloads and configured OT destination definitions

Step 2: Reconcile against the documented flows in your Cybersecurity
        Architecture Design Review
  → For each observed flow, find the corresponding documented flow;
    flag missing flows (observed but not documented) and stale
    documentation (documented but no longer observed)

Step 3: Propose policy update + documentation update for each delta
  → Observed-but-undocumented: investigate, then either remove the
    flow or document the rationale
  → Documented-but-not-observed: candidate for removal during the
    next architecture review cycle

Step 4: Continuously monitor for new IT→OT edges
  → CSW alert: "new flow source/destination pair to OT range"
  → Routes to the IT/OT change board for review under Section III.A
```

**Evidence:** (a) IT→OT flow inventory dated within the period;
(b) observed-vs-documented delta report; (c) new-edge alert log.

---

## 5. Section III.B — Access Control Measures

The SD requires access control measures to enforce least privilege
and to prevent unauthorised access to Critical Cyber Systems.

**CSW Implementation — Workload-level least-privilege:**
```
Step 1: Enforce deny-by-default at the CSW workload identity layer
  → Every flow must match an explicit allow rule; everything else
    is denied with audit logging
  → Identity for CSW policy = workload + scope + tag set, not just
    IP or subnet (this matters because IPs reassign in cloud and
    virtualised environments)

Step 2: Limit lateral access between CCS-Supporting-IT workloads
  → Default: workloads in different ccs_function categories may
    not communicate
  → Explicit allow only for documented operational paths (e.g.,
    historian needs read from SCADA-jump for replication)

Step 3: Limit access to vendor-access hosts to specific source set
  → ALLOW: {documented MFA-VPN pool} → vendor-access hosts only
  → DENY:  any other source → vendor-access hosts

Step 4: Schedule cadence-based access review
  → Quarterly: review the allow ruleset; sunset any allow rule
    whose last-observed flow is older than 90 days
  → Annual: full ruleset review with the Cybersecurity Officer
```

**Evidence:** (a) policy export with rule provenance and last-flow
timestamp; (b) quarterly access review minutes; (c) sunset log for
removed rules.

---

## 6. Section III.C — Continuous Monitoring and Detection

The SD calls for continuous monitoring and detection policies and
procedures designed to detect cybersecurity threats and correct
anomalies that affect Critical Cyber System operations.

**CSW Implementation:**
```
Step 1: Enable behavioural / process-based detections on CSW-managed
        workloads
  CSW UI → Defend → Forensics → Rules
  → Out-of-the-box rules: privilege escalation, persistence, lateral
    movement, suspicious child processes
  → Custom rules: encode SD-relevant abuse patterns
        Example: "Process on SCADA-jump host writes to startup paths"
        Example: "Outbound to non-allowlisted FQDN from historian"
        Example: "New listening port opened on engineering workstation"

Step 2: Conversation-graph anomaly detection
  → CSW auto-flags new edges in the dependency graph for OT-Facing-IT
    and CCS-Supporting-IT scopes
  → Auto-flags changes in port/protocol distribution per workload

Step 3: Wire alerts to the SOC
  CSW UI → Manage → Data Tap → SIEM
  → Splunk, QRadar, Sentinel, Cisco XDR
  → Tag every alert with ccs_id and ot_facing so the SOC can route
    by criticality
  → Pair with your OT-aware sensor alerts for full IT+OT coverage

Step 4: Track detection latency
  → CSW timestamps every detection; SIEM timestamps acknowledgement
  → Compute MTTD per CCS function; report quarterly to the Senior
    Cybersecurity Officer
```

**Evidence:** (a) detection rule catalogue with last-modified dates;
(b) SIEM forwarding configuration; (c) MTTD trend report per CCS
function.

---

## 7. Section III.D — Reduce Risk of Exploitation of Unpatched Systems

The SD requires a documented patch management strategy and the
controls to reduce risk on unpatched IT systems.

**CSW Implementation:**
```
Step 1: Continuous CVE inventory at workload level
  CSW UI → Investigate → Vulnerability Report
  → Per-workload CVE list with CVSS, exploit availability, EPSS score
  → Filter by ccs_function != null → prioritise CCS-supporting tier

Step 2: Compensating controls for unpatchable systems
  → For workloads where patching is delayed (vendor lifecycle,
    operational window, regulatory test):
        Restrict source set for the vulnerable port
        Add behavioural detection for known exploit patterns
        Log every flow involving the affected port for review
  → Document each compensating control in the workload's CSW
    workspace notes; this is the audit trail for the "reduce risk"
    standard when patching is not feasible

Step 3: Patch verification
  → After patch, CSW package inventory updates within the next
    snapshot cycle
  → Diff report shows the patched version; CVE inventory drops the
    addressed vulnerability automatically

Step 4: Reporting
  → Monthly: CVE backlog by CCS function and severity
  → Quarterly: trend of mean-time-to-patch by impact rating
  → Annual: input to the CAP self-assessment
```

**Evidence:** (a) per-CCS CVE list dated to the period; (b) patch
remediation tracking with ticket IDs; (c) compensating control
register for unpatched-but-mitigated workloads.

---

## 8. Cybersecurity Incident Response Plan

The SD requires owner/operators to develop and maintain a
Cybersecurity Incident Response Plan and to report Cybersecurity
Incidents to CISA within 24 hours.

**CSW Implementation — Incident Reconstruction Bundle:**
```
For each Cybersecurity Incident on a CSW-managed workload, assemble:

  (a) Affected workload set
      → Inventory query: hostnames, IPs, OS, CCS labels, site,
        ot_facing flag

  (b) Time-anchored flow record
      → CSW historical conversations: source, destination, port, byte
        counts, timestamps, process attribution

  (c) Process activity record
      → Every process spawned on affected workloads in the window

  (d) Software footprint at time of incident
      → Package list, CVE exposure at that moment (not "today")

  (e) Containment evidence
      → Quarantine policy applied; flow drop count after policy;
        time-to-quarantine

  (f) Configuration baseline diff
      → Before/after package list, listening ports, process set

These six artefacts populate the incident dossier your IRP requires
and the CISA reporting submission you must make within 24 hours
under the SD.
```

**Evidence:** (a) standard incident dossier template; (b) MTTD/MTTR
metrics by CCS function; (c) annual aggregate incident-trend report
for the Senior Cybersecurity Officer.

---

## 9. Cybersecurity Assessment Plan (CAP)

The SD requires owner/operators to develop and maintain a CAP and to
conduct annual assessments. CSW directly supports the IT-side
evidence layer for the CAP.

**CSW Implementation — CAP evidence pack:**
```
Annual CAP self-assessment evidence (per IT-side substantive control):

  Section III.A (segmentation):
    → Workspace export per site; simulation→enforcement log;
      observed-vs-documented IT→OT flow delta

  Section III.B (access control):
    → Policy export with rule provenance; quarterly review minutes;
      sunset log for removed rules

  Section III.C (continuous monitoring):
    → Detection rule catalogue; SIEM forwarding configuration; MTTD
      trend report; sample alert with full forensic context

  Section III.D (vulnerability/patching):
    → CVE inventory dated to assessment period; patch tracking with
      ticket IDs; compensating control register for delayed patches

  Cross-cutting:
    → Inventory snapshot dated to assessment start
    → Configuration baseline diff log for the period
    → Quarterly diff reports demonstrating continuous improvement
```

**Evidence:** (a) annual CAP evidence binder organised by SD
section; (b) prior-period delta showing what changed since last CAP;
(c) Senior Cybersecurity Officer sign-off summary.

---

## 10. Cybersecurity Architecture Design Review

The SD requires periodic architecture design reviews. CSW does not
*perform* the review, but provides telemetry-based inputs.

**CSW inputs to the design review:**

1. Current IT-side workload inventory with CCS labelling.
2. Current ADM-derived dependency graph per CCS function.
3. Observed IT→OT flow inventory for reconciliation against the
   documented architecture.
4. Vendor-egress inventory per OT-Facing-IT workload.
5. Quarterly enforcement diff history showing how the IT-side has
   evolved since the last review.

These inputs let the architecture review focus on *gaps and changes*
rather than rebuilding the as-is picture from scratch.

---

## 11. Mapping Table — TSA SD Requirement → CSW Capability

| Requirement | Requirement summary | CSW capability (IT-side) |
|---|---|---|
| Section II | Critical Cyber System identification | Inventory + scope labelling for CSW-managed workloads supporting CCS (§2) |
| Section II | Cybersecurity Coordinator | Quarterly evidence pack to the Cybersecurity Coordinator |
| Section III.A | Network segmentation (IT/OT) | Per-site IT-side enclave segmentation (§3); deny-by-default to boundary firewall (§3) |
| Section III.A | Documented data flows | IT→OT flow inventory + observed-vs-documented delta (§4) |
| Section III.B | Access control measures | Workload-level least-privilege; quarterly access review (§5) |
| Section III.C | Continuous monitoring & detection | Behavioural rules + flow telemetry to SIEM (§6) |
| Section III.D | Patch / unpatched-system risk | Continuous CVE inventory + compensating-control register (§7) |
| Cybersecurity Incident Response Plan | Detection, response, 24-hour CISA reporting | Six-artefact reconstruction bundle (§8) |
| Cybersecurity Assessment Plan | Annual implementation assessment | Per-section evidence pack with prior-period delta (§9) |
| Cybersecurity Architecture Design Review | Periodic architecture review | Workload inventory, dependency graph, flow inventory as inputs (§10) |

---

## 12. TSA Inspector Response Guide

When TSA inspectors ask for evidence under the SD:

| Inspector asks | You provide |
|---|---|
| "Show your Critical Cyber System inventory and the IT systems that support them" | Per-scope inventory snapshot with `ccs_id`, `ccs_function`, `ot_facing`, `site` labels (§2) |
| "Demonstrate your Section III.A IT/OT segmentation" | Workspace export per site + simulation→enforcement log (§3) |
| "Provide the documented IT-to-OT data flow inventory" | Observed IT→OT flow inventory + reconciliation against architecture (§4) |
| "Show your Section III.B access control implementation" | Policy export + quarterly review minutes + sunset log (§5) |
| "Provide Section III.C continuous monitoring evidence" | Detection rule catalogue + SIEM forwarding + MTTD report (§6) |
| "Show Section III.D patch programme evidence" | CVE inventory dated to period + remediation tracking + compensating-control register (§7) |
| "Provide the incident reconstruction for event X" | Six-artefact incident dossier (§8) |
| "Show your CAP for the most recent annual cycle" | Annual CAP evidence binder organised by SD section (§9) |

---

## 13. Related Frameworks

The TSA Pipeline SD shares substantial control surface with:

- **NIST SP 800-53 Rev 5** — almost all SD substantive requirements
  have direct 800-53 analogues (AC-3, AC-4, SC-7, SI-4, RA-5, CM-2,
  CM-3, CM-7, AU-2, IR-4 cover the bulk of Sections III.A–III.D).
  See [800-53 reference design](../NIST-800-53/CSW-NIST-800-53-Reference-Design.md).
- **NIST SP 800-207 (ZTA)** — the deny-by-default, identity-aware,
  observability-driven posture in §3, §5, and §6 implements the
  seven ZTA tenets in the pipeline IT context. See
  [800-207 reference design](../NIST-800-207/CSW-NIST-800-207-Reference-Design.md).
- **NIST SP 800-82 Rev 3** *(out of repository scope but worth
  pairing externally)* — guide to OT security; CSW addresses the IT
  estate around the OT footprint that 800-82 describes.
- **NERC CIP** — sister sector framework for the bulk electric
  system; identical IT-side patterns apply. See
  [NERC CIP reference design](../NERC-CIP/CSW-NERC-CIP-Reference-Design.md).
- **ISO/IEC 27001:2022** — entities operating under ISO 27001 can
  re-use Annex A.8 evidence. See
  [ISO 27001 reference design](../ISO-27001-2022/CSW-ISO27001-Reference-Design.md).
- **CISA Zero Trust Maturity Model** — the SD's substantive
  requirements align with CISA ZTMM Network and Application/Workload
  pillars on the IT side. See
  [CISA ZTMM reference design](../CISA-ZeroTrust/CSW-CISA-ZTMM-Reference-Design.md).

---

## 14. Disclaimer

This reference design is **draft v1** describing how Cisco Secure Workload
capabilities can support a TSA Pipeline Security Directive
cybersecurity programme on the **IT side** of the IT/OT boundary.
It is **not** legal or regulatory advice and does not constitute a
finding of compliance.

Specifically:

- TSA Security Directives are issued and revised by the
  Transportation Security Administration; the active revision letter
  (02, 02A, 02B, 02C, 02D, ...) and the substantive requirements
  evolve. Always validate against the **current effective revision**
  available from TSA, against your inspector's current guidance,
  and against any subsequent rulemaking that supersedes the SD.
- Designation as a Critical Pipeline owner/operator is a TSA
  determination. Nothing in this reference design substitutes for that
  designation analysis.
- CSW does not enforce policy on RTUs, flow computers, PLCs, IEDs,
  HMIs, or any other OT device, and is not certified as an OT-
  protocol deep-packet-inspection or architecture review tool.

This document should receive subject-matter-expert review for both
TSA SD regulatory accuracy and current Cisco product capability
before being relied upon in a formal compliance engagement.
