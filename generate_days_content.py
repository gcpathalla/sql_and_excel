#!/usr/bin/env python3
"""
Generate detailed content for Days 11-30 following the same structure as Days 1-10
"""

# Day content templates and data
days_data = {
    13: {
        "title": "DAY 13: Excel - What-If Analysis (Goal Seek, Data Tables, Scenarios)",
        "learning_objectives": """- Master Excel What-If Analysis tools
- Use Goal Seek to find target values
- Create one-variable and two-variable Data Tables
- Build and compare Scenarios for forecasting
- Apply sensitivity analysis techniques""",
        "topics": """<p><strong>1. Goal Seek</strong>
- Find input value to achieve desired output
- Data → What-If Analysis → Goal Seek
- Example: Find sales needed to reach profit target
- Set cell (formula), To value (target), By changing cell (input)</p>

<p><strong>2. Data Tables - One Variable</strong>
- Test multiple values for one input
- Row or column input format
- Example: Loan payment with different interest rates
- Creates automatic result table</p>

<p><strong>3. Data Tables - Two Variable</strong>
- Test combinations of two inputs
- Row input and column input
- Example: Payment varies by rate AND loan term
- Creates matrix of results</p>

<p><strong>4. Scenario Manager</strong>
- Create named scenarios (Best Case, Worst Case, Most Likely)
- Save multiple sets of input values
- Compare scenarios side-by-side
- Generate Scenario Summary reports
- Use for budget forecasting and planning</p>""",
        "videos": [
            ("Excel Goal Seek Tutorial", "10 min", "https://www.youtube.com/watch?v=SyGb2sRa8zM", "Excel Campus"),
            ("Data Tables Explained", "15 min", "https://www.youtube.com/watch?v=a8XzoU2t29M", "Leila Gharani"),
            ("Scenario Manager", "12 min", "https://www.youtube.com/watch?v=7lSu8pja76w", "MyOnlineTrainingHub")
        ],
        "ai_prompts": [
            ("Understanding What-If Analysis", """I'm learning Excel What-If Analysis tools. Please explain:

1. What is the difference between Goal Seek, Data Tables, and Scenarios?
2. When should I use each tool?
3. Show me how to use Goal Seek to find break-even point
4. How do one-variable and two-variable Data Tables differ?
5. Provide a practical example using loan calculations

Use step-by-step examples for beginners."""),
            ("Understanding Scenario Analysis", """Help me understand Scenario Manager in Excel:

1. What are scenarios and why use them?
2. How do I create Best Case, Worst Case, and Most Likely scenarios?
3. Show me how to compare scenarios side-by-side
4. How do I create a Scenario Summary report?
5. Provide examples using business forecasting (revenue/cost projections)

Explain with practical examples.""")
        ],
        "practice_summary": "Create loan calculator with Goal Seek, build Data Tables for interest rate sensitivity, create budget scenarios",
        "assignment": """Create a comprehensive Business Forecasting Model:
1. **Revenue Model:** Input variables (price, units, growth rate), use Goal Seek to find units needed for revenue target
2. **Sensitivity Analysis:** Two-variable Data Table showing revenue at different price/volume combinations
3. **Scenario Planning:** Create 3 scenarios (Conservative, Expected, Optimistic) with different assumptions, generate Scenario Summary report
4. **Break-Even Analysis:** Use Goal Seek to find sales volume needed to break even"""
    },

    14: {
        "title": "DAY 14: SQL - Window Functions Part 2 (LAG, LEAD, Running Totals)",
        "learning_objectives": """- Use LAG and LEAD for accessing previous/next rows
- Calculate running totals with window functions
- Compute moving averages
- Perform period-over-period comparisons
- Master cumulative aggregations""",
        "topics": """<p><strong>1. LAG Function</strong>
- Access previous row value
- Syntax: <code>LAG(column, offset, default) OVER (ORDER BY column)</code>
- Compare current row to previous row
- Example: Compare this month sales vs last month</p>

<p><strong>2. LEAD Function</strong>
- Access next row value
- Syntax: <code>LEAD(column, offset, default) OVER (ORDER BY column)</code>
- Look ahead in data
- Example: Compare current order to next order</p>

<p><strong>3. Running Totals</strong>
- Cumulative sum using SUM() OVER
- Syntax: <code>SUM(amount) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)</code>
- Year-to-date, quarter-to-date calculations
- Running balance calculations</p>

<p><strong>4. Moving Averages</strong>
- Calculate average over sliding window
- Example: 7-day moving average
- Syntax: <code>AVG(sales) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)</code>
- Smoothing trends and patterns</p>""",
        "videos": [
            ("LAG and LEAD Functions", "14 min", "https://www.youtube.com/watch?v=Ww71knvhQ-s", "Alex The Analyst"),
            ("Running Totals in SQL", "10 min", "https://www.youtube.com/watch?v=tys7f0Fdv0k", "Data with Baraa"),
            ("Moving Averages", "12 min", "https://www.youtube.com/watch?v=zJ8_kT8AhsI", "Programming with Mosh")
        ],
        "ai_prompts": [
            ("Understanding LAG and LEAD", """I'm learning SQL LAG and LEAD functions. Please explain:

1. What is the difference between LAG and LEAD?
2. How do I compare current month sales to previous month?
3. Show me how to calculate month-over-month growth rate
4. How do I use PARTITION BY with LAG/LEAD?
5. Provide examples using sales data with time series

Use SQL Server syntax with clear examples."""),
            ("Understanding Running Totals", """Help me understand running totals and moving averages:

1. What is the difference between running total and regular SUM?
2. How do I calculate year-to-date sales?
3. Explain ROWS BETWEEN in window functions
4. Show me how to calculate 7-day moving average
5. How do I create running balance for account transactions?

Provide practical examples for financial analysis.""")
        ],
        "practice_summary": "Calculate month-over-month sales changes, create running totals for revenue, compute 30-day moving averages",
        "assignment": """Create Advanced Time-Series Analysis:
1. **Period Comparisons:** Calculate sales for current month, previous month (LAG), and month-over-month % change
2. **Running Totals:** Create year-to-date sales, quarter-to-date sales, running customer count
3. **Moving Averages:** 7-day, 30-day, and 90-day moving averages for daily sales
4. **Customer Analysis:** Calculate days between orders per customer using LAG, identify customers with increasing order frequency"""
    },

    15: {
        "title": "DAY 15: Excel - Power Query Basics + WEEK 3 TEST",
        "learning_objectives": """- Introduction to Power Query Editor
- Import and transform data from multiple sources
- Clean and reshape data
- Combine queries (merge and append)
- Review Week 3 concepts""",
        "topics": """<p><strong>1. Power Query Introduction</strong>
- Data → Get Data → From File/Database/Web
- Power Query Editor interface
- Applied Steps pane (transformation history)
- Load data to worksheet or data model</p>

<p><strong>2. Data Cleaning Operations</strong>
- Remove duplicates
- Fill down/up missing values
- Replace values
- Change data types
- Trim and clean text
- Split columns by delimiter</p>

<p><strong>3. Data Transformation</strong>
- Filter rows
- Remove columns
- Pivot/Unpivot columns
- Group by aggregations
- Add custom columns with formulas</p>

<p><strong>4. Combining Queries</strong>
- Merge queries (like JOIN in SQL)
- Append queries (union/stack tables)
- Reference vs duplicate queries
- Merge types: Left, Right, Inner, Full Outer</p>""",
        "videos": [
            ("Power Query Beginner Tutorial", "20 min", "https://www.youtube.com/watch?v=0aeZX1l4JT4", "Leila Gharani"),
            ("Power Query Data Cleaning", "15 min", "https://www.youtube.com/watch?v=gR2K_GksMDY", "MyOnlineTrainingHub"),
            ("Merge and Append Queries", "12 min", "https://www.youtube.com/watch?v=qGABnvlm9Ss", "Excel Campus")
        ],
        "ai_prompts": [
            ("Understanding Power Query", """I'm learning Power Query in Excel. Please explain:

1. What is Power Query and when should I use it vs regular Excel formulas?
2. How do I import data from CSV files and clean it?
3. What are Applied Steps and how do they work?
4. Show me how to remove duplicates and fill missing values
5. Provide a beginner-friendly workflow for cleaning messy data

Use step-by-step examples."""),
            ("Understanding Merge and Append", """Help me understand combining queries in Power Query:

1. What is the difference between Merge and Append?
2. How is Merge similar to SQL JOIN?
3. Explain Left, Right, Inner, and Full Outer merge
4. When should I use Append vs Merge?
5. Show me examples using customer and order tables

Explain with practical scenarios.""")
        ],
        "practice_summary": "Import CSV data, clean with Power Query, merge customer and order tables, create transformations",
        "assignment": """Power Query Data Integration Project + Week 3 Test:
1. **Data Import:** Import 2-3 CSV files with sales data
2. **Data Cleaning:** Remove duplicates, handle nulls, fix data types, clean text
3. **Transformation:** Create calculated columns, group by category, pivot data
4. **Merge Queries:** Combine customer table with orders table
5. **Week 3 Review:** Complete 30-minute test covering Days 11-15 (Date functions, Window functions, What-If Analysis, Power Query basics)"""
    },

    # Week 4 Days
    16: {
        "title": "DAY 16: SQL - CTEs & Recursive Queries",
        "learning_objectives": """- Master Common Table Expressions (CTEs)
- Write recursive CTEs
- Understand hierarchical data queries
- Improve query readability with CTEs
- Solve complex problems with temporary result sets""",
        "topics": """<p><strong>1. Common Table Expressions (CTEs)</strong>
- WITH clause syntax
- Temporary named result set
- Improves readability over subqueries
- Example: <code>WITH SalesCTE AS (SELECT ...) SELECT * FROM SalesCTE</code></p>

<p><strong>2. Multiple CTEs</strong>
- Chain multiple WITH clauses
- Reference earlier CTEs in later ones
- Break complex queries into logical steps
- Example: Calculate sales, then costs, then profit</p>

<p><strong>3. Recursive CTEs</strong>
- CTE that references itself
- Anchor member (base case)
- Recursive member (iterative case)
- UNION ALL between members
- Use for: org charts, bill of materials, hierarchies</p>

<p><strong>4. Practical Applications</strong>
- Employee hierarchies (manager chains)
- Date series generation
- Graph traversal
- Parts explosion (manufacturing)
- MAXRECURSION option to prevent infinite loops</p>""",
        "videos": [
            ("SQL CTEs Explained", "18 min", "https://www.youtube.com/watch?v=QVRfyGPm_kc", "Alex The Analyst"),
            ("Recursive CTE Tutorial", "15 min", "https://www.youtube.com/watch?v=vzS7RSjdJiI", "Programming with Mosh"),
            ("Hierarchical Queries", "12 min", "https://www.youtube.com/watch?v=EToKsS8WnCg", "Data with Baraa")
        ],
        "ai_prompts": [
            ("Understanding CTEs", """I'm learning Common Table Expressions (CTEs) in SQL. Please explain:

1. What is a CTE and how is it different from a subquery or temp table?
2. When should I use CTEs vs subqueries?
3. Show me how to chain multiple CTEs together
4. How do I use CTEs to simplify complex queries?
5. Provide examples using sales and customer data

Use SQL Server syntax with practical examples."""),
            ("Understanding Recursive CTEs", """Help me understand recursive CTEs:

1. What is recursion in SQL and when do I need it?
2. Explain anchor member vs recursive member
3. Show me how to query an employee hierarchy (find all reports under a manager)
4. How do I generate a date series (all dates in a month)?
5. What is MAXRECURSION and why is it important?

Provide step-by-step examples for beginners.""")
        ],
        "practice_summary": "Write CTEs to simplify queries, create recursive CTE for employee hierarchy, generate date series",
        "assignment": """CTE Mastery Project:
1. **Sales Analysis with CTEs:** Create 3 chained CTEs (monthly sales, costs, profit calculation)
2. **Employee Hierarchy:** Write recursive CTE to show all employees under a specific manager with levels
3. **Date Series:** Generate all dates for current year using recursive CTE
4. **Complex Reporting:** Replace a complex nested subquery with clean, readable CTEs"""
    },

    17: {
        "title": "DAY 17: Excel - Power Pivot & Data Modeling (DAX basics)",
        "learning_objectives": """- Introduction to Power Pivot and data modeling
- Create relationships between tables
- Understand star schema design
- Write basic DAX formulas
- Build calculated columns and measures""",
        "topics": """<p><strong>1. Power Pivot Introduction</strong>
- Enable Power Pivot add-in
- Import multiple tables
- Data Model vs regular worksheets
- Benefits: handle millions of rows, relate tables</p>

<p><strong>2. Table Relationships</strong>
- One-to-many relationships
- Primary key and foreign key
- Create relationships in diagram view
- Star schema: Fact table + Dimension tables
- Example: Orders (Fact) → Customers, Products, Dates (Dimensions)</p>

<p><strong>3. DAX Basics - Calculated Columns</strong>
- DAX = Data Analysis Expressions
- Similar to Excel formulas but for tables
- Example: <code>Profit = [Revenue] - [Cost]</code>
- Calculated once when data refreshes
- Table[Column] reference syntax</p>

<p><strong>4. DAX Measures</strong>
- Dynamic calculations (recalculate based on filters)
- Aggregation functions: SUM, AVERAGE, COUNT, etc.
- Example: <code>Total Sales = SUM(Orders[Sales])</code>
- Use in PivotTables with slicers
- Measures vs Calculated Columns</p>""",
        "videos": [
            ("Power Pivot Introduction", "20 min", "https://www.youtube.com/watch?v=UN0RHmOaJPM", "Leila Gharani"),
            ("DAX Basics for Beginners", "25 min", "https://www.youtube.com/watch?v=klQAZLr5vxA", "SQLBI"),
            ("Creating Relationships", "15 min", "https://www.youtube.com/watch?v=fJM_jCdT0rE", "MyOnlineTrainingHub")
        ],
        "ai_prompts": [
            ("Understanding Power Pivot", """I'm learning Power Pivot and data modeling. Please explain:

1. What is Power Pivot and how is it different from regular Excel?
2. What is a data model and why create relationships between tables?
3. Explain star schema design (fact and dimension tables)
4. How do I create a relationship between Orders and Customers tables?
5. Provide a beginner-friendly example using sales data

Use simple examples to explain the concepts."""),
            ("Understanding DAX", """Help me understand DAX formulas:

1. What is DAX and how is it different from Excel formulas?
2. What is the difference between calculated columns and measures?
3. Show me basic DAX formulas: SUM, AVERAGE, COUNT
4. How do I reference columns from different tables?
5. Provide examples creating Total Sales, Average Price, Profit measures

Explain with practical scenarios.""")
        ],
        "practice_summary": "Build data model with relationships, create calculated columns for profit, write DAX measures",
        "assignment": """Power Pivot Data Model Project:
1. **Import Tables:** Load Orders, Customers, Products, Dates tables
2. **Create Relationships:** Build star schema (Orders as fact table)
3. **Calculated Columns:** Add Profit, Margin%, Days to Ship columns using DAX
4. **DAX Measures:** Create Total Sales, Total Profit, Avg Order Value, Customer Count measures
5. **PivotTable:** Build dashboard using measures with slicers for Category, Region, Year"""
    },

    18: {
        "title": "DAY 18: SQL - CASE Statements & PIVOT/UNPIVOT",
        "learning_objectives": """- Master CASE expressions for conditional logic
- Create calculated columns with CASE
- Use PIVOT to transform rows to columns
- Use UNPIVOT to transform columns to rows
- Apply conditional aggregations""",
        "topics": """<p><strong>1. CASE Expressions - Simple CASE</strong>
- Conditional logic in SQL
- Syntax: <code>CASE column WHEN value THEN result END</code>
- Example: <code>CASE Category WHEN 'Tech' THEN 'Technology' END</code>
- Use in SELECT, WHERE, ORDER BY</p>

<p><strong>2. CASE Expressions - Searched CASE</strong>
- Multiple conditions
- Syntax: <code>CASE WHEN condition THEN result ELSE default END</code>
- Example: Categorize sales as High/Medium/Low
- Can use AND, OR, comparison operators</p>

<p><strong>3. PIVOT Operator</strong>
- Transform rows into columns
- Syntax: <code>PIVOT (AGG(column) FOR pivot_column IN ([value1], [value2]))</code>
- Example: Sales by year as columns instead of rows
- Creates crosstab/matrix format</p>

<p><strong>4. UNPIVOT Operator</strong>
- Transform columns into rows
- Normalize wide tables
- Example: Convert Q1, Q2, Q3, Q4 columns to Quarter and Sales rows
- Inverse of PIVOT operation</p>""",
        "videos": [
            ("SQL CASE Statement", "15 min", "https://www.youtube.com/watch?v=V9WUoRmsies", "Programming with Mosh"),
            ("PIVOT and UNPIVOT", "18 min", "https://www.youtube.com/watch?v=iFqB8YL2Jd4", "WiseOwlTutorials"),
            ("Advanced CASE Examples", "12 min", "https://www.youtube.com/watch?v=KBBEOxQjXxI", "Data with Baraa")
        ],
        "ai_prompts": [
            ("Understanding CASE", """I'm learning SQL CASE statements. Please explain:

1. What is the difference between simple CASE and searched CASE?
2. Show me how to categorize sales amounts (< 100 = Low, 100-500 = Medium, > 500 = High)
3. How do I use CASE in WHERE clause and ORDER BY?
4. Provide examples for customer segmentation (Active, Inactive, New)
5. Show conditional aggregation examples

Use SQL Server syntax with clear examples."""),
            ("Understanding PIVOT/UNPIVOT", """Help me understand PIVOT and UNPIVOT:

1. What does PIVOT do and when should I use it?
2. Show me how to convert sales data from rows to columns (months as columns)
3. What is UNPIVOT and when do I need it?
4. How do I pivot by multiple columns?
5. Provide examples using sales data by region and time period

Explain with step-by-step examples.""")
        ],
        "practice_summary": "Create customer segments with CASE, build sales matrix with PIVOT, normalize data with UNPIVOT",
        "assignment": """CASE and PIVOT Mastery:
1. **Customer Segmentation:** Use CASE to classify customers (VIP > $10k, Regular $1k-10k, New < $1k)
2. **Sales Categorization:** CASE to categorize products by price range, sales performance
3. **PIVOT Report:** Create sales report with months as columns, regions as rows
4. **Conditional Aggregation:** Count customers by segment, sum sales by category using CASE
5. **UNPIVOT Practice:** Take quarterly sales table (Q1, Q2, Q3, Q4 columns) and unpivot to normalized format"""
    },

    19: {
        "title": "DAY 19: Excel - Advanced Charts & Dashboards",
        "learning_objectives": """- Create advanced chart types
- Build combination charts
- Design interactive dashboards
- Use slicers and timelines
- Apply professional formatting and design""",
        "topics": """<p><strong>1. Advanced Chart Types</strong>
- Waterfall charts (show incremental changes)
- Funnel charts (conversion analysis)
- Combo charts (column + line)
- Sparklines (mini charts in cells)
- Histogram and Pareto charts</p>

<p><strong>2. Dynamic Charts</strong>
- Charts with named ranges
- OFFSET function for dynamic ranges
- Charts that update automatically with new data
- Dropdown lists to switch chart data</p>

<p><strong>3. Dashboard Design Principles</strong>
- Layout and white space
- Color scheme and consistency
- Key metrics at top (KPIs)
- Supporting details below
- Minimize clutter, maximize insights</p>

<p><strong>4. Interactive Elements</strong>
- Slicers for filtering data
- Timelines for date filtering
- Form controls (dropdowns, checkboxes)
- Link slicers to multiple PivotTables
- Report Connections for coordinated filtering</p>""",
        "videos": [
            ("Advanced Excel Charts", "20 min", "https://www.youtube.com/watch?v=7cX5vYxCa-A", "MyOnlineTrainingHub"),
            ("Excel Dashboard Tutorial", "30 min", "https://www.youtube.com/watch?v=K74_FNnlIF8", "Leila Gharani"),
            ("Slicers and Timelines", "12 min", "https://www.youtube.com/watch?v=RlZBgSwn4cc", "Excel Campus")
        ],
        "ai_prompts": [
            ("Understanding Advanced Charts", """I'm learning advanced Excel charts. Please explain:

1. When should I use waterfall charts vs combo charts?
2. How do I create a combination chart (column and line together)?
3. What are sparklines and when should I use them?
4. Show me how to create dynamic charts that update automatically
5. Provide examples for sales trend analysis

Use step-by-step explanations."""),
            ("Understanding Dashboards", """Help me understand Excel dashboard design:

1. What makes a good dashboard?
2. How do I use slicers to filter multiple PivotTables?
3. What is the difference between slicers and timelines?
4. Show me dashboard layout best practices
5. Provide examples for sales performance dashboards

Explain design principles and practical implementation.""")
        ],
        "practice_summary": "Create waterfall chart for profit breakdown, build combo chart for trends, design interactive dashboard",
        "assignment": """Sales Dashboard Creation:
1. **KPI Cards:** Display Total Sales, Total Profit, Avg Order Value, Customer Count
2. **Trend Charts:** Combo chart showing sales (columns) and profit margin (line) by month
3. **Category Analysis:** Waterfall chart showing contribution of each category to total sales
4. **Regional Breakdown:** Map or column chart by region
5. **Interactive Filters:** Add slicers for Year, Category, Region - connect to all charts/tables"""
    },

    20: {
        "title": "DAY 20: SQL - Views, Stored Procedures, Optimization + WEEK 4 TEST",
        "learning_objectives": """- Create and manage Views
- Write basic Stored Procedures
- Understand query execution plans
- Apply indexing strategies
- Review Week 4 concepts""",
        "topics": """<p><strong>1. Views</strong>
- Virtual tables based on query
- <code>CREATE VIEW view_name AS SELECT ...</code>
- Simplify complex queries
- Security: hide underlying table structure
- Can SELECT from views like tables</p>

<p><strong>2. Stored Procedures</strong>
- Saved SQL code with parameters
- <code>CREATE PROCEDURE proc_name @param datatype AS BEGIN ... END</code>
- Execute: <code>EXEC proc_name @param = value</code>
- Benefits: reusability, security, performance
- Can include logic, variables, loops</p>

<p><strong>3. Query Optimization Basics</strong>
- Execution plans (Ctrl+L in SSMS)
- Identify costly operations
- Use indexes on WHERE, JOIN columns
- Avoid SELECT *, use specific columns
- WHERE before JOIN when possible</p>

<p><strong>4. Indexing</strong>
- <code>CREATE INDEX idx_name ON table(column)</code>
- Clustered vs Non-clustered indexes
- Speed up searches, slow down inserts
- Index columns used in WHERE, JOIN, ORDER BY
- Don't over-index</p>""",
        "videos": [
            ("SQL Views Tutorial", "10 min", "https://www.youtube.com/watch?v=mPT9ta3inJw", "Programming with Mosh"),
            ("Stored Procedures Basics", "15 min", "https://www.youtube.com/watch?v=Sk-_I5bWsHA", "Alex The Analyst"),
            ("Query Optimization", "20 min", "https://www.youtube.com/watch?v=BHwzDmr6d7s", "Data with Baraa")
        ],
        "ai_prompts": [
            ("Understanding Views and Procedures", """I'm learning SQL Views and Stored Procedures. Please explain:

1. What is a View and when should I use it?
2. How are Views different from tables?
3. What is a Stored Procedure and what are its benefits?
4. Show me how to create a simple procedure with parameters
5. Provide examples using customer and sales data

Use SQL Server syntax with practical examples."""),
            ("Understanding Query Optimization", """Help me understand SQL query optimization:

1. What is an execution plan and how do I read it?
2. When should I create an index?
3. What is the difference between clustered and non-clustered indexes?
4. Show me common query performance problems and solutions
5. Provide best practices for writing efficient queries

Explain with beginner-friendly examples.""")
        ],
        "practice_summary": "Create views for common reports, write stored procedure with parameters, analyze execution plans",
        "assignment": """Database Optimization Project + Week 4 Test:
1. **Create Views:** Build 3 views (CustomerSales, ProductPerformance, RegionalSummary)
2. **Stored Procedure:** Create procedure to get sales by date range with parameters
3. **Optimization:** Analyze slow query, add appropriate indexes, compare before/after performance
4. **Week 4 Review:** Complete 30-minute test covering CTEs, Power Pivot, CASE/PIVOT, Views/Procedures"""
    },

    # Week 5 Days
    21: {
        "title": "DAY 21: Excel - Statistical Analysis & Forecasting",
        "learning_objectives": """- Perform statistical analysis in Excel
- Use regression analysis tools
- Create forecasts with FORECAST functions
- Understand correlation and trends
- Apply data analysis tools""",
        "topics": """<p><strong>1. Descriptive Statistics</strong>
- Data Analysis Toolpak (Add-in)
- Descriptive Statistics tool
- Mean, median, mode, standard deviation
- Quartiles, range, variance
- Skewness and kurtosis</p>

<p><strong>2. Correlation and Regression</strong>
- <code>CORREL()</code> function - relationship strength
- Regression tool (Y vs X analysis)
- Interpret R-squared value
- Trend lines in charts
- Example: Sales vs Marketing Spend</p>

<p><strong>3. Forecasting Functions</strong>
- <code>FORECAST.LINEAR()</code> - linear trend projection
- <code>FORECAST.ETS()</code> - exponential smoothing (seasonality)
- Moving averages for smoothing
- Seasonal decomposition</p>

<p><strong>4. What-If Scenarios</strong>
- Probability distributions
- Monte Carlo simulation basics
- Confidence intervals
- Sensitivity analysis with Data Tables</p>""",
        "videos": [
            ("Excel Statistical Analysis", "18 min", "https://www.youtube.com/watch?v=9WyFUO_llBc", "Leila Gharani"),
            ("Excel Forecasting", "15 min", "https://www.youtube.com/watch?v=lCN5GyURbZ4", "MyOnlineTrainingHub"),
            ("Regression Analysis", "20 min", "https://www.youtube.com/watch?v=JLH5e-SZToQ", "Excel Campus")
        ],
        "ai_prompts": [
            ("Understanding Statistical Analysis", """I'm learning statistical analysis in Excel. Please explain:

1. What statistics should I calculate for sales data (mean, median, std dev)?
2. How do I interpret correlation between two variables?
3. Show me how to perform regression analysis
4. What is R-squared and what does it mean?
5. Provide examples using sales and marketing data

Use beginner-friendly explanations."""),
            ("Understanding Forecasting", """Help me understand Excel forecasting:

1. What is the difference between FORECAST.LINEAR and FORECAST.ETS?
2. When should I use each forecasting method?
3. How do I account for seasonality in forecasts?
4. Show me how to create a 12-month sales forecast
5. How do I measure forecast accuracy?

Provide practical examples with sales data.""")
        ],
        "practice_summary": "Calculate descriptive statistics, perform regression analysis, create sales forecast",
        "assignment": """Statistical Analysis & Forecasting Project:
1. **Descriptive Stats:** Use Data Analysis Toolpak on sales data (mean, median, std dev, quartiles)
2. **Correlation Analysis:** Calculate correlation between Price and Sales Volume
3. **Regression:** Analyze relationship between Marketing Spend and Revenue
4. **Sales Forecast:** Use FORECAST.ETS to predict next 6 months sales with seasonality
5. **Dashboard:** Create summary showing key statistics, trend chart, forecast chart"""
    },

    22: {
        "title": "DAY 22: SQL - Advanced Aggregations (GROUPING SETS, CUBE, ROLLUP)",
        "learning_objectives": """- Use GROUPING SETS for multiple aggregations
- Create summary reports with ROLLUP
- Generate cross-tabulations with CUBE
- Understand subtotals and grand totals
- Master multi-dimensional analysis""",
        "topics": """<p><strong>1. GROUPING SETS</strong>
- Multiple GROUP BY in single query
- Syntax: <code>GROUP BY GROUPING SETS ((col1), (col2), (col1, col2))</code>
- Replaces multiple UNION ALL queries
- Example: Sales by Region, by Product, by Both</p>

<p><strong>2. ROLLUP</strong>
- Hierarchical subtotals
- Syntax: <code>GROUP BY ROLLUP (col1, col2)</code>
- Creates hierarchy: (col1, col2), (col1), ()
- Grand total row
- Example: Sales by Region → City with subtotals</p>

<p><strong>3. CUBE</strong>
- All possible grouping combinations
- Syntax: <code>GROUP BY CUBE (col1, col2)</code>
- Creates: (col1, col2), (col1), (col2), ()
- Cross-dimensional analysis
- Example: Sales by Region AND Product (all combinations)</p>

<p><strong>4. GROUPING and GROUPING_ID</strong>
- Identify NULL vs subtotal rows
- <code>GROUPING(column)</code> returns 1 for subtotal
- <code>GROUPING_ID(col1, col2)</code> binary identifier
- Use with CASE to label subtotals</p>""",
        "videos": [
            ("GROUPING SETS Explained", "15 min", "https://www.youtube.com/watch?v=5K9FNtGQQEE", "WiseOwlTutorials"),
            ("ROLLUP and CUBE", "18 min", "https://www.youtube.com/watch?v=rGfGmwWRqPE", "Programming with Mosh"),
            ("Advanced GROUP BY", "12 min", "https://www.youtube.com/watch?v=KI2fLk8Q1ak", "Data with Baraa")
        ],
        "ai_prompts": [
            ("Understanding GROUPING SETS", """I'm learning SQL advanced aggregations. Please explain:

1. What is GROUPING SETS and why use it instead of UNION ALL?
2. Show me how to get sales by Category, by Region, and Total in one query
3. What is the difference between GROUPING SETS, ROLLUP, and CUBE?
4. Provide examples using sales data with multiple dimensions
5. When should I use each method?

Use SQL Server syntax with clear examples."""),
            ("Understanding ROLLUP and CUBE", """Help me understand ROLLUP and CUBE:

1. What does ROLLUP do and how does it create hierarchies?
2. Show me ROLLUP with Region → State → City
3. What is CUBE and when should I use it?
4. How do I identify subtotal rows with GROUPING()?
5. Provide practical examples for multi-dimensional sales reports

Explain with step-by-step examples.""")
        ],
        "practice_summary": "Create GROUPING SETS for multi-level summary, use ROLLUP for hierarchical totals, build CUBE for cross-tabs",
        "assignment": """Advanced Aggregation Analysis:
1. **GROUPING SETS:** Create report showing sales by (Category), (Region), (Category + Region), (Total)
2. **ROLLUP:** Hierarchical summary by Year → Quarter → Month with subtotals
3. **CUBE:** Cross-tabulation of sales by Region and Product Category (all combinations)
4. **Labeled Subtotals:** Use GROUPING() with CASE to label rows as 'Category Total', 'Region Total', 'Grand Total'
5. **Performance Analysis:** Compare performance of GROUPING SETS vs multiple queries"""
    },

    23: {
        "title": "DAY 23: Excel - Advanced Conditional Formatting & Data Validation",
        "learning_objectives": """- Master advanced conditional formatting
- Create custom formatting rules
- Use formulas in conditional formatting
- Build data validation with custom rules
- Design user-friendly data entry forms""",
        "topics": """<p><strong>1. Advanced Conditional Formatting</strong>
- Formula-based rules
- Highlight duplicates across columns
- Color scales and data bars
- Icon sets with custom thresholds
- Stop If True option</p>

<p><strong>2. Formula-Based Rules</strong>
- Use formulas to determine formatting
- Example: <code>=AND($B2>1000, $C2<0.5)</code>
- Reference entire row with $
- Highlight based on other columns
- Multiple conditions with AND/OR</p>

<p><strong>3. Data Validation Rules</strong>
- List (dropdown)
- Whole number, Decimal, Date
- Text length restrictions
- Custom formula validation
- Input message and error alert</p>

<p><strong>4. Advanced Validation</strong>
- Dependent dropdowns (INDIRECT)
- Prevent duplicates
- Validation based on other cells
- Custom error messages
- Circle Invalid Data tool</p>""",
        "videos": [
            ("Advanced Conditional Formatting", "18 min", "https://www.youtube.com/watch?v=YvV7Jinnv-w", "Leila Gharani"),
            ("Data Validation Tricks", "15 min", "https://www.youtube.com/watch?v=ZYJHgGp-RL0", "MyOnlineTrainingHub"),
            ("Dependent Dropdowns", "12 min", "https://www.youtube.com/watch?v=mGTcBfmL4Ss", "Excel Campus")
        ],
        "ai_prompts": [
            ("Understanding Conditional Formatting", """I'm learning advanced conditional formatting. Please explain:

1. How do I use formulas in conditional formatting rules?
2. Show me how to highlight an entire row based on one cell's value
3. How do I create alternating row colors that don't break when filtering?
4. Explain color scales vs icon sets vs data bars
5. Provide examples for sales performance dashboards

Use step-by-step instructions."""),
            ("Understanding Data Validation", """Help me understand data validation:

1. What is data validation and why use it?
2. How do I create dependent dropdowns (second dropdown based on first)?
3. Show me how to prevent duplicate entries
4. How do I validate based on another cell's value?
5. Provide examples for order entry forms

Explain with practical scenarios.""")
        ],
        "practice_summary": "Create formula-based formatting rules, build dependent dropdowns, add custom validation",
        "assignment": """Data Entry Form with Advanced Validation:
1. **Conditional Formatting:** Highlight overdue invoices (due date < today), profit margins < 20%, top 10% sales
2. **Data Validation:** Create dropdowns for Category, Region, Product; add date validation, number ranges
3. **Dependent Dropdowns:** Category dropdown → Product dropdown (products filtered by category)
4. **Duplicate Prevention:** Validate Order ID is unique, prevent duplicate customer entries
5. **Professional Form:** Add input messages, error alerts, formatted for user-friendly data entry"""
    },

    24: {
        "title": "DAY 24: SQL - Query Optimization & Performance Tuning",
        "learning_objectives": """- Analyze query execution plans
- Identify performance bottlenecks
- Optimize JOIN operations
- Use appropriate indexing strategies
- Write efficient WHERE clauses""",
        "topics": """<p><strong>1. Execution Plan Analysis</strong>
- View Actual Execution Plan (Ctrl+M)
- Read plan from right to left
- Identify expensive operations (Table Scan, Sort)
- Look for warnings (missing index, type conversion)
- % of total cost</p>

<p><strong>2. Indexing Strategy</strong>
- Clustered index (1 per table, sorts data)
- Non-clustered index (pointers to data)
- Composite indexes (multiple columns)
- Include columns for covering index
- When to rebuild/reorganize indexes</p>

<p><strong>3. Query Optimization Techniques</strong>
- Use WHERE before JOIN
- Avoid SELECT *, specify needed columns
- Use EXISTS instead of IN for large datasets
- Avoid functions on indexed columns in WHERE
- Use UNION ALL instead of UNION when possible</p>

<p><strong>4. JOIN Optimization</strong>
- Join order matters (smaller table first)
- Use appropriate join types
- Index foreign key columns
- Avoid Cartesian products
- Consider temp tables for complex joins</p>""",
        "videos": [
            ("Query Optimization Tutorial", "25 min", "https://www.youtube.com/watch?v=BHwzDmr6d7s", "Data with Baraa"),
            ("SQL Indexing Explained", "20 min", "https://www.youtube.com/watch?v=fsG1XaZEa78", "Programming with Mosh"),
            ("Execution Plans", "18 min", "https://www.youtube.com/watch?v=J4TE3jYIo20", "Brent Ozar")
        ],
        "ai_prompts": [
            ("Understanding Query Optimization", """I'm learning SQL query optimization. Please explain:

1. How do I read an execution plan?
2. What is a table scan vs index seek and which is better?
3. Show me how to identify slow queries
4. What are the most common performance mistakes?
5. Provide examples of before/after query optimization

Use SQL Server with practical examples."""),
            ("Understanding Indexing", """Help me understand SQL indexing:

1. What is the difference between clustered and non-clustered indexes?
2. When should I create an index?
3. Can too many indexes be bad?
4. Show me how to find missing indexes
5. Explain covering indexes and when to use them

Provide beginner-friendly explanations.""")
        ],
        "practice_summary": "Analyze execution plans, add appropriate indexes, optimize slow queries",
        "assignment": """Query Performance Tuning Project:
1. **Baseline:** Run 3-5 slow queries, capture execution time and plans
2. **Analysis:** Identify bottlenecks (table scans, missing indexes, inefficient joins)
3. **Optimization:** Add indexes, rewrite queries, apply best practices
4. **Comparison:** Measure performance improvement (before/after execution time)
5. **Documentation:** Document each optimization with explanation"""
    },

    25: {
        "title": "DAY 25: Integration Project: Excel + SQL + WEEK 5 TEST",
        "learning_objectives": """- Integrate Excel and SQL workflows
- Import SQL data into Excel
- Create automated reports
- Build end-to-end analysis
- Review Week 5 concepts""",
        "topics": """<p><strong>1. Excel-SQL Connection</strong>
- Data → Get Data → From Database → SQL Server
- Write SQL query in Power Query
- Import to Excel table or Power Pivot
- Refresh connection for updated data</p>

<p><strong>2. Integrated Workflow</strong>
- SQL: Extract and aggregate data
- Excel: Analysis, visualization, reporting
- Combine SQL power with Excel flexibility
- Automated refresh schedules</p>

<p><strong>3. Best Practices</strong>
- Do heavy lifting in SQL (filtering, aggregating)
- Use Excel for final formatting and visualization
- Parameter-based queries for flexibility
- Document data sources and refresh frequency</p>

<p><strong>4. End-to-End Project</strong>
- SQL queries for data extraction
- Power Query for transformations
- Power Pivot for data modeling
- Excel dashboard for presentation
- Complete analysis pipeline</p>""",
        "videos": [
            ("Excel SQL Integration", "20 min", "https://www.youtube.com/watch?v=d8WCcEMQ8Pc", "Leila Gharani"),
            ("Power Query SQL", "15 min", "https://www.youtube.com/watch?v=1XQJy_9MqK8", "MyOnlineTrainingHub"),
            ("Automated Reports", "18 min", "https://www.youtube.com/watch?v=0aeZX1l4JT4", "Excel Campus")
        ],
        "ai_prompts": [
            ("Understanding Excel-SQL Integration", """I'm learning to integrate Excel and SQL. Please explain:

1. How do I connect Excel to a SQL database?
2. What should I do in SQL vs what should I do in Excel?
3. Show me how to import SQL query results into Power Pivot
4. How do I create a refreshable connection?
5. Provide a workflow example for monthly sales reports

Use practical examples."""),
            ("Understanding Automated Reporting", """Help me understand automated reporting:

1. How do I create reports that update with one click?
2. What are parameters in SQL queries for Excel?
3. Show me how to schedule automatic data refresh
4. How do I combine multiple SQL queries in Excel?
5. Provide examples for executive dashboard automation

Explain the complete workflow.""")
        ],
        "practice_summary": "Connect Excel to SQL database, import data with Power Query, create automated dashboard",
        "assignment": """Complete Integration Project + Week 5 Test:
1. **SQL Queries:** Write 3-5 optimized queries for sales analysis
2. **Excel Connection:** Import SQL data using Power Query with parameters
3. **Data Model:** Build Power Pivot model with relationships
4. **Dashboard:** Create interactive dashboard with slicers (KPIs, charts, tables)
5. **Automation:** Set up refresh schedule and test
6. **Week 5 Review:** Complete 30-minute test covering Statistical Analysis, Advanced Aggregations, Optimization, Integration"""
    },

    # Week 6 Days
    26: {
        "title": "DAY 26: Excel - Macros & Automation Basics",
        "learning_objectives": """- Record and run macros
- Edit VBA code basics
- Create buttons for macros
- Understand macro security
- Automate repetitive tasks""",
        "topics": """<p><strong>1. Macro Recording</strong>
- Developer tab (enable in Options)
- Record Macro button
- Perform actions to record
- Stop recording
- Macro storage locations</p>

<p><strong>2. Running Macros</strong>
- View → Macros → View Macros
- Assign macro to button or shape
- Keyboard shortcuts
- Quick Access Toolbar
- Macro security settings</p>

<p><strong>3. VBA Editor Basics</strong>
- Alt+F11 to open VBA editor
- Modules, procedures, code structure
- Sub procedures and functions
- Basic VBA: Range, Cells, Worksheets
- Comments and code organization</p>

<p><strong>4. Practical Automation</strong>
- Format data automatically
- Generate reports with one click
- Clear and reset forms
- Copy/paste operations
- Loop through data ranges</p>""",
        "videos": [
            ("Excel Macros Tutorial", "20 min", "https://www.youtube.com/watch?v=AIhKv1IxNTQ", "Leila Gharani"),
            ("VBA for Beginners", "25 min", "https://www.youtube.com/watch?v=G05TrN7nt6k", "MyOnlineTrainingHub"),
            ("Automate Excel Tasks", "15 min", "https://www.youtube.com/watch?v=KHO5NIcZAc4", "Excel Campus")
        ],
        "ai_prompts": [
            ("Understanding Macros", """I'm learning Excel macros. Please explain:

1. What are macros and when should I use them?
2. How do I record a macro and assign it to a button?
3. What is VBA and how is it related to macros?
4. Show me basic VBA code structure
5. Provide examples of common automation tasks

Use beginner-friendly explanations."""),
            ("Understanding VBA Basics", """Help me understand VBA programming:

1. What are the basic VBA objects (Range, Cells, Worksheets)?
2. How do I reference cells and ranges in VBA?
3. Show me how to create a simple loop
4. What are variables and how do I use them?
5. Provide examples for formatting and data manipulation

Explain with simple code examples.""")
        ],
        "practice_summary": "Record macros for common tasks, create buttons, edit simple VBA code",
        "assignment": """Macro Automation Project:
1. **Data Formatting Macro:** Record macro to format raw data (headers, borders, colors, number formats)
2. **Report Generation:** Create macro to generate monthly summary report from data
3. **Button Controls:** Add form buttons to run macros, clear data, reset form
4. **VBA Editing:** Modify recorded macro to add custom logic
5. **Error Handling:** Add basic error handling and user messages"""
    },

    27: {
        "title": "DAY 27: SQL - Advanced Analytics (Cohort, Retention, RFM Analysis)",
        "learning_objectives": """- Perform cohort analysis
- Calculate retention rates
- Conduct RFM analysis
- Build customer segmentation
- Apply advanced analytical techniques""",
        "topics": """<p><strong>1. Cohort Analysis</strong>
- Group customers by acquisition date
- Track behavior over time by cohort
- Example: Month 0, Month 1, Month 2 retention
- Use DATEDIFF and CASE for cohort buckets
- Pivot results for cohort matrix</p>

<p><strong>2. Retention Analysis</strong>
- Calculate repeat purchase rate
- Monthly/quarterly retention cohorts
- Churn rate calculation
- Retention curve visualization
- Identify patterns in customer lifecycle</p>

<p><strong>3. RFM Analysis</strong>
- Recency: Days since last purchase
- Frequency: Number of purchases
- Monetary: Total spending
- Score each dimension (1-5 scale)
- Combine for customer segments
- Example: 555 = Champions, 111 = Lost</p>

<p><strong>4. Customer Segmentation</strong>
- Use NTILE for percentile-based scoring
- Create meaningful segments
- Action strategies per segment
- Lifetime value estimation
- Predictive scoring</p>""",
        "videos": [
            ("Cohort Analysis SQL", "20 min", "https://www.youtube.com/watch?v=7XW1bRYU1Vg", "Data with Baraa"),
            ("RFM Analysis Tutorial", "18 min", "https://www.youtube.com/watch?v=sFaCdxMpC6w", "Alex The Analyst"),
            ("Customer Analytics", "22 min", "https://www.youtube.com/watch?v=gR2K_GksMDY", "Programming with Mosh")
        ],
        "ai_prompts": [
            ("Understanding Cohort Analysis", """I'm learning cohort and retention analysis. Please explain:

1. What is cohort analysis and why is it useful?
2. How do I group customers by signup month and track retention?
3. Show me how to calculate month-over-month retention
4. What is churn rate and how do I calculate it?
5. Provide SQL examples using customer order data

Use SQL Server syntax with clear examples."""),
            ("Understanding RFM Analysis", """Help me understand RFM analysis:

1. What is RFM and what do Recency, Frequency, Monetary mean?
2. How do I calculate RFM scores (1-5 for each)?
3. Show me how to segment customers based on RFM
4. What actions should I take for each segment?
5. Provide complete SQL example with customer data

Explain with step-by-step implementation.""")
        ],
        "practice_summary": "Build cohort retention matrix, calculate RFM scores, create customer segments",
        "assignment": """Advanced Customer Analytics Project:
1. **Cohort Analysis:** Group customers by signup month, calculate retention for each cohort over 12 months
2. **Retention Metrics:** Calculate overall retention rate, churn rate, average customer lifetime
3. **RFM Scoring:** Calculate Recency (days since last order), Frequency (order count), Monetary (total spend); score 1-5 for each
4. **Segmentation:** Create segments (Champions, Loyal, At Risk, Lost) based on RFM scores
5. **Recommendations:** Provide action plan for each customer segment"""
    },

    28: {
        "title": "DAY 28: Excel - Executive Dashboard Creation",
        "learning_objectives": """- Design professional executive dashboards
- Create KPI scorecards
- Build dynamic visualizations
- Apply advanced formatting
- Tell stories with data""",
        "topics": """<p><strong>1. Dashboard Planning</strong>
- Identify key metrics (KPIs)
- Understand audience and purpose
- Sketch layout before building
- Data requirements and sources
- Update frequency</p>

<p><strong>2. KPI Design</strong>
- Card-style metrics
- Comparison to target (arrows, colors)
- Sparklines for trends
- Variance analysis (actual vs budget)
- Year-over-year comparisons</p>

<p><strong>3. Advanced Visualizations</strong>
- Combination charts (targets + actuals)
- Heat maps with conditional formatting
- Bullet charts for performance
- Small multiples for comparison
- Geographical maps</p>

<p><strong>4. Design Best Practices</strong>
- Consistent color scheme
- Minimize chart junk
- Use white space effectively
- Proper font hierarchy
- Mobile/print friendly
- Interactivity with slicers</p>""",
        "videos": [
            ("Executive Dashboard Tutorial", "35 min", "https://www.youtube.com/watch?v=K74_FNnlIF8", "Leila Gharani"),
            ("KPI Dashboard Design", "25 min", "https://www.youtube.com/watch?v=z89v8EGZX_I", "MyOnlineTrainingHub"),
            ("Dashboard Best Practices", "20 min", "https://www.youtube.com/watch?v=OZzVdBBKEFs", "Excel Campus")
        ],
        "ai_prompts": [
            ("Understanding Dashboard Design", """I'm learning executive dashboard design. Please explain:

1. What makes an effective executive dashboard?
2. How do I choose which KPIs to display?
3. Show me how to design KPI cards with variance indicators
4. What chart types work best for different data?
5. Provide examples of good vs bad dashboard designs

Use design principles and Excel techniques."""),
            ("Understanding Data Storytelling", """Help me tell stories with data:

1. How do I guide the viewer through insights?
2. What is the proper hierarchy of information?
3. Show me how to use color effectively
4. How do I balance detail vs simplicity?
5. Provide examples of dashboards that tell clear stories

Explain design thinking for dashboards.""")
        ],
        "practice_summary": "Design KPI scorecard, create executive summary dashboard, apply professional formatting",
        "assignment": """Executive Dashboard Creation:
1. **KPI Scorecard:** Display 6-8 key metrics (Sales, Profit, Customers, Orders) with sparklines, vs target, YoY change
2. **Trend Analysis:** Combo charts showing monthly trends with targets
3. **Performance Breakdown:** Sales by category, region, product (top N)
4. **Heat Map:** Monthly performance matrix with conditional formatting
5. **Professional Design:** Consistent colors, clean layout, interactive slicers, print-ready format"""
    },

    29: {
        "title": "DAY 29: SQL - Complex Business Scenarios",
        "learning_objectives": """- Solve multi-step business problems
- Combine advanced SQL techniques
- Optimize complex queries
- Handle real-world scenarios
- Apply best practices""",
        "topics": """<p><strong>1. Multi-Table Complex Queries</strong>
- Combine JOINs, subqueries, CTEs
- Window functions with aggregations
- Nested CTEs for step-by-step logic
- Handle NULL values properly
- Performance considerations</p>

<p><strong>2. Time-Based Analysis</strong>
- Month-over-month, year-over-year
- Rolling calculations (12-month rolling average)
- Fiscal calendars vs calendar year
- Time-series gaps and islands problems
- Date range overlaps</p>

<p><strong>3. Advanced Patterns</strong>
- Gap analysis (missing sequences)
- Duplicate detection and removal
- Hierarchical queries (bill of materials)
- Graph problems (shortest path)
- Running balance calculations</p>

<p><strong>4. Business Logic Implementation</strong>
- Discount and pricing rules
- Inventory calculations (FIFO, LIFO)
- Allocation algorithms
- Commission calculations
- Complex business rules with CASE</p>""",
        "videos": [
            ("Complex SQL Queries", "25 min", "https://www.youtube.com/watch?v=zJ8_kT8AhsI", "Programming with Mosh"),
            ("Real-World SQL Problems", "30 min", "https://www.youtube.com/watch?v=rGfGmwWRqPE", "Data with Baraa"),
            ("Advanced SQL Patterns", "22 min", "https://www.youtube.com/watch?v=KI2fLk8Q1ak", "Alex The Analyst")
        ],
        "ai_prompts": [
            ("Understanding Complex Queries", """I'm learning to solve complex SQL business problems. Please explain:

1. How do I break down complex requirements into steps?
2. Show me how to combine CTEs, JOINs, and window functions
3. What is the best approach for multi-step calculations?
4. How do I handle edge cases (NULLs, missing data)?
5. Provide example: Calculate customer lifetime value with cohorts

Use step-by-step problem-solving approach."""),
            ("Understanding Business Logic", """Help me implement business logic in SQL:

1. How do I calculate tiered discounts (5% for $100-500, 10% for $500+)?
2. Show me commission calculation (different rates by product category)
3. How do I allocate shared costs across products?
4. Provide example of inventory FIFO calculation
5. Show complex pricing rules implementation

Explain with real business scenarios.""")
        ],
        "practice_summary": "Solve multi-step business problems, implement complex calculations, optimize queries",
        "assignment": """Complex Business Analysis Project:
1. **Customer Lifetime Value:** Calculate CLV considering acquisition cost, retention rate, average order value, purchase frequency
2. **Product Performance:** Identify best/worst performers by multiple metrics, year-over-year comparison, seasonality analysis
3. **Sales Attribution:** Multi-touch attribution model (credit to first, last, and middle touchpoints)
4. **Inventory Analysis:** Calculate stock turnover, identify slow-moving items, forecast reorder quantities
5. **Optimization:** Ensure all queries run efficiently with proper indexes and execution plans"""
    },

    30: {
        "title": "DAY 30: FINAL PROJECT & COMPREHENSIVE ASSESSMENT",
        "learning_objectives": """- Complete end-to-end analytics project
- Demonstrate all learned skills
- Create comprehensive deliverable
- Document analysis process
- Present insights effectively""",
        "topics": """<p><strong>1. Project Requirements</strong>
- Choose business scenario (Sales, HR, Finance, Operations)
- Define business questions to answer
- Identify data sources needed
- Plan analysis approach
- Determine deliverables</p>

<p><strong>2. SQL Component</strong>
- Data extraction queries
- Complex aggregations and calculations
- Window functions and CTEs
- Views and stored procedures
- Query optimization</p>

<p><strong>3. Excel Component</strong>
- Data import and transformation
- Power Query and Power Pivot
- Advanced formulas and calculations
- Interactive dashboard
- Professional formatting</p>

<p><strong>4. Final Deliverable</strong>
- Executive dashboard
- Supporting analysis sheets
- Documentation of methodology
- Key insights and recommendations
- Presentation-ready format</p>""",
        "videos": [
            ("Data Analytics Portfolio", "25 min", "https://www.youtube.com/watch?v=oW3cUCPBpms", "Alex The Analyst"),
            ("Project Presentation Tips", "15 min", "https://www.youtube.com/watch?v=8aN4G29Y1l4", "Data with Baraa"),
            ("Final Project Examples", "30 min", "https://www.youtube.com/watch?v=v5QP3M7pA4Y", "Leila Gharani")
        ],
        "ai_prompts": [
            ("Planning Final Project", """I'm planning my final analytics project. Please help:

1. What makes a strong data analytics portfolio project?
2. How do I choose a business problem to analyze?
3. What structure should my analysis follow?
4. How do I document my methodology?
5. What should I include in my deliverables?

Provide guidance for creating impressive project."""),
            ("Presenting Insights", """Help me present data insights effectively:

1. How do I structure my findings (executive summary, details, recommendations)?
2. What visualizations best communicate different insights?
3. How do I tailor presentation to different audiences?
4. Show me how to create actionable recommendations
5. Provide examples of strong data storytelling

Explain best practices for communication.""")
        ],
        "practice_summary": "Complete comprehensive project combining SQL and Excel skills learned throughout 30 days",
        "assignment": """FINAL COMPREHENSIVE PROJECT:

**Choose ONE scenario:**
A) **E-Commerce Sales Analysis:** Analyze sales performance, customer behavior, product trends, forecasting
B) **HR Workforce Analytics:** Employee retention, turnover analysis, performance metrics, headcount planning
C) **Financial Performance:** Revenue/cost analysis, profitability, budget vs actual, financial forecasting

**Required Components:**

**SQL Analysis:**
1. 10+ queries demonstrating advanced SQL (JOINs, CTEs, window functions, aggregations)
2. Views for repeated reporting
3. Cohort/retention OR RFM analysis
4. Time-based analysis (YoY, MoM)
5. Complex business calculations

**Excel Dashboard:**
1. Power Query connection to SQL or CSV data
2. Power Pivot data model with relationships
3. 8-10 KPIs with trends and comparisons
4. 5+ visualizations (charts, heat maps, etc.)
5. Interactive slicers and filters
6. Professional design

**Documentation:**
1. Business questions being answered
2. Data sources and methodology
3. Key insights (bullet points)
4. Recommendations for action
5. Limitations and assumptions

**Comprehensive Assessment:**
- 60-minute test covering all 30 days
- Mix of Excel and SQL questions
- Practical problems to solve
- Upload final project + take assessment

**Congratulations on completing the 30-Day Excel & SQL Training Program!**"""
    }
}


def generate_day_html(day_num, data):
    """Generate full HTML for a day"""
    html = []

    # Day heading
    html.append(f'<h2 id="day-{day_num}-{data["title"].lower().replace(":", "").replace(" ", "-").replace("&", "").replace("(", "").replace(")", "").replace(",", "").replace("/", "-")}">{data["title"]}</h2>')
    html.append('')

    # Learning objectives
    html.append(f'<p><strong>Learning Objectives:</strong>\n{data["learning_objectives"]}</p>')
    html.append('')

    # Topics
    html.append(f'<h3 id="topics-covered-hour-1---60-min-{day_num}">Topics Covered (60 min):</h3>')
    html.append('')
    html.append(data["topics"])
    html.append('')

    # Videos
    html.append(f'<h3 id="video-resources-{day_num}">📺 Video Resources:</h3>')
    html.append('<ol type="1">')
    for title, duration, url, channel in data["videos"]:
        html.append(f'<li><strong>{title}</strong> ({duration})<br />')
        html.append(f'{url} - {channel}</li>')
    html.append('</ol>')
    html.append('')

    # AI Prompts
    html.append(f'<h3 id="ai-learning-prompts-concept-understanding-only-{day_num}">🤖 AI Learning Prompts (Concept Understanding Only):</h3>')
    html.append('')
    for prompt_title, prompt_text in data["ai_prompts"]:
        html.append(f'<p><strong>{prompt_title}:</strong></p>')
        html.append(f'<pre><code>{prompt_text}</code></pre>')
    html.append('')

    # Practice sections
    html.append(f'<h3 id="guided-practice-hour-2---60-min-{day_num}">Guided Practice (60 min):</h3>')
    html.append('')
    html.append(f'<p><em>{data["practice_summary"]}</em></p>')
    html.append('')

    html.append(f'<h3 id="independent-practice-hour-3---60-min-{day_num}">Independent Practice (60 min):</h3>')
    html.append('')
    html.append(f'<p>Apply the concepts learned to different datasets and scenarios.</p>')
    html.append('')

    # Assignment
    html.append(f'<h3 id="daily-assignment-hour-4---60-min-{day_num}">Daily Assignment (60 min):</h3>')
    html.append('')
    html.append(f'<p><strong>Assignment:</strong></p>')
    html.append(f'<p>{data["assignment"]}</p>')
    html.append('')

    # Expected outcomes
    html.append(f'<h3 id="expected-outcomes-{day_num}">Expected Outcomes:</h3>')
    html.append('<ul>')
    for line in data["learning_objectives"].strip().split('\n'):
        if line.strip().startswith('-'):
            html.append(f'<li>{line.strip()[1:].strip()}</li>')
    html.append('</ul>')
    html.append('')
    html.append('<hr />')
    html.append('')

    return '\n'.join(html)


# Generate all content
print("Generating detailed content for Days 13-30...")

with open('days_13_30_additional.html', 'w', encoding='utf-8') as f:
    for day_num in range(13, 31):
        if day_num in days_data:
            print(f"Generating Day {day_num}...")
            f.write(generate_day_html(day_num, days_data[day_num]))
            f.write('\n')

print("\n✅ Content generation complete!")
print("Generated detailed HTML for Days 13-30")
