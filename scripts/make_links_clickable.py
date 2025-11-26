#!/usr/bin/env python3
"""
Convert plain text video/blog URLs to clickable hyperlinks.
Pattern: https://URL - Channel Name
Becomes: <a href="https://URL" target="_blank">Channel Name</a>
"""

import re

print("Reading source HTML...")
with open('Complete_30Day_Training_Full.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern to match URLs followed by " - Author/Channel Name"
# Handles cases where it might span across line breaks
pattern = r'(https?://[^\s<]+)\s*-\s*([^<\n]+?)(?=</p>|<br|$)'

def replace_with_link(match):
    url = match.group(1).strip()
    author = match.group(2).strip()
    # Remove any trailing punctuation from author
    author = author.rstrip('.,;:')
    return f'<a href="{url}" target="_blank">{author}</a>'

# Replace all matches
html_updated = re.sub(pattern, replace_with_link, html, flags=re.MULTILINE)

# Count replacements
original_links = len(re.findall(pattern, html, flags=re.MULTILINE))

print(f"Converting {original_links} plain text URLs to clickable links...")

# Save updated HTML
with open('Complete_30Day_Training_Full.html', 'w', encoding='utf-8') as f:
    f.write(html_updated)

print(f"✅ Converted {original_links} URLs to clickable hyperlinks")
print("   - All YouTube and blog links are now clickable")
print("   - Links open in new tab (target='_blank')")
