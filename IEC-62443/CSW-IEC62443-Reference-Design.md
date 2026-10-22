# Cisco Secure Workload — IEC 62443 Compliance Framework
## Reference Design | Industrial Automation & Control Systems (IACS)

**Version:** 1.0  
**Use Case:** Fresh Install, Hybrid Environment (On-Prem + Cloud)  
**Standards anchor:** IEC 62443-3-3 (System security requirements and security levels); IEC 62443-2-1 (Security program requirements for IACS asset owners) — consult your SL-T target and zone/conduit documentation for authoritative control text.

---

## Reader's Guide

**Who this is for.** IACS asset owners, OT/IT security architects, plant
or operations cybersecurity teams, and integrators preparing for
IEC 62443-aligned assessments, customer security requirements, or
internal security management system (SMS) evidence for industrial
environments.

**Scope boundary you must understand before reading further.** Cisco
Secure Workload (CSW) enforces segmentation, discovers dependencies,
and produces forensic telemetry on **servers, virtual machines,
containers, and cloud workloads** — the **IT side of the IT/OT
boundary** and the systems that **support** IACS (jump hosts,
engineering workstations, historians, MES interfaces, DMZ brokers,
identity services, patch servers, vendor remote-access concentrators).
CSW does **not** replace dedicated OT visibility for Level 0–2 devices
(PLCs, RTUs, IEDs, drives, field instruments). Pair CSW at the IT
layer with **Cisco Cyber Vision**, **Claroty**, **Nozomi**, or
equivalent for asset discovery, ICS protocol analytics, and
device-level integrity signals.

**Questions this reference design helps you answer:**

- *SR 5.1–5.4 (restricted data flow / zones & conduits): Can I prove
  that only documented conduits carry traffic between OT-support
  tiers and corporate/cloud, and that lateral movement outside those
  conduits is structurally denied or logged?*
- *SR 1.1–1.13 (identification / authentication / access control):
  Can I show identity-aligned allow rules and deny-by-default paths
  for systems that administer or bridge into IACS zones?*
- *SR 3.1–3.9 (data / system integrity): Can I baseline inventory
  (processes, binaries, listening services) and detect unexpected
  change or unauthorized software on IACS-adjacent IT workloads?*
- *SR 6.1–6.2 (event monitoring & timely response): Can I reconstruct
  a timeline of flows and processes during an OT-adjacent incident?*
- *SR 7.1–7.8 (resource availability): Can I detect volumetric or
  connection storms indicative of denial-of-service against critical
  IT services that underpin OT availability?*
- *IEC 62443-2-1 (security program / operations): Can I produce
  continuous monitoring dashboards and exports that feed our SMS
  without manual spreadsheet reconciliation?*

**What you'll need.** Your zone & conduit model (per IEC 62443-3-2 or
customer ZCRD), Security Level Target (SL-T) per zone, inventory of
IACS-adjacent IT systems (EWS, jump hosts, AD/PKI, historians), change
management approval for sensor install, and naming alignment between
your PAS/OT tools and CMDB labels.

**Where to start.** Sections 1–2 while scoping; 3–5 during pilot
sensor and baseline; 6–8 when designing enforcement; 9–10 for control
mapping and SMS reporting; section **Boundaries** before promising CSW
coverage to integrators or auditors.

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

- Zones & conduits segmentation on IT-side OT boundaries
- SR control evidence; pair with Cyber Vision/Claroty for device layer
- Jump host and historian path visibility

**Compared to manual programmes:** static diagrams and annual firewall samples age immediately; CSW ties evidence to **live workload behaviour** and produces queryable exports on demand — supporting "operating effectively" language in PCI v4.0, SOC 2 CC7, and HIPAA risk analysis.

---

## 1. Overview

IEC 62443 provides a lifecycle-oriented security framework for
industrial automation and control systems. **IEC 62443-3-3** specifies
foundational requirements (FRs) and associated **system requirements
(SRs)** for IACS components and systems. **IEC 62443-2-1** defines
requirements for an IACS **security management system** operated by the
asset owner. CSW contributes **technical evidence** for restricted data
flow, access enforcement, integrity-related visibility, detection
support, and availability-oriented anomaly awareness on the **IT
workloads** that border or support IACS — not as a substitute for OT
protocol inspection or safety-instrumented logic.

### IEC 62443 structure mapped to CSW capabilities

| IEC 62443 topic | Typical artifacts | Relevant CSW capabilities |
|---|---|---|
| **FR 5 / SR 5.1–5.4** — Restricted data flow (zones & conduits) | Zone diagrams, conduit allowlists, firewall/ACL rules | Microsegmentation workspaces; scope hierarchy mirroring zones; default-deny with explicit conduits |
| **FR 1 / SR 1.1–1.13** — Identification, authentication, access control | Account lifecycle, RBAC, remote access paths | Identity-aware policies (where integrated); least-privilege allowlists; jump-host-only admin paths |
| **FR 3 / SR 3.1–3.9** — System & data integrity | Software inventory, patch posture, change detection | Process/binary inventory; listening-port baseline; vulnerability context; drift alerts |
| **FR 6 / SR 6.1–6.2** — Event monitoring & timely response | SOC reference designs, timelines, ticket exports | Flow + process forensics; alert correlation inputs to SIEM |
| **FR 7 / SR 7.1–7.8** — Resource availability | SLAs, capacity plans, DoS playbooks | Flow anomaly detection (connection/session volume spikes); early warning on saturation patterns |
| **62443-2-1** — Security management / operations | KPIs, dashboards, management review | Continuous inventory/policy dashboards; scheduled evidence export |

**Regional or contractual note:** Many asset owners implement 62443
requirements through customer purchase specifications or national
interpretations. Map this reference design’s **SR** references to *your*
contractual clauses and audit questionnaires; numbering alone is not
sufficient for certification evidence without your target SL and scope.

---

## 2. Pre-Deployment Checklist

Before deploying CSW sensors on IACS-adjacent IT estates, confirm:

- [ ] CSW cluster (SaaS or on-prem) is provisioned; **air-gap / data
  residency** rules reviewed if telemetry leaves the plant DMZ
- [ ] Network path from workloads to CSW cluster (typically **443
  outbound**); proxy exceptions documented
- [ ] Linux/Windows agent compatibility verified for **engineering
  workstations, jump servers, historians, AD/PKI**, and cloud broker VMs
- [ ] Cloud connectors configured where plant data lands in **AWS /
  Azure / GCP** (historian mirrors, IoT hubs, analytics lakes)
- [ ] Stakeholders engaged: **OT security lead**, **plant IT**,
  **integrator**, **SOC**, and **SMS owner** (62443-2-1)
- [ ] **Maintenance window** approved; **OT change freeze** rules
  respected — start in **Monitoring Only**
- [ ] **PAS / OT tool** (Cyber Vision, Claroty, Nozomi) inventory
  export available for cross-walk of hostnames / VLANs / cell IDs

---

## 3. Phase 1 — Sensor Deployment (Days 1–5)

### 3.1 On-premises IT adjacent to IACS

**Install software sensors on representative tiers:** EWS images, jump
hosts, historian/MES application servers, AD connectors, vendor VPN
concentrators — *never* on safety PLCs or real-time controllers if
those run unsupported or prohibited agent OSes.

```bash
# Linux (RHEL/CentOS/Ubuntu family)
sudo rpm -ivh tet-sensor-<version>.rpm    # RHEL/CentOS-compatible
sudo dpkg -i tet-sensor-<version>.deb    # Debian/Ubuntu

# Verify sensor service
sudo systemctl status csw-agent
sudo systemctl enable --now csw-agent
```

**Windows (engineering workstation build):**

```powershell
# Example: install from staged MSI (version/path per release)
msiexec /i "C:\Deploy\tet-sensor-<version>.msi" /qn
Get-Service | Where-Object { $_.Name -like "*tet*" -or $_.Name -like "*csw*" }
```

**Initial posture:**

- Enforcement: **Monitoring Only** (no blocks until ADM + simulation
  complete)
- Collection: **process hash**, **network flow**, **listening
  services**, **vulnerability exposure** (where licensed)
- Tags from day one: `zone:<cell>`, `conduit:<id>`, `iqs:iacs-adj`,
  `sl-target:SL2` (example)

### 3.2 Cloud & hybrid IACS data paths

Use **cloud connectors** when historian/analytics or IT control plane
lives in public cloud:

```
CSW UI → Platform → External Orchestrators
  → Add AWS / Azure / GCP connector
  → Least-privilege IAM / service principal
  → Enable flow visibility (VPC/VNet flow ingestion where supported)
```

### 3.3 Sensor validation

```
CSW UI → Manage → Agents
  → Status: Active for all pilot hosts
  → Confirm telemetry (flow/process) within 15–30 minutes of install
  → Record agent build in baseline export (62443-3 SR 3 / change mgmt input)
```

---

## 4. Phase 2 — Scope & Inventory Design — Zones, Conduits, SL (Days 6–12)

### 4.1 Map CSW scopes to IEC zones & conduits

Model scopes to mirror **62443-3-2** zone definitions without renaming
your-certified drawings — use **labels** that reference drawing IDs.

```
Root: Industrial-Enterprise
├── Plant-<Site>-OT-Support        # IT that touches OT (EWS, jump, historian app tier)
│   ├── Cell-A-Conduit-IT-OT       # Scoped to hosts in conduit endpoints only
│   ├── Cell-B-Conduit-IT-OT
│   └── Shared-Services-IACS       # AD, PKI, patch, backup — constrained to conduits
├── Plant-DMZ-Brokers              # Data diodes / OPC brokers / MQTT gateways (VM-based)
├── Corporate-IT                   # Default no direct path to OT-support
└── Vendor-Remote-Access           # Termination servers for integrator VPN
```

**Conduit rule of thumb:** One CSW policy workspace per **documented
conduit** (or group of symmetric conduits) so evidence maps 1:1 to
the ZCRD.

### 4.2 Discovery filters for IACS-adjacent candidates

```
Filter: Historian-MES-Tier
  - Process name contains: historian, mes, opc*, scada, "wonderware"
  - Ports: 1433, 1521, 5432, 135, 502 (context-dependent — validate in YOUR env)
  - Tag pas:ot-adjacent (if synchronized from PAS)

Filter: Jump-EWS
  - Hostname regex: (?i)(ews|eng|hmi-jump|vendor-jump)
  - User workload tag: role=engineering
```

Validate every automated filter with **OT SME sign-off** — **SR 5**
evidence must match the *as-engineered* conduit list, not a guessed list.

### 4.3 Label strategy (SMS-friendly)

| Label key | Examples | Purpose |
|---|---|---|
| `zone` | `cell-a`, `line-3` | Aligns to 62443 zone ID |
| `conduit` | `c-ot-to-mes-01` | Audit trail for restricted data flow |
| `sl-target` | `SL2`, `SL3` | Drive rule strictness / monitoring cadence |
| `ics-role` | `ews`, `jump`, `historian`, `broker` | Policy grouping |
| `owner` | `ot-sec`, `plant-it` | Accountability in exports |

---

## 5. Phase 3 — Application Dependency Mapping & Baseline (Days 13–28)

### 5.1 ADM workspace

ADM establishes **observed** vs **designed** conduits — essential for
**SR 5** and access **SR 1** reviews.

```
CSW UI → Investigate → Application Dependency Mapping
  → New Workspace
  → Name: IACS-Conduit-Baseline-<Site>
  → Scope: Plant-<Site>-OT-Support + DMZ brokers
  → Window: minimum 2–4 weeks (capture patch Tuesday, recipe changes, campaigns)
  → Enable process context; retain ≥ 30 days if storage policy allows
```

### 5.2 ADM review checklist (62443-oriented)

| Investigation question | SR / FR linkage |
|---|---|
| Which corporate subnets talk to historians or OPC brokers? | **SR 5** — restricted data flow |
| Are there HTTPS/LD/RDP paths bypassing EWS/jump? | **SR 1** — access paths |
| Do EWS images reach the internet directly? | **SR 5**, **SR 1** |
| New binary or service on jump host? | **SR 3** — integrity |
| Sudden east-west fan-out from a broker VM? | **SR 6** — detection; **SR 7** — availability stress |

### 5.3 Baselining for integrity (SR 3 inputs)

Export **inventory snapshots** after accepted build state:

```
CSW UI → Investigate → Inventory (or equivalent workload inventory view)
  → Filter: scope = Plant-<Site>-OT-Support
  → Export: processes, packages, listening ports, hashes (as available)
  → Store in secure evidence library with version + timestamp
```

Repeat on **known-good** patch cycles to update baseline registers.

---

## 6. Phase 4 — Policy Design & Enforcement (Days 29–45)

### 6.1 Conduit-aligned policy framework

Translate **allowlisted conduits** into CSW rules. **Example pattern**
— adjust ports, scopes, and identities to your ZCRD.

**Absolute denies (illustrative):**

```
DENY: Corporate-IT → Plant-<Site>-OT-Support (all)
  EXCEPTION: documented Intermediary / jump subnet only

DENY: Vendor-Remote-Access → any except Plant-DMZ-Brokers & Jump hosts

DENY: Plant-<Site>-OT-Support → Internet (0.0.0.0/0)
  EXCEPTION: explicit patch/CDN allowlist + CSW SaaS egress if required
```

**Conduit allows (illustrative):**

```
ALLOW: Plant-DMZ-Brokers ↔ Historian-MES-Tier
  - TCP 135, 49320–49330 (DCOM range — validate), OPC-UA 4840 (if used)

ALLOW: Jump-EWS → Plant-<Site>-OT-Support
  - RDP 3389 / SSH 22 only from Jump-EWS scope

ALLOW: Plant-<Site>-OT-Support → AD-PKI
  - LDAPS 636, Kerberos 88, DNS 53 — block cleartext LDAP 389 where possible
```

**Audit unmatched:**

```
LOG + ALERT: any flow not matching explicit conduit rules
```

### 6.2 Policy workspace

```
CSW UI → Defend → Segmentation
  → New Workspace: IEC62443-Conduits-<Site>
  → Import ADM-suggested rules → reconcile with ZCRD
  → Mode: Simulation (minimum 2 weeks typical) → Enforcement by conduit tier
```

### 6.3 Enforcement progression

| Step | Mode | Objective |
|---|---|---|
| 1 | Simulation | Prove OTSupport apps still function; tune OPC/RPC ranges |
| 2 | Selective enforcement | Lock down highest-risk corporate lateral paths first |
| 3 | Full enforcement on IT border | Default deny except conduits; maintain break-glass procedure |

**Integrator coordination:** Provide **simulation reports** before
enabling blocks on lines under warranty support.

---

## 7. Phase 5 — Monitoring, Availability Signals & SMS Feeds

### 7.1 Alerts aligned to 62443 operations

| Alert | Example trigger | SR mapping |
|---|---|---|
| Undocumented conduit attempt | New src→dst across OT-support boundary | **SR 5** |
| Cleartext admin | LDAP/HTTP to AD from EWS | **SR 1**, **SR 3** |
| New listening service on jump | Port opens not in baseline | **SR 3** |
| Flow anomaly / storm | Connection rate >> baseline | **SR 6** (detect), **SR 7** (availability) |
| Critical CVE on historian tier | CVSS ≥ threshold | **SR 3**, **62443-2-1** risk treatment |
| Sensor offline | Loss of heartbeats | **SR 6** — visibility gap |

### 7.2 IEC 62443-2-1 continuous monitoring dashboard

Schedule **weekly** management-visible tiles (exact UI path may vary
by release):

- **Scope coverage** — % of IACS-adjacent IT with active agent
- **Policy drift** — rules changed since last approval export
- **Open simulation violations** — unreviewed would-block flows
- **Top talkers** across conduits — compare to PAS asset roles

Export snapshots into your SMS review record **monthly** minimum.

---

## 8. Control-by-control mapping — Framework requirement → CSW → evidence

Use this table to **start** questionnaire mapping. Official conformity
assessment requires your **SL-T**, **scope statement**, and **test
methods** from the certification body or customer spec.

### 8.1 SR 5 — Restricted data flow (zones & conduits)

| IEC 62443-3-3 requirement (summary) | CSW capability | Evidence produced |
|---|---|---|
| **SR 5.1** — Segmentation / zones | Scope hierarchy; segmentation workspaces; labels `zone`, `conduit` | Scope export; diagram cross-walk memo |
| **SR 5.2** — Segmentation for zones of differing security requirements | Tiered scopes by SL labels; stricter workspaces for higher SL | Policy diff between SL scopes |
| **SR 5.3** — Conduit control | Allowlist rules per conduit; default deny | Policy JSON/export + simulation/enforcement logs |
| **SR 5.4** — Covert channel mitigation (as applicable at IT layer) | Egress restrictions; anomaly detection on volume | Flow anomaly reports + change tickets |

### 8.2 SR 1 — Identification, authentication, and access control

| IEC 62443-3-3 requirement (summary) | CSW capability | Evidence produced |
|---|---|---|
| **SR 1.1–1.13** (human / process / service access paths) | Identity-aware policies (when integrated); admin path lock-down; least privilege allowlists | Flow logs with user/process context; policy allow/deny history |
| **Remote access** paths via jump | Rules limiting src to jump scope; deny corporate→OTSupport direct | ADM + enforcement hit logs |

### 8.3 SR 3 — System integrity

| IEC 62443-3-3 requirement (summary) | CSW capability | Evidence produced |
|---|---|---|
| **SR 3.1–3.9** (software integrity, malware deterrence inputs, etc.) | Process & binary inventory; package visibility; vulnerability data | Inventory export; drift alerts; VA connectors / built-in reports |
| **Unauthorized software** indicators | New process / listener alerts vs baseline | Ticket + before/after inventory |

### 8.4 SR 6 — Event monitoring & timely response

| IEC 62443-3-3 requirement (summary) | CSW capability | Evidence produced |
|---|---|---|
| **SR 6.1** — Audit logging support | Flow + process retention; export APIs / UI exports | Raw & summary logs with UTC stamps |
| **SR 6.2** — Continuous monitoring inputs | Alerts; SIEM forwarders | Alert rule catalog; SOC ingest proof |

### 8.5 SR 7 — Resource availability

| IEC 62443-3-3 requirement (summary) | CSW capability | Evidence produced |
|---|---|---|
| **SR 7.1–7.8** (DoS considerations at system level) | Flow volumetrics; session rate anomalies; saturation precursors | Time-series anomaly exports + IR narrative |

### 8.6 IEC 62443-2-1 — Security management system (technical contributors only)

| 62443-2-1 theme (summary) | CSW capability | Evidence produced |
|---|---|---|
| Operations monitoring & KPIs | Dashboards; scheduled exports | Monthly PDF/CSV appendices to SMS review |
| Incident response support | Forensic drill exports | Tabletop package — flow + process trace |

---

## 9. Vulnerability, patch & compensating controls

### 9.1 Vulnerability visibility

```
CSW UI → Investigate → Vulnerability Report
  → Scope: Plant-<Site>-OT-Support
  → Filter: CVSS ≥ 7.0 (example)
  → Export CSV for SMS risk register linkage
```

### 9.2 Compensating controls when patching waits for outage

- Narrow allow rules to **known peer scopes** only
- Raise **alert severity** on vulnerable process names
- Capture **full flow logs** to affected workload until patched

---

## 10. Forensics & incident reconstruction

```
CSW UI → Investigate → Flow Search
  → Time range: incident window (extend for long-running OT campaigns)
  → Source/Destination: suspected broker or EWS
  → Export: CSV/JSON with process + user context

CSW UI → Investigate → Process Search
  → Parent/child chain for suspicious binaries on jump hosts
```

Retain exports per **your** SMS / legal hold policy; correlate with **PAS**
PCAP or ICS alerts for full OT picture.

---

## 11. Audit preparation & evidence export

### 11.1 Quarterly evidence pack (adjust to customer cadence)

| Evidence item | CSW source | Typical IEC mapping |
|---|---|---|
| Conduit policy export | Defend → workspace export | **SR 5.x** |
| Simulation vs enforcement history | Policy lifecycle / audit log | **SR 5**, **SR 1** |
| ADM cluster report | ADM workspace | **SR 5**, **SR 1** |
| Inventory baseline delta | Inventory exports | **SR 3.x** |
| Vulnerability exposure | Vulnerability report | **SR 3**, **62443-2-1** |
| Alert & flow excerpts | Flow Search, Alerts | **SR 6**, incident packs |
| Coverage report | Agent inventory | **62443-2-1** monitoring scope |

### 11.2 Bash helper examples (on analysis workstation)

After UI export to `/evidence/csw/`:

```bash
# Verify exported policy archive integrity (after UI download)
shasum -a 256 /evidence/csw/iec62443-policy-export-YYYYMMDD.zip | tee /evidence/csw/SHA256SUMS

# Redact non-production subnets before sharing with integrator
perl -pe 's/\b10\.\d{1,3}\.\d{1,3}\.\d{1,3}\b/10.REDACTED.0.0/g' \
  /evidence/csw/flows-incident-window.csv > /evidence/csw/flows-incident-window-redacted.csv
```

---

## 12. Boundaries — what CSW does **not** cover

- **Level 0–2 OT devices** (PLCs, IEDs, devices without supported agents) —
  use PAS/OT security tools; CSW does not inspect proprietary fieldbus
  payloads at wire speed.
- **Safety instrumented functions** — CSW is not a SIL-rated safety
  device; engineering lifecycle evidence stays with SIS vendor tools.
- **Physical security & personnel screening** — access badges, gates,
  contractor vetting — outside CSW.
- **Cryptographic key management policy** — CSW may enforce **paths**
  (e.g., TLS-only) but does not replace PKI governance or HSM decisions.
- **62443-2-1 organizational processes** — CSW supplies **telemetry and
  policy exports**; it does not author your procedures, training roster,
  or supplier security clauses.

---

## 13. Common pitfalls

| Pitfall | Mitigation |
|---|---|
| Mis-mapping CSW scopes to **electrical zones** instead of **cyber zones** | Anchor labels to approved cyber ZCRD IDs |
| Blocking **dynamic RPC/OPC** ranges without ADM | Long simulation + integrator test scripts |
| Deploying only on corporate IT | **OT-adjacent** IT is the compliance-critical tier |
| Ignoring cloud **shadow IT** paths to plant data | Enable cloud connectors for mirrored historians |
| Expecting CSW to **replace** OT IDS | Maintain Cyber Vision / Claroty / Nozomi for ICS context |

---

## Related Frameworks

- [NERC CIP](../NERC-CIP/CSW-NERC-CIP-Reference-Design.md) —
  analogous IT/OT boundary evidence pattern for BES entities.
- [NIST SP 800-82](https://csrc.nist.gov/publications/detail/sp/800-82/rev-3/final) —
  operational technology companion guidance (external).
- [ISO/IEC 27001:2022](../ISO-27001-2022/CSW-ISO27001-Reference-Design.md) —
  when plants pair 62443 with enterprise ISMS audits.
- [NIST SP 800-207](../NIST-800-207/CSW-NIST-800-207-Reference-Design.md) —
  zero trust patterns for conduit enforcement narratives.


- [UK NCSC CAF v3.2](../UK-NCSC-CAF/caf-mapping.md) — zones and conduits are the reuse path for CAF B5 on the IT side of an IT/OT boundary.

---

### Appendix A — Sample segmentation policy fragment (illustrative YAML-style)

> **Do not paste verbatim into production.** Replace scopes, addresses,
> and L4 tuples with values from your ZCRD. Syntax mirrors conceptual
> CSW rule metadata; exact API/UI format follows product version.

```yaml
workspace: IEC62443-Conduits-Site01
mode: simulation          # change to enforcement after sign-off
default_action: deny
rules:
  - name: conduit-opcua-historian
    action: allow
    src_scope: Plant-DMZ-Brokers
    dst_scope: Historian-MES-Tier
    services:
      - tcp/4840
  - name: admin-via-jump-only
    action: allow
    src_scope: Jump-EWS
    dst_scope: Plant-Site01-OT-Support
    services:
      - tcp/22
      - tcp/3389
  - name: log-unknown-east-west
    action: alert
    src_scope: Plant-Site01-OT-Support
    dst_scope: Plant-Site01-OT-Support
    match: not_in_conduit_allowlist
```

### Appendix B — PAS correlation workflow

1. Export **asset list** from Cyber Vision / Claroty / Nozomi (IP,
   MAC, VLAN, firmware).
2. Join on **IP or hostname** with CSW inventory.
3. Flag **CSW-only** or **PAS-only** assets — resolve before **SR 5**
   attestation.
4. For discrepancies, **field-verify** with plant engineering.

---

*Document prepared for industrial account engagements. Replace site
names, drawing references, and SL targets with customer-specific
values before delivery.*
