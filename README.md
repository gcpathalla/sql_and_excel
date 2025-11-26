# 30-Day Excel & SQL Training Program

**By Guru Charan Pathalla**

A comprehensive, interactive training program designed to take you from beginner to advanced in both Excel and SQL over 30 days.

## 🎯 Features

- **30 Complete Days** of structured learning covering Excel and SQL
- **Interactive Content** with video tutorials, practice exercises, and assignments
- **Modern Design** inspired by Anthropic's aesthetic
- **Dark/Light Theme** toggle for comfortable viewing
- **Font Customization** with 5 font options including dyslexia-friendly fonts
- **Responsive Layout** with persistent TOC sidebar
- **External Links** all formatted as clickable buttons with icons
- **Practice Guidance** with detailed notes and hints for every day

## 📚 Content Structure

### Weeks 1-6 Coverage:
- **Week 1**: Foundations (Excel formulas, SQL basics)
- **Week 2**: Data Analysis (Pivot tables, JOINs, aggregations)
- **Week 3**: Intermediate Concepts (Power Query, window functions)
- **Week 4**: Advanced Concepts (Power Pivot, CTEs, DAX)
- **Week 5**: Analytics & Optimization (Query optimization, VBA)
- **Week 6**: Mastery & Projects (Final comprehensive project)

## 🛠️ Technical Details

- **37 HTML Pages**: 1 index + 6 week pages + 30 day pages
- **Consistent Styling**: All external links formatted as buttons with icons
- **Fresh Content**: All video links updated for 2024-2025
- **Accessibility**: Font size controls, dyslexia-friendly options

## 📁 File Structure

```
sql_and_excel/
├── index.html                          # Main landing page
├── pages/
│   ├── week1.html - week6.html        # Week overview pages
│   └── day1.html - day30.html         # Individual day lesson pages
├── Complete_30Day_Training_Full.html  # Source content
└── restructure_modern.py              # Page generation script
```

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

### For Developers:
- Edit `Complete_30Day_Training_Full.html` for content changes
- Run `restructure_modern.py` to regenerate all pages
- Custom styling in the script's CSS section

## 📧 Feedback

Have questions or feedback? Email: **gcpath@live.com**

## 📜 License

© 2025 Guru Charan Pathalla. All rights reserved.

---

**Repository**: https://github.com/gcpathalla/sql_and_excel
