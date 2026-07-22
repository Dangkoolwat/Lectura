#!/usr/bin/env python3
"""
Lectura Security Pre-commit Secret Scanner
Scans files or git staged changes for sensitive keys, API tokens, and credentials.
"""

import os
import sys
import re
import subprocess
from pathlib import Path

# Secret patterns to detect
SECRET_PATTERNS = [
    (re.compile(r"nvapi-[a-zA-Z0-9\-_]{20,}"), "NVIDIA API Key"),
    (re.compile(r"sk-[a-zA-Z0-9]{20,}"), "OpenAI / Secret API Key"),
    (re.compile(r"AIzaSy[a-zA-Z0-9\-_]{33}"), "Google Gemini / Firebase API Key"),
    (re.compile(r"ghp_[a-zA-Z0-9]{36}"), "GitHub Personal Access Token"),
    (re.compile(r"github_pat_[a-zA-Z0-9_]{82}"), "GitHub Fine-grained Token"),
    (re.compile(r"-----BEGIN (RSA|EC|OPENSSH|PRIVATE) KEY-----"), "Private Key File"),
]

EXCLUDE_DIRS = {".git", ".venv", "venv", "__pycache__", "node_modules", "agent-logs"}
EXCLUDE_FILES = {".env", ".env.local", ".env.example", ".DS_Store"}

def scan_content(filename, content):
    findings = []
    lines = content.splitlines()
    for idx, line in enumerate(lines, start=1):
        for pattern, label in SECRET_PATTERNS:
            match = pattern.search(line)
            if match:
                matched_text = match.group(0)
                masked = matched_text[:4] + "..." + matched_text[-4:] if len(matched_text) > 8 else "***"
                findings.append((filename, idx, label, masked))
    return findings

def get_staged_files(repo_root):
    try:
        res = subprocess.run(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
            cwd=repo_root,
            capture_output=True,
            text=True,
            check=True
        )
        files = [f.strip() for f in res.stdout.splitlines() if f.strip()]
        return files
    except Exception:
        return []

def scan_staged_files(repo_root):
    findings = []
    staged_files = get_staged_files(repo_root)
    for rel_path in staged_files:
        if rel_path in EXCLUDE_FILES or Path(rel_path).name in EXCLUDE_FILES:
            continue
        full_path = repo_root / rel_path
        if full_path.is_file():
            try:
                with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                findings.extend(scan_content(rel_path, content))
            except Exception:
                pass
    return findings

def scan_all_workspace(repo_root):
    findings = []
    for root, dirs, files in os.walk(repo_root):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for file_name in files:
            if file_name in EXCLUDE_FILES:
                continue
            full_path = Path(root) / file_name
            rel_path = str(full_path.relative_to(repo_root))
            try:
                with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                findings.extend(scan_content(rel_path, content))
            except Exception:
                pass
    return findings

def main():
    repo_root = Path(__file__).resolve().parent.parent
    staged_only = "--staged" in sys.argv or "--staged-only" in sys.argv

    print(f"[+] Running Lectura Security Secret Scan ({'staged files' if staged_only else 'workspace'})...")

    if staged_only:
        findings = scan_staged_files(repo_root)
    else:
        findings = scan_all_workspace(repo_root)

    if findings:
        print("\n[SECURITY ALERT] Hardcoded secret(s) detected!")
        for file_name, line_num, label, masked in findings:
            print(f"  - File: {file_name}:{line_num} [{label}] -> Found: {masked}")
        print("\n[FAILED] Secret leak prevention triggered. Remove hardcoded keys before committing.")
        sys.exit(1)
    else:
        print("\n[PASS] No hardcoded secrets detected. Security check clean.")
        sys.exit(0)

if __name__ == "__main__":
    main()
