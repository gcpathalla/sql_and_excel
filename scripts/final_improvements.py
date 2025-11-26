#!/usr/bin/env python3
"""
Final improvements:
1. Add light/dark theme CSS (Claude desktop style)
2. Add theme toggle button functionality
3. Create better week summaries
4. Regenerate all pages
"""

import re

# Read the current restructure script
with open('restructure_modern.py', 'r', encoding='utf-8') as f:
    script_content = f.read()

# 1. Update the color variables to support both themes
claude_themes = """
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
    }"""

# Replace the :root section
script_content = re.sub(
    r':root\s*\{[^}]+\}',
    claude_themes,
    script_content
)

# 2. Add theme toggle button CSS (if not exists)
if '.theme-toggle' not in script_content:
    theme_toggle_css = """
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
    }"""

    # Insert before the button class
    script_content = script_content.replace(
        '    .button {',
        theme_toggle_css + '\n\n    .button {'
    )

# 3. Update header controls to include theme toggle
script_content = script_content.replace(
    '<h1 class="title">{title}</h1>',
    '''<h1 class="title">{title}</h1>
    <div class="header-controls">
      <button class="theme-toggle" id="theme-toggle" aria-label="Toggle theme">
        <span class="theme-icon">🌙</span>
        <span class="theme-text">Dark</span>
      </button>
    </div>'''
)

# 4. Update JavaScript to handle theme toggle
theme_toggle_js = '''
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
  }'''

# Add theme toggle before the closing of DOMContentLoaded
script_content = script_content.replace(
    '});',
    theme_toggle_js + '\n});',
    1  # Only first occurrence
)

# 5. Add week summary generation function
week_summary_function = '''
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

    summary = f\'\'\'<div class="section-card">
<h2>Week {week_num} Overview</h2>
<p>{info["intro"]}</p>
<p><strong>Key Focus Areas:</strong> {info["focus"]}</p>
</div>

<h2>This Week\\'s Learning Path</h2>
<p>Click any day below to view detailed lessons, practice exercises, and assignments:</p>

<div class="section-card">\'\'\'

    for day_num in days:
        title = day_titles.get(day_num, f"Day {day_num}")
        topic = re.sub(r\'^DAY \\d+:\\s*\', \'\', title)
        summary += f\'\'\'<div style="margin-bottom: 1.5rem;">
<h3 style="margin-bottom: 0.5rem;"><a href="day{day_num}.html" style="color: var(--accent-orange); text-decoration: none;">📚 {topic}</a></h3>
<p style="margin-left: 1.5rem; color: var(--text-secondary); font-size: 0.9rem;">Comprehensive 4-hour lesson with tutorials, practice exercises, and assignments</p>
</div>
\'\'\'

    summary += \'</div>\'
    return summary

'''

# Insert the function before the extract_week_content function
script_content = script_content.replace(
    'def extract_week_content(week_num):',
    week_summary_function + '\ndef extract_week_content(week_num):'
)

# 6. Update week page generation to use summaries
old_week_gen = '''for week_num in range(1, 7):
    print(f"Generating pages/week{week_num}.html...")
    week_content = extract_week_content(week_num)
    toc = create_toc(f'week{week_num}')'''

new_week_gen = '''for week_num in range(1, 7):
    print(f"Generating pages/week{week_num}.html...")
    week_days = list(range((week_num-1)*5+1, week_num*5+1))
    week_summary = create_week_summary(week_num, week_days)
    week_content = extract_week_content(week_num)
    # Prepend summary to content
    week_content = week_summary + '\\n' + week_content
    toc = create_toc(f'week{week_num}')'''

script_content = script_content.replace(old_week_gen, new_week_gen)

# Save updated script
with open('restructure_modern.py', 'w', encoding='utf-8') as f:
    f.write(script_content)

print("✅ Updated restructure_modern.py with:")
print("  - Claude-style light/dark theme")
print("  - Theme toggle button")
print("  - Enhanced week summaries")
print("\nNow run: python3 restructure_modern.py")
