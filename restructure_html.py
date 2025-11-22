#!/usr/bin/env python3
"""
Restructure the single-page 30-Day Training HTML into multiple pages:
- index.html (main page with intro and overview)
- week1.html through week6.html (week summaries and links to days)
- day1.html through day30.html (individual day content)
"""

from bs4 import BeautifulSoup
import re
import os

# Read the original HTML file
with open('Complete_30Day_Training_Full.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Extract the head section (CSS and JS)
head_content = str(soup.find('head'))

# Extract the header
header_content = str(soup.find('header', id='title-block-header'))

# Extract all scripts at the end
scripts = soup.find_all('script')
end_scripts = '\n'.join([str(script) for script in scripts])

# Find the main content div
content_div = soup.find('div', class_='content')

def create_html_page(title, toc_html, content_html, current_page=''):
    """Create a complete HTML page with the given content"""
    return f'''<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">
{head_content.replace('<title>30-Day Excel &amp; SQL Training Plan - Complete Guide</title>', f'<title>{title}</title>')}
<body>
{header_content.replace('<h1 class="title">30-Day Excel &amp; SQL Training Plan - Complete Guide</h1>', f'<h1 class="title">{title}</h1>')}
<div class="page">
  <nav id="TOC" role="doc-toc">
{toc_html}
  </nav>
  <div class="dragbar" id="dragbar" aria-hidden="true"></div>
  <div class="content">
{content_html}
    <a href="#top" class="back-to-top">↑ Back to Top</a>
  </div>
</div>
{end_scripts}
</body>
</html>'''

def build_toc(current_page='index'):
    """Build the TOC for navigation with proper links"""
    toc_items = []

    # Main overview link
    toc_items.append('<ul>')
    toc_items.append('<li><a href="index.html">30-DAY EXCEL &amp; SQL TRAINING PLAN</a>')
    toc_items.append('<ul>')
    toc_items.append('<li><a href="index.html#how-to-use-this-plan">📖 HOW TO USE THIS PLAN</a></li>')
    toc_items.append('<li><a href="index.html#program-overview">PROGRAM OVERVIEW</a></li>')
    toc_items.append('</ul>')
    toc_items.append('</li>')

    # Week and day structure
    weeks = [
        ("WEEK 1: FOUNDATIONS", "week1.html", [1, 2, 3, 4, 5]),
        ("WEEK 2: DATA ANALYSIS FUNDAMENTALS", "week2.html", [6, 7, 8, 9, 10]),
        ("WEEK 3: INTERMEDIATE CONCEPTS", "week3.html", [11, 12, 13, 14, 15]),
        ("WEEK 4: ADVANCED CONCEPTS", "week4.html", [16, 17, 18, 19, 20]),
        ("WEEK 5: ANALYTICS &amp; OPTIMIZATION", "week5.html", [21, 22, 23, 24, 25]),
        ("WEEK 6: MASTERY &amp; PROJECTS", "week6.html", [26, 27, 28, 29, 30])
    ]

    day_titles = extract_day_titles()

    for week_name, week_file, days in weeks:
        toc_items.append(f'<li><a href="{week_file}">{week_name}</a>')
        toc_items.append('<ul>')
        for day_num in days:
            day_title = day_titles.get(day_num, f"DAY {day_num}")
            toc_items.append(f'<li><a href="day{day_num}.html">{day_title}</a></li>')
        toc_items.append('</ul>')
        toc_items.append('</li>')

    toc_items.append('</ul>')
    return '\n'.join(toc_items)

def extract_day_titles():
    """Extract day titles from the HTML"""
    day_titles = {}

    # Find all h2 tags with day IDs
    all_h2 = soup.find_all('h2')
    for h2 in all_h2:
        if h2.get('id', '').startswith('day-'):
            text = h2.get_text()
            match = re.match(r'DAY (\d+):', text)
            if match:
                day_num = int(match.group(1))
                day_titles[day_num] = text

    return day_titles

def extract_intro_content():
    """Extract the introduction and overview content for index.html"""
    content = []

    # Find the main h1
    main_h1 = soup.find('h1', id='day-excel-sql-training-plan')
    if main_h1:
        current = main_h1
        while current:
            current = current.find_next_sibling()
            if current and current.name == 'h1' and 'week' in current.get('id', '').lower():
                break
            if current:
                content.append(str(current))

    return '\n'.join(content)

def extract_week_content(week_num):
    """Extract content for a specific week"""
    week_ids = {
        1: 'week-1-foundations',
        2: 'week-2-data-analysis-fundamentals',
        3: 'week-3-intermediate-concepts-days-11-15',
        4: 'week-4-advanced-concepts-days-16-20',
        5: 'week-5-analytics-optimization-days-21-25',
        6: 'week-6-mastery-projects-days-26-30'
    }

    week_id = week_ids.get(week_num)
    if not week_id:
        return ""

    week_h1 = soup.find('h1', id=week_id)
    if not week_h1:
        return ""

    content = [str(week_h1)]

    # Get content until next week or end
    current = week_h1
    while current:
        current = current.find_next_sibling()
        if current and current.name == 'h1' and current != week_h1:
            break
        if current and current.name == 'h2':
            # This is a day heading, create a link instead
            day_text = current.get_text()
            day_match = re.match(r'DAY (\d+):', day_text)
            if day_match:
                day_num = day_match.group(1)
                content.append(f'<h2><a href="day{day_num}.html">{day_text}</a></h2>')
                # Skip day content, just show the heading
                continue
        if current:
            # Check if it's day content (skip it for week pages)
            if current.name in ['h3', 'h4', 'h5', 'p', 'ul', 'ol', 'div', 'pre', 'blockquote', 'table']:
                # Check if we're inside a day section
                prev_h2 = current.find_previous('h2')
                if prev_h2 and prev_h2.get('id', '').startswith('day-'):
                    continue
            content.append(str(current))

    return '\n'.join(content)

def extract_day_content(day_num):
    """Extract content for a specific day"""
    all_h2 = soup.find_all('h2')
    day_h2 = None

    for h2 in all_h2:
        if h2.get('id', '').startswith('day-'):
            text = h2.get_text()
            match = re.match(rf'DAY {day_num}:', text)
            if match:
                day_h2 = h2
                break

    if not day_h2:
        return f"<h1>DAY {day_num}</h1><p>Content coming soon...</p>"

    content = [str(day_h2)]

    # Get all content until the next day
    current = day_h2
    while current:
        current = current.find_next_sibling()
        # Stop at next day (h2) or next week (h1)
        if current and current.name == 'h2' and current.get('id', '').startswith('day-'):
            break
        if current and current.name == 'h1':
            break
        if current:
            content.append(str(current))

    return '\n'.join(content)

def add_week_summary(week_num, week_content):
    """Add a summary section to week pages with links to days"""
    week_day_ranges = {
        1: (1, 5),
        2: (6, 10),
        3: (11, 15),
        4: (16, 20),
        5: (21, 25),
        6: (26, 30)
    }

    day_start, day_end = week_day_ranges[week_num]
    day_titles = extract_day_titles()

    summary = f'<div class="section-card">\n<h2>Week {week_num} Overview</h2>\n'
    summary += f'<p>This week covers Days {day_start}-{day_end}. Click on any day below to view detailed content.</p>\n'
    summary += '<ul>\n'

    for day_num in range(day_start, day_end + 1):
        day_title = day_titles.get(day_num, f"DAY {day_num}")
        summary += f'<li><a href="day{day_num}.html">{day_title}</a></li>\n'

    summary += '</ul>\n</div>\n'

    return summary + week_content

# Generate index.html
print("Generating index.html...")
intro_content = extract_intro_content()
toc = build_toc('index')
index_html = create_html_page(
    '30-Day Excel &amp; SQL Training Plan - Complete Guide',
    toc,
    intro_content,
    'index'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

# Generate week pages
for week_num in range(1, 7):
    print(f"Generating week{week_num}.html...")
    week_content = extract_week_content(week_num)
    week_content_with_summary = add_week_summary(week_num, week_content)
    toc = build_toc(f'week{week_num}')

    week_titles = {
        1: "WEEK 1: FOUNDATIONS",
        2: "WEEK 2: DATA ANALYSIS FUNDAMENTALS",
        3: "WEEK 3: INTERMEDIATE CONCEPTS",
        4: "WEEK 4: ADVANCED CONCEPTS",
        5: "WEEK 5: ANALYTICS &amp; OPTIMIZATION",
        6: "WEEK 6: MASTERY &amp; PROJECTS"
    }

    week_html = create_html_page(
        week_titles[week_num],
        toc,
        week_content_with_summary,
        f'week{week_num}'
    )

    with open(f'week{week_num}.html', 'w', encoding='utf-8') as f:
        f.write(week_html)

# Generate day pages
for day_num in range(1, 31):
    print(f"Generating day{day_num}.html...")
    day_content = extract_day_content(day_num)
    toc = build_toc(f'day{day_num}')

    day_titles = extract_day_titles()
    day_title = day_titles.get(day_num, f"DAY {day_num}")

    day_html = create_html_page(
        day_title,
        toc,
        day_content,
        f'day{day_num}'
    )

    with open(f'day{day_num}.html', 'w', encoding='utf-8') as f:
        f.write(day_html)

print("\n✅ Done! Generated:")
print("  - 1 index.html (main page)")
print("  - 6 week pages (week1.html - week6.html)")
print("  - 30 day pages (day1.html - day30.html)")
print("\nAll pages maintain the same styling and TOC navigation.")
