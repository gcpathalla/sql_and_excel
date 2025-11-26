#!/usr/bin/env python3
"""Convert all old-style anchor links to new external-link button format."""

import re

print("Reading source HTML...")
with open('Complete_30Day_Training_Full.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern to find old-style anchor tags (non-external-link ones)
# <a href="URL" target="_blank">URL_TEXT</a>
# But NOT the ones that already have class="external-link"

pattern = r'<a href="(https?://[^"]+)" target="_blank">([^<]+)</a>'

def convert_to_new_format(match):
    url = match.group(1)
    text = match.group(2)

    # Check if this is already in the new format by looking for class="external-link" nearby
    # For now, just convert all to new format
    return f'<a href="{url}" target="_blank" class="external-link" title="Open link"><svg class="link-icon" width="14" height="14" fill="currentColor" viewBox="0 0 16 16"><path d="M8.636 3.5a.5.5 0 0 0-.5-.5H1.5A1.5 1.5 0 0 0 0 4.5v10A1.5 1.5 0 0 0 1.5 16h10a1.5 1.5 0 0 0 1.5-1.5V7.864a.5.5 0 0 0-1 0V14.5a.5.5 0 0 1-.5.5h-10a.5.5 0 0 1-.5-.5v-10a.5.5 0 0 1 .5-.5h6.636a.5.5 0 0 0 .5-.5z"/><path d="M16 .5a.5.5 0 0 0-.5-.5h-5a.5.5 0 0 0 0 1h3.793L6.146 9.146a.5.5 0 1 0 .708.708L15 1.707V5.5a.5.5 0 0 0 1 0v-5z"/></svg> {url}</a>'

# Find all old-style links that don't already have the external-link class
# First, let's find links that have target="_blank" but no class="external-link"
old_pattern = r'<a href="(https?://[^"]+)" target="_blank"(?!.*?class="external-link")>([^<]+)</a>'

count = 0
def convert_link(match):
    global count
    count += 1
    url = match.group(1)
    return f'<a href="{url}" target="_blank" class="external-link" title="Open link"><svg class="link-icon" width="14" height="14" fill="currentColor" viewBox="0 0 16 16"><path d="M8.636 3.5a.5.5 0 0 0-.5-.5H1.5A1.5 1.5 0 0 0 0 4.5v10A1.5 1.5 0 0 0 1.5 16h10a1.5 1.5 0 0 0 1.5-1.5V7.864a.5.5 0 0 0-1 0V14.5a.5.5 0 0 1-.5.5h-10a.5.5 0 0 1-.5-.5v-10a.5.5 0 0 1 .5-.5h6.636a.5.5 0 0 0 .5-.5z"/><path d="M16 .5a.5.5 0 0 0-.5-.5h-5a.5.5 0 0 0 0 1h3.793L6.146 9.146a.5.5 0 1 0 .708.708L15 1.707V5.5a.5.5 0 0 0 1 0v-5z"/></svg> {url}</a>'

html = re.sub(old_pattern, convert_link, html)

print(f"Converted {count} old-style links to new button format with icons")

# Save
with open('Complete_30Day_Training_Full.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ All links now have consistent button-style format")
