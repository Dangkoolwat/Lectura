#!/usr/bin/env python3
"""
Lectura Knowledge Base Index & Graph Builder
Scans kb/ directory and builds kb/index.json & kb/graph.json automatically.
"""

import os
import sys
import json
import re
from pathlib import Path

def parse_frontmatter(content):
    frontmatter = {}
    body = content
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
                    val_str = val.strip().strip('"').strip("'")
                    if val_str.startswith("[") and val_str.endswith("]"):
                        items = [i.strip().strip('"').strip("'") for i in val_str[1:-1].split(",") if i.strip()]
                        frontmatter[key.strip()] = items
                    else:
                        frontmatter[key.strip()] = val_str
            body = parts[2]
    return frontmatter, body

def extract_references(content):
    """Extract asset references formatted as [asset_id] or asset_id references."""
    refs = re.findall(r"\[([a-zA-Z0-9_]{5,})\]", content)
    return sorted(list(set(refs)))

def build_kb_index_and_graph(kb_dir):
    nodes = []
    edges = []
    assets_map = {}

    md_files = sorted(list(Path(kb_dir).rglob("*.md")))

    for file_path in md_files:
        rel_path = str(file_path.relative_to(kb_dir))
        if rel_path.startswith("_candidates") or rel_path == "README.md":
            continue

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception:
            continue

        fm, body = parse_frontmatter(content)
        
        # Derive asset ID
        asset_id = fm.get("id") or file_path.stem
        category = fm.get("category") or (rel_path.split(os.sep)[0] if os.sep in rel_path else "general")

        # Derive title
        title = fm.get("title")
        if not title:
            h1_match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
            title = h1_match.group(1).strip() if h1_match else asset_id

        tags = fm.get("tags")
        if isinstance(tags, str):
            tags = [tags]
        elif not isinstance(tags, list):
            tags = []

        references = extract_references(body)
        if asset_id in references:
            references.remove(asset_id)

        asset_entry = {
            "id": asset_id,
            "title": title,
            "category": category,
            "path": rel_path,
            "tags": tags,
            "references": references
        }

        assets_map[asset_id] = asset_entry
        nodes.append({
            "id": asset_id,
            "label": title,
            "category": category
        })

        for ref in references:
            edges.append({
                "source": asset_id,
                "target": ref
            })

    index_data = {
        "version": "1.0",
        "total_assets": len(assets_map),
        "assets": assets_map
    }

    graph_data = {
        "nodes": nodes,
        "edges": edges
    }

    return index_data, graph_data

def main():
    workspace_root = Path(__file__).resolve().parent.parent
    kb_dir = workspace_root / "kb"

    print(f"[+] Building KB Graph & Index for: {kb_dir}")
    index_data, graph_data = build_kb_index_and_graph(kb_dir)

    index_path = kb_dir / "index.json"
    graph_path = kb_dir / "graph.json"

    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)

    with open(graph_path, "w", encoding="utf-8") as f:
        json.dump(graph_data, f, ensure_ascii=False, indent=2)

    print(f"[PASS] Successfully updated {index_path.name} ({index_data['total_assets']} assets) and {graph_path.name}.")

if __name__ == "__main__":
    main()
