# Cisco Secure Workload — NIST SP 800-171 Rev. 3
## Reference Design | CUI in Nonfederal Systems

**Version:** 1.0  
**Standard:** NIST SP 800-171 Rev. 3 (May 2024), *Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations*  
**Use Case:** Fresh install, hybrid environment (on-premises + cloud), CUI processing enclaves

---

## Reader's Guide

**Who this is for.** Nonfederal organizations that process, store, or transmit CUI under federal contracts or agreements; security architects building CUI enclaves; and assessors collecting technical evidence for 800-171A assessment procedures.

**Questions this reference design helps you answer:**

- *For requirement 03.13.06 (deny by default, allow by exception), can I show continuous enforcement at the workload tier—not only perimeter firewalls—with a documented allow-list derived from observed traffic?*
- *For 03.01.03 (information flow enforcement for CUI), can I prove authorized flows between CUI and non-CUI segments and detect or block unauthorized cross-boundary paths?*
- *For 03.03.x (audit and accountability), can I export flow and process-level telemetry that traces CUI-adjacent workloads to specific processes and time windows for SIEM retention?*
- *For 03.04.x (configuration management), can I baseline communications and software exposure, then demonstrate drift when new services, ports, or binaries appear on CUI systems?*
- *For 03.11.x (risk assessment) and vulnerability prioritization, can I combine CVE exposure with east-west reachability and EPSS-style context to support POA&M and risk narratives?*

**What you'll need.** A current CUI boundary definition (which components process, store, or transmit CUI), a system security plan (SSP) or equivalent scope description, labeling standards for workloads, and assessor or PMO expectations for evidence format (reports, exports, screenshots).

**Where to start.** Sections 1–2 for scope alignment; 3–6 for deployment and baseline; 7–9 for policy design tied to 03.01.03, 03.01.05, and 03.13.x; section 13 if you are packaging evidence for an assessment window.

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

- CUI enclave isolation with 03.01/03.13 flow enforcement
- CMMC L2 underpinning evidence
- 800-53 Rev 3 family alignment for assessors

**Compared to manual programmes:** static diagrams and annual firewall samples age immediately; CSW ties evidence to **live workload behaviour** and produces queryable exports on demand — supporting "operating effectively" language in PCI v4.0, SOC 2 CC7, and HIPAA risk analysis.

---

## 1. Overview

NIST SP 800-171 Rev. 3 modernizes the CUI protection requirements, aligns requirement numbering and structure with **NIST SP 800-53 Rev. 5**, and preserves the core outcome: confidentiality of CUI in nonfederal systems. Cisco Secure Workload (CSW) contributes **technical and operational evidence** for requirements where workload visibility, micro-segmentation, vulnerability context, and forensic telemetry are relevant. It does not replace administrative, physical, or personnel controls, identity providers, or cryptographic implementations.

### 1.1 Alignment with NIST SP 800-53 Rev. 5 and CMMC

Rev. 3 requirements include source-control references to 800-53 (for example, 03.13.06 maps from SC-7(5)). For a detailed control-family treatment mapped to CSW at the 800-53 control level, see the companion reference design below. **CMMC 2.0** uses NIST SP 800-171 as its technical basis for Level 2; contractors should **confirm which revision (Rev. 2 vs. Rev. 3)** their contracts, PMO, or assessment framework specify during any transition period. This reference design is written to **Rev. 3** identifiers (e.g., 03.01.03).

### 1.2 Rev. 3 Family Structure and CSW Relevance

| Family (Rev. 3) | Title | CSW relevance |
|---|---|---|
| 03.01 | Access Control | **Direct** — identity-aware and scope-based micro-segmentation; deny-by-default enforcement paths |
| 03.02 | Awareness and Training | Out of scope — HR/training systems |
| 03.03 | Audit and Accountability | **Direct** — flow + process telemetry; export to SIEM |
| 03.04 | Configuration Management | **Direct** — software inventory, ADM baselines, drift versus approved communication profiles |
| 03.05 | Identification and Authentication | Supporting — enforcement of authenticated paths (e.g., Kerberos/LDAPS-only); IdP configuration remains outside CSW |
| 03.06 | Incident Response | **Supporting (evidence)** — forensics, timelines, scope of compromise views |
| 03.07 | Maintenance | Supporting — monitoring of maintenance-related connectivity if expressed in policy baselines |
| 03.08 | Media Protection | Limited — no physical media control; logical exfiltration paths may be constrained by policy |
| 03.09 | Personnel Security | Out of scope |
| 03.10 | Physical Protection | Out of scope |
| 03.11 | Risk Assessment | **Direct** — CVE visibility, reachability from threat-facing workloads, prioritization inputs |
| 03.12 | Security Assessment and Monitoring | Supporting — continuous monitoring artifacts; CSW does not replace formal control testing |
| 03.13 | System and Communications Protection | **Direct** — CUI enclave isolation, boundary enforcement, plaintext/unauthorized protocol detection |
| 03.14 | System and Information Integrity | **Direct** — process monitoring, anomaly signals, forensic integrity of telemetry |
| 03.15 | Planning | Supporting — inventory and scope evidence feed SSP accuracy |
| 03.16 | System and Services Acquisition | Limited — monitor connectivity to external services; contract terms remain organizational |
| 03.17 | Supply Chain Risk Management | Limited — workload component visibility; full SCRM is organizational |

---

## 2. Pre-Deployment Checklist

Before deploying CSW sensors into CUI or CUI-adjacent enclaves, confirm the following:

- [ ] CSW cluster (SaaS or customer-managed) is provisioned; data residency and IRP for telemetry meet organizational and contractual rules for CUI.
- [ ] Outbound connectivity from workloads to the CSW cluster (typically TCP 443) is allowed and documented in the SSP connection table.
- [ ] Linux and Windows sensor versions are approved for all target OS builds in the CUI baseline.
- [ ] Cloud connectors (AWS, Azure, GCP) are authorized if agentless visibility is used; IAM roles / service principals are least-privilege and documented.
- [ ] Stakeholders engaged: ISSO, system owner, network operations, contracting/CUI program office.
- [ ] Change windows approved; **initial mode is monitoring**, not enforcement, until ADM and policy simulation complete.

---

## 3. Phase 1 — Sensor Deployment (Days 1–5)

### 3.1 On-Premises Workloads

**Install software sensors:**

```bash
# Linux (RHEL / CentOS stream / Ubuntu variants — use package matching your distro)
sudo rpm -ivh tet-sensor-<version>.rpm    # RHEL family
# or
sudo dpkg -i tet-sensor-<version>.deb     # Debian family

# Verify agent service (name may vary slightly by release; consult release notes)
sudo systemctl status tet-engine || sudo systemctl status csw-agent
```

**Configuration guardrails for CUI:**

- Enforcement mode: **Monitoring only** until policy sign-off.
- Enable process hash, connection telemetry, and vulnerability exposure features supported on your agents.
- Apply labels at install time: `cui_scope`, `enclave`, `environment`, `owner`.

### 3.2 Cloud Workloads

**Option A — Agent on every CUI-bearing instance:** same as on-prem.

**Option B — Cloud connector (complementary):**

```
CSW UI → Platform → External Orchestrators
  → Add AWS / Azure / GCP connector
  → Attach read-only discovery role (EC2/VM inventory, optional flow log paths per vendor)
  → Map cloud tags → CSW labels (e.g., tag CuiEnclave=ALPHA → scope CUI-ALPHA)
```

### 3.3 Validation

```
CSW UI → Manage → Agents
  → Status: Active for every in-scope workload
  → Version alignment with approved standard image
  → Confirm flows visible within 15–30 minutes of agent start
```

---

## 4. Phase 2 — Scope Design and CUI Inventory (Days 6–12)

### 4.1 Recommended Scope Hierarchy

Model **CUI enclaves** explicitly; never rely on a single flat “production” scope for assessment evidence.

```
Root
└── Organization
    ├── CUI-Enclaves
    │   ├── CUI-Tier1-Apps
    │   ├── CUI-Datastores
    │   └── CUI-Integration-Brokers
    ├── Security-Protection-Assets
    │   ├── Identity (read-only policy exceptions)
    │   ├── Patch-Repo / Artifactories (as approved)
    │   ├── SOC-SIEM-Collectors
    │   └── Backup / DR targets
    └── Non-CUI (or “Corporate”)
        ├── Dev/Test (must not share policy workspace with CUI if contract requires segregation)
        └── General IT
```

### 4.2 Label Schema (Minimum)

| Label key | Example values | Purpose |
|---|---|---|
| `cui_scope` | `in_scope`, `spa`, `out_of_scope` | Aligns workload to SSP boundary |
| `cui_role` | `processes`, `stores`, `transmits` | Maps to CUI handling roles |
| `enclave_id` | `ENCLAVE-A` | Groups policies and ADM workspaces |
| `data_class` | `cui`, `internal`, `public` | Drives segmentation rules |
| `owner_team` | `prog-office-xyz` | Accountability in exports |

### 4.3 Discovery Filters (Examples)

```
Filter: CUI-Candidate-DBs
  - Process: postgres, oracle, mysqld, sqlservr, mongod
  - Ports: 5432, 1521, 1433, 3306, 27017

Filter: CUI-Candidate-App-Tiers
  - Tag from cloud: DataClassification=CUI
  - Hostname pattern: *cui*, *gov*, *fed*

Filter: Common-Exfil-Protocols (review only — policy may block after baseline)
  - Outbound destination not in approved list AND process in (curl, wget, ftp, scp)
```

---

## 5. Phase 3 — Visibility and Baseline (Days 10–25)

### 5.1 Application Dependency Mapping (ADM)

ADM establishes the **authorized communication baseline** needed for 03.01.03, 03.04.x comparison, and 03.13.06 allow-lists.

```
CSW UI → Investigate → Application Dependency Mapping
  → New Workspace
  → Name: CUI-ADM-<Enclave>-<YYYYQQ>
  → Scope: CUI-Enclaves (or single enclave for stricter separation)
  → Duration: ≥ 14 days (include month-end / payroll / batch cycles if applicable)
  → Enable rich process context and user context where supported
```

**During review, document:**

| Question | Relevance |
|---|---|
| Which workloads initiate sessions **from** non-CUI into CUI? | 03.01.03, 03.13.01 |
| Which CUI workloads initiate **to** non-CUI (break-glass, SaaS, email)? | 03.01.03, 03.01.20 |
| Where is traffic cleartext (HTTP, LDAP, FTP) versus encrypted? | 03.13.x, 03.13.08 (as applicable) |
| What is the blast radius if a given internet-facing tier is compromised? | 03.11.x |

### 5.2 Software Inventory and Drift

```
CSW UI → Investigate → Inventory / Vulnerability (per product navigation)
  → Scope: CUI-Enclaves
  → Export: workload, package/CVE summary, listening ports, last seen
```

Re-run ADM **at least quarterly** or after major releases; treat newly observed flows as **configuration changes** under 03.04.x.

---

## 6. Phase 4 — Policy Design (Days 22–40)

### 6.1 Policy Workspace Pattern

```
CSW UI → Defend → Segmentation
  → New Workspace: CUI-<Enclave>-Enforcement
  → Scope: matching CUI scope from section 4
  → Import ADM-suggested rules → translate to explicit allow/deny with change tickets
  → Mode: Simulation → Enforcement (staged)
```

### 6.2 Illustrative Policy Stanzas (Conceptual)

Translate organizational policy into CSW rules. Examples below are **patterns**; port lists and peers must come from your ADM and SSP.

**03.13.06 — Deny by default, allow by exception (east-west at workload tier):**

```
# Implicit default: DENY unmatched intra-scope traffic after cutover
# Explicit allows (examples):
ALLOW: CUI-App-Tier → CUI-DB-Tier  [TCP 443, 5432 from approved SG/workload set only]
ALLOW: CUI-App-Tier → Identity  [TCP 636, 88, 464 — Kerberos/LDAPS paths per your design]
ALLOW: SOC-Collector → All-CUI  [TCP 443 agent telemetry — if architected this way]
DENY:  Non-CUI → CUI  [except documented jump hosts / service accounts]
DENY:  CUI → Internet  [except explicit proxy or vetted SaaS egress IPs]
LOG:   Any → CUI unmatched traffic (alert + SOC review)
```

**03.01.03 — Information flow enforcement between CUI and non-CUI:**

```
# Separate policy chain or rule section titled "CUI-Boundary-Flow"
ALLOW: Approved-Integration-Host ↔ Partner-VDI  [documented in connection agreement]
DENY:  CUI-Datastores → Non-CUI-Desktops (default)
ALLOW: CUI-Datastores → Backup-Appliance  [narrow destination list]
```

**03.01.05 — Least privilege (network dimension):**

- Every ALLOW rule has: business owner, ticket ID, expected process set, expiry/review date.
- Prefer **workload identity** (agent visibility) over coarse subnet-only rules.

### 6.3 Plaintext and Unexpected Protocol Handling (Support to 03.13.x)

Create alerts for flows that indicate cleartext or risky transports from CUI scopes (examples: HTTP to sensitive ports, LDAP:389 from CUI app tiers, unapproved RDP paths). Pair technical blocks with compensating monitoring where applications cannot yet migrate to TLS.

---

## 7. Phase 5 — Enforcement and Validation (Days 40+)

| Stage | Mode | Objective |
|---|---|---|
| 1 | Simulation (2+ weeks) | Tune alerts; no production impact |
| 2 | Selective enforcement | Enforce **obvious deny** rules (e.g., CUI → open internet) |
| 3 | Full enforcement | Default deny with signed allow-list; break-glass process documented |

**Break-glass:** maintain an auditable process (ticket + time-bound policy toggle or scoped exception) for emergency change; avoid permanent “ANY ANY” exceptions.

---

## 8. Phase 6 — Risk Assessment and Vulnerability Context (Ongoing)

```
CSW UI → Investigate → Vulnerability Report
  → Scope: CUI-Enclaves
  → Sort by environmental priority (e.g., critical CVE on internet-adjacent + ADM path to datastore)
  → Export for POA&M / risk register
```

Use **reachability** from ADM plus exposure to justify remediation order (supports 03.11.x narrative). Where patching is delayed, document **compensating** CSW controls (tightened source IP, removal of path, extra logging on affected tier).

---

## 9. Phase 7 — Audit Readiness: Monitoring and Accountability (Ongoing)

### 9.1 Alerts Suited to CUI Operations

| Alert theme | Example trigger | Typical requirement tie-in |
|---|---|---|
| Boundary violation | Non-approved source connects to CUI tier | 03.01.02, 03.13.01 |
| Flow policy deny hit | Enforcement drop / reject | 03.13.06 |
| Novel lateral path | New east-west service on CUI datastore | 03.01.03, 03.04.x |
| Cleartext indicator | HTTP/LDAP from CUI app to sensitive listener | 03.13.x |
| Sensor gap | Agent offline on CUI server | 03.03.x (visibility gap) |

### 9.2 Forensic Export Pattern

```
CSW UI → Investigate → Flow Search
  → Time UTC window, source/destination workload, action
  → Export CSV/JSON per SOC reference design

CSW UI → Investigate → Process Search
  → Process tree for suspect host during same window
  → Attach exports to incident record
```

Integrate alerts and enriched logs with SIEM (syslog, API, or vendor connector per your subscription).

---

## 10. Control-by-Control Mapping (Representative Set)

The table below links **selected** Rev. 3 requirements to **CSW capabilities** and **example evidence**. It is not exhaustive; complete coverage requires mapping every applicable requirement in your SSP and 800-171A assessment procedures.

| Requirement | Title / intent (summary) | CSW capability | Evidence produced |
|---|---|---|---|
| 03.01.02 | Access enforcement | Scope-based micro-segmentation; deny default with explicit ALLOW | Policy workspace export; enforcement hit logs; simulation vs production diff |
| 03.01.03 | Information flow enforcement for CUI (CUI flow between connected systems) | Boundary policies CUI↔non-CUI; ADM-approved paths | ADM workspace export; boundary rule set; denied-flow report for violations |
| 03.01.05 | Least privilege (incl. network) | Minimal allow-list; process-scoped visibility | Rule review with owner/ticket metadata; process-attributed flows |
| 03.01.12 | Remote access | Restrict remote paths to managed gateways; log allowed admin sessions | Policies targeting jump hosts / bastions; flow logs for admin ports |
| 03.03.01 | Event logging | Flow + process telemetry | SIEM feed samples; retention configuration record |
| 03.03.02 | Audit events | Detailed connection records | Exported flows with 5-tuple, process, user context |
| 03.03.03 | Audit record content | Rich telemetry | Field mapping doc (see Appendix B) |
| 03.03.04 | Response to audit logging process failures | Alert when sensor/connectors stop; SIEM ingest health dashboards | SOC reference designs; tickets for logging pipeline failures |
| 03.03.05 | Audit record review, analysis, and reporting | Export to SIEM; correlation with identity and netflow | SOC review cadence; sample investigation reports |
| 03.03.06 | Audit record reduction and report generation | Flow/process summaries for investigations | Saved queries / reports used for after-action review |
| 03.03.07 | Time stamps (UTC granularity) | Telemetry timestamps aligned to enterprise time standard | Sample records + NTP configuration reference |
| 03.03.08 | Protection of audit information | RBAC on CSW console; least-privilege admin to change logging | Admin access list; change control for log integrations |
| 03.04.01 | Baseline configuration | ADM as communication baseline | Baseline vs current diff after change window |
| 03.04.02 | Configuration change | New flows / listeners flagged | Change tickets linked to observed deltas |
| 03.04.08 | Authorized software — allow by exception | Process / software inventory; block unexpected listeners via policy | Approved software list vs CSW inventory reconciliation |
| 03.11.x | Risk assessment inputs | CVE + reachability + EPSS-style prioritization if enabled | Risk workshop slides + CSW export attachments |
| 03.13.01 | Boundary protection | Enclave segmentation; internal key interfaces controlled | Topology from ADM; internal boundary rule list |
| 03.13.06 | Deny by default / allow by exception | Workload-level default deny | Signed allow-list; percentage of traffic denied as “unknown” near zero post-tuning |
| 03.13.08 | Transmission and storage confidentiality | Detect/block prohibited cleartext paths; visibility into sensitive flows (**transmission**); *encryption at rest* is validated outside CSW | Protocol analysis exports; blocked-flow metrics; SSP narrative for TLS/IPsec coverage |
| 03.14.01 | Flaw remediation (visibility / prioritization support) | Vulnerability exposure reports; reachability-aware prioritization | POA&M extracts; weekly export samples |
| 03.14.02 | Malicious code protection (complementary signal) | Process lineage; anomalous egress **in addition to** AV/EDR | CSW process-tree exports correlated with AV findings |
| 03.14.06 | System monitoring | Workload network + process monitoring; unauthorized connection detection | Alert catalog; dashboard screenshots; SOC coverage statement |
| 03.06.x | Incident handling (technical evidence) | Scope and timeline reconstruction | Forensic export bundle per IR playbook |
| 03.12.03 | Continuous monitoring | Ongoing workload telemetry + policy effectiveness metrics | Monitoring strategy attachment referencing CSW dashboards |
| 03.12.05 | Information exchange agreements (technical interfaces) | ADM shows live interfaces; policy enforces approved interconnections only | Interface list from ADM + signed exchange agreement references in SSP |

---

## 11. Common Pitfalls

| Pitfall | Mitigation |
|---|---|
| CUI workload missing from CSW inventory | Weekly reconcile against SSP; auto-label from cloud metadata where possible |
| Over-broad rules (subnet-only) undermine 03.01.05 evidence | Prefer workload + process context from ADM; document exceptions |
| ADM window too short (misses batch jobs) | Run ≥14 days; include month-end and patch cycles |
| Silent cleartext on non-standard ports | Inspect process-level protocol data; do not assume encryption by port number alone |
| Enforcement without successful simulation | Complete simulation with CAB sign-off; stage by enclave |
| Logs retained only in CSW console | Forward to SIEM / immutable store for assessor retention tests |

---

## 12. Boundaries — What CSW Does **Not** Cover

- **Policy, training, personnel, and HR workflows** (families 03.02, 03.09, parts of 03.15–03.17 documentation obligations).
- **Physical security** (03.10) and **media handling** procedures (03.08).
- **Cryptographic module validation** (FIPS 140) — CSW may help you see **where** crypto should be enforced, not **certify** implementations.
- **Authoritative identity lifecycle** (account provisioning, MFA enrollment, PIV issuance) — CSW consumes identity context where integrated but does not replace IdP/IAM.
- **Formal security assessments** — CSW supplies artifacts; assessors render official findings.
- **Out-of-scope workloads** — if an asset is missing an agent or connector, CSW cannot assert controls for it.

---

## 13. Audit Preparation and Evidence Export

### 13.1 Quarterly Evidence Bundle (Suggested Contents)

| Artifact | CSW source | Notes |
|---|---|---|
| Scope membership export | Inventory | Must reconcile to SSP component list |
| ADM baseline snapshot | ADM workspace | Time-bounded, signed by owner |
| Active policy workspace | Defend | Version ID + approver |
| Enforcement / simulation report | Policy analytics | Show drift vs prior quarter |
| Vulnerability exposure report | Vulnerability | CUI scope only |
| Sample SIEM ingest | SOC | Proof of central retention |

### 13.2 Optional CLI / Automation Examples

Use your enterprise automation pattern (CI pipeline, SOC playbook). Example: **periodic inventory pull** via your supported API/automation tool (replace with your gateway host and tokens):

```bash
#!/usr/bin/env bash
set -euo pipefail
# Illustrative only — use the official Cisco Secure Workload API / automation documented for your tenant.
export CSW_API_BASE="https://<tenant-api-endpoint>"
export CSW_API_TOKEN="$(vault kv get -field=token secret/csw/automation)"
curl -sS -H "Authorization: Bearer ${CSW_API_TOKEN}" \
  "${CSW_API_BASE}/v2/inventory/export?scope=CUI-Enclaves" \
  -o "cui_inventory_$(date -u +%Y%m%dT%H%M%SZ).csv"
```

Store exports in protectively marked storage consistent with CUI handling rules.

---

## Appendix A — Cross-Walk to NIST SP 800-53 Rev. 5 (Illustrative)

| 800-171 Rev. 3 | Related 800-53 control(s) (per NIST mapping) |
|---|---|
| 03.01.03 | AC-4 |
| 03.01.05 | AC-6 |
| 03.13.01 | SC-7 |
| 03.13.06 | SC-7(5) |
| 03.03.x | AU-2, AU-3, AU-6, AU-12 (family-dependent) |
| 03.14.x | SI-4, SI-7 (representative) |

Use official NIST mapping tables in **SP 800-171** and **SP 800-171A** as the authoritative cross-walk.

---

## Appendix B — SIEM Field Mapping (Example)

Map exported events to your logging standard. Minimum useful fields:

- Timestamp (UTC), sensor/workload ID, source/destination IP and port, protocol, action (allow/deny/alert), policy ID, process name, process hash, user (if available), scope labels (`cui_scope`, `enclave_id`).

---

## Appendix C — Related Framework Reference designs

- [NIST SP 800-53 Rev. 5](../NIST-800-53/CSW-NIST-800-53-Reference-Design.md) — federal control catalog alignment at AC, AU, CM, IR, RA, SC, SI.
- [CMMC 2.0](../CMMC-2/CSW-CMMC-Reference-Design.md) — assessment-oriented CUI scope patterns and Level 2 practice mapping (verify Rev. 2 vs. Rev. 3 contract baseline).
- [NIST SP 800-207](../NIST-800-207/CSW-NIST-800-207-Reference-Design.md) — Zero Trust architectural context for segmentation and telemetry.
- [FedRAMP](../FedRAMP/CSW-FedRAMP-Reference-Design.md) — when CUI processing shares infrastructure with FedRAMP-style packages.

---

*Replace organization-specific names and bracketed placeholders before external distribution. For contractual compliance, rely on your legal and program office interpretation of applicable NIST revisions.*
