# Audience and usage guide

> Companion to the
> [CSW Compliance Mapping repository](../README.md). Everything in
> this page is about *how to navigate* the assets — who should lead
> with which document, when to pick the reference design vs the report, which
> file format to share, and where to find things in the folder tree.

## Audience guide

| Audience | Lead with | Key takeaway |
|---|---|---|
| **CISO / Security leadership** | The PDF report's executive summary and the *Compliance Posture Summary* table | CSW collapses several manual evidence-gathering programs (segmentation reviews, change attestation, drift tracking) into continuous, query-able state. |
| **Security architect** | The full PDF report's control-by-control mapping | Where CSW can contribute to control evidence (agent telemetry, policy enforcement, conversation graph, forensic flows) and what gaps remain to be designed around. |
| **Compliance / GRC team** | The *Audit Evidence* and *Gap Analysis* sections in the PDF | Which CSW reports, exports, and dashboards can become candidate auditor-review artefacts, and what supplementary attestation language to use. |
| **Operations / SRE / DevSecOps** | The Markdown reference design | Concrete configuration steps, policy patterns, and "what to show the auditor on day 1" playbooks. |
| **You already have firewalls and EDR** | The reference designs and the 800-207 / 207A reports | Workload-resident telemetry and identity-aware segmentation address many evidence questions about *process-to-process* and *intra-host East–West* flows that perimeter and endpoint controls usually see only partially. The frameworks below spell out which obligations sit in that gap — and which still require other tools. |

## How to get the most out of this repo

Whether you found this from a search for a specific control, were
pointed here by your Cisco account team, or are doing a broader
evaluation, here's a way to navigate the material that respects your
time:

0. **If you are new to CSW, read the
   [Compliance evidence playbook](./compliance-evidence-playbook.md)
   first.** It explains CSW console areas, Monitor→Simulation→Enforce,
   and a universal 4-phase evidence programme before you dive into
   framework-specific control IDs.
1. **Open the framework that's actually on your roadmap.** The one tied
   to a current audit, a customer contractual ask, or board-level
   pressure. Skimming all thirty-four will dilute the signal — pick one
   and stay with it.
2. **Start with the reference design (`*-Reference-Design.md` in the
   same folder).** Each reference design now includes a **CSW primer**, **universal
   evidence workflow checklists**, and **framework-specific CSW effectiveness**
   highlights at the top — then the detailed phased deployment for that
   standard. It shows the *how*: sensor deployment phases, policy
   patterns, evidence collection cadence, and typical proof points to
   validate with your auditor or assessor. If the reference design's level of detail looks
   plausible for your environment, that's the strongest signal that the
   mapping is real and not marketing — and it's the right place to
   stress-test scope before investing in a wider read.
3. **Then read the matching report.** Use it to explain how CSW can
   contribute evidence, where customer-owned or complementary controls
   remain necessary, and which scope assumptions must be validated.
   Do not interpret the report as a compliance attestation or a claim
   that CSW alone fully addresses a control family.
4. **Once you've grounded the conversation in compliance language, read
   the NIST 800-207 and 800-207A reports.** These shift the lens from
   *"what do we have to do?"* to *"what does a defensible zero-trust
   architecture actually look like at the workload tier?"* — useful
   even if zero trust isn't your stated initiative, because the same
   patterns underlie most modern compliance frameworks.
5. **When you're ready, ask your Cisco account team for a discovery
   exercise.** Specifically: a short engagement where CSW is deployed
   in a representative slice of your environment and the same evidence
   tables in these reports are populated with *your real workloads,
   your real flows, your real CVEs*. That converts these documents from
   abstract mappings into scope-specific artefacts you can validate with
   auditors and leadership.

## Reference design or report — when to use which

- **Reference design** is the technical foundation everything else rests on. It's
  written for the **security engineers and platform owners actually doing
  the work**: deployment playbooks, CSW configuration steps, sample
  policies, evidence-collection commands, and the auditor-response guidance
  the report cites. If a customer wants to know whether a mapping is real
  or just slideware, the reference design is where they look. Use **Markdown** when
  editing or diff-reviewing in a code editor, **HTML** when reading through
  it in a browser.
- **Report** is the customer-facing narrative built on top of the reference design.
  It's for **leaders, auditors, customers in due diligence, and
  procurement** — explaining how Cisco Secure Workload supports the
  framework, the artefacts produced, and where the boundaries are. Use
  **PDF** for review meetings, **DOCX** when you need to tailor placeholders
  before sharing externally, **HTML** for a link you can drop into
  Slack/email or read on a phone.

## File formats

- **Markdown reference designs** — The technical foundation. Reference for the
  security engineers and platform owners doing the work: deployment
  playbooks, CSW configuration steps, sample policies, and the
  auditor-response guidance the report cites. Markdown for editing or
  diff-reviewing in a code editor; HTML for reading in a browser.
- **DOCX reports** — Customer-facing editable master built on top of the
  reference design. Replace `[Customer Name]` and `[Month Year]` placeholders, and
  tailor the Compliance Posture Summary table to the customer's specific
  scope and deployment stage before sharing externally.
- **PDF reports** — Render of the DOCX for customer review and audit
  conversations; renders natively in the GitHub web UI. Generated from
  the DOCX via LibreOffice; treat the DOCX as the editable master and
  re-generate the PDF after any edits.
- **Generated niche PDFs** — Summary renderings for selected frameworks.
  Use the matching Markdown reference design and editable DOCX as the primary
  engineering/evidence sources; do not submit a simplified generated PDF
  alone as an audit evidence package.
- **HTML** — Browseable, mobile-friendly view for both reference designs and
  reports. Once GitHub Pages is enabled, the same HTML is published at
  `https://chandrapati.github.io/CSW-Compliance-Mapping/` (landing page:
  [`index.html`](../index.html)).

## Folder structure

```
CSW-Compliance-Mapping/
├── README.md            ← compliance-mapping focus, asset library, scope notes
├── INDEX.md             ← control-ID lookup across all frameworks
├── docs/                ← background and navigation pages (this folder)
│   ├── about-csw.md     ← what Cisco Secure Workload actually is
│   ├── compliance-evidence-playbook.md  ← NEW: step-by-step for CSW newcomers
│   ├── why-these-mappings-matter.md
│   └── audience-and-usage.md
├── templates/           ← customer-evidence templates (no customer data)
│   └── evidence-package-manifest.yaml
├── HIPAA/
├── SOC2/
├── PCI-DSS-v4/
├── NIST-800-53/
├── ISO-27001-2022/
├── CISA-ZeroTrust/
├── FIPS-140/
├── NIST-800-207/
├── NIST-800-207A/
├── DORA/                ← EU financial sector
├── NIS2/                ← EU essential & important entities
├── NERC-CIP/            ← North American bulk electric system (IT side)
├── TSA-Pipeline/        ← TSA-designated natural gas / oil pipelines (IT side)
├── CIS-Controls-v8/     ← CIS Critical Security Controls v8.1 (IG2 lead)
├── NIST-CSF-2/          ← NIST Cybersecurity Framework 2.0 (Govern + 5 functions)
├── CMMC-2/              ← CMMC 2.0 (Level 2 lead, with L1 / L3 deltas)
└── …                    ← 18 additional framework folders; see README
```

Every framework folder follows the same shape: a Markdown technical
reference design, a DOCX (editable master) and PDF (review render) of the
customer-facing report, and HTML versions of both built by
[`.html-tools/build-html.py`](../.html-tools/build-html.py).

---

**See also**

- [Background — What is Cisco Secure Workload?](./about-csw.md)
- [Why these mappings matter](./why-these-mappings-matter.md)
- [Governance and Evidence Standards](./governance-and-evidence-standards.md)
- [Repository README](../README.md) — asset library, scope notes, and
  disclaimer.
