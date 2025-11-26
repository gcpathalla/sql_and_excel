#!/usr/bin/env python3
"""Convert ALL plain text URLs to clickable links with link icon."""

import re

print("Reading source HTML...")
with open('Complete_30Day_Training_Full.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Store original for comparison
original_html = html

# Pattern to find URLs in plain text (not already in href="...")
# We need to avoid URLs that are already part of <a href="...">
def convert_plain_urls(text):
    """Convert plain text URLs to clickable links with icon."""

    # Find all URLs in the text
    url_pattern = r'(?<!href=")(?<!src=")(https?://[^\s<>"]+)'

    def make_link(match):
        url = match.group(0)
        # Clean up URL (remove trailing punctuation that might be part of text)
        url = url.rstrip('.,;:)')

        # Skip if this is in the DOCTYPE or meta tags area
        # We'll handle this by checking context later

        # Create link with external link icon
        return f'<a href="{url}" target="_blank" class="external-link" title="Open link"><svg class="link-icon" width="14" height="14" fill="currentColor" viewBox="0 0 16 16"><path d="M8.636 3.5a.5.5 0 0 0-.5-.5H1.5A1.5 1.5 0 0 0 0 4.5v10A1.5 1.5 0 0 0 1.5 16h10a1.5 1.5 0 0 0 1.5-1.5V7.864a.5.5 0 0 0-1 0V14.5a.5.5 0 0 1-.5.5h-10a.5.5 0 0 1-.5-.5v-10a.5.5 0 0 1 .5-.5h6.636a.5.5 0 0 0 .5-.5z"/><path d="M16 .5a.5.5 0 0 0-.5-.5h-5a.5.5 0 0 0 0 1h3.793L6.146 9.146a.5.5 0 1 0 .708.708L15 1.707V5.5a.5.5 0 0 0 1 0v-5z"/></svg> {url}</a>'

    return re.sub(url_pattern, make_link, text)

# We need to be careful not to convert URLs in:
# 1. <head> section
# 2. Already existing <a href="...">
# 3. DOCTYPE declarations

# Split HTML into head and body
head_match = re.search(r'(<head>.*?</head>)', html, re.DOTALL)
body_match = re.search(r'(<body>.*?</body>)', html, re.DOTALL)

if head_match and body_match:
    head = head_match.group(1)
    body = body_match.group(1)

    # Only convert URLs in body, preserving existing links
    # Split body by existing anchor tags to avoid double-linking
    parts = re.split(r'(<a\s+[^>]*>.*?</a>)', body, flags=re.DOTALL)

    new_parts = []
    for i, part in enumerate(parts):
        if i % 2 == 0:  # Not an anchor tag
            new_parts.append(convert_plain_urls(part))
        else:  # Is an anchor tag, keep as-is
            new_parts.append(part)

    new_body = ''.join(new_parts)

    # Reconstruct HTML
    html = html.replace(body, new_body)

# Count changes
original_urls = len(re.findall(r'(?<!href=")(?<!src=")(https?://[^\s<>"]+)', original_html))
new_urls = len(re.findall(r'class="external-link"', html))

print(f"Converted {new_urls} plain text URLs to clickable links")
print("Each link now has an external link icon")

# Save
with open('Complete_30Day_Training_Full.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ All plain text URLs are now clickable with link icons")
