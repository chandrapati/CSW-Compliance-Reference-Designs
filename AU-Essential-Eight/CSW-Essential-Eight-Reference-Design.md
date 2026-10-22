# Cisco Secure Workload — Australian Cyber Security Centre (ACSC) Essential Eight
## Reference Design | Essential Eight Maturity Model (EEMM)

**Version:** 1.0  
**Use Case:** Fresh Install, Hybrid Environment (On-Prem + Cloud)  
**Reference framework:** ACSC *Essential Eight Maturity Model* (strategies E1–E8; Maturity Levels ML1–ML3)

---

## Reader's Guide

**Who this is for.** Australian Government entities and organizations aligning with the ACSC Essential Eight; security architects translating the eight mitigation strategies into technical evidence; and assurance teams preparing for assessments against ML1–ML3 while using Cisco Secure Workload (CSW) as part of the control stack.

**Questions this reference design helps you answer:**

- *Where does CSW provide **primary** technical evidence versus **complementary** visibility alongside dedicated tools (application control, patching, MFA, backups)?*
- *How do I map CSW telemetry and segmentation to each Essential Eight strategy (E1–E8)?*
- *What can I demonstrate at **ML1**, **ML2**, and **ML3** maturity levels using CSW exports and enforcement artifacts—without over-claiming coverage for strategies that are fundamentally endpoint- or identity-provider-led?*
- *How do I prioritize patch effort using CVE, EPSS, and reachability context (**E2**, **E6**)?*
- *How do I evidence restriction of administrative privilege **paths** and visibility into privileged tooling usage (**E5**), in addition to identity controls?*

**What you'll need.** Your organization’s Essential Eight target maturity level per strategy, an accurate workload inventory, authoritative patching sources for OS and applications, and (where used) allowlisting or endpoint protection tooling that pairs with CSW for E1.

**Where to start.** Sections 1–4 for scope and sensor rollout; 5–6 for ADM baselines aligned to E1/E4/E5; 7 for maturity-level evidence; 8–10 for audit exports and boundaries.

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

- E2/E6 patch prioritisation via CVE+EPSS+reachability
- E5 admin privilege path restriction
- ML1–ML3 maturity evidence progression

**Compared to manual programmes:** static diagrams and annual firewall samples age immediately; CSW ties evidence to **live workload behaviour** and produces queryable exports on demand — supporting "operating effectively" language in PCI v4.0, SOC 2 CC7, and HIPAA risk analysis.

---

## 1. Overview

The **Essential Eight** is a prioritized set of mitigation strategies published by the Australian Cyber Security Centre (ACSC). The **Essential Eight Maturity Model (EEMM)** defines three maturity levels (**ML1**, **ML2**, **ML3**) with increasing rigor. **CSW is not a complete Essential Eight solution.** It **strongly complements** patch prioritization and admin-path containment (**E2**, **E5**, **E6**), and provides **meaningful but partial** visibility for application execution and hardening signals (**E1**, **E4**). Several strategies are **predominantly out of CSW scope** (**E3** configuration, **E7** MFA, **E8** backups), though CSW may still provide **peripheral** telemetry (for example, flows associated with backup or macro-enabled application behavior).

### 1.1 Essential Eight Strategies and CSW Support Summary

| Strategy | Name | CSW support level | Primary CSW mechanisms |
|---|---|---|---|
| **E1** | Application Control | **Partial / complementary** | Process and hash visibility; execution telemetry; forensic hunting for unapproved binaries *alongside* allowlisting |
| **E2** | Patch Applications | **Strong** | Software inventory, CVE awareness, EPSS where available, reachability/exposure prioritization |
| **E3** | Configure Microsoft Office Macro Settings | **Limited** | Detection of macro-enabled processes with unexpected network egress *after the fact*; does not set Office trust settings |
| **E4** | User Application Hardening | **Partial** | Unexpected connection patterns from browsers/office suites; depends on baseline/normalcy |
| **E5** | Restrict Administrative Privileges | **Strong (network path); partial (usage)** | Microsegmentation of admin ports; observation of admin tool usage at process level |
| **E6** | Patch Operating Systems | **Strong** | OS inventory, CVE mapping, prioritization via exposure |
| **E7** | Multi-Factor Authentication | **Out of scope** | Identity provider / IdP function; CSW does not perform MFA |
| **E8** | Regular Backups | **Out of scope (core)** | Optional: monitor backup traffic paths; does not prove backup integrity or immutability |

### 1.2 How to Read This Reference design with the EEMM

The ACSC defines **maturity levels per strategy**, not globally. Your evidence pack should **label each strategy separately**. CSW evidence is typically **cross-cutting** (inventory, flows, policy enforcement) and must be **mapped** to the subset of EEMM requirements it can support—never substitute CSW for endpoint configuration or IdP controls.

---

## 2. Pre-Deployment Checklist

- [ ] Target maturity (**ML1** / **ML2** / **ML3**) documented **per strategy** with accountable owners
- [ ] CSW cluster available; connectivity from in-scope workloads (typically TCP 443 outbound)
- [ ] Sensor support validated for Windows/Linux versions in scope (patch posture **E6** prerequisites)
- [ ] Cloud connectors configured where workloads run on AWS, Azure, or GCP
- [ ] Change windows approved for agent rollout; communications plan for security and application teams
- [ ] Complementary tools identified: **E1** allowlisting, **E3** Office GPO/MDM, **E7** IdP, **E8** backup/DR
- [ ] Evidence storage location defined (retention, classification, access control) for audit exports

---

## 3. Phase 1 — Sensor Deployment (Days 1–5)

### 3.1 Install Sensors (Linux)

```bash
sudo rpm -ivh tet-sensor-<version>.rpm    # RHEL/CentOS/Rocky/Alma
sudo dpkg -i tet-sensor-<version>.deb    # Debian/Ubuntu

sudo systemctl enable --now csw-agent 2>/dev/null || sudo systemctl enable --now tetration-agent
systemctl status csw-agent || systemctl status tetration-agent
```

### 3.2 Install Sensors (Windows)

Use the CSW-provided Windows installer package from your tenant; verify service health:

```powershell
Get-Service | Where-Object { $_.Name -match 'tetration|csw' }
```

### 3.3 Initial Posture

- **Enforcement:** Monitoring Only until ADM and owner sign-off (**E2**/**E6** patching still proceed via patch management; CSW does not patch)
- **Tagging:** Use labels that support Essential Eight reporting, for example `e8:e1`, `e8:e5-admin`, `tier:crown-jewel`, `patch_group:windows-servers`

---

## 4. Phase 2 — Scope Design for Essential Eight

### 4.1 Recommended Scope Layout

```
Enterprise
├── Crown-Jewels-Apps
├── Windows-Servers          # E6 heavy
├── Windows-Desktops         # E1/E3/E4/E5
├── Linux-Servers            # E2/E6 heavy
├── Admins-Jump-Zone         # E5 path controls
└── Backup-Infrastructure    # E8 adjacent telemetry only
```

### 4.2 Label Taxonomy

| Label | Values | Purpose |
|---|---|---|
| `e8_strategy` | E1…E8 | Filter evidence by strategy narrative |
| `admin_tier` | tier0/tier1/user | **E5** path policies |
| `internet_exposed` | true/false | **E2**/**E6** prioritization |
| `patch_source` | wsus, sccm, vendor | Correlate inventory to patch authority |

---

## 5. Phase 3 — Visibility and Baseline (ADM)

### 5.1 ADM for Unexpected Behavior (**E1**, **E4**, **E5**)

```
CSW UI → Investigate → Application Dependency Mapping
  → Workspace: "EssentialEight-Baseline"
  → Scope: Windows-Desktops + Linux-Servers (iterate)
  → Duration: ≥ 14 days (capture patch Tuesdays and admin windows)
```

**Baseline questions:**

| Question | Strategy |
|---|---|
| Which executables initiate network connections on endpoints? | **E1**, **E4** |
| Do browsers talk to rare external IPs or ports? | **E4** |
| Which hosts initiate inbound admin protocol sessions? | **E5** |
| Do Office processes spawn child processes with egress? | **E3** (complementary) |

### 5.2 Software Inventory for Patch Posture (**E2**, **E6**)

```
CSW UI → Investigate → Inventory
  → Filter: OS family, package/version, last observed
  → Export CSV weekly for reconciliation with WSUS/SCCM/Intune or Linux repos
```

Use inventory **gaps** (unknown agents) as ML2/ML3 coverage metrics for **visibility completeness**, not as a substitute for patch SLAs.

---

## 6. Phase 4 — Policy Design and Enforcement

### 6.1 **E5** — Administrative Privilege Paths (Illustrative Policies)

CSW enforces **who can reach** admin services—not **who authenticates**. Pair with PAM/MFA (**E7**).

```
DENY: Any-NonJumpHost → Windows-Servers (dst ports 3389, 5985, 5986)
DENY: Any-NonJumpHost → Linux-Servers (dst port 22) except Bastion-Subnet
ALLOW: Admins-Jump-Zone → Windows-Servers (3389/RDP gateway paths as validated)
ALLOW: Admins-Jump-Zone → Linux-Servers (22)
LOG: any other administrative port attempts
```

### 6.2 **E2** / **E6** — Network Containment While Patching (Compensating)

During delayed patching on exposed tiers, **narrow** connectivity:

```
DENY: Internet → Vulnerable-App-Tier (except approved WAF/load-balancer paths)
ALLOW: Patch-Management-Infra → Windows-Servers / Linux-Servers (update ports per tool)
```

### 6.3 **E1** / **E4** — Detection-Oriented Rules (Complementary)

After baseline, alert on **first-seen unsigned binary path** or **unexpected child of browser**—tune aggressively to avoid noise:

```
ALERT: first_seen_process = true AND scope = Windows-Desktops
ALERT: parent_process in (browser_set) AND dst_port not in (443, 80) AND dst not in approved_proxy
```

> Application allowlisting (**E1** primary) remains the authoritative control; CSW **augments** with network/process context.

### 6.4 Workspace Publication

```
CSW UI → Defend → Segmentation
  → Workspace: "EssentialEight-E5-AdminPaths"
  → Mode: Simulation (2+ weeks) → staged Enforcement
```

---

## 7. Phase 5 — Maturity Level Mapping (ML1–ML3)

The ACSC defines requirements per strategy at each maturity level. The tables below state **what CSW evidence commonly supports**—your assessor’s official checklist remains authoritative.

### 7.1 **E1 — Application Control**

| Maturity | ACSC intent (summary) | CSW evidence that may support | CSW limitations |
|---|---|---|---|
| **ML1** | Basic controls for workstations | Process inventory and notable execution telemetry samples | Not an allowlist enforcer |
| **ML2** | Stronger coverage/focus areas | Longer ADM baselines; alerts on rare executables with network activity | Tuning burden; requires baselining |
| **ML3** | Organization-wide / advanced | Coverage dashboards (% agents active per desktop population); hunt exports | Does not replace centralized application control policy |

### 7.2 **E2 — Patch Applications** & **E6 — Patch Operating Systems**

| Maturity | CSW evidence that may support | Notes |
|---|---|---|
| **ML1** | Inventory exports showing versions; CVE lists for in-scope apps/OS | Prioritization narratives for risk acceptance |
| **ML2** | Reachability-informed priority queues; evidence of exposed vs internal-only risk | Pair with patch ticket closure from patch tool |
| **ML3** | Continuous monitoring of inventory drift; alerting on high-risk deltas | CSW **detects** drift; patching action is external |

### 7.3 **E3 — Office Macros**

| Maturity | CSW evidence that may support | CSW limitations |
|---|---|---|
| **ML1–ML3** | Flows showing WINWORD/EXCEL/POWERPNT child processes with egress | Does not prove macro trust settings or ASR rules |

### 7.4 **E4 — User Application Hardening**

| Maturity | CSW evidence that may support | CSW limitations |
|---|---|---|
| **ML1** | Basic external connection inventory from browsers | No browser configuration management |
| **ML2–ML3** | Anomaly alerts on rare destinations, protocols, or lateral use | Requires sound baseline; false positives possible |

### 7.5 **E5 — Restrict Administrative Privileges**

| Maturity | CSW evidence that may support | Pair with |
|---|---|---|
| **ML1** | Visibility into admin protocol usage | Jump host/PAM design |
| **ML2** | Simulation and then enforcement restricting admin ports | IdP + MFA (**E7**) for actual privilege restriction |
| **ML3** | Ongoing conformance dashboards; deny logs for policy violations | Privileged access reviews (process outside CSW) |

### 7.6 **E7 — Multi-Factor Authentication**

| Maturity | CSW role |
|---|---|
| **ML1–ML3** | **No primary CSW mapping.** Maintain IdP/MFA evidence separately. Optional: enforce paths to auth infrastructure only. |

### 7.7 **E8 — Regular Backups**

| Maturity | CSW role |
|---|---|
| **ML1–ML3** | **No backup immutability or restore testing.** Optional: monitor backup client flows; alert on backup traffic to unexpected destinations. |

---

## 8. Phase 6 — Control-by-Control Mapping Table

| Essential Eight requirement (strategy) | CSW capability | Evidence produced |
|---|---|---|
| **E1** Application control | Process visibility; execution telemetry; forensic search | Process export for sample period; alerts on anomalous executions *with* allowlist policy records from endpoint tool |
| **E2** Patch applications | Inventory; CVE + EPSS + exposure | Vulnerability CSV; prioritized remediation list with reachability column |
| **E3** Office macros | Egress patterns from Office processes | Flow exports for investigation windows; **not** macro policy config |
| **E4** Application hardening | Browser/Office network baselines; anomalies | ADM diff; alert history |
| **E5** Restrict admin privileges | Segmentation around admin services; process visibility | Policy exports; deny logs; jump-host path diagrams backed by flows |
| **E6** Patch operating systems | OS inventory; CVE mapping | Same as **E2**, OS-focused filters |
| **E7** Multi-factor authentication | N/A (identity) | Maintain MFA platform logs; CSW optional path allowlists only |
| **E8** Regular backups | Peripheral flow monitoring | Backup traffic baselines; anomaly alerts **plus** backup product reports |

---

## 9. Boundaries — What CSW Does **Not** Cover

- **Application allowlisting** implementation (**E1** primary control) and **Microsoft Office macro trust configuration** (**E3**)
- **Multi-factor authentication** enrollment and enforcement (**E7**)
- **Backup** scheduling, immutability, offline copies, and restore testing (**E8**)
- **Endpoint hardening baselines** (ASR, AppLocker, browser settings) for **E4**
- **Patch deployment** itself (**E2**/**E6**): CSW informs priority; patch systems execute change
- **People and process** maturity artifacts (policies, training records, governance minutes) required by EEMM assessments

---

## 10. Audit Preparation and Evidence Export

### 10.1 Suggested Evidence Schedule

| Evidence | CSW source | Suggested frequency | Strategies served |
|---|---|---|---|
| Agent coverage by population | Manage → Agents | Monthly | **E1**–**E6** (visibility completeness) |
| ADM baseline snapshot | Investigate → ADM | 90 days | **E1**, **E4**, **E5** |
| Inventory export (OS + apps) | Investigate → Inventory | Weekly | **E2**, **E6** |
| Vulnerability prioritized export | Investigate → Vulnerability | Monthly | **E2**, **E6** |
| Segmentation policy version | Defend → Segmentation | Each change | **E5** (paths), compensating **E2**/**E6** |
| Alert sample pack | Alerts / SIEM | Quarterly or ad hoc | **E1**, **E4**, **E5** incidents |

### 10.2 Export Workflows

```
CSW UI → Investigate → Flow Search
  → Scope + time window
  → Export CSV/JSON with process metadata

CSW UI → Investigate → Process Search
  → Filter: suspicious parent chains or first-seen binaries
  → Export for IR or assessor sampling

CSW UI → Defend → Segmentation
  → Export policy workspace and change history notes
```

### 10.3 Bash Helper — Evidence Folder Staging (Illustrative)

```bash
#!/usr/bin/env bash
set -euo pipefail
# Example output: 2026-Q2
AUDIT_CYCLE="$(date +%Y-Q$(( ( $(date +%-m) - 1 ) / 3 + 1 )))"
TARGET_ROOT="/secure/evidence/acsc-e8/${AUDIT_CYCLE}"
mkdir -p "${TARGET_ROOT}"/{inventory,vuln,policies,adm}
echo "Copy CSW UI/API exports into the subfolders and generate MANIFEST.sha256"
find "${TARGET_ROOT}" -type f -print0 | sort -z | xargs -0 sha256sum > "${TARGET_ROOT}/MANIFEST.sha256"
```

> Store manifests and exports under your records management policy; redact sensitive endpoints for third-party sharing.

---

## 11. Common Pitfalls

| Pitfall | Mitigation |
|---|---|
| Claiming CSW satisfies **E7** or **E8** | Keep IdP and backup evidence separate; use CSW only as supplementary |
| Over-alerting on **E4** without baseline | Run ADM for full business cycles before enforcement/detection thresholds |
| **E5** enforcement breaking emergency access | Document break-glass paths; alert-only exceptions with expiry |
| Inventory false confidence | Reconcile CSW inventory with CMDB; chase agents not reporting |
| Assuming macro security is “fixed” due to CSW | Validate Office trust settings via MDM/GPO and ASR |

---

## Appendix A — Related Frameworks

- [CIS Controls v8](../CIS-Controls-v8/CSW-CIS-Reference-Design.md) — control themes aligned to hardening and visibility narratives.
- [NIST SP 800-207](../NIST-800-207/CSW-NIST-800-207-Reference-Design.md) — zero trust segmentation patterns supporting **E5** path restriction.
- [ISO/IEC 27001:2022](../ISO-27001-2022/CSW-ISO27001-Reference-Design.md) — for organizations mapping Essential Eight to broader ISMS audits.


- [UK NCSC CAF v3.2](../UK-NCSC-CAF/caf-mapping.md) — E2 and E6 patch evidence is the reuse path for CAF B4.

---

## Appendix B — Official References (External)

- Australian Cyber Security Centre — *Essential Eight* and *Essential Eight Maturity Model* publications: [https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/essential-eight](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/essential-eight)

> Verify you use the **current** ACSC version and assessment guidance; maturity requirements evolve.

---

*Document prepared for Cisco customer engagements. Tailor scopes, maturity targets, and evidence indexes to your ACSC assessment boundary before external sharing.*
