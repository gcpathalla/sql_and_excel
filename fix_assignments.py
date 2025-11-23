#!/usr/bin/env python3
"""Fix Daily Assignment formatting - convert from paragraphs to proper HTML lists."""

import re
from bs4 import BeautifulSoup

print("Reading source HTML...")
with open('Complete_30Day_Training_Full.html', 'r', encoding='utf-8') as f:
    content = f.read()

soup = BeautifulSoup(content, 'html.parser')

# Find all Daily Assignment sections
assignment_headings = soup.find_all('h3', string=re.compile(r'Daily Assignment.*:', re.IGNORECASE))

print(f"Found {len(assignment_headings)} Daily Assignment sections")

fixed_count = 0

for heading in assignment_headings:
    # Get the content after this heading
    next_elem = heading.find_next_sibling()

    # Skip if not a paragraph with "Assignment:"
    if not next_elem or next_elem.name != 'p':
        continue

    # Get the assignment content paragraph
    assignment_p = next_elem.find_next_sibling('p')
    if not assignment_p:
        continue

    text = assignment_p.get_text()

    # Check if this needs formatting (has numbered lists or **bold** markdown)
    if '**' in text or (re.search(r'^\d+\.', text, re.MULTILINE)):
        # Convert markdown-style ** to HTML
        html_text = text

        # Replace **text** with <strong>text</strong>
        html_text = re.sub(r'\*\*([^\*]+)\*\*', r'<strong>\1</strong>', html_text)

        # Split by lines and process
        lines = html_text.split('\n')
        new_html = []
        in_list = False
        current_list_items = []

        for line in lines:
            line = line.strip()
            if not line:
                if in_list:
                    # Close current list
                    new_html.append('<ul>')
                    new_html.extend([f'<li>{item}</li>' for item in current_list_items])
                    new_html.append('</ul>')
                    current_list_items = []
                    in_list = False
                continue

            # Check if line starts with number (1., 2., etc.)
            if re.match(r'^\d+\.', line):
                line = re.sub(r'^\d+\.\s*', '', line)
                current_list_items.append(line)
                in_list = True
            # Check if line starts with letter (A), B), etc.)
            elif re.match(r'^[A-Z]\)', line):
                current_list_items.append(line)
                in_list = True
            else:
                if in_list:
                    # Close current list
                    new_html.append('<ul>')
                    new_html.extend([f'<li>{item}</li>' for item in current_list_items])
                    new_html.append('</ul>')
                    current_list_items = []
                    in_list = False

                new_html.append(f'<p>{line}</p>')

        # Close any remaining list
        if in_list and current_list_items:
            new_html.append('<ul>')
            new_html.extend([f'<li>{item}</li>' for item in current_list_items])
            new_html.append('</ul>')

        # Replace the paragraph with new HTML
        new_content = '\n'.join(new_html)
        assignment_p.replace_with(BeautifulSoup(new_content, 'html.parser'))
        fixed_count += 1

print(f"Fixed {fixed_count} assignments")

# Save
with open('Complete_30Day_Training_Full.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("✅ Daily Assignment formatting fixed")
