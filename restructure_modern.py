#!/usr/bin/env python3
"""
Restructure with modern Anthropic-inspired design and organized folder structure
"""

from bs4 import BeautifulSoup
import re
import os
import shutil
from pathlib import Path

# Create pages directory
pages_dir = Path('pages')
pages_dir.mkdir(exist_ok=True)

# Read the original HTML file
with open('Complete_30Day_Training_Full.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Modern Anthropic-inspired head section with updated styling
modern_head_template = '''<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">

  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    
    :root {
      /* Light theme (default - Claude style) */
      --bg-primary: #F5F3EF;
      --bg-secondary: #FFFFFF;
      --bg-sidebar: #FDFCFA;
      --text-primary: #1A1A1A;
      --text-secondary: #6B6B6B;
      --text-tertiary: #9B9B9B;
      --accent-orange: #D97757;
      --accent-brown: #8B6B47;
      --border-subtle: #E5E2DC;
      --border-light: #F0EDE7;
      --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.05);
      --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.07);
      --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
      --radius-sm: 6px;
      --radius-md: 10px;
      --radius-lg: 16px;
    }

    [data-theme="dark"] {
      /* Dark theme (Claude desktop style) */
      --bg-primary: #1F1F1F;
      --bg-secondary: #2B2B2B;
      --bg-sidebar: #242424;
      --text-primary: #ECECEC;
      --text-secondary: #A8A8A8;
      --text-tertiary: #7A7A7A;
      --accent-orange: #E89A7A;
      --accent-brown: #B8936A;
      --border-subtle: #3A3A3A;
      --border-light: #333333;
      --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.3);
      --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.4);
      --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.5);
    }

    html, body {
      height: 100%;
      background: var(--bg-primary);
      color: var(--text-primary);
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      font-size: 16px;
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    /* Header */
    #title-block-header {
      background: var(--bg-secondary);
      border-bottom: 1px solid var(--border-subtle);
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(10px);
      background: rgba(255, 255, 255, 0.95);
    }

    .header-row {
      max-width: 1400px;
      margin: 0 auto;
      padding: 1rem 2rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1.5rem;
    }

    .title {
      font-size: 1.25rem;
      font-weight: 600;
      color: var(--text-primary);
      letter-spacing: -0.01em;
    }

    .header-controls {
      display: flex;
      gap: 0.5rem;
      align-items: center;
    }


    .theme-toggle {
      background: var(--bg-primary);
      border: 1px solid var(--border-subtle);
      color: var(--text-secondary);
      padding: 0.5rem 0.875rem;
      border-radius: var(--radius-sm);
      cursor: pointer;
      font-size: 0.875rem;
      font-weight: 500;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .theme-toggle:hover {
      background: var(--bg-secondary);
      border-color: var(--accent-brown);
      color: var(--text-primary);
    }

    .button {
      background: var(--bg-primary);
      color: var(--text-secondary);
      border: 1px solid var(--border-subtle);
      padding: 0.5rem 0.875rem;
      border-radius: var(--radius-sm);
      font-size: 0.875rem;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .button:hover {
      background: var(--bg-secondary);
      border-color: var(--accent-brown);
      color: var(--text-primary);
      transform: translateY(-1px);
      box-shadow: var(--shadow-sm);
    }

    /* Layout */
    .page {
      max-width: 1400px;
      margin: 0 auto;
      display: flex;
      gap: 2rem;
      padding: 2rem;
      min-height: calc(100vh - 80px);
    }

    /* Modern Sidebar */
    nav#TOC {
      width: 320px;
      min-width: 320px;
      background: var(--bg-sidebar);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-lg);
      padding: 1.5rem;
      align-self: flex-start;
      position: sticky;
      top: 100px;
      max-height: calc(100vh - 120px);
      overflow-y: auto;
      box-shadow: var(--shadow-sm);
      scroll-behavior: smooth;
    }

    nav#TOC::-webkit-scrollbar {
      width: 6px;
    }

    nav#TOC::-webkit-scrollbar-track {
      background: transparent;
    }

    nav#TOC::-webkit-scrollbar-thumb {
      background: var(--border-subtle);
      border-radius: 3px;
    }

    nav#TOC::-webkit-scrollbar-thumb:hover {
      background: var(--accent-brown);
    }

    nav#TOC ul {
      list-style: none;
      padding: 0;
      margin: 0;
    }

    nav#TOC > ul > li {
      margin-bottom: 1.5rem;
    }

    nav#TOC li {
      margin: 0;
    }

    nav#TOC a {
      display: block;
      color: var(--text-secondary);
      text-decoration: none;
      padding: 0.5rem 0.75rem;
      border-radius: var(--radius-sm);
      font-size: 0.8125rem;
      font-weight: 500;
      transition: all 0.2s ease;
      line-height: 1.4;
    }

    nav#TOC > ul > li > a {
      font-weight: 600;
      color: var(--text-primary);
      font-size: 0.875rem;
      margin-bottom: 0.5rem;
    }

    nav#TOC a:hover {
      background: var(--bg-secondary);
      color: var(--accent-orange);
      transform: translateX(2px);
    }

    /* Active page highlighting */
    nav#TOC a.active {
      background: var(--accent-orange);
      color: white;
      font-weight: 600;
    }

    nav#TOC a.active:hover {
      background: var(--accent-brown);
      color: white;
    }

    nav#TOC ul ul {
      margin-top: 0.25rem;
      margin-left: 0.75rem;
      padding-left: 0.75rem;
      border-left: 2px solid var(--border-light);
    }

    /* Content Area */
    .content {
      flex: 1;
      min-width: 0;
      background: var(--bg-secondary);
      border-radius: var(--radius-lg);
      padding: 3rem;
      box-shadow: var(--shadow-sm);
    }

    /* Typography */
    h1 {
      font-size: 2.25rem;
      font-weight: 700;
      color: var(--text-primary);
      letter-spacing: -0.02em;
      margin-bottom: 1.5rem;
      padding-bottom: 1rem;
      border-bottom: 2px solid var(--border-subtle);
    }

    h2 {
      font-size: 1.75rem;
      font-weight: 600;
      color: var(--text-primary);
      letter-spacing: -0.01em;
      margin: 2.5rem 0 1rem 0;
      padding-top: 1rem;
    }

    h3 {
      font-size: 1.25rem;
      font-weight: 600;
      color: var(--text-primary);
      margin: 2rem 0 1rem 0;
    }

    p {
      color: var(--text-secondary);
      margin-bottom: 1rem;
      line-height: 1.7;
    }

    strong {
      color: var(--text-primary);
      font-weight: 600;
    }

    a {
      color: var(--accent-orange);
      text-decoration: none;
      transition: color 0.2s ease;
    }

    a:hover {
      color: var(--accent-brown);
      text-decoration: underline;
    }

    /* Lists */
    ul, ol {
      margin: 1rem 0;
      padding-left: 1.5rem;
      color: var(--text-secondary);
    }

    li {
      margin: 0.5rem 0;
      line-height: 1.6;
    }

    /* Code */
    code {
      background: var(--bg-primary);
      color: var(--accent-brown);
      padding: 0.125rem 0.375rem;
      border-radius: 4px;
      font-family: 'SF Mono', 'Monaco', 'Inconsolata', monospace;
      font-size: 0.875em;
      font-weight: 500;
    }

    pre {
      background: var(--bg-primary);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 1.5rem;
      overflow-x: auto;
      margin: 1.5rem 0;
      position: relative;
    }

    pre code {
      background: none;
      padding: 0;
      color: var(--text-primary);
      font-size: 0.9rem;
      line-height: 1.6;
    }

    /* Copy button for code blocks */
    .copy-btn {
      position: absolute;
      top: 0.75rem;
      right: 0.75rem;
      background: var(--bg-secondary);
      border: 1px solid var(--border-subtle);
      color: var(--text-secondary);
      padding: 0.375rem 0.75rem;
      border-radius: var(--radius-sm);
      font-size: 0.75rem;
      font-weight: 500;
      cursor: pointer;
      opacity: 0;
      transition: all 0.2s ease;
    }

    pre:hover .copy-btn {
      opacity: 1;
    }

    .copy-btn:hover {
      background: var(--accent-orange);
      color: white;
      border-color: var(--accent-orange);
    }

    .copy-btn.copied {
      background: var(--accent-brown);
      color: white;
    }

    /* AI Prompts Note */
    .ai-prompts-note {
      background: #FFF9F0;
      border-left: 4px solid var(--accent-orange);
      padding: 1rem 1.25rem;
      margin: 1rem 0 1.5rem 0;
      border-radius: var(--radius-sm);
      font-size: 0.9rem;
      color: var(--text-primary);
    }

    .ai-prompts-note strong {
      color: var(--accent-orange);
    }

    /* Tables */
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 1.5rem 0;
      background: var(--bg-secondary);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      overflow: hidden;
    }

    th, td {
      padding: 0.875rem 1rem;
      text-align: left;
      border-bottom: 1px solid var(--border-light);
    }

    th {
      background: var(--bg-primary);
      color: var(--text-primary);
      font-weight: 600;
      font-size: 0.875rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    td {
      color: var(--text-secondary);
    }

    tr:last-child td {
      border-bottom: none;
    }

    /* Horizontal Rule */
    hr {
      border: none;
      height: 1px;
      background: var(--border-subtle);
      margin: 2.5rem 0;
    }

    /* Back to top */
    .back-to-top {
      display: inline-block;
      margin-top: 3rem;
      padding: 0.75rem 1.5rem;
      background: var(--bg-primary);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      color: var(--text-secondary);
      font-weight: 500;
      transition: all 0.2s ease;
    }

    .back-to-top:hover {
      background: var(--accent-orange);
      color: white;
      border-color: var(--accent-orange);
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
      text-decoration: none;
    }

    /* Section Cards */
    .section-card {
      background: var(--bg-primary);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 1.5rem;
      margin: 1.5rem 0;
    }

    /* Responsive */
    @media (max-width: 1024px) {
      .page {
        flex-direction: column;
        padding: 1rem;
      }

      nav#TOC {
        position: static;
        width: 100%;
        max-height: none;
        margin-bottom: 2rem;
      }

      .content {
        padding: 2rem 1.5rem;
      }
    }

    @media (max-width: 640px) {
      .header-row {
        padding: 1rem;
      }

      .title {
        font-size: 1rem;
      }

      .content {
        padding: 1.5rem 1rem;
      }

      h1 {
        font-size: 1.75rem;
      }

      h2 {
        font-size: 1.5rem;
      }
    }
  </style>
</head>
'''

# Enhanced scripts with requested features
enhanced_scripts = '''
<script>
document.addEventListener('DOMContentLoaded', function() {
  // 1. Add copy buttons to all code blocks
  document.querySelectorAll('pre').forEach(pre => {
    const button = document.createElement('button');
    button.className = 'copy-btn';
    button.textContent = 'Copy';
    button.setAttribute('aria-label', 'Copy code');

    button.addEventListener('click', async () => {
      const code = pre.querySelector('code') || pre;
      const text = code.textContent;

      try {
        await navigator.clipboard.writeText(text);
        button.textContent = 'Copied!';
        button.classList.add('copied');
        setTimeout(() => {
          button.textContent = 'Copy';
          button.classList.remove('copied');
        }, 2000);
      } catch (err) {
        button.textContent = 'Error';
        setTimeout(() => button.textContent = 'Copy', 2000);
      }
    
  // 4. Theme toggle functionality (Claude-style)
  const themeToggle = document.getElementById('theme-toggle');
  const themeIcon = document.querySelector('.theme-icon');
  const themeText = document.querySelector('.theme-text');

  // Load saved theme
  const savedTheme = localStorage.getItem('training-theme') || 'light';
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeButton(savedTheme);

  function updateThemeButton(theme) {
    if (theme === 'dark') {
      themeIcon.textContent = '☀️';
      themeText.textContent = 'Light';
    } else {
      themeIcon.textContent = '🌙';
      themeText.textContent = 'Dark';
    }
  }

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const currentTheme = document.documentElement.getAttribute('data-theme');
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('training-theme', newTheme);
      updateThemeButton(newTheme);
    });
  }
});

    pre.appendChild(button);
  });

  // 2. Highlight active page in TOC and scroll to it
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  const tocLinks = document.querySelectorAll('nav#TOC a');

  tocLinks.forEach(link => {
    const linkHref = link.getAttribute('href');
    if (linkHref === currentPage || linkHref === `../${currentPage}`) {
      link.classList.add('active');

      // Auto-scroll TOC to show active item
      setTimeout(() => {
        const nav = document.querySelector('nav#TOC');
        const linkTop = link.offsetTop;
        const navHeight = nav.clientHeight;
        const linkHeight = link.clientHeight;

        // Scroll so the active link is roughly in the middle
        nav.scrollTop = linkTop - (navHeight / 2) + (linkHeight / 2);
      }, 100);
    }
  });

  // 3. Add AI prompts usage note
  const aiPromptsHeadings = document.querySelectorAll('h3[id*="ai-learning-prompts"]');
  aiPromptsHeadings.forEach(heading => {
    // Check if note already exists
    const nextElement = heading.nextElementSibling;
    if (nextElement && nextElement.classList.contains('ai-prompts-note')) {
      return;
    }

    const note = document.createElement('div');
    note.className = 'ai-prompts-note';
    note.innerHTML = '<strong>💡 How to use these prompts:</strong> Copy any prompt below and paste it into <strong>Claude</strong>, <strong>ChatGPT</strong>, <strong>Gemini</strong>, or any other AI assistant to learn the concepts. These are for understanding only—solve practice problems yourself!';

    heading.parentNode.insertBefore(note, heading.nextSibling);
  });
});
</script>
'''

def create_toc(current_page=''):
    """Build clean TOC"""
    weeks = [
        ("Week 1: Foundations", "week1.html", list(range(1, 6))),
        ("Week 2: Data Analysis", "week2.html", list(range(6, 11))),
        ("Week 3: Intermediate Concepts", "week3.html", list(range(11, 16))),
        ("Week 4: Advanced Concepts", "week4.html", list(range(16, 21))),
        ("Week 5: Analytics & Optimization", "week5.html", list(range(21, 26))),
        ("Week 6: Mastery & Projects", "week6.html", list(range(26, 31)))
    ]

    day_titles = extract_day_titles()

    toc = ['<ul>']
    toc.append('<li><a href="../index.html" if "pages/" in current_page else "index.html">📚 Training Overview</a></li>')

    for week_name, week_file, days in weeks:
        week_link = f'pages/{week_file}' if current_page == 'index' else week_file
        toc.append(f'<li><a href="{week_link}">{week_name}</a>')
        toc.append('<ul>')
        for day_num in days:
            day_title = day_titles.get(day_num, f"Day {day_num}")
            day_link = f'pages/day{day_num}.html' if current_page == 'index' else f'day{day_num}.html'
            # Shorten titles for TOC
            short_title = day_title.replace('DAY ' + str(day_num) + ': ', '')
            if len(short_title) > 40:
                short_title = short_title[:37] + '...'
            toc.append(f'<li><a href="{day_link}">Day {day_num}: {short_title}</a></li>')
        toc.append('</ul>')
        toc.append('</li>')

    toc.append('</ul>')
    return '\n'.join(toc)

def extract_day_titles():
    """Extract day titles from HTML"""
    day_titles = {}
    all_h2 = soup.find_all('h2')
    for h2 in all_h2:
        if h2.get('id', '').startswith('day-'):
            text = h2.get_text()
            match = re.match(r'DAY (\d+):', text)
            if match:
                day_num = int(match.group(1))
                day_titles[day_num] = text
    return day_titles

def create_html_page(title, toc_html, content_html, current_page=''):
    """Create complete HTML page"""
    modern_head = modern_head_template.replace('{title}', title)
    return modern_head + f'''
<body>
<header id="title-block-header">
  <div class="header-row">
    <h1 class="title">{title}</h1>
    <div class="header-controls">
      <button class="theme-toggle" id="theme-toggle" aria-label="Toggle theme">
        <span class="theme-icon">🌙</span>
        <span class="theme-text">Dark</span>
      </button>
    </div>
  </div>
</header>
<div class="page">
  <nav id="TOC" role="navigation">
{toc_html}
  </nav>
  <div class="content">
{content_html}
    <a href="#" class="back-to-top">↑ Back to Top</a>
  </div>
</div>
{enhanced_scripts}
</body>
</html>'''

def extract_intro_content():
    """Extract intro for index"""
    content = []
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


def create_week_summary(week_num, days):
    """Create detailed week summary with day descriptions"""
    day_titles = extract_day_titles()

    week_info = {
        1: {"intro": "This week establishes the foundation for both Excel and SQL. You'll learn core concepts that everything else builds upon.", "focus": "Basic formulas, functions, filtering, lookups, and SELECT queries"},
        2: {"intro": "Week 2 focuses on data analysis fundamentals. Learn to combine data, summarize information, and create meaningful visualizations.", "focus": "JOINs, GROUP BY, pivot tables, charts, and aggregations"},
        3: {"intro": "Move to intermediate concepts with date handling, window functions, and what-if analysis for more sophisticated data work.", "focus": "Date functions, window functions (ROW_NUMBER, RANK, LAG, LEAD), Power Query"},
        4: {"intro": "Master advanced techniques including recursive queries, data modeling, and professional dashboard creation.", "focus": "CTEs, Power Pivot with DAX, CASE statements, PIVOT/UNPIVOT, advanced charts"},
        5: {"intro": "Apply analytics and optimization techniques to real-world scenarios. Learn performance tuning and integration.", "focus": "Statistical analysis, query optimization, advanced aggregations, Excel-SQL integration"},
        6: {"intro": "Final week focuses on mastery-level skills and creating portfolio-ready projects that showcase your abilities.", "focus": "Macros, advanced analytics (cohort, RFM), executive dashboards, final project"}
    }

    info = week_info.get(week_num, {"intro": "", "focus": ""})

    summary = f'''<div class="section-card">
<h2>Week {week_num} Overview</h2>
<p>{info["intro"]}</p>
<p><strong>Key Focus Areas:</strong> {info["focus"]}</p>
</div>

<h2>This Week\'s Learning Path</h2>
<p>Click any day below to view detailed lessons, practice exercises, and assignments:</p>

<div class="section-card">'''

    for day_num in days:
        title = day_titles.get(day_num, f"Day {day_num}")
        topic = re.sub(r'^DAY \d+:\s*', '', title)
        summary += f'''<div style="margin-bottom: 1.5rem;">
<h3 style="margin-bottom: 0.5rem;"><a href="day{day_num}.html" style="color: var(--accent-orange); text-decoration: none;">📚 {topic}</a></h3>
<p style="margin-left: 1.5rem; color: var(--text-secondary); font-size: 0.9rem;">Comprehensive 4-hour lesson with tutorials, practice exercises, and assignments</p>
</div>
'''

    summary += '</div>'
    return summary


def extract_week_content(week_num):
    """Extract week content"""
    week_ids = {
        1: 'week-1-foundations',
        2: 'week-2-data-analysis-fundamentals',
        3: 'week-3-intermediate-concepts',
        4: 'week-4-advanced-concepts',
        5: 'week-5-analytics-optimization',
        6: 'week-6-mastery-projects'
    }

    week_id = week_ids.get(week_num)
    if not week_id:
        # Try alternate IDs
        week_id = f'week-{week_num}'

    week_h1 = soup.find('h1', id=lambda x: x and week_id in x if x else False)
    if not week_h1:
        return f"<h1>Week {week_num}</h1><p>Content coming soon...</p>"

    content = [str(week_h1)]
    current = week_h1
    while current:
        current = current.find_next_sibling()
        if current and current.name == 'h1' and current != week_h1:
            break
        if current and current.name == 'h2':
            day_text = current.get_text()
            day_match = re.match(r'DAY (\d+):', day_text)
            if day_match:
                day_num = day_match.group(1)
                content.append(f'<h2><a href="day{day_num}.html">{day_text}</a></h2>')
                continue
        if current:
            content.append(str(current))

    return '\n'.join(content)

def extract_day_content(day_num):
    """Extract day content"""
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
        return f"<h1>Day {day_num}</h1><p>Content coming soon...</p>"

    content = [str(day_h2)]
    current = day_h2
    while current:
        current = current.find_next_sibling()
        if current and current.name == 'h2' and current.get('id', '').startswith('day-'):
            break
        if current and current.name == 'h1':
            break
        if current:
            content.append(str(current))

    return '\n'.join(content)

# Generate index.html (at root)
print("Generating index.html...")
intro_content = extract_intro_content()
toc = create_toc('index')
index_html = create_html_page(
    '30-Day Excel & SQL Training Plan',
    toc,
    intro_content,
    'index'
)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

# Generate week pages (in pages/)
week_titles = [
    "Week 1: Foundations",
    "Week 2: Data Analysis Fundamentals",
    "Week 3: Intermediate Concepts",
    "Week 4: Advanced Concepts",
    "Week 5: Analytics & Optimization",
    "Week 6: Mastery & Projects"
]

for week_num in range(1, 7):
    print(f"Generating pages/week{week_num}.html...")
    week_days = list(range((week_num-1)*5+1, week_num*5+1))
    week_summary = create_week_summary(week_num, week_days)
    week_content = extract_week_content(week_num)
    # Prepend summary to content
    week_content = week_summary + '\n' + week_content
    toc = create_toc(f'week{week_num}')
    week_html = create_html_page(
        week_titles[week_num - 1],
        toc,
        week_content,
        f'week{week_num}'
    )
    with open(f'pages/week{week_num}.html', 'w', encoding='utf-8') as f:
        f.write(week_html)

# Generate day pages (in pages/)
day_titles_dict = extract_day_titles()
for day_num in range(1, 31):
    print(f"Generating pages/day{day_num}.html...")
    day_content = extract_day_content(day_num)
    toc = create_toc(f'day{day_num}')
    day_title = day_titles_dict.get(day_num, f"Day {day_num}")
    day_html = create_html_page(
        day_title,
        toc,
        day_content,
        f'day{day_num}'
    )
    with open(f'pages/day{day_num}.html', 'w', encoding='utf-8') as f:
        f.write(day_html)

print("\n✅ Done! Generated modern design with:")
print("  - index.html (at root)")
print("  - pages/week1-6.html")
print("  - pages/day1-30.html")
print("  - Anthropic-inspired modern design")
print("  - Clean, organized file structure")
