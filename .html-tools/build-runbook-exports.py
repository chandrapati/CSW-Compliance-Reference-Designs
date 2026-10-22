#!/usr/bin/env python3
"""
Build DOCX and PDF from Markdown runbooks and shared docs.

Usage:
    python3 .html-tools/build-runbook-exports.py

Requires: pandoc, LibreOffice (soffice) for PDF conversion from DOCX.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Shared docs (in addition to all *-Reference-Design.md)
EXTRA_MD = [
    ROOT / "docs/compliance-evidence-playbook.md",
]


def md_sources() -> list[Path]:
    sources = sorted(ROOT.glob("**/*-Reference-Design.md"))
    sources.extend(p for p in EXTRA_MD if p.exists())
    return sources


def run_pandoc_docx(src: Path) -> Path:
    out = src.with_suffix(".docx")
    cmd = [
        "pandoc",
        str(src),
        "--from", "gfm",
        "--to", "docx",
        "--toc",
        "--toc-depth=3",
        "-o", str(out),
    ]
    subprocess.run(cmd, check=True, cwd=ROOT)
    return out


def run_soffice_pdf(docx: Path) -> Path:
    out = docx.with_suffix(".pdf")
    cmd = [
        "soffice",
        "--headless",
        "--convert-to", "pdf",
        "--outdir", str(docx.parent),
        str(docx),
    ]
    subprocess.run(cmd, check=True)
    if not out.exists():
        raise FileNotFoundError(f"PDF not created: {out}")
    return out


def main() -> int:
    if not shutil_which("pandoc"):
        print("ERROR: pandoc not found", file=sys.stderr)
        return 1
    if not shutil_which("soffice"):
        print("ERROR: soffice (LibreOffice) not found", file=sys.stderr)
        return 1

    sources = md_sources()
    print(f"Building DOCX + PDF for {len(sources)} markdown files...\n")

    ok = 0
    for src in sources:
        rel = src.relative_to(ROOT)
        print(f"  {rel}")
        try:
            docx = run_pandoc_docx(src)
            pdf = run_soffice_pdf(docx)
            print(f"    -> {docx.name}, {pdf.name}")
            ok += 1
        except subprocess.CalledProcessError as exc:
            print(f"    FAILED: {exc}", file=sys.stderr)

    print(f"\nDone: {ok}/{len(sources)} succeeded")
    return 0 if ok == len(sources) else 1


def shutil_which(cmd: str) -> bool:
    import shutil
    return shutil.which(cmd) is not None


if __name__ == "__main__":
    raise SystemExit(main())
