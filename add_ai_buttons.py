#!/usr/bin/env python3
"""Add ChatGPT, Claude, and Google quick action buttons to all AI prompts."""

import re
from urllib.parse import quote

print("Adding AI assistant quick action buttons to all prompts...")

with open('Complete_30Day_Training_Full.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all AI Learning Prompts sections
ai_sections = re.findall(
    r'<h3 id="ai-learning-prompts[^"]*">AI Learning Prompts.*?</h3>(.*?)(?=<h3|<h2|$)',
    html,
    re.DOTALL
)

print(f"Found {len(ai_sections)} AI Learning Prompts sections")

# For each prompt code block, we'll add quick action buttons
# Pattern: <pre><code>PROMPT_TEXT</code></pre>

def add_quick_actions(match):
    """Add quick action buttons to a code block."""
    prompt_text = match.group(1)

    # URL encode the prompt
    encoded_prompt = quote(prompt_text.strip())

    # Create the quick action buttons HTML
    buttons_html = f'''<div class="ai-quick-actions">
  <span class="quick-actions-label">Quick Actions:</span>
  <a href="https://chat.openai.com/?q={encoded_prompt}" target="_blank" class="ai-quick-btn chatgpt-btn" title="Open in ChatGPT">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
      <path d="M22.282 9.821a5.985 5.985 0 0 0-.516-4.91 6.046 6.046 0 0 0-6.51-2.9A6.065 6.065 0 0 0 4.981 4.18a5.985 5.985 0 0 0-3.998 2.9 6.046 6.046 0 0 0 .743 7.097 5.98 5.98 0 0 0 .51 4.911 6.051 6.051 0 0 0 6.515 2.9A5.985 5.985 0 0 0 13.26 24a6.056 6.056 0 0 0 5.772-4.206 5.99 5.99 0 0 0 3.997-2.9 6.056 6.056 0 0 0-.747-7.073zM13.26 22.43a4.476 4.476 0 0 1-2.876-1.04l.141-.081 4.779-2.758a.795.795 0 0 0 .392-.681v-6.737l2.02 1.168a.071.071 0 0 1 .038.052v5.583a4.504 4.504 0 0 1-4.494 4.494zM3.6 18.304a4.47 4.47 0 0 1-.535-3.014l.142.085 4.783 2.759a.771.771 0 0 0 .78 0l5.843-3.369v2.332a.08.08 0 0 1-.033.062L9.74 19.95a4.5 4.5 0 0 1-6.14-1.646zM2.34 7.896a4.485 4.485 0 0 1 2.366-1.973V11.6a.766.766 0 0 0 .388.676l5.815 3.355-2.02 1.168a.076.076 0 0 1-.071 0l-4.83-2.786A4.504 4.504 0 0 1 2.34 7.872zm16.597 3.855l-5.833-3.387L15.119 7.2a.076.076 0 0 1 .071 0l4.83 2.791a4.494 4.494 0 0 1-.676 8.105v-5.678a.79.79 0 0 0-.407-.667zm2.01-3.023l-.141-.085-4.774-2.782a.776.776 0 0 0-.785 0L9.409 9.23V6.897a.066.066 0 0 1 .028-.061l4.83-2.787a4.5 4.5 0 0 1 6.68 4.66zm-12.64 4.135l-2.02-1.164a.08.08 0 0 1-.038-.057V6.075a4.5 4.5 0 0 1 7.375-3.453l-.142.08L8.704 5.46a.795.795 0 0 0-.393.681zm1.097-2.365l2.602-1.5 2.607 1.5v2.999l-2.597 1.5-2.607-1.5z"/>
    </svg>
    ChatGPT
  </a>
  <a href="https://claude.ai/new?q={encoded_prompt}" target="_blank" class="ai-quick-btn claude-btn" title="Open in Claude">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
      <path d="M16.77 3.5L12 1l-4.77 2.5L2 1v13.5l5.23 2.5L12 14.5l4.77 2.5L22 14.5V1l-5.23 2.5zM7.5 13.38L4 11.63V4.37l3.5 1.75v7.26zm4.5 1.12l-3.5-1.75V5.5L12 7.25v7.25zm4.5-1.12l-3.5 1.75V7.88l3.5-1.75v7.25zm3.5-1.75l-3.5 1.75V5.5l3.5-1.75v7.88z"/>
    </svg>
    Claude
  </a>
  <a href="https://www.google.com/search?q={encoded_prompt}" target="_blank" class="ai-quick-btn google-btn" title="Search in Google">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
      <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/>
      <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/>
      <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05"/>
      <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/>
    </svg>
    Google
  </a>
</div>
'''

    # Return the original code block plus the quick actions
    return f'<pre><code>{prompt_text}</code></pre>\n{buttons_html}'

# Process all code blocks within AI prompts sections
# We need to be careful to only add buttons to AI prompt code blocks

count = 0
for section in ai_sections:
    # Find all <pre><code> blocks in this section
    original_section = section

    # Replace code blocks with code blocks + quick actions
    updated_section = re.sub(
        r'<pre><code>(.*?)</code></pre>',
        lambda m: add_quick_actions(m),
        section,
        flags=re.DOTALL
    )

    # Count how many were replaced
    count += section.count('<pre><code>') - updated_section.count('<div class="ai-quick-actions">')

    # Replace in main HTML
    html = html.replace(original_section, updated_section)

# Actually, let's take a different approach - find ALL pre>code blocks that are
# preceded by AI Learning Prompts heading

# Better pattern: Find h3 AI Learning Prompts, then find all code blocks until next h3
pattern = r'(<h3 id="ai-learning-prompts[^"]*">.*?</h3>.*?)(<pre><code>(.*?)</code></pre>)'

def replace_with_buttons(match):
    global count
    before = match.group(1)
    code_block = match.group(2)
    prompt_text = match.group(3)

    # Skip if already has quick actions
    if 'ai-quick-actions' in before:
        return match.group(0)

    count += 1

    # URL encode the prompt
    encoded_prompt = quote(prompt_text.strip())

    # Create the quick action buttons HTML
    buttons_html = f'''<div class="ai-quick-actions">
  <span class="quick-actions-label">Ask AI:</span>
  <a href="https://chat.openai.com/?q={encoded_prompt}" target="_blank" class="ai-quick-btn chatgpt-btn" title="Open in ChatGPT">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
      <path d="M22.282 9.821a5.985 5.985 0 0 0-.516-4.91 6.046 6.046 0 0 0-6.51-2.9A6.065 6.065 0 0 0 4.981 4.18a5.985 5.985 0 0 0-3.998 2.9 6.046 6.046 0 0 0 .743 7.097 5.98 5.98 0 0 0 .51 4.911 6.051 6.051 0 0 0 6.515 2.9A5.985 5.985 0 0 0 13.26 24a6.056 6.056 0 0 0 5.772-4.206 5.99 5.99 0 0 0 3.997-2.9 6.056 6.056 0 0 0-.747-7.073zM13.26 22.43a4.476 4.476 0 0 1-2.876-1.04l.141-.081 4.779-2.758a.795.795 0 0 0 .392-.681v-6.737l2.02 1.168a.071.071 0 0 1 .038.052v5.583a4.504 4.504 0 0 1-4.494 4.494zM3.6 18.304a4.47 4.47 0 0 1-.535-3.014l.142.085 4.783 2.759a.771.771 0 0 0 .78 0l5.843-3.369v2.332a.08.08 0 0 1-.033.062L9.74 19.95a4.5 4.5 0 0 1-6.14-1.646zM2.34 7.896a4.485 4.485 0 0 1 2.366-1.973V11.6a.766.766 0 0 0 .388.676l5.815 3.355-2.02 1.168a.076.076 0 0 1-.071 0l-4.83-2.786A4.504 4.504 0 0 1 2.34 7.872zm16.597 3.855l-5.833-3.387L15.119 7.2a.076.076 0 0 1 .071 0l4.83 2.791a4.494 4.494 0 0 1-.676 8.105v-5.678a.79.79 0 0 0-.407-.667zm2.01-3.023l-.141-.085-4.774-2.782a.776.776 0 0 0-.785 0L9.409 9.23V6.897a.066.066 0 0 1 .028-.061l4.83-2.787a4.5 4.5 0 0 1 6.68 4.66zm-12.64 4.135l-2.02-1.164a.08.08 0 0 1-.038-.057V6.075a4.5 4.5 0 0 1 7.375-3.453l-.142.08L8.704 5.46a.795.795 0 0 0-.393.681zm1.097-2.365l2.602-1.5 2.607 1.5v2.999l-2.597 1.5-2.607-1.5z"/>
    </svg>
    ChatGPT
  </a>
  <a href="https://claude.ai/new?q={encoded_prompt}" target="_blank" class="ai-quick-btn claude-btn" title="Open in Claude">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
      <path d="M16.77 3.5L12 1l-4.77 2.5L2 1v13.5l5.23 2.5L12 14.5l4.77 2.5L22 14.5V1l-5.23 2.5zM7.5 13.38L4 11.63V4.37l3.5 1.75v7.26zm4.5 1.12l-3.5-1.75V5.5L12 7.25v7.25zm4.5-1.12l-3.5 1.75V7.88l3.5-1.75v7.25zm3.5-1.75l-3.5 1.75V5.5l3.5-1.75v7.88z"/>
    </svg>
    Claude
  </a>
  <a href="https://www.google.com/search?q={encoded_prompt}" target="_blank" class="ai-quick-btn google-btn" title="Search in Google">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
      <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/>
    </svg>
    Google
  </a>
</div>'''

    return before + code_block + '\n' + buttons_html

# Reset count
count = 0

# Apply the replacement
html = re.sub(pattern, replace_with_buttons, html, flags=re.DOTALL)

print(f"Added quick action buttons to {count} AI prompts")

# Save
with open('Complete_30Day_Training_Full.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ All AI prompts now have ChatGPT, Claude, and Google quick action buttons!")
