#!/usr/bin/env python3
"""Change hyperlink text from author names to actual URLs."""

import re

print("Reading source HTML...")
with open('Complete_30Day_Training_Full.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern to find links with href and text
# <a href="URL" target="_blank">AUTHOR_NAME</a>
# Replace with:
# <a href="URL" target="_blank">URL</a>

pattern = r'<a href="(https?://[^"]+)" target="_blank">([^<]+)</a>'

def replace_link(match):
    url = match.group(1)
    # Return the link with URL as the text
    return f'<a href="{url}" target="_blank">{url}</a>'

# Replace all matches
html_new = re.sub(pattern, replace_link, html)

# Count changes
original_count = len(re.findall(pattern, html))

print(f"Updated {original_count} hyperlinks to show URLs instead of author names")

# Save
with open('Complete_30Day_Training_Full.html', 'w', encoding='utf-8') as f:
    f.write(html_new)

print("✅ All hyperlinks now show direct URLs")
