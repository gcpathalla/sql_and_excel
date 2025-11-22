#!/usr/bin/env python3
"""
Update the original HTML file with detailed content for Days 11-30
"""

# Read the original HTML up to Day 10
print("Reading original HTML...")
with open('Complete_30Day_Training_Full.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find where "WEEKS 3-6 CONTINUE" starts
insert_point = None
for i, line in enumerate(lines):
    if 'WEEKS 3-6 CONTINUE WITH' in line and '<h1' in line:
        insert_point = i
        break

if not insert_point:
    print("ERROR: Could not find insertion point!")
    exit(1)

print(f"Found insertion point at line {insert_point + 1}")

# Keep everything before the insertion point
html_before = ''.join(lines[:insert_point])

# Read Days 11-12 content
print("Reading Days 11-12 content...")
with open('days_11_30_content.html', 'r', encoding='utf-8') as f:
    days_11_12 = f.read()

# Read Days 13-30 content
print("Reading Days 13-30 content...")
with open('days_13_30_additional.html', 'r', encoding='utf-8') as f:
    days_13_30 = f.read()

# Find the closing tags in the original file
closing_start = None
for i in range(len(lines) - 1, 0, -1):
    if '</body>' in lines[i]:
        # Go back a bit more to find where content ends
        # Look for the last meaningful content before scripts
        for j in range(i - 1, 0, -1):
            if '<a href="#top"' in lines[j]:
                closing_start = j + 1
                break
        break

if not closing_start:
    print("ERROR: Could not find closing section!")
    exit(1)

print(f"Found closing section at line {closing_start + 1}")

# Get closing HTML (scripts and body/html tags)
html_closing = ''.join(lines[closing_start:])

# Combine everything
print("Combining all sections...")
new_html = html_before + '\n' + days_11_12 + '\n' + days_13_30 + '\n' + html_closing

# Write the updated HTML
print("Writing updated HTML...")
with open('Complete_30Day_Training_Full.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("\n✅ Successfully updated Complete_30Day_Training_Full.html")
print(f"   - Kept original content up to line {insert_point}")
print(f"   - Inserted detailed Days 11-30 content")
print(f"   - Preserved closing sections")
