#!/usr/bin/env python3
"""
Remove all static AI quick action buttons from the source HTML.
These will be replaced with dynamically generated buttons via JavaScript.
"""

import re

def remove_static_ai_buttons():
    # Read the source HTML file
    with open('Complete_30Day_Training_Full.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Count how many button sections exist
    button_count = content.count('<div class="ai-quick-actions">')
    print(f"Found {button_count} static AI quick action button sections to remove")

    # Remove all ai-quick-actions divs and their contents
    # Pattern to match the entire ai-quick-actions div block
    pattern = r'\s*<div class="ai-quick-actions">.*?</div>\s*'

    content = re.sub(pattern, '\n', content, flags=re.DOTALL)

    # Write the updated content back
    with open('Complete_30Day_Training_Full.html', 'w', encoding='utf-8') as f:
        f.write(content)

    # Verify removal
    remaining_count = content.count('<div class="ai-quick-actions">')
    print(f"✅ Removed {button_count} static AI button sections")
    print(f"   Remaining: {remaining_count} (should be 0)")

if __name__ == '__main__':
    print("Removing all static AI quick action buttons...")
    remove_static_ai_buttons()
