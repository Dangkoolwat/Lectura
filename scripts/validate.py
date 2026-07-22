#!/usr/bin/env python3
"""
Lectura KB Validation Script
Checks knowledge base integrity, markdown frontmatter/structure, and JSON index files.
"""

import os
import sys
import json
import re
from pathlib import Path

def parse_frontmatter(content):
    """Simple parser for YAML frontmatter without external dependencies."""
    frontmatter = {}
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            yaml_text = parts[1]
            for line in yaml_text.splitlines():
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if ":" in line:
                    key, val = line.split(":", 1)
                    frontmatter[key.strip()] = val.strip().strip('"').strip("'")
            body = parts[2]
            return frontmatter, body
    return frontmatter, content

def validate_kb(kb_dir):
    errors = []
    warnings = []
    
    if not os.path.exists(kb_dir):
        errors.append(f"KB directory not found: {kb_dir}")
        return errors, warnings

    # Check index.json and graph.json if present
    for json_name in ["index.json", "graph.json"]:
        json_path = os.path.join(kb_dir, json_name)
        if os.path.exists(json_path):
            try:
                with open(json_path, "r", encoding="utf-8") as f:
                    json.load(f)
            except Exception as e:
                errors.append(f"Invalid JSON format in {json_name}: {str(e)}")
        else:
            warnings.append(f"Index file missing: {json_name}")

    # Scan markdown files
    md_files = list(Path(kb_dir).rglob("*.md"))
    if not md_files:
        warnings.append(f"No markdown files found under {kb_dir}")

    for file_path in md_files:
        rel_path = str(file_path.relative_to(kb_dir))
        
        # Skip certain internal/candidate files if needed
        if rel_path.startswith("_candidates"):
            continue

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            if not content.strip():
                errors.append(f"Empty markdown file: {rel_path}")
                continue

            fm, body = parse_frontmatter(content)
            
            # Check for title either in frontmatter or in markdown H1
            has_fm_title = bool(fm.get("title"))
            has_h1_title = bool(re.search(r"^#\s+.+", body, re.MULTILINE))

            if not (has_fm_title or has_h1_title):
                warnings.append(f"Missing title or H1 heading in: {rel_path}")

        except Exception as e:
            errors.append(f"Error reading {rel_path}: {str(e)}")

    return errors, warnings

def main():
    workspace_root = Path(__file__).resolve().parent.parent
    kb_dir = workspace_root / "kb"
    
    print(f"[+] Validating Lectura Knowledge Base at: {kb_dir}")
    errors, warnings = validate_kb(kb_dir)

    if warnings:
        print(f"\n[!] Warnings ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")

    if errors:
        print(f"\n[X] Errors ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")
        print("\n[FAILED] Validation failed with errors.")
        sys.exit(1)
    else:
        print(f"\n[PASS] Validation completed successfully (Errors: 0, Warnings: {len(warnings)}).")
        sys.exit(0)

if __name__ == "__main__":
    main()
