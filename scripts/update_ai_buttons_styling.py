#!/usr/bin/env python3
"""
Update AI prompt button styling:
1. Rename 'Quick actions' to 'Ask AI'
2. Update Claude icon to spider-like Anthropic logo
"""

import re

def update_ai_buttons():
    # Read the source HTML file
    with open('Complete_30Day_Training_Full.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Count original occurrences
    original_quick_actions = content.count('quick-actions-label">Ask AI:')
    print(f"Found {original_quick_actions} 'Ask AI' labels (already correct)")

    # Replace 'Quick actions' with 'Ask AI' if any exist
    content = content.replace('quick-actions-label">Quick actions:', 'quick-actions-label">Ask AI:')

    # Updated Claude icon - Anthropic's spider-like logo
    claude_old_icon = '''<svg fill="currentColor" height="14" viewbox="0 0 24 24" width="14">
      <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm0 22C6.486 22 2 17.514 2 12S6.486 2 12 2s10 4.486 10 10-4.486 10-10 10zm-1-17h2v10h-2V5zm0 12h2v2h-2v-2z"></path>
    </svg>'''

    # New Claude spider-like icon (Anthropic logo)
    claude_new_icon = '''<svg fill="currentColor" height="14" viewbox="0 0 24 24" width="14">
      <path d="M14.5 1.5L18 8.5L24 9.5L19.5 14.5L20.5 20.5L14.5 17.5L8.5 20.5L9.5 14.5L5 9.5L11 8.5L14.5 1.5Z"></path>
    </svg>'''

    # Actually, let me use the correct Anthropic Claude icon
    # The Anthropic logo is more complex, but I'll create a simplified version
    claude_correct_icon = '''<svg fill="currentColor" height="14" viewbox="0 0 24 24" width="14">
      <path d="M17.5 3L19 6.5L22.5 8L19 9.5L17.5 13L16 9.5L12.5 8L16 6.5L17.5 3ZM7.5 11L9 14.5L12.5 16L9 17.5L7.5 21L6 17.5L2.5 16L6 14.5L7.5 11ZM14 14L15 16.5L17.5 17.5L15 18.5L14 21L13 18.5L10.5 17.5L13 16.5L14 14Z"></path>
    </svg>'''

    # Count how many Claude icons we need to update
    claude_icon_count = content.count('claude-btn')
    print(f"Found {claude_icon_count} Claude buttons to update icons")

    # Find all Claude button icons and replace them with the new spider-like icon
    # Pattern to match the Claude button's SVG icon
    pattern = r'(<a[^>]*class="ai-quick-btn claude-btn"[^>]*>)\s*<svg[^>]*>.*?</svg>'

    def replace_claude_icon(match):
        return match.group(1) + '\n    ' + claude_correct_icon

    content = re.sub(pattern, replace_claude_icon, content, flags=re.DOTALL)

    # Write the updated content back
    with open('Complete_30Day_Training_Full.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n✅ Updated AI button styling:")
    print(f"   - 'Ask AI' label (already correct)")
    print(f"   - Updated {claude_icon_count} Claude icons to spider-like Anthropic logo")

if __name__ == '__main__':
    print("Updating AI button styling...")
    update_ai_buttons()
