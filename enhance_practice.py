#!/usr/bin/env python3
"""Add helpful notes and hints to Guided and Independent Practice sections."""

import re

print("Reading source HTML...")
with open('Complete_30Day_Training_Full.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Generic helpful content for Guided Practice
guided_practice_note = '''<div class="practice-note">
<p><strong>📝 How to approach Guided Practice:</strong></p>
<ul>
<li><strong>Follow step-by-step:</strong> Work through each exercise in order</li>
<li><strong>Use provided resources:</strong> Reference the video tutorials and AI prompts if you get stuck</li>
<li><strong>Verify your work:</strong> Check your results match expected outcomes</li>
<li><strong>Take notes:</strong> Document key learnings and shortcuts you discover</li>
<li><strong>Ask for help:</strong> Use AI assistants to clarify concepts you don't understand</li>
</ul>
</div>

'''

# Generic helpful content for Independent Practice
independent_practice_hint = '''<div class="practice-note">
<p><strong>💡 Hints for Independent Practice:</strong></p>
<ul>
<li><strong>Start simple:</strong> Begin with basic variations before attempting complex modifications</li>
<li><strong>Break it down:</strong> Divide complex problems into smaller, manageable steps</li>
<li><strong>Test incrementally:</strong> Verify each step works before moving to the next</li>
<li><strong>Use documentation:</strong> Refer to official docs or tutorials when needed</li>
<li><strong>Experiment:</strong> Try different approaches to find what works best</li>
</ul>
</div>

'''

# Find all Guided Practice sections and add notes
# Pattern: <h3 id="guided-practice...">Guided Practice...</h3>
guided_pattern = r'(<h3 id="guided-practice[^"]*">Guided Practice[^<]*</h3>\s*)'

guided_count = 0
def add_guided_note(match):
    global guided_count
    guided_count += 1
    return match.group(1) + guided_practice_note

html = re.sub(guided_pattern, add_guided_note, html)

# Find all Independent Practice sections and add hints
independent_pattern = r'(<h3 id="independent-practice[^"]*">Independent Practice[^<]*</h3>\s*)'

independent_count = 0
def add_independent_hint(match):
    global independent_count
    independent_count += 1
    return match.group(1) + independent_practice_hint

html = re.sub(independent_pattern, add_independent_hint, html)

print(f"Added helpful notes to {guided_count} Guided Practice sections")
print(f"Added hints to {independent_count} Independent Practice sections")

# Save
with open('Complete_30Day_Training_Full.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ Practice sections enhanced with notes and hints")
