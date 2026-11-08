# -*- coding: utf-8 -*-
import os
import re

workspace_dir = "/Users/ricksabchez/workspace/projects/autoplazaterhan.github.io"

# 1. Read index.html
with open(os.path.join(workspace_dir, "index.html"), "r", encoding="utf-8") as f:
    index_raw = f.read()

lines = index_raw.splitlines(True)

# Slices of each section in index.html (1-indexed line numbers)
clean_ranges = {
    "posts": (654, 15849),
    "timeline": (15852, 18879),
    "platforms": (18882, 18965),
    "campaigns": (18968, 19151),
    "critiques": (19155, 19319),
    "news": (19326, 21038),
    "broadcast": (21043, 21213),
    "specs": (21216, 21241),
    "rawpdf": (21244, 21276),
    "faq": (21279, 21387),
    "investigation": (21390, 21477),
    "audio-sentiment": (21485, 22221),
    "influencers": (22224, 25588),
    "production": (25593, 25692),
    "hashtags": (25696, 25929),
    "ai-audit": (25934, 26221),
    "market-guild": (26226, 26369)
}

# Verify slices
extracted_sections = {}
for sid, (start, end) in clean_ranges.items():
    sec_content = "".join(lines[start-1:end])
    # Remove 'hidden' class from section tag for standalone pages
    sec_content_clean = re.sub(r'(<section[^>]*class="[^"]*)hidden([^"]*")', r'', sec_content, count=1)
    extracted_sections[sid] = sec_content_clean

print(f"Extracted {len(extracted_sections)} clean section contents.")
