#!/usr/bin/env python3
"""Fetch a job posting URL and print Markdown using skill-local parsers."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[3]
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))


def _pick_markdown(result: Any, field: str) -> str:
    if isinstance(result, str):
        return result
    if not isinstance(result, dict):
        return str(result)
    if result.get("error"):
        raise RuntimeError(str(result["error"]))
    value = result.get(field) or result.get("refined") or result.get("raw")
    if not value:
        raise RuntimeError("No Markdown content returned by parser.")
    return str(value)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fetch a job posting URL and print Markdown using skill-local parsers."
    )
    parser.add_argument("url", help="Job posting URL")
    parser.add_argument(
        "--field",
        choices=["refined", "raw", "common_info", "refined_common_info"],
        default="refined",
        help="Result field to print. Defaults to refined.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the full parser result as JSON instead of Markdown.",
    )
    args = parser.parse_args()

    try:
        result = fetch_job_post(args.url)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2, default=str))
        return 0

    print(_pick_markdown(result, args.field))
    return 0


def fetch_job_post(url: str) -> dict[str, Any]:
    from parsers import dynamic, general, jobkorea, samsungcareers, saramin

    if "samsungcareers.com" in url and "/hr/" in url and "no=" in url:
        return samsungcareers.build(url)
    if "jumpit" in url:
        return dynamic.build_jumpit(url)
    if "rallit" in url:
        return dynamic.build_rallit(url)
    if "zighang" in url:
        return dynamic.build_zighang(url)
    if "wanted" in url:
        return dynamic.build_wanted(url)
    if "groupby" in url or "grpby" in url:
        return dynamic.build_groupby(url)
    if "jasoseol" in url:
        return dynamic.build_jasoseol(url)
    if "jobkorea" in url:
        return jobkorea.build(url)
    if "saramin" in url:
        return saramin.build(url)
    return general.build(url)


if __name__ == "__main__":
    raise SystemExit(main())
