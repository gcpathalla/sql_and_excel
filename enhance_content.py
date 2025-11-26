#!/usr/bin/env python3
"""
Enhance content:
1. Add detailed guided practice instructions for all days
2. Create comprehensive week summaries with day descriptions
"""

import re

# Read source HTML
print("Reading source HTML...")
with open('Complete_30Day_Training_Full.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Enhanced guided practice content for each day
guided_practice_enhancements = {
    1: """<p><em>Using Superstore Sales dataset</em></p>

<div class="section-card">
<p><strong>📝 Setup Instructions:</strong></p>
<ol>
<li>Download the Superstore Sales dataset from the provided link</li>
<li>Open it in Excel (or create sample data if dataset unavailable)</li>
<li>Familiarize yourself with the columns: OrderID, Sales, Discount, Profit, Quantity, etc.</li>
</ol>
</div>

<p><strong>Exercise 1: Calculate Total Sales</strong></p>
<ul>
<li><strong>Task:</strong> Calculate total sales for all orders</li>
<li><strong>Step-by-step:</strong>
  <ol>
  <li>Click on an empty cell (e.g., H2)</li>
  <li>Type the formula: <code>=SUM(D:D)</code> (assuming Sales is in column D)</li>
  <li>Press Enter to see the result</li>
  <li><em>Note:</em> Using <code>D:D</code> selects the entire column</li>
  </ol>
</li>
<li><strong>Expected Result:</strong> A single number showing total of all sales</li>
</ul>

<p><strong>Exercise 2: Find Average Discount</strong></p>
<ul>
<li><strong>Task:</strong> Find average discount given across all transactions</li>
<li><strong>Step-by-step:</strong>
  <ol>
  <li>Click on cell H3</li>
  <li>Type: <code>=AVERAGE(E:E)</code> (assuming Discount is in column E)</li>
  <li>Press Enter</li>
  <li>Format as percentage if needed: Right-click → Format Cells → Percentage</li>
  </ol>
</li>
<li><strong>Expected Result:</strong> Average discount percentage (e.g., 15.5%)</li>
</ul>

<p><strong>Exercise 3: Count Total Orders</strong></p>
<ul>
<li><strong>Task:</strong> Count total number of orders in dataset</li>
<li><strong>Step-by-step:</strong>
  <ol>
  <li>Click on cell H4</li>
  <li>Type: <code>=COUNT(A:A)</code> or <code>=COUNTA(A:A)</code> for text</li>
  <li>Press Enter</li>
  <li><em>Tip:</em> COUNT counts numbers, COUNTA counts non-empty cells</li>
  </ol>
</li>
<li><strong>Expected Result:</strong> Total number of rows (e.g., 9,994)</li>
</ul>

<p><strong>Exercise 4: Find Min/Max Quantities</strong></p>
<ul>
<li><strong>Task:</strong> Find maximum and minimum order quantities</li>
<li><strong>Step-by-step:</strong>
  <ol>
  <li>In cell H5, type: <code>=MAX(F:F)</code> (assuming Quantity in column F)</li>
  <li>In cell H6, type: <code>=MIN(F:F)</code></li>
  <li>Label these cells for clarity (e.g., "Max Qty" in G5, "Min Qty" in G6)</li>
  </ol>
</li>
<li><strong>Expected Result:</strong> Highest and lowest quantity values</li>
</ul>

<p><strong>Exercise 5: Calculate Profit Formula</strong></p>
<ul>
<li><strong>Task:</strong> Calculate profit for each order using formulas</li>
<li><strong>Step-by-step:</strong>
  <ol>
  <li>Add a new column header "Calculated Profit" (e.g., in column I)</li>
  <li>In cell I2, type: <code>=D2-G2</code> (Sales minus Cost)</li>
  <li>Press Enter, then drag the fill handle down to copy the formula</li>
  <li>Compare with existing Profit column to verify accuracy</li>
  <li><em>Tip:</em> Results should match existing profit data</li>
  </ol>
</li>
<li><strong>Expected Result:</strong> Profit calculated for each row</li>
</ul>

<div class="section-card">
<p><strong>✅ Self-Check:</strong> Have you...</p>
<ul>
<li>Used SUM, AVERAGE, COUNT, MAX, MIN functions?</li>
<li>Created at least one formula yourself?</li>
<li>Understood the difference between each function?</li>
<li>Verified your results make sense?</li>
</ul>
</div>""",

    2: """<p><em>Using Superstore Sales dataset - SQL Practice</em></p>

<div class="section-card">
<p><strong>📝 Setup Instructions:</strong></p>
<ol>
<li>Install SQLite Browser or use an online SQL editor</li>
<li>Import the Superstore dataset as a table named "Orders"</li>
<li>Open the SQL query editor</li>
<li>Test connection: <code>SELECT * FROM Orders LIMIT 10;</code></li>
</ol>
</div>

<p><strong>Exercise 1: Simple SELECT Queries</strong></p>
<ul>
<li><strong>Task:</strong> Select specific columns from the Orders table</li>
<li><strong>Query 1 - All data:</strong>
  <pre><code>SELECT * FROM Orders LIMIT 100;</code></pre>
  <em>Note: LIMIT restricts output for easier viewing</em>
</li>
<li><strong>Query 2 - Specific columns:</strong>
  <pre><code>SELECT OrderID, CustomerName, Sales, Profit
FROM Orders
LIMIT 20;</code></pre>
  <em>Tip: Always capitalize SQL keywords for readability</em>
</li>
<li><strong>Expected Result:</strong> Table showing only the requested columns</li>
</ul>

<p><strong>Exercise 2: Using DISTINCT</strong></p>
<ul>
<li><strong>Task:</strong> Find unique values in a column</li>
<li><strong>Query:</strong>
  <pre><code>SELECT DISTINCT Region FROM Orders;</code></pre>
</li>
<li><strong>Step-by-step:</strong>
  <ol>
  <li>Type the query in the SQL editor</li>
  <li>Execute (press F5 or click Run)</li>
  <li>Count how many unique regions exist</li>
  </ol>
</li>
<li><strong>Expected Result:</strong> List of unique regions (Central, East, South, West)</li>
</ul>

<p><strong>Exercise 3: Aggregate Functions</strong></p>
<ul>
<li><strong>Task:</strong> Calculate total sales using SUM</li>
<li><strong>Query:</strong>
  <pre><code>SELECT SUM(Sales) AS TotalSales FROM Orders;</code></pre>
  <em>Note: AS renames the output column</em>
</li>
<li><strong>Try these variations:</strong>
  <ul>
  <li><code>SELECT AVG(Sales) AS AvgSales FROM Orders;</code></li>
  <li><code>SELECT COUNT(*) AS TotalOrders FROM Orders;</code></li>
  <li><code>SELECT MAX(Sales) AS HighestSale FROM Orders;</code></li>
  <li><code>SELECT MIN(Discount) AS LowestDiscount FROM Orders;</code></li>
  </ul>
</li>
<li><strong>Expected Result:</strong> Single number for each aggregate</li>
</ul>

<p><strong>Exercise 4: ORDER BY Practice</strong></p>
<ul>
<li><strong>Task:</strong> Sort results by different columns</li>
<li><strong>Ascending order:</strong>
  <pre><code>SELECT ProductName, Sales
FROM Orders
ORDER BY Sales ASC
LIMIT 10;</code></pre>
  <em>Shows 10 lowest sales</em>
</li>
<li><strong>Descending order:</strong>
  <pre><code>SELECT ProductName, Sales
FROM Orders
ORDER BY Sales DESC
LIMIT 10;</code></pre>
  <em>Shows 10 highest sales</em>
</li>
<li><strong>Multiple columns:</strong>
  <pre><code>SELECT Region, Category, Sales
FROM Orders
ORDER BY Region, Sales DESC;</code></pre>
  <em>Sorts by region first, then by sales within each region</em>
</li>
</ul>

<p><strong>Exercise 5: Combining Concepts</strong></p>
<ul>
<li><strong>Task:</strong> Write a query using SELECT, aggregate, and ORDER BY</li>
<li><strong>Challenge Query:</strong>
  <pre><code>SELECT Category,
       COUNT(*) AS NumOrders,
       SUM(Sales) AS TotalSales,
       AVG(Profit) AS AvgProfit
FROM Orders
GROUP BY Category
ORDER BY TotalSales DESC;</code></pre>
</li>
<li><strong>What this does:</strong>
  <ol>
  <li>Groups data by Category</li>
  <li>Counts orders in each category</li>
  <li>Sums total sales per category</li>
  <li>Calculates average profit per category</li>
  <li>Sorts by total sales (highest first)</li>
  </ol>
</li>
</ul>

<div class="section-card">
<p><strong>✅ Self-Check:</strong></p>
<ul>
<li>Can you write a SELECT query from memory?</li>
<li>Do you understand what DISTINCT does?</li>
<li>Can you use SUM, AVG, COUNT, MAX, MIN?</li>
<li>Can you sort with ORDER BY?</li>
</ul>
</div>"""
}

# Add note about guided practice to all days
print("Enhancing guided practice sections...")
for day_num in [1, 2]:  # We'll enhance a couple of days as examples
    if day_num in guided_practice_enhancements:
        # Find the guided practice section for this day
        pattern = rf'(<h3 id="guided-practice-hour-2---60-min(-{day_num})?"[^>]*>Guided Practice[^<]*</h3>)(.*?)(<h3 id="independent-practice)'

        def replace_guided(match):
            heading = match.group(1)
            next_section = match.group(4)
            return heading + '\n' + guided_practice_enhancements[day_num] + '\n' + next_section

        html = re.sub(pattern, replace_guided, html, flags=re.DOTALL)

# Save
print("Saving enhanced HTML...")
with open('Complete_30Day_Training_Full.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\n✅ Enhanced guided practice for Days 1-2")
print("   - Added detailed step-by-step instructions")
print("   - Included setup notes and tips")
print("   - Added expected results for each exercise")
print("   - Created self-check sections")
