#!/usr/bin/env python3
"""
Fix all issues:
1. Add proper week headings for weeks 3-6
2. Fix assignment formatting in days 11-30
3. Update design with all requested features
"""

import re

# Read source HTML
print("Reading source HTML...")
with open('Complete_30Day_Training_Full.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add proper week headings
print("Adding week headings...")

# Week 3 heading
week3_marker = '<!-- WEEK 3: INTERMEDIATE CONCEPTS -->'
week3_heading = '''<h1 id="week-3-intermediate-concepts">WEEK 3: INTERMEDIATE CONCEPTS</h1>
<hr />
<p><strong>Focus:</strong> Date functions, window functions, what-if analysis, and Power Query basics.</p>
<p><strong>Days 11-15:</strong> Building on fundamentals with more advanced Excel and SQL techniques.</p>
<hr />
'''
html = html.replace(week3_marker, week3_heading)

# Find where Day 16 starts and add Week 4 heading
day16_marker = '<h2 id="day-16'
if day16_marker in html:
    pos = html.find(day16_marker)
    week4_heading = '''<h1 id="week-4-advanced-concepts">WEEK 4: ADVANCED CONCEPTS</h1>
<hr />
<p><strong>Focus:</strong> CTEs, Power Pivot, CASE statements, dashboards, and database optimization.</p>
<p><strong>Days 16-20:</strong> Advanced techniques for professional data analysis.</p>
<hr />

'''
    html = html[:pos] + week4_heading + html[pos:]

# Find where Day 21 starts and add Week 5 heading
day21_marker = '<h2 id="day-21'
if day21_marker in html:
    pos = html.find(day21_marker)
    week5_heading = '''<h1 id="week-5-analytics-optimization">WEEK 5: ANALYTICS & OPTIMIZATION</h1>
<hr />
<p><strong>Focus:</strong> Statistical analysis, advanced aggregations, performance tuning, and integration.</p>
<p><strong>Days 21-25:</strong> Professional-level analytics and optimization techniques.</p>
<hr />

'''
    html = html[:pos] + week5_heading + html[pos:]

# Find where Day 26 starts and add Week 6 heading
day26_marker = '<h2 id="day-26'
if day26_marker in html:
    pos = html.find(day26_marker)
    week6_heading = '''<h1 id="week-6-mastery-projects">WEEK 6: MASTERY & PROJECTS</h1>
<hr />
<p><strong>Focus:</strong> Automation, advanced analytics, dashboards, and final comprehensive project.</p>
<p><strong>Days 26-30:</strong> Mastery-level skills and portfolio-ready projects.</p>
<hr />

'''
    html = html[:pos] + week6_heading + html[pos:]

# 2. Fix assignment formatting - convert numbered items to proper lists
print("Fixing assignment formatting...")

# Pattern to find assignment sections with numbered items
def fix_assignment_formatting(match):
    content = match.group(1)

    # If it contains numbered items like "1. **Something:**"
    if re.search(r'\d+\.\s+\*\*', content):
        # Split by numbered items
        items = re.split(r'(\d+\.\s+\*\*[^:]+:\*\*)', content)

        # Rebuild as list
        result_parts = []
        for i, item in enumerate(items):
            if re.match(r'\d+\.\s+\*\*', item):
                # This is a list item header
                result_parts.append('<li>' + item)
            elif item.strip() and i > 0:
                # This is the content of the list item
                result_parts.append(item + '</li>')

        if result_parts:
            return '<p><strong>Assignment:</strong></p>\n<ul>\n' + '\n'.join(result_parts) + '\n</ul>'

    return match.group(0)

# Find and fix assignment sections (Days 11-30)
pattern = r'<p><strong>Assignment:</strong></p>\s*<p>([^<]+(?:<[^>]+>[^<]*</[^>]+>)*[^<]*)</p>'
# This is complex, so let's use a simpler approach

# Find all assignment paragraphs and fix them
for day_num in range(11, 31):
    # Find assignment section for this day
    assignment_pattern = rf'(<h3 id="daily-assignment-hour-4---60-min-{day_num}">.*?</h3>)(.*?)(<h3|<hr)'

    def fix_day_assignment(m):
        heading = m.group(1)
        content = m.group(2)
        next_section = m.group(3)

        # Check if content has numbered items
        if re.search(r'\d+\.\s+\*\*', content):
            # Extract the assignment intro
            intro_match = re.search(r'(<p><strong>Assignment:.*?</strong></p>)', content)
            intro = intro_match.group(1) if intro_match else '<p><strong>Assignment:</strong></p>'

            # Extract numbered items
            items = re.findall(r'\d+\.\s+\*\*([^:]+):\*\*([^0-9]+?)(?=\d+\.\s+\*\*|$)', content, re.DOTALL)

            if items:
                list_html = '<ul>\n'
                for title, desc in items:
                    list_html += f'<li><strong>{title.strip()}:</strong>{desc.strip()}</li>\n'
                list_html += '</ul>'

                # Keep any requirements section
                req_match = re.search(r'(<p><strong>Requirements:.*?</p>.*?)(?=<h3|<hr|$)', content, re.DOTALL)
                req_section = req_match.group(1) if req_match else ''

                return heading + '\n' + intro + '\n' + list_html + '\n' + req_section + '\n' + next_section

        return m.group(0)

    html = re.sub(assignment_pattern, fix_day_assignment, html, flags=re.DOTALL)

# Save updated HTML
print("Saving updated HTML...")
with open('Complete_30Day_Training_Full.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\n✅ Source HTML updated:")
print("  - Added week headings for weeks 3-6")
print("  - Fixed assignment formatting for days 11-30")
