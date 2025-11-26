#!/usr/bin/env python3
"""Scan for plain text URLs that aren't wrapped in anchor tags."""

import re

print("Reading source HTML...")
with open('Complete_30Day_Training_Full.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find URLs that are NOT already in anchor tags
# Pattern: URL that is not preceded by href=" and not followed by "
# This will find plain text URLs

# Split by <a href to separate linked vs unlinked content
parts = re.split(r'<a\s+href="([^"]+)"[^>]*>([^<]+)</a>', html)

plain_text_urls = []
for i, part in enumerate(parts):
    # Skip the href and text parts (they're already linked)
    if i % 3 == 0:
        # Find URLs in plain text
        urls = re.findall(r'https?://[^\s<>"]+', part)
        for url in urls:
            # Check if this URL is truly plain text (not in any tag)
            context_start = max(0, part.find(url) - 50)
            context_end = min(len(part), part.find(url) + len(url) + 50)
            context = part[context_start:context_end]

            if url not in plain_text_urls:
                plain_text_urls.append({
                    'url': url,
                    'context': context.strip()
                })

print(f"\n Found {len(plain_text_urls)} plain text URLs (not clickable)")
print("\nFirst 10 examples:")
for i, item in enumerate(plain_text_urls[:10]):
    print(f"\n{i+1}. {item['url']}")
    print(f"   Context: {item['context'][:80]}...")

print(f"\n✅ Scan complete - {len(plain_text_urls)} URLs need to be made clickable")
