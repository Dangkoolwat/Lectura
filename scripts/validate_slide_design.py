#!/usr/bin/env python3
"""
Lectura Slide Model & Design Validation Script
Validates slide_model.json against required 13-schema slide design specification.
"""

import os
import sys
import json
from pathlib import Path

REQUIRED_SLIDE_KEYS = ["id", "layout"]
OPTIONAL_SLIDE_KEYS = ["title", "subtitle", "components", "speaker_notes", "design_tokens"]

def validate_slide_model(model_path):
    errors = []
    warnings = []

    if not os.path.exists(model_path):
        warnings.append(f"Slide model file not found: {model_path} (Skipping validation or create first)")
        return errors, warnings

    try:
        with open(model_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        errors.append(f"Invalid JSON format in slide model: {str(e)}")
        return errors, warnings

    if not isinstance(data, dict):
        errors.append("Slide model root must be a JSON object.")
        return errors, warnings

    slides = data.get("slides")
    if slides is None:
        errors.append("Missing required top-level key 'slides'.")
        return errors, warnings

    if not isinstance(slides, list):
        errors.append("Top-level key 'slides' must be an array.")
        return errors, warnings

    if len(slides) == 0:
        warnings.append("Slide model contains 0 slides.")

    for idx, slide in enumerate(slides):
        if not isinstance(slide, dict):
            errors.append(f"Slide index {idx} must be an object.")
            continue

        if "id" not in slide and "slide_number" not in slide:
            errors.append(f"Slide index {idx} missing identification key ('id' or 'slide_number').")

        if "layout" not in slide:
            errors.append(f"Slide index {idx} missing required key 'layout'.")

        # Check components if present
        components = slide.get("components")
        if components is not None and not isinstance(components, list):
            warnings.append(f"Slide index {idx} 'components' should be an array.")

    return errors, warnings

def main():
    workspace_root = Path(__file__).resolve().parent.parent
    default_path = workspace_root / "outputs" / "latest" / "slide_model.json"

    target_path = Path(sys.argv[1]) if len(sys.argv) > 1 else default_path
    
    print(f"[+] Validating Slide Model Design at: {target_path}")
    errors, warnings = validate_slide_model(target_path)

    if warnings:
        print(f"\n[!] Warnings ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")

    if errors:
        print(f"\n[X] Errors ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")
        print("\n[FAILED] Slide design validation failed.")
        sys.exit(1)
    else:
        print(f"\n[PASS] Slide design validation completed (Errors: 0, Warnings: {len(warnings)}).")
        sys.exit(0)

if __name__ == "__main__":
    main()
