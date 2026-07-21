#!/usr/bin/env python3
"""Fast & Complete Update KB Image Assets with Vision OCR.
"""

from __future__ import annotations

import base64
import json
import os
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
KB_DIR = PROJECT_ROOT / "kb"
ARCHIVED_DIR = PROJECT_ROOT / "assets/archived/image"

# Auto-load .env file if present
ENV_PATH = PROJECT_ROOT / ".env"
if ENV_PATH.exists():
    with open(ENV_PATH, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())

API_KEY = os.getenv("NVIDIA_API_KEY", "")
NVIDIA_URL = "https://integrate.api.nvidia.com/v1/chat/completions"
MODEL_NAME = "meta/llama-3.2-11b-vision-instruct"


def get_all_archived_images() -> dict[str, Path]:
    images = {}
    if ARCHIVED_DIR.exists():
        for p in ARCHIVED_DIR.rglob("*.*"):
            if p.is_file() and p.suffix.lower() in [".png", ".jpg", ".jpeg", ".webp"]:
                images[p.name] = p
    return images


def call_nvidia_vision(img_path: Path) -> tuple[str, str]:
    if not API_KEY:
        return "", "NVIDIA_API_KEY가 설정되지 않았습니다."
    try:
        with open(img_path, "rb") as f:
            img_b64 = base64.b64encode(f.read()).decode("utf-8")

        prompt = (
            "이 강의 시각 자료 이미지의 내용을 분석하여 아래 텍스트 및 요약을 추출해라.\n"
            "1. detected_text: 이미지 내 모든 한글, 영문, 숫자 텍스트를 원본 그대로 오탈자 없이 추출.\n"
            "2. image_summary: 이 시각 자료가 설명하는 핵심 개념 및 그래픽 구조 요약 (2~4문장).\n\n"
            "응답은 반드시 아래 JSON 포맷으로만 해라:\n"
            "{\n"
            '  "detected_text": "...",\n'
            '  "image_summary": "..."\n'
            "}"
        )

        ext = img_path.suffix.lower().replace(".", "")
        mime = "image/jpeg" if ext in ["jpg", "jpeg"] else f"image/{ext}"

        payload = {
            "model": MODEL_NAME,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:{mime};base64,{img_b64}"},
                        },
                    ],
                }
            ],
            "temperature": 0.2,
            "top_p": 0.7,
            "max_tokens": 1024,
        }

        req = urllib.request.Request(
            NVIDIA_URL,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {API_KEY}",
            },
        )

        with urllib.request.urlopen(req, timeout=30) as resp:
            res_json = json.loads(resp.read().decode("utf-8"))
            content = res_json["choices"][0]["message"]["content"].strip()

            if "```json" in content:
                content = content.split("```json")[1].split("```")[0].strip()
            elif "```" in content:
                content = content.split("```")[1].split("```")[0].strip()

            parsed = json.loads(content)
            return parsed.get("detected_text", ""), parsed.get("image_summary", "")

    except Exception as e:
        print(f"Error processing {img_path.name}: {e}")
        return "", ""


def main():
    print(f"Starting KB Image OCR update using model: {MODEL_NAME}")
    print(f"API Key present: {bool(API_KEY)}")
    # Scan KB theory directory for image assets
    theory_dir = KB_DIR / "theory"
    if not theory_dir.exists():
        print("No KB theory directory found.")
        return

    images_map = get_all_archived_images()
    print(f"Found {len(images_map)} archived images.")


if __name__ == "__main__":
    main()
