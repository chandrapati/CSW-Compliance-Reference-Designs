#!/usr/bin/env python3
"""
Inject shared CSW primer + evidence workflow into all *-Reference-Design.md files.

Skips files that already contain marker: <!-- CSW-RUNBOOK-PRIMER:v1 -->
"""

from pathlib import Path

MARKER = "<!-- CSW-RUNBOOK-PRIMER:v1 -->"

# Framework folder -> short effectiveness bullets (from README coverage)
FRAMEWORK_HIGHLIGHTS = {
    "HIPAA": [
        "Continuous ePHI boundary proof via scope + enforce — not just BAA paperwork",
        "Process-level flow telemetry answers OCR 'who accessed what' faster than SIEM alone",
        "ADM replaces stale PHI network diagrams with behaviour-derived maps",
    ],
    "HIPAA-2025-NPRM": [
        "Supports proposed mandatory segmentation evidence (§164.312(a)(2)(vi))",
        "Asset inventory + 72-hour breach timeline inputs from flow/process search",
        "Continuous logging architecture vs. point-in-time log samples",
    ],
    "SOC2": [
        "CC6/CC7: continuous control operation vs. auditor sample windows",
        "Change and drift evidence from policy audit log + ADM refresh",
        "Customer due-diligence pack from repeatable quarterly exports",
    ],
    "PCI-DSS-v4": [
        "CDE isolation with simulation→enforce — Req 1 evidence at workload tier",
        "Live CDE flow map (Req 1.2.1) from ADM, not annual Visio",
        "CVE + reachability prioritisation for Req 6.3.3",
    ],
    "NIST-800-53": [
        "AC-4 information-flow enforcement with exportable policy artefacts",
        "CA-7 continuous monitoring via inventory, flows, and violations",
        "CM-2/3/8 baseline and change tracking through ADM drift",
    ],
    "ISO-27001-2022": [
        "A.8.20–A.8.22 network segregation with workload-resident enforcement",
        "A.8.16 monitoring evidence from flow + denied-connection logs",
        "Supplier egress reconciliation via observed outbound flows",
    ],
    "CISA-ZeroTrust": [
        "Networks + Applications/Workloads pillar progression with measurable maturity",
        "Observable enforce mode vs. monitor-only baseline",
        "Policy enforcement at workload as ZT PEP placement",
    ],
    "FIPS-140": [
        "Plaintext-protocol DENY policies with violation logs",
        "Programme-level crypto hygiene visibility (modules out of scope)",
        "140-2→140-3 transition tracking on workload connections",
    ],
    "NIST-800-207": [
        "Workload-side evidence for ZTA Tenets 2/3/5/6",
        "PEP placement on workload with policy export for assessors",
        "PIP-style telemetry from process + flow graph",
    ],
    "NIST-800-207A": [
        "CSW Defend as PDP/PEP mapping with traceable components",
        "Telemetry as PIP for cloud-native ZTA architectures",
        "Logical-component evidence for draft 800-207A reviews",
    ],
    "DORA": [
        "Art. 8/9 segmentation + ICT asset inventory from live scope",
        "Art. 19 incident dossier templates from flow/process export",
        "Art. 28 third-party egress from observed outbound flows",
    ],
    "NIS2": [
        "Art. 21(2) risk-management mapping with continuous workload evidence",
        "Art. 23 incident timeline support (24h/72h/1-month)",
        "Art. 21(2)(d) supply-chain egress visibility",
    ],
    "NERC-CIP": [
        "IT-side ESP boundary hardening (CIP-005 R1) — pair with OT tools",
        "IRA evidence inputs (CIP-005 R2) from access logs",
        "CIP-007/010 ports + baseline from process-aware telemetry",
    ],
    "TSA-Pipeline": [
        "IT/OT segmentation evidence (Section III.A) on IT workloads",
        "Access control + monitoring (III.B/C) at workload tier",
        "CIRP/CAP evidence packs from forensic flow export",
    ],
    "CIS-Controls-v8": [
        "Direct evidence on Controls 1, 2, 4, 7, 8, 13",
        "IG2 lead with IG1/IG3 deltas documented in runbook",
        "Asset/software inventory + secure config from agent telemetry",
    ],
    "NIST-CSF-2": [
        "Govern (GV.OV/GV.SC) + ID.AM, PR.IR, DE.CM, RS.AN subcategories",
        "Outcomes wrapper aligned to 800-53 evidence underneath",
        "Continuous vs. periodic evidence for CSF maturity conversations",
    ],
    "CMMC-2": [
        "Level 2 (800-171) AC/AU/CM/RA/SC/SI family evidence",
        "CUI enclave labelling and scope export for SSP inputs",
        "Prepares POA&M items with workload-level gap visibility",
    ],
    "IEC-62443": [
        "Zones & conduits segmentation on IT-side OT boundaries",
        "SR control evidence; pair with Cyber Vision/Claroty for device layer",
        "Jump host and historian path visibility",
    ],
    "GDPR": [
        "Art. 32 security-of-processing from enforcement + logging",
        "Art. 30 RoPA support via data-flow mapping",
        "Art. 33/34 breach timeline from flow search exports",
    ],
    "MITRE-ATTACK": [
        "Technique-level forensic alignment (TA0001–TA0011)",
        "Lateral movement visibility (TA0008) at east-west workload tier",
        "SOC integration guidance for detection/prevention mapping",
    ],
    "FedRAMP": [
        "Moderate baseline AC-4/SC-7/CA-7/SI-4 with ConMon-ready exports",
        "POA&M inputs from gap and drift reports",
        "3PAO assessment preparation artefacts",
    ],
    "SWIFT-CSCF": [
        "SWIFT secure zone isolation with mandatory/advisory mapping",
        "Internet access restriction evidence from deny logs",
        "Operator session integrity via identity-aware paths (where integrated)",
    ],
    "HITRUST-CSF": [
        "Harmonized HIPAA+ISO+NIST+PCI evidence in one scope model",
        "e1/i1/r2 assessment level guidance",
        "Single workload evidence source for multiple inherited controls",
    ],
    "NIST-800-171": [
        "CUI enclave isolation with 03.01/03.13 flow enforcement",
        "CMMC L2 underpinning evidence",
        "800-53 Rev 3 family alignment for assessors",
    ],
    "CSA-CCM": [
        "IVS-09 network security + DSP data isolation",
        "TVM reachability for cloud workload context",
        "STAR certification evidence support",
    ],
    "COBIT-2019": [
        "DSS05.02 network security continuous proof",
        "MEA01/02 conformance monitoring from drift exports",
        "BAI06/10 change evidence from policy audit log",
    ],
    "AU-Essential-Eight": [
        "E2/E6 patch prioritisation via CVE+EPSS+reachability",
        "E5 admin privilege path restriction",
        "ML1–ML3 maturity evidence progression",
    ],
    "UK-Cyber-Essentials": [
        "CE1 workload-level firewall enforcement proof",
        "CE2 secure configuration baseline from agent inventory",
        "CE5 patch management evidence scoped to workloads",
    ],
    "MAS-TRM": [
        "Critical-system segmentation for Singapore financial sector",
        "Outsourcing/third-party egress reconciliation",
        "Incident investigation support from flow exports",
    ],
    "APRA-CPS-234": [
        "Critical information asset visibility",
        "Control testing evidence from simulation/enforce cadence",
        "Service-provider dependency flows",
    ],
    "NY-DFS-23-NYCRR-500": [
        "Covered-system workload visibility",
        "NPI application scope with continuous inventory",
        "Third-party service-provider egress monitoring",
    ],
    "TISAX": [
        "Prototype/confidential engineering workload segmentation",
        "Supplier/customer egress evidence",
        "Assessment-ready export pack",
    ],
    "NIST-800-82": [
        "OT-adjacent IT segmentation (jump hosts, historians, patch repos)",
        "Pair with OT visibility for end-to-end zones",
        "Vendor access path documentation",
    ],
    "BSI-C5": [
        "Cloud service assurance with tenant boundary enforcement",
        "Cloud communication security evidence",
        "Vulnerability and incident artefacts for C5 auditors",
    ],
}


def build_primer(folder: str) -> str:
    bullets = FRAMEWORK_HIGHLIGHTS.get(folder, [
        "Continuous workload inventory and scope membership proof",
        "Behaviour-derived dependency maps replace static diagrams",
        "Simulation→enforce path produces assessor-ready segmentation evidence",
    ])
    highlights = "\n".join(f"- {b}" for b in bullets)

    return f"""
{MARKER}

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

{highlights}

**Compared to manual programmes:** static diagrams and annual firewall samples age immediately; CSW ties evidence to **live workload behaviour** and produces queryable exports on demand — supporting "operating effectively" language in PCI v4.0, SOC 2 CC7, and HIPAA risk analysis.

---
"""


def main():
    root = Path(__file__).resolve().parents[1]
    runbooks = sorted(root.glob("**/*-Reference-Design.md"))
    updated = 0
    skipped = 0

    for path in runbooks:
        text = path.read_text(encoding="utf-8")
        if MARKER in text:
            skipped += 1
            continue

        folder = path.parent.name
        primer = build_primer(folder)

        # Insert after Reader's Guide section (before next ## heading at same level)
        anchor = "**Where to start.**"
        if anchor not in text:
            # fallback: before ## 1. Overview
            anchor = "## 1. Overview"
            if anchor not in text:
                print(f"SKIP (no anchor): {path}")
                continue
            idx = text.index(anchor)
            text = text[:idx] + primer + "\n" + text[idx:]
        else:
            # find end of Reader's Guide (next --- or ## 1.)
            start = text.index(anchor)
            rest = text[start:]
            sep = rest.find("\n---\n")
            if sep == -1:
                sep = rest.find("\n## 1.")
            if sep == -1:
                print(f"SKIP (no section end): {path}")
                continue
            insert_at = start + sep + (5 if rest[sep:sep+5] == "\n---\n" else 0)
            if rest[sep:sep+5] == "\n---\n":
                insert_at = start + sep + 5
            else:
                insert_at = start + sep
            text = text[:insert_at] + primer + text[insert_at:]

        path.write_text(text, encoding="utf-8")
        updated += 1
        print(f"UPDATED: {path.relative_to(root)}")

    print(f"\nDone: {updated} updated, {skipped} already had primer, {len(runbooks)} total")


if __name__ == "__main__":
    main()
