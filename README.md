# 30-Day Excel & SQL Training Program

**By Guru Charan Pathalla**

A comprehensive, interactive training program designed to take you from beginner to advanced in both Excel and SQL over 30 days.

## 🚀 Getting Started

**To start the course:** Simply open `index.html` in your web browser!

**NEW: Single-Page Application!** All 37 pages (6 weeks + 30 days + overview) are now consolidated into one seamless HTML file for instant navigation.

## 🎯 Features

- **Single-Page Application**: All content in one file - no page reloads!
- **⚡ Instant Navigation**: Hash-based routing with smooth fade-in animations
- **📊 Progress Tracker**: Track which pages you've visited with localStorage persistence
- **30 Complete Days** of structured learning covering Excel and SQL
- **Interactive Content** with video tutorials, practice exercises, and assignments
- **Modern Design** inspired by Anthropic's aesthetic
- **Dark/Light Theme** toggle for comfortable viewing
- **Font Customization** with 5 font options including dyslexia-friendly fonts
- **Responsive Layout** with persistent TOC sidebar
- **External Links** all formatted as clickable buttons with icons
- **Practice Guidance** with detailed notes and hints for every day
- **Deep Linking**: Bookmark specific days with URLs like `index.html#day5`

## 📚 Content Structure

### Weeks 1-6 Coverage:
- **Week 1**: Foundations (Excel formulas, SQL basics)
- **Week 2**: Data Analysis (Pivot tables, JOINs, aggregations)
- **Week 3**: Intermediate Concepts (Power Query, window functions)
- **Week 4**: Advanced Concepts (Power Pivot, CTEs, DAX)
- **Week 5**: Analytics & Optimization (Query optimization, VBA)
- **Week 6**: Mastery & Projects (Final comprehensive project)

## 🛠️ Technical Details

- **Single HTML File**: All 37 sections (overview + 6 weeks + 30 days) in one ~210KB file
- **Hash-Based Navigation**: URL routing using #overview, #week1-6, #day1-30
- **Smooth Animations**: Fade-in transitions between sections (0.4s ease-in-out)
- **Progress Tracking**: LocalStorage-based tracker shows completion percentage
- **Consistent Styling**: All external links formatted as buttons with icons
- **Fresh Content**: All video links updated for 2024-2025
- **Accessibility**: Font size controls, dyslexia-friendly options
- **No Dependencies**: Pure HTML/CSS/JavaScript - works offline!

## 📁 File Structure

```
sql_and_excel/
├── index.html                          # 👈 START HERE - Single-page app with all content
├── SQL-and-Excel-Course.html           # Legacy multi-page entry point (kept for reference)
├── README.md                           # This file
├── pages/                              # Legacy individual pages (kept for reference)
│   ├── week1.html - week6.html        # Week overview pages
│   └── day1.html - day30.html         # Individual day lesson pages
└── scripts/                            # Development tools (for maintainers)
    ├── restructure_modern.py           # Page generation script
    └── (20 other Python utility scripts)
```

**Note:** The new `index.html` is a self-contained single-page application. The `pages/` directory and `SQL-and-Excel-Course.html` are kept for backward compatibility and reference.

## 🔄 Keeping Video Links Fresh

As YouTube videos may become outdated, use this prompt to generate fresh video links:

---

**PROMPT FOR VIDEO LINK GENERATION:**

I need fresh, high-quality YouTube tutorial video links for a 30-day Excel & SQL training program. For each day below, please find 3-4 recent (2023-2025) tutorial videos that are:
- From reputable channels (10K+ views preferred)
- Clear and beginner-to-intermediate friendly
- Comprehensive coverage of the topic
- 10-30 minutes in length

**Please provide the results in this exact format for easy parsing:**

```
DAY X: Topic Name
- Video Title (Duration) - Channel Name
  URL: https://www.youtube.com/watch?v=...
```

---

**DAY 1: Excel - Formulas & Basic Functions**
Topics: SUM, AVERAGE, COUNT, MIN, MAX, basic calculations, cell references

**DAY 2: SQL - SELECT & WHERE**
Topics: SELECT statements, WHERE clause, filtering data, basic queries

**DAY 3: Excel - Data Management & Formatting**
Topics: Sort, filter, conditional formatting, data validation, tables

**DAY 4: SQL - JOINs**
Topics: INNER JOIN, LEFT JOIN, RIGHT JOIN, joining tables

**DAY 5: Excel - Advanced Functions (IFs, TEXT, LOOKUP)**
Topics: IF, IFERROR, TEXT functions, VLOOKUP, XLOOKUP

**DAY 6: SQL - GROUP BY & Aggregations**
Topics: GROUP BY, HAVING, aggregate functions, COUNT, SUM, AVG

**DAY 7: Excel - Pivot Tables & Charts**
Topics: Creating pivot tables, pivot charts, slicers, data analysis

**DAY 8: SQL - Subqueries & CTEs**
Topics: Subqueries, Common Table Expressions (WITH clause), nested queries

**DAY 9: Excel - Advanced Functions**
Topics: INDEX/MATCH, array formulas, dynamic arrays, SUMIFS, COUNTIFS

**DAY 10: SQL - CASE Statements & UNION**
Topics: CASE WHEN, conditional logic, UNION, UNION ALL

**DAY 11: Excel - Date & Time Functions**
Topics: DATE, TODAY, NOW, DATEDIF, EDATE, EOMONTH, date calculations

**DAY 12: SQL - Window Functions**
Topics: ROW_NUMBER, RANK, LAG, LEAD, OVER clause, partitioning

**DAY 13: Excel - Power Query Basics**
Topics: Get & Transform, importing data, Power Query editor, data cleaning

**DAY 14: SQL - String Functions & Pattern Matching**
Topics: CONCAT, SUBSTRING, LIKE, wildcards, text manipulation

**DAY 15: Excel - Data Visualization**
Topics: Advanced charts, sparklines, conditional formatting, dashboards

**DAY 16: SQL - Advanced JOINs & Set Operations**
Topics: CROSS JOIN, SELF JOIN, EXISTS, set operations

**DAY 17: Excel - What-If Analysis**
Topics: Goal Seek, Scenario Manager, Data Tables, Solver

**DAY 18: SQL - Date & Time Functions**
Topics: DATE functions, DATEADD, DATEDIFF, time zone handling

**DAY 19: Excel - Power Query Advanced**
Topics: Merging, appending, custom columns, M language basics

**DAY 20: SQL - Views & Indexes**
Topics: Creating views, materialized views, index optimization

**DAY 21: Excel - Power Pivot & Data Modeling**
Topics: Power Pivot basics, data models, relationships, calculated columns

**DAY 22: SQL - Stored Procedures & Functions**
Topics: Creating procedures, user-defined functions, parameters

**DAY 23: Excel - DAX Basics**
Topics: DAX formulas, CALCULATE, FILTER, measures vs columns

**DAY 24: SQL - Query Optimization**
Topics: Execution plans, indexing strategies, query performance

**DAY 25: Excel - Advanced DAX**
Topics: Time intelligence, context transition, advanced calculations

**DAY 26: SQL - Transactions & Error Handling**
Topics: BEGIN/COMMIT/ROLLBACK, TRY/CATCH, transaction management

**DAY 27: Excel - VBA & Macros Basics**
Topics: Recording macros, VBA editor, basic automation

**DAY 28: SQL - Advanced Analytics**
Topics: Statistical functions, percentiles, moving averages

**DAY 29: Excel - Advanced Dashboards**
Topics: Interactive dashboards, form controls, advanced visualizations

**DAY 30: SQL - Integration & Best Practices**
Topics: SQL with Excel, ETL basics, best practices, optimization

---

**After receiving updated links:**
1. Provide them to the maintainer
2. Run `update_all_videos.py` script to replace old links
3. Regenerate all pages with `restructure_modern.py`
4. Commit and push changes

## 🎨 Customization Options

### For Users:
- **Theme Toggle**: Switch between light and dark modes
- **Font Selector**: Choose from 5 fonts (Candara, Arial, Courier New, Georgia, OpenDyslexic)
- **Font Size**: Adjust text size with A- and A+ buttons (4 levels)
- **Progress Tracker**: Automatically tracks visited pages, with reset option
- **Deep Linking**: Share specific sections with `index.html#day15` style URLs

### For Developers:
- Edit individual page HTML files in `pages/` directory
- Run the builder script to regenerate the single-page `index.html`
- All settings are stored in localStorage for persistence
- Custom styling through CSS variables

## 📧 Feedback

Have questions or feedback? Email: **gcpath@live.com**

## 📜 License

© 2025 Guru Charan Pathalla. All rights reserved.

---

**Repository**: https://github.com/gcpathalla/sql_and_excel
