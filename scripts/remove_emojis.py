#!/usr/bin/env python3
"""Remove 📺 and 🤖 emojis from content and update headings for elegance."""

print("Reading source HTML...")
with open('Complete_30Day_Training_Full.html', 'r', encoding='utf-8') as f:
    html = f.read()

original_html = html

# Remove TV and robot emojis
html = html.replace('📺 ', '')
html = html.replace(' 📺', '')
html = html.replace('🤖 ', '')
html = html.replace(' 🤖', '')

# Also remove from headings if they're directly in tags
html = html.replace('<strong>📺 ', '<strong>')
html = html.replace('<strong>🤖 ', '<strong>')

# Count changes
tv_count = original_html.count('📺')
robot_count = original_html.count('🤖')

print(f"Removed {tv_count} 📺 TV emojis")
print(f"Removed {robot_count} 🤖 robot emojis")

# Update heading text for elegance
# Change "Recommended Tutorial Videos:" to "Tutorial Videos"
html = html.replace('Recommended Tutorial Videos:', 'Tutorial Videos')
html = html.replace('<strong>Recommended Tutorial Videos:</strong>', '<strong>Tutorial Videos</strong>')

# Change "AI Learning Prompts:" to "AI Learning Prompts"
html = html.replace('AI Learning Prompts:', 'AI Learning Prompts')

print("Updated heading text for elegance")

# Save
with open('Complete_30Day_Training_Full.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✅ Content cleaned and headings improved")
