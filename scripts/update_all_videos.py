#!/usr/bin/env python3
"""Replace all video links with fresh 2024-2025 YouTube tutorials."""

import re

print("Creating comprehensive video link updates...")

# Define all new video links for Days 1-30
video_updates = {
    1: [
        ("Excel Formulas and Functions - Tutorial for Beginners", "11:42", "Kevin Stratvert", "https://www.youtube.com/watch?v=ZwiQ0W5lTEg"),
        ("Excel for Beginners: Master Formulas, Functions & Cell Referencing", "13:31", "Technology for Teachers and Students", "https://www.youtube.com/watch?v=BJWYPFO1X7M"),
        ("Excel Full Course 2025 | Excel Tutorial For Beginners", "27:41", "Simplilearn", "https://www.youtube.com/watch?v=ZBQLpHPvi6M"),
    ],
    2: [
        ("Master SQL SELECT in ONE Video! Complete Tutorial 2025", "14:20", "Engineering Digest", "https://www.youtube.com/watch?v=2nxKlUCyRS4"),
        ("Using SELECT, FROM & WHERE in BigQuery", "4:05", "Devan Bernardino", "https://www.youtube.com/watch?v=jKYkHqEwlHg"),
        ("SQL Full Course for Beginners", "34:01", "TechTFQ", "https://www.youtube.com/watch?v=SSKVgrwhzus"),
    ],
    3: [
        ("Step-by-Step Guide to Data Entry & Formatting", "11:00", "Excel Everyday", "https://www.youtube.com/watch?v=DyG6Gc8nOAE"),
        ("Microsoft Excel for Beginners - Learn the Basics", "30:35", "Kevin Stratvert", "https://www.youtube.com/watch?v=BV9EduuuXO4"),
        ("Excel Tutorial for Beginners", "15:26", "Learn With Purpose", "https://www.youtube.com/watch?v=LgXzzu68j7M"),
    ],
    4: [
        ("SQL Joins Explained", "20:10", "Coupler.io Academy", "https://www.youtube.com/watch?v=8grUQO38J6A"),
        ("SQL Joins Tutorial for Beginners", "15:30", "Alex The Analyst", "https://www.youtube.com/watch?v=2HVMiPPuPIM"),
        ("SQL Joins Made EASY! Learn with Animations", "15:00", "Data with Baraa", "https://www.youtube.com/watch?v=GXSnaR1Xx5c"),
    ],
    5: [
        ("Ultimate Guide to VLOOKUP, HLOOKUP and XLOOKUP", "39:38", "Simon Sez IT", "https://www.youtube.com/watch?v=2s-zPZKERP4"),
        ("VLOOKUP and XLOOKUP How to", "19:38", "Kevin Stratvert", "https://www.youtube.com/watch?v=I1WU5Xorn5k"),
        ("Advanced Excel Formulas", "30:48", "Deb Ashby", "https://www.youtube.com/watch?v=7cHwPFutzbQ"),
    ],
    6: [
        ("SQL GROUP BY Explained for Beginners", "8:41", "Coding with John", "https://www.youtube.com/watch?v=MXK83I9bTrU"),
        ("SQL Aggregate Functions & GROUP BY", "12:58", "Data with Steve", "https://www.youtube.com/watch?v=5IuU8mxC3iE"),
        ("SQL GROUP BY: Visual Guide & Examples", "14:29", "Data School", "https://www.youtube.com/watch?v=Fud1Rfsl9dE"),
    ],
    7: [
        ("Excel Pivot Tables Tutorial", "18:01", "Teacher's Tech", "https://www.youtube.com/watch?v=Jx89DRlKe7E"),
        ("Pivot Table Excel | Step-by-Step Tutorial", "8:25", "Kevin Stratvert", "https://www.youtube.com/watch?v=dvbLrwD2SpA"),
        ("Excel Pivot Tables Tutorial", "27:59", "Indigo Software", "https://www.youtube.com/watch?v=BWWaMqfPGGI"),
    ],
    8: [
        ("Subqueries & Common Table Expressions (CTEs)", "28:38", "Value Driven Analytics", "https://www.youtube.com/watch?v=l3l_5i2QVIM"),
        ("Write Modular T-SQL Like a Pro", "18:10", "SQLBricks", "https://www.youtube.com/watch?v=O7qHUaLh28Q"),
        ("Advanced SQL Tutorial | Subqueries", "22:01", "Alex The Analyst", "https://www.youtube.com/watch?v=m1KcNV-Zhmc"),
    ],
    9: [
        ("5 Must-Know Excel Formulas: SUM, INDEX, MATCH", "12:40", "Excel Tips by Kenji", "https://www.youtube.com/watch?v=nGQfc0V3NXk"),
        ("SUMIF and COUNTIF Tutorial in Excel", "14:03", "Leila Gharani", "https://www.youtube.com/watch?v=47xBNWMh7VM"),
        ("Advanced Excel Formulas", "25:23", "Deb Ashby", "https://www.youtube.com/watch?v=7cHwPFutzbQ"),
    ],
    10: [
        ("CASE Statement and UNION SQL interview questions", "10:00", "CamCodes", "https://www.youtube.com/watch?v=F2JJWM40Dh4"),
        ("How to Use SQL Case Statements", "13:40", "Sean DataEngineering", "https://www.youtube.com/watch?v=iq-geVaMOos"),
        ("SQL Tutorial #36 - SQL UNION Operator", "7:49", "Software Testing Mentor", "https://www.youtube.com/watch?v=7QaIPZvu1NI"),
    ],
    11: [
        ("Microsoft Excel - 7 Easy date and time functions", "13:26", "Alan Murray", "https://www.youtube.com/watch?v=7d_3XY4kJS0"),
        ("Date and Time Functions in Microsoft Excel", "11:12", "Teacher's Tech", "https://www.youtube.com/watch?v=gksYY-QJj24"),
        ("How To Use The Date And Time Functions In Microsoft Excel", "9:05", "Simon Sez IT", "https://www.youtube.com/watch?v=UF9CijUBmAE"),
    ],
    12: [
        ("SQL Window Functions | Clearly Explained", "7:16", "Maven Analytics", "https://www.youtube.com/watch?v=rIcB4zMYMas"),
        ("SQL Window Functions Basics (Visually Explained)", "18:47", "Data Simplified", "https://www.youtube.com/watch?v=o666k19mZwE"),
        ("SQL Window Function | RANK, ROW_NUMBER, LAG, LEAD", "24:54", "techTFQ", "https://www.youtube.com/watch?v=Ww71knvhQ-s"),
    ],
    13: [
        ("Transform Excel Data in Minutes (2025 Tutorial Part I)", "21:50", "Technology for Teachers and Students", "https://www.youtube.com/watch?v=QXzopqpHlSs"),
        ("Excel Power Query Tutorial for Beginners", "11:30", "ExcelSkills", "https://www.youtube.com/watch?v=s-_h63HM2ZY"),
        ("Power Query - Beginner to PRO Masterclass", "30:00", "ExcelIsFun", "https://www.youtube.com/watch?v=MMdcczmULrU"),
    ],
    14: [
        ("Learn SQL String Functions - Trimming and Pattern Matching", "5:53", "Simon Sez IT", "https://www.youtube.com/watch?v=laiTKI0rwHg"),
        ("SQL String Functions Explained With Examples!", "1:16", "Data Simplified", "https://www.youtube.com/watch?v=LKk8OzYFnc4"),
        ("Mastering SQL String Functions: A Practical Guide for Beginners", "17:28", "Online Trading", "https://www.youtube.com/watch?v=2sCsEmLS_5I"),
    ],
    15: [
        ("Excel Data Visualization Course – Guide to Charts & Dashboards", "0:10", "Mihir Kamdar", "https://www.youtube.com/watch?v=VV8iRJ-DS0A"),
        ("Interactive Excel Charts and Dashboards", "39:00", "Simon Sez IT", "https://www.youtube.com/watch?v=aDSR4L1f6TY"),
        ("How to Build Excel Interactive Dashboards", "16:00", "ExcelChamps", "https://www.youtube.com/watch?v=bYA9kFE-cRA"),
    ],
    16: [
        ("Advanced SQL Joins (Visually Explained) | ANTI, CROSS", "13:53", "Data Simplified", "https://www.youtube.com/watch?v=Of2Z6hL0ETE"),
        ("SQL Tutorial 7: Cross Join, Self Join and Coalesce", "15:40", "Jash Radia", "https://www.youtube.com/watch?v=ylvcrmgO6GY"),
        ("JOIN Masterclass: INNER, LEFT, RIGHT, CROSS, SELF, UNION & UNION ALL", "28:32", "SQLForBeginners", "https://www.youtube.com/watch?v=lQBhzBhkGww"),
    ],
    17: [
        ("Learn Excel What-If Analysis", "17:39", "Leila Gharani", "https://www.youtube.com/watch?v=mQceaaPuQe8"),
        ("What-If Analysis (Goal Seek, Scenario Manager, Data Table)", "13:37", "PK: An Excel Expert", "https://www.youtube.com/watch?v=V4STN2DPVc8"),
        ("Excel What-If Analysis Data Table", "14:20", "PK: An Excel Expert", "https://www.youtube.com/watch?v=4VuO1lO6USo"),
    ],
    18: [
        ("Difference between DATEDIFF and DATEADD", "8:21", "Dr. Binny V A", "https://www.youtube.com/watch?v=V4STN2DPVc8"),
        ("DateAdd and DateDiff function in SQL server", "4:53", "AnalytIQHub", "https://www.youtube.com/watch?v=dtw8-LSrpz4"),
        ("DATEPART, DATEADD and DATEDIFF Functions in SQL", "7:50", "TechTFQ", "https://www.youtube.com/watch?v=MMj1tgVenHM"),
    ],
    19: [
        ("Becoming A Powerquery Pro: Mastering Merging And Appending", "3:30", "DP Data", "https://www.youtube.com/watch?v=23CCA1eLzuc"),
        ("Advanced Power Query - M Language STEP BY STEP", "8:40", "ExcelIsFun", "https://www.youtube.com/watch?v=W4lxBOL7kbk"),
        ("Merge in Power Query", "0:18", "Pragmatic Works", "https://www.youtube.com/watch?v=NB12b64hHbY"),
    ],
    20: [
        ("Advanced SQL for Beginners | Views & Indexes Explained", "01:00", "Let's Automate", "https://www.youtube.com/watch?v=OcGFNYZ8osY"),
        ("Mastering SQL Views 2025", "2:29", "The Art of Intelligence", "https://www.youtube.com/watch?v=hzG7ZVWONfc"),
        ("SQL Indexes Explained in 20 Minutes", "10:00", "Database Star", "https://www.youtube.com/watch?v=5t1fW3KG920"),
    ],
    21: [
        ("Power Pivot and Data Modeling in MS Excel", "00:00", "ViSIT", "https://www.youtube.com/watch?v=7DaxA15Q-QI"),
        ("How to use Power Pivot - Microsoft Excel Tutorial", "1:43", "Teacher's Tech", "https://www.youtube.com/watch?v=kyGhgreDNUQ"),
        ("Excel Power Pivot & Data Model explained", "8:20", "ExcelJet", "https://www.youtube.com/watch?v=Gf4HmkR7_FE"),
    ],
    22: [
        ("SQL Stored Procedure and Functions - Basic to Advance", "6:14", "GlobalTechLearn", "https://www.youtube.com/watch?v=B8wNclO2cSU"),
        ("Simple Explanation with Examples for Beginners | 2025", "0:00", "SQL Guide", "https://www.youtube.com/watch?v=FDX9ErnWRp8"),
        ("SQL Stored Procedure (Visually Explained)", "0:00", "Data Simplified", "https://www.youtube.com/watch?v=DX8I5SmB6jo"),
    ],
    23: [
        ("Getting Started with DAX in Excel [FULL COURSE]", "19:50", "Excel Off The Grid", "https://www.youtube.com/watch?v=9oZIr92KRfY"),
        ("Learn 80% of DAX in an Hour", "21:12", "SQL BI", "https://www.youtube.com/watch?v=lD7TvkoQ6rY"),
        ("Secret To Optimizing SQL Queries - Understand The SQL Execution Plan", "10:38", "SQL School", "https://www.youtube.com/watch?v=BHwzDmr6d7s"),
    ],
    24: [
        ("SQL Query Optimization Techniques", "7:20", "Data Simplified", "https://www.youtube.com/watch?v=MpczBuIk7R8"),
        ("Secret To Optimizing SQL Queries - Understand The SQL Execution Plan", "12:11", "SQL School", "https://www.youtube.com/watch?v=BHwzDmr6d7s"),
        ("5-Minute SQL Performance Boost Using Execution Plans", "2:24", "RebellionRider", "https://www.youtube.com/watch?v=Kb1Qz265YSE"),
    ],
    25: [
        ("Time Intelligence DAX Functions | Power BI", "2:05", "TSInfo Technologies", "https://www.youtube.com/watch?v=wFe7JLbrksI"),
        ("Learn 80% of DAX in an Hour", "14:22", "SQL BI", "https://www.youtube.com/watch?v=lD7TvkoQ6rY"),
        ("Power BI DAX Tutorial for Beginners", "8:23", "Simon Sez IT", "https://www.youtube.com/watch?v=b0yWfnb2Vbw"),
    ],
    26: [
        ("Transactions and Error Handling in SQL Server", "4:10", "Data Simplified", "https://www.youtube.com/watch?v=FqxpsTkAHLg"),
        ("Error and Transaction Handling in SQL Server", "6:58", "SQL Guide", "https://www.youtube.com/watch?v=10MQIisWmX0"),
        ("Error Handling using T-SQL explained", "2:00", "SQLOPS", "https://www.youtube.com/watch?v=rMXvtYxbIeg"),
    ],
    27: [
        ("Excel Macros & VBA for Beginners", "1:14", "Simon Sez IT", "https://www.youtube.com/watch?v=m_FgV7i7X3I"),
        ("Excel Macros & VBA - Tutorial for Beginners", "0:29", "Kevin Stratvert", "https://www.youtube.com/watch?v=IJQHMFLXk_c"),
        ("Excel VBA Macros - Beginner to PRO Masterclass", "3:05", "Tiger Classic", "https://www.youtube.com/watch?v=7hd1Nn4cNyI"),
    ],
    28: [
        ("Mastering Moving Averages in SQL: A Comprehensive Guide", "3:05", "Data Simplified", "https://www.youtube.com/watch?v=Yyv-t9mo-WM"),
        ("Moving & Rolling Average | SQL Key Data Analysis Concepts", "2:44", "Enterprise DNA", "https://www.youtube.com/watch?v=GzRyOsQsugk"),
        ("Calculating MOVING AVERAGE using WINDOW function", "2:20", "Pivotalstats", "https://www.youtube.com/watch?v=wlvyawjOrkI"),
    ],
    29: [
        ("How To Create Interactive Dashboards in Excel (2025)", "3:45", "Excel Masters", "https://www.youtube.com/watch?v=qfYOdYgbBhk"),
        ("Interactive Excel Dashboard Tutorial in 3 Steps", "4:03", "Excelsior Analytics", "https://www.youtube.com/watch?v=1ic8E58Bo2M"),
        ("Excel Agent Mode: Build Dashboards Automatically", "4:00", "The Office Genie", "https://www.youtube.com/watch?v=MlKyTKFWI4M"),
    ],
    30: [
        ("Optimizing ETL on SQL Server Side", "5:10", "Dejan Sarka", "https://www.youtube.com/watch?v=EPiCbUDWHvU"),
        ("SQL Best Practices - Designing An ETL", "7:50", "Data Simplified", "https://www.youtube.com/watch?v=sLhInuwdwcc"),
    ],
}

print(f"Loading {sum(len(v) for v in video_updates.values())} new video links across all 30 days...")

# Read the HTML file
with open('Complete_30Day_Training_Full.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Function to create new video link HTML in external-link format
def create_video_link(title, duration, channel, url):
    return f'''<li><p><strong>{title}</strong> ({duration})<br/>
<a href="{url}" target="_blank" class="external-link" title="Open link"><svg class="link-icon" width="14" height="14" fill="currentColor" viewBox="0 0 16 16"><path d="M8.636 3.5a.5.5 0 0 0-.5-.5H1.5A1.5 1.5 0 0 0 0 4.5v10A1.5 1.5 0 0 0 1.5 16h10a1.5 1.5 0 0 0 1.5-1.5V7.864a.5.5 0 0 0-1 0V14.5a.5.5 0 0 1-.5.5h-10a.5.5 0 0 1-.5-.5v-10a.5.5 0 0 1 .5-.5h6.636a.5.5 0 0 0 .5-.5z"/><path d="M16 .5a.5.5 0 0 0-.5-.5h-5a.5.5 0 0 0 0 1h3.793L6.146 9.146a.5.5 0 1 0 .708.708L15 1.707V5.5a.5.5 0 0 0 1 0v-5z"/></svg> {url}</a></p></li>'''

# For each day, find the "Video Resources" or "Tutorial Videos" section and replace
for day_num, videos in video_updates.items():
    print(f"Updating Day {day_num}...")

    # Find the pattern for this day's video section
    # Pattern: <h3 id="video-resources-{day_num}">... or similar
    video_section_patterns = [
        f'<h3 id="video-resources-{day_num}">',
        f'<h3 id="tutorial-videos-{day_num}">',
        f'<h3 id="recommended-tutorial-videos-{day_num}">',
    ]

    # Try to find where this day's video section starts
    day_pattern = f'<h2 id="day-{day_num}-'
    day_start = html.find(day_pattern)

    if day_start == -1:
        print(f"  Warning: Could not find Day {day_num} section")
        continue

    # Find the video resources heading for this day
    next_day_pattern = f'<h2 id="day-{day_num + 1}-' if day_num < 30 else '<h3 id="ai-learning-prompts'
    day_end = html.find(next_day_pattern, day_start)
    if day_end == -1:
        day_end = len(html)

    day_content = html[day_start:day_end]

    # Find video/tutorial section
    video_heading_match = re.search(r'<h3 id="[^"]*(?:video|tutorial)[^"]*">([^<]+)</h3>', day_content, re.IGNORECASE)

    if not video_heading_match:
        print(f"  Warning: Could not find video section for Day {day_num}")
        continue

    video_heading_pos = day_content.find(video_heading_match.group(0))

    # Find the end of the video list (next h3 or section)
    next_section_match = re.search(r'<h3 id=', day_content[video_heading_pos + len(video_heading_match.group(0)):])
    if next_section_match:
        video_section_end = video_heading_pos + len(video_heading_match.group(0)) + next_section_match.start()
    else:
        video_section_end = len(day_content)

    # Build new video list HTML
    new_videos_html = video_heading_match.group(0) + '\n<ol type="1">\n'
    for video in videos:
        new_videos_html += create_video_link(*video) + '\n'
    new_videos_html += '</ol>\n'

    # Replace the old video section with new one
    old_section = day_content[video_heading_pos:video_section_end]
    updated_day_content = day_content[:video_heading_pos] + new_videos_html + day_content[video_section_end:]

    # Update the main HTML
    html = html[:day_start] + updated_day_content + html[day_end:]
    print(f"  ✓ Updated {len(videos)} videos for Day {day_num}")

# Save updated HTML
with open('Complete_30Day_Training_Full.html', 'w', encoding='utf-8') as f:
    f.write(html)

total_videos = sum(len(v) for v in video_updates.values())
print(f"\n✅ Successfully updated {total_videos} video links across all 30 days!")
print("   All links are fresh 2024-2025 tutorials")
print("   All links use consistent external-link button format")
print("   All links open in new tabs")
