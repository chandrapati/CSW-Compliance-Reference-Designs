# Cisco Secure Workload — GxP Compliance Framework
## Reference Design | Life Sciences Accounts (Pharma · Biotech · Medical Devices · CDMO/CRO)

**Version:** 1.0
**Audience:** Solutions Architects, Security Engineers
**Use Case:** Fresh Install, Hybrid Environment (On-Prem + Cloud + Manufacturing OT)
**Regulatory basis:** EU GMP Annex 11 · FDA 21 CFR Part 11 · GAMP 5 (2nd Ed.) · FDA Computer Software Assurance (2022 draft guidance)

---

## 1. Overview

This reference design guides deployment of Cisco Secure Workload (CSW) in regulated life-sciences environments to produce **inspection-ready evidence** for GxP computerised-system controls.

GxP is **not a certification**. There is no GxP certificate, no attestation report, and no audit opinion. Customers are inspected by regulators (FDA, EMA, MHRA) and must demonstrate a **validated state** on demand. CSW's role is to make a subset of those controls *enforced and evidenced* rather than asserted in a document.

### What GxP means here

| Regulation | Scope | Why CSW matters |
|---|---|---|
| **EU GMP Annex 11** | Computerised systems used in GMP activities | Clauses 9 (audit trails), 10 (change control), 12 (security), 16 (business continuity) |
| **21 CFR Part 11** | Electronic records and signatures (US) | §11.10(d) access limitation, §11.10(e) audit trails, §11.10(k) documentation controls |
| **GAMP 5 (2nd Ed.)** | Risk-based validation methodology | Infrastructure qualification; supplier assessment |
| **ALCOA+** | Data-integrity principles | CSW evidences *control* integrity, not record integrity — see §1.2 |

### 1.1 Where CSW genuinely contributes

| GxP need | CSW capability |
|---|---|
| **Segregation of validated from non-validated systems** | Scopes, labels, enforced segmentation policy with flow evidence |
| **Logical access restriction to authorised systems** | Workload-identity policy (not IP-based ACLs) |
| **Change control on the validated environment** | Policy versioning, simulate-before-enforce, drift detection |
| **Audit trail of the security control** | Immutable flow records, policy change history |
| **Compensating controls for un-patchable validated systems** | Native CVE inventory + targeted segmentation. **This is the strongest single use case — see §8** |
| **Incident reconstruction** | Full flow and process forensic telemetry |

### 1.2 Scope boundary — state this before the customer asks

CSW does **not**:

- Perform Computer System Validation. It cannot validate an application, and it is not a CSV/CSA tool.
- Produce **ALCOA+ evidence at the record level**. CSW never touches the GxP record itself — the batch record, LIMS result, chromatography data file or clinical dataset. Its audit trail is of the *security control*, not the *regulated record*. A quality auditor will make this distinction immediately.
- Provide **electronic signature** capability. All of Part 11 Subpart C (§11.50, §11.70, §11.100–§11.300) is out of scope.
- Qualify infrastructure on the customer's behalf (IQ/OQ/PQ remains theirs).

> **Expect the reverse question.** If CSW is deployed into a GxP environment, the customer's quality organisation may require **CSW itself to be qualified** as a supporting system. Be ready for a supplier assessment, a request for qualification documentation, and for CSW upgrades to fall under their change control. Raise this proactively — being first to say it builds more credibility than any feature.

---

## 2. Pre-Deployment Checklist

- [ ] CSW cluster (SaaS or on-prem) provisioned and accessible
- [ ] Network connectivity from workloads to CSW cluster (port 443 outbound)
- [ ] Linux/Windows agent compatibility verified — **including legacy OS on validated systems** (see §11)
- [ ] Cloud provider accounts connected (AWS, Azure, GCP) via CSW cloud connectors
- [ ] **Validated System Inventory (VSI) obtained** from the quality organisation — this is the authoritative GxP scope list, not an IT asset list
- [ ] Stakeholders identified: **QA / Quality Systems**, Validation Lead, CSIRT/Security, Manufacturing IT/OT, CISO
- [ ] **Change control record raised** for agent installation on validated systems — agent install on a validated system is itself a change
- [ ] Agreement on whether CSW is in scope for qualification (see §1.2)
- [ ] GxP vs non-GxP boundary agreed in writing with QA

> **Do not skip the change-control item.** Installing software on a validated system without a change record is a finding in its own right, regardless of what the software does.

---

## 3. Phase 1 — Sensor Deployment (Days 1–10)

Longer than the HIPAA equivalent by design: validated systems move through change control, not change windows.

### 3.1 On-Premises Workloads

```bash
# Linux (RHEL/CentOS/Ubuntu)
rpm -ivh tet-sensor-<version>.rpm    # RHEL/CentOS
dpkg -i tet-sensor-<version>.deb     # Ubuntu/Debian

# Verify sensor is running
systemctl status tetd
```

**Key Sensor Configuration:**
- Enforcement Mode: **Monitoring Only** — never enforce on a validated system before simulation review and QA sign-off
- Data Collection: enable process hash, network flow, vulnerability scan
- Tags from Day 1: `env:production`, `compliance:gxp`, `gxp:validated`, `system:<VSI-ID>`

> **Tag with the Validated System Inventory ID.** The `system:<VSI-ID>` label is what lets you produce evidence the quality organisation can reconcile against their own register. Without it, your reports and their register are two unrelated documents.

### 3.2 Manufacturing / OT Workloads

GMP manufacturing sits in the Purdue model, and the segmentation story maps cleanly onto ISA/IEC 62443:

| Purdue Level | Typical systems | CSW approach |
|---|---|---|
| **Level 4** | ERP (SAP), enterprise IT | Standard agent |
| **Level 3.5** | DMZ | Policy boundary — the critical enforcement point |
| **Level 3** | MES, historians (OSIsoft PI, Aspen IP.21), site servers | Agent where supported |
| **Level 2** | SCADA / HMI (DeltaV, PCS 7, Experion) | Agent only if vendor-supported; otherwise agentless |
| **Levels 0–1** | PLCs, sensors, instruments | **No agent.** Visibility via connectors and flow telemetry only |

For Levels 0–2, use agentless discovery and treat CSW as the enforcement boundary *around* the cell rather than inside it.

### 3.3 Cloud Workloads (AWS / Azure / GCP)

**Option A — Software Sensor on Cloud VMs:** as above.

**Option B — CSW Cloud Connectors (agentless):**
```
CSW UI → Platform → External Orchestrators
  → Add AWS/Azure/GCP connector
  → Provide IAM Role (AWS) or Service Principal (Azure)
  → Enable VPC Flow Log ingestion
```

### 3.4 Sensor Validation

```
CSW UI → Manage → Agents
  → Confirm all sensors show "Active"
  → Verify telemetry flowing
  → Check agent version alignment
```

**GxP addition:** export the agent inventory and reconcile against the VSI. Any validated system *without* an agent is a documented gap requiring either an agent or a compensating control — not silence.

---

## 4. Phase 2 — Scope & Inventory Design (Days 11–18)

### 4.1 GxP Scope Architecture

Design scopes around **validation status first, application second.** This is the inverse of most deployments, and it is what makes the Annex 11 §12 story work.

```
Root Scope
└── LifeSciences-Org
    ├── GxP-Validated (strict change control)
    │   ├── Manufacturing-MES
    │   ├── LIMS-Laboratory
    │   ├── CDS-Chromatography        (Empower, Chromeleon, OpenLab)
    │   ├── QMS-EDMS                  (Veeva Vault, TrackWise, MasterControl)
    │   ├── Historian-EMS-BMS         (environmental / cleanroom monitoring)
    │   └── Clinical-Systems          (CTMS, EDC, eTMF, Pharmacovigilance)
    ├── GxP-Supporting (qualified infrastructure)
    │   ├── Validated-Databases
    │   ├── Backup-Archive
    │   └── Time-Sync-NTP             (Annex 11 §9 — audit trail timestamps)
    ├── Non-GxP-Corporate (standard controls)
    │   ├── Active-Directory
    │   ├── Email-Collaboration
    │   └── General-IT
    └── External-Partners
        ├── CRO-CDMO-Access
        └── Vendor-Remote-Support     (instrument OEM support paths)
```

> **The `Non-GxP-Corporate` → `GxP-Validated` boundary is the single most valuable policy in this entire reference design.** It is the control that Annex 11 and GAMP both expect and that most customers can only assert on paper.

### 4.2 Inventory Filters for GxP System Discovery

```
Filter: GxP-Candidates-Laboratory
  - Process contains: "empower", "chromeleon", "openlab", "labware",
                      "starlims", "samplemanager", "unicorn"
  - Port listened: 1521 (Oracle), 1433 (MSSQL)
  - Hostname contains: "lims", "cds", "qc", "lab"

Filter: GxP-Candidates-Manufacturing
  - Process contains: "opcenter", "pharmasuite", "deltav", "pcs7", "pi-server"
  - Port listened: 4840 (OPC UA), 5450 (OSIsoft PI), 502 (Modbus),
                   44818 (EtherNet/IP), 135 (OPC DA / DCOM)
  - Hostname contains: "mes", "scada", "hmi", "historian"

Filter: GxP-Candidates-Quality
  - Process contains: "veeva", "trackwise", "mastercontrol", "documentum"
  - Hostname contains: "qms", "edms", "dms"

Filter: Legacy-Unpatchable
  - OS version: Windows Server 2008/2012, RHEL 6
  - AND scope: GxP-Validated
  → Feeds the compensating-control workflow in §8
```

### 4.3 Labelling Strategy

| Label Key | Example Values | Purpose |
|---|---|---|
| `gxp` | validated, supporting, none | **Primary segregation axis** |
| `system` | VSI-0142, VSI-0291 | Reconciles to the quality register |
| `gxp_category` | gmp, glp, gcp, gdp, gvp | Which GxP discipline applies |
| `gamp` | cat3, cat4, cat5 | GAMP 5 software category — drives validation rigour |
| `validation_state` | validated, revalidation-due, retired | Lifecycle tracking |
| `patch_constraint` | revalidation-required, vendor-locked, none | **Drives §8 compensating controls** |
| `env` | production, qual, dev | Environment segregation |
| `owner` | qa-ops, mfg-it, lab-ops | Accountability |

---

## 5. Phase 3 — Application Dependency Mapping (Days 19–40)

### 5.1 ADM Configuration

```
CSW UI → Investigate → Application Dependency Mapping
  → New Workspace
  → Name: "GxP-Validated-ADM"
  → Select Scope: GxP-Validated
  → Time Window: 4–6 weeks
  → Start ADM
```

> **Run longer than you would elsewhere — 4 to 6 weeks minimum.** GxP environments have cycles that shorter windows miss entirely: monthly batch release, quarterly stability testing, periodic review, annual product quality review, instrument calibration schedules. A two-week ADM in a pharma plant will generate policy that breaks at month-end.

**Collection settings:**
- Enable **process context**
- Enable **user context** where OS sensors support it
- Retention: align to the customer's GxP record retention, which is commonly **years, not months** — confirm with QA before assuming

### 5.2 ADM Analysis for GxP

| Question | GxP relevance |
|---|---|
| Which non-GxP systems connect into GxP-Validated? | **Annex 11 §12.1** — the core segregation finding |
| Do validated systems reach the internet directly? | Annex 11 §12 · uncontrolled change vector |
| Which vendor/OEM remote-support paths are live? | Annex 11 §3 — supplier access control |
| Are GxP database connections encrypted? | Annex 11 §7.1 — data storage security |
| Do all validated systems reach a common NTP source? | **Annex 11 §9** — audit-trail timestamps require reliable time |
| Unexpected lateral flows inside GxP-Validated? | Annex 11 §12.2 · §13 incident management |
| Which systems write to the archive/backup tier? | Annex 11 §7.2 · §17 archiving |

> The **NTP question is a genuine differentiator.** Annex 11 §9 audit trails and Part 11 §11.10(e) time-stamped records both depend on trustworthy time, and almost nobody can evidence that every validated system actually reaches an approved time source. CSW can show it in a flow query.

### 5.3 GxP System Identification Workflow

1. **Start from the VSI**, not from ADM output — the quality register is authoritative
2. **Export ADM clusters** and reconcile against the VSI
3. **Flag discrepancies in both directions** — VSI entries with no observed traffic (retired but not decommissioned?) and active clusters absent from the VSI (shadow GxP system?)
4. **Escalate unregistered candidates to QA.** An unregistered system handling GxP data is a finding you have just discovered for them
5. **Tag confirmed systems** with `gxp` and `system:<VSI-ID>`
6. **Re-run ADM** scoped to GxP-Validated for policy generation

> Step 3 is often the first tangible value the customer sees, and it arrives before any policy is written.

---

## 6. Phase 4 — Policy Development (Days 41–60)

### 6.1 GxP-Aligned Policy Framework

**Absolute Policies (always enforced):**
```
DENY:  Non-GxP-Corporate → GxP-Validated   (except approved jump hosts)
DENY:  GxP-Validated → Internet            (no direct egress from validated systems)
DENY:  External-Partners → GxP-Validated   (except brokered vendor-support paths)
DENY:  GxP-Validated → GxP-Validated       cross-system, unless ADM-confirmed
```

**Allowlist Policies (least privilege):**
```
ALLOW: LIMS-Laboratory ↔ Validated-Databases      (1521, 1433)
ALLOW: CDS-Chromatography → LIMS-Laboratory       (443)
ALLOW: Manufacturing-MES ↔ Historian              (5450 PI, 4840 OPC UA)
ALLOW: Manufacturing-MES → ERP                    (3200-3299 SAP)
ALLOW: GxP-Validated → Time-Sync-NTP              (123)   # Annex 11 §9
ALLOW: GxP-Validated → Backup-Archive             (per backup vendor)  # §7.2 · §17
ALLOW: Jump-Host → GxP-Validated                  (22, 3389)
ALLOW: Vendor-Remote-Support → <named system>     (time-bounded, brokered only)
```

**Catch-All (audit everything else):**
```
LOG: Any → GxP-Validated     (unmatched inbound — alert)
LOG: GxP-Validated → Any     (unmatched outbound — alert)
```

### 6.2 Policy Workspace Setup

```
CSW UI → Defend → Segmentation
  → New Workspace
  → Name: "GxP-Validated-Enforcement"
  → Scope: GxP-Validated
  → Import ADM policies (auto-generated baseline)
  → Review and refine with QA + system owners
  → Set mode: Simulation first → then Enforcement
```

### 6.3 Enforcement Progression

| Phase | Mode | Duration | Purpose | QA gate |
|---|---|---|---|---|
| 1 | Simulation | **4 weeks** | Validate no false positives across a full business cycle | Simulation report reviewed |
| 2 | Enforce — non-GxP boundary only | 2 weeks | Enforce the Corporate → Validated deny first | Change record approved |
| 3 | Enforce — intra-GxP allowlist | 2–4 weeks | Staged per system | Change record per system |
| 4 | Full enforcement | Ongoing | Steady-state posture | Periodic review per Annex 11 §11 |

> **Each enforcement step is a change to a validated environment and needs its own change-control record.** Build the QA gate into the project plan from the start; discovering it at phase 2 costs weeks. Simulation output is the evidence package that gets the change approved — which makes simulate-before-enforce a *regulatory* feature here, not just a safety feature.

---

## 7. Phase 5 — GxP Control Mapping

### 7.1 EU GMP Annex 11

| Annex 11 Clause | Requirement | CSW Implementation | Coverage |
|---|---|---|---|
| **§3** Suppliers & Service Providers | Assess and control supplier access | Brokered, time-bounded vendor-support policy; flow evidence of every OEM session | Partial |
| **§4** Validation | System validated for intended use | *Customer-owned.* CSW supplies qualification docs for its own assessment | Supporting |
| **§7.1** Data Storage | Data secured against damage/unauthorised access | Segmentation of data tier; detection of unencrypted paths | Partial |
| **§7.2** Backups | Regular backup, integrity checked | Policy permitting and evidencing backup paths | Partial |
| **§9** Audit Trails | Secure, time-stamped record of GMP-relevant changes | Immutable flow records; policy change history. **Evidence of NTP reachability for all validated systems** | Partial — control layer only |
| **§10** Change & Configuration Mgmt | Changes made in a controlled manner | Policy versioning, simulate-before-enforce, **out-of-sync drift detection** | **Strong** |
| **§11** Periodic Evaluation | Systems periodically evaluated as still valid | Scheduled ADM re-runs; policy drift reports; quarterly posture export | **Strong** |
| **§12.1** Security | Physical/logical controls restrict access to authorised persons | **Enforced workload-identity segmentation** — the core control | **Strong** |
| **§12.2** Security | Extent of controls depends on criticality | Scope-tiered policy: Validated / Supporting / Non-GxP | **Strong** |
| **§12.3** Security | Record creation/change/cancellation of access authorisations | Policy change history with approver and timestamp | Partial |
| **§13** Incident Management | Incidents assessed, root cause identified | Forensic flow and process telemetry for reconstruction | **Strong** |
| **§14** Electronic Signature | — | **Out of scope** | None |
| **§16** Business Continuity | Continuity of system in event of breakdown | Agents continue enforcing cached policy if the control plane is unreachable | Partial |
| **§17** Archiving | Data archived, readable, integrity-checked | Policy permitting and evidencing archive paths | Partial |

### 7.2 FDA 21 CFR Part 11 — Subpart B (§11.10 Closed Systems)

| Control | Requirement | CSW Implementation | Coverage |
|---|---|---|---|
| **§11.10(a)** | Validation of systems | *Customer-owned.* CSW is a supporting system | Supporting |
| **§11.10(c)** | Protection of records through retention period | Segmentation of record and archive tiers | Partial |
| **§11.10(d)** | **Limiting system access to authorised individuals** | **Enforced network-layer access restriction by workload identity** | **Strong** |
| **§11.10(e)** | Secure, computer-generated, time-stamped audit trails | Flow and policy audit trail *of the control*; NTP path evidence | Partial — control layer only |
| **§11.10(g)** | Authority checks | Policy enforcement that only authorised systems may interact | Partial |
| **§11.10(h)** | Device checks — validity of data source/input device | Workload identity (OS fingerprint, process hash) rather than spoofable IP | Partial |
| **§11.10(k)** | Documentation controls / change-record audit trail | Policy versioning and change history | Partial |
| **§11.30** | Open systems — additional controls | Detection of unencrypted flows; egress restriction | Partial |
| **Subpart C** | Electronic signatures (§11.50–§11.300) | **Out of scope** | None |

> **Use the Coverage column honestly in customer materials.** "Strong" on four or five controls that the customer currently cannot evidence at all is a better position than claiming broad coverage that a quality auditor will dismantle in ten minutes.

---

## 8. Phase 6 — Vulnerability Management and the Un-Patchable System

**This is the highest-value section of the reference design for a life-sciences buyer.**

### 8.1 Why this is different from every other vertical

In a GxP environment, patching a validated system is not a maintenance task — it is a **change requiring impact assessment and, frequently, re-validation**. The practical result is that known vulnerabilities sit unremediated on critical systems for months or years, often on operating systems well past end of support, because the instrument vendor only qualifies a specific OS build.

The quality organisation knows this. It is a standing risk item they cannot close. **A documented, enforced compensating control is the answer they have been unable to produce.**

### 8.2 Vulnerability Detection

```
CSW UI → Investigate → Vulnerability Report
  → Scope: GxP-Validated
  → Filter: CVSS ≥ 7.0
  → Cross-filter: patch_constraint = revalidation-required | vendor-locked
  → Export for the quality record
```

### 8.3 Risk-Based Prioritisation

Prioritise by **exposure**, not CVSS alone. A critical CVE on a system reachable only from one jump host is a lower real risk than a high CVE on a system reachable from the corporate network.

```
Priority 1: Critical CVE + reachable from Non-GxP or External  → immediate segmentation
Priority 2: Critical CVE + GxP-internal reachability only      → segment, schedule patch
Priority 3: High CVE + patchable without revalidation          → normal change control
Priority 4: High CVE + vendor-locked                           → documented compensating control
```

### 8.4 The Compensating-Control Workflow

For each vulnerability that cannot be patched within the risk-based timeline:

1. **Document the constraint** — revalidation required, vendor-locked OS, instrument qualification
2. **Reduce reachability** — restrict the vulnerable port to named source workloads only
3. **Enforce it**, don't just alert
4. **Add a forensic rule** on the affected process
5. **Export the evidence**: the CVE, the constraint, the enforced policy, and the flow records proving the restriction holds
6. **File into the quality system** as the compensating control for that risk item

> The deliverable is a sentence the customer could not previously write: *"CVE-XXXX-YYYY remains unpatched on VSI-0142 pending revalidation. Reachability is restricted by enforced policy to two named hosts, continuously monitored, with flow evidence retained."* That closes an open risk item, which is worth more to a QA director than any dashboard.

---

## 9. Phase 7 — Monitoring & Alerting

### 9.1 GxP-Required Alerts

| Alert | Trigger | Control |
|---|---|---|
| Non-GxP → Validated access | Any unapproved corporate source → GxP-Validated | Annex 11 §12.1 · Part 11 §11.10(d) |
| Validated system egress to internet | GxP-Validated → external | Annex 11 §12 |
| Unbrokered vendor access | External-Partners → GxP-Validated outside an approved window | Annex 11 §3 |
| **NTP path failure** | Validated system stops reaching approved time source | **Annex 11 §9 · Part 11 §11.10(e)** |
| Policy drift / out of sync | Enforced policy no longer matches intended state | **Annex 11 §10** |
| New lateral flow inside GxP | Previously unobserved east-west flow | Annex 11 §12.2 · §13 |
| Unencrypted GxP data flow | Cleartext protocol from validated system | Annex 11 §7.1 |
| New critical CVE on validated system | CVE appears on `gxp:validated` workload | Annex 11 §1 risk management |
| Agent offline on validated system | Sensor stops reporting | Annex 11 §9 — evidence gap |
| Archive/backup path failure | Expected backup flow absent | Annex 11 §7.2 · §17 |

> **"Agent offline" is a GxP alert, not just an ops alert.** A gap in the evidence record is itself a compliance problem — you cannot demonstrate a control was operating during a period you have no data for.

### 9.2 Forensic Telemetry for Incident Management (Annex 11 §13)

```
CSW UI → Investigate → Flow Search
  → Time range: incident window
  → Source/Destination: affected validated system
  → Export: full flow log with process context

CSW UI → Investigate → Process Search
  → Filter: GxP workload + time range
  → Identify anomalous processes + parent-child relationships
```

Retain forensic exports to the customer's **GxP record retention period** — confirm with QA. This is commonly far longer than security-industry norms, and in some cases extends to the product lifetime plus a statutory margin.

---

## 10. Reporting & Evidence Collection

### 10.1 Evidence per Review Cycle

| Evidence Item | CSW Source | Annex 11 / Part 11 |
|---|---|---|
| **GxP segregation proof** — no unapproved Non-GxP → Validated flows | Flow Search + policy analysis | §12.1 · §11.10(d) |
| Enforced policy export with version and approver | Defend → Policy Analysis | §10 · §11.10(k) |
| Policy drift report vs approved baseline | Policy comparison | §10 · §11 |
| Vulnerability report on validated systems | Investigate → Vulnerability | §1 risk management |
| **Compensating-control register** | §8.4 workflow output | §1 · §12.2 |
| Scope membership snapshot reconciled to VSI | Inventory → Export | §4 · §11 |
| NTP reachability evidence for all validated systems | Flow Search (port 123) | §9 · §11.10(e) |
| Vendor/OEM access log | Flow Search (External-Partners) | §3 |
| Agent coverage report vs VSI | Manage → Agents export | §9 |
| Incident reconstruction package | Flow + Process Search | §13 |

### 10.2 Ongoing Compliance Posture

- **Monthly** — scope/inventory reconciliation against the VSI; agent coverage check
- **Quarterly** — policy workspace review; drift report; compensating-control register refresh
- **Per periodic review cycle (Annex 11 §11)** — full evidence pack, aligned to the customer's own periodic-evaluation schedule rather than a security calendar
- **Every 90 days** — ADM re-run to detect new dependencies
- **On every validated-system change** — confirm policy still reflects intended state

> Align the reporting calendar to **their periodic review schedule**, not to a generic quarterly security cadence. Evidence that arrives in the right format at the right point in the quality cycle gets used; evidence that arrives on a security team's timetable gets filed.

---

## 11. Common Pitfalls

| Pitfall | Mitigation |
|---|---|
| **Agent installed without a change record** | Raise change control *before* deployment on any validated system. This is the most common own-goal |
| **Claiming "CSW makes you GxP compliant"** | There is no such thing. Position as evidence for specific clauses; name the gaps first |
| **Conflating control audit trail with record audit trail** | Be explicit that CSW evidences the security control, never the GxP record itself |
| Legacy OS on validated systems won't take an agent | Plan agentless coverage and boundary enforcement; document as a known gap with compensating control |
| ADM window too short | Minimum 4–6 weeks. Must span month-end batch release and periodic testing cycles |
| Enforcement breaks a manufacturing or lab system | Simulation first, always. Stage by scope. Never enforce into a running batch |
| Scoping from the IT asset list | The **Validated System Inventory from QA** is authoritative. IT asset lists miss instruments and include retired systems |
| Treating OT like IT | Levels 0–2 often cannot take agents. Enforce at the boundary, observe inside |
| Retention set to security norms | GxP retention is often years. Confirm with QA before configuring |
| Ignoring whether CSW itself needs qualification | Ask early; supply the supplier assessment pack proactively |

---

## 12. Product-Accuracy Guardrails

Before any of this goes into customer-facing material:

- **Live Protect is GA for Nexus switches. Live Protect for applications is not GA** — it arrives in CSW 4.1 via the CSW unified agent with Tetragon. Do not present application-level CVE shielding as available today. The §8 compensating-control story stands on **segmentation plus native CVE**, both GA in CSW 4.0, and does not need Live Protect to work.
- **Cisco SmartSwitch (N9300) is a separate Cisco product**, not a CSW feature. It requires its own on-prem VM-based controller, and the service shipping on it today is Hypershield. Do not imply a shared policy plane with CSW.
- **CSW 4.0 GA** covers ADM/AI policy, native CVE, simulation, agents and connectors, Secure Firewall CVE→IPS, and the NVIDIA BlueField DPU agent.

---

*Document prepared for Cisco life-sciences account engagements. Replace [Customer Name] and bracketed fields before customer delivery. GxP is a regulatory regime, not a certification — nothing in this reference design should be presented as conferring compliance.*
