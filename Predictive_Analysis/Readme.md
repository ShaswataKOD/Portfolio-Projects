# 🛍️ Customer Segmentation & Purchase Behavior Analysis

## 📊 Project Overview
This project dives deep into understanding customer purchase behavior using the UK Online Retail Dataset (2010-2011). The aim is to identify valuable customer segments, understand seasonal sales trends, and provide actionable strategies for increasing revenue and retention.

## 🧠 Skills Demonstrated
- Data Cleaning & Preprocessing (handling missing data, duplicates)
- RFM Analysis for Customer Segmentation
- Exploratory Data Analysis (EDA)
- Time Series Analysis & Seasonality Trends
- Data Visualization (Matplotlib, Seaborn)
- Business Recommendations & Strategic Thinking

## ⚙️ Tools & Technologies Used
- **Language:** Python (Pandas, NumPy)
- **Visualization:** Seaborn, Matplotlib
- **Analysis:** RFM, GroupBy Aggregations
- **Environment:** Jupyter Notebook

## 📁 Project Structure
| Folder/File | Description |
|-------------|-------------|
| `Retail_Data.csv` | Raw transactional data |
| `customer_analysis.ipynb` | Main notebook for EDA and segmentation |
| `images/` | Saved plots and visualizations |
| `README.md` | Project overview and findings |

## 📂 Data Description
- **Dataset:** UK Online Retail Dataset (Dec 2010–Dec 2011)
- **Rows:** 541,909
- **Columns:** InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country

## 🧹 Data Cleaning & Preprocessing
- Removed missing Customer IDs (~20% of rows)
- Converted `InvoiceDate` to datetime format
- Created new variables: `TotalPrice = Quantity * UnitPrice`

## 📌 Customer Behavior & Segmentation Report
### 🎯 RFM Analysis
- **Recency:** Days since last purchase
- **Frequency:** Number of transactions
- **Monetary:** Total money spent

### 📊 Segments Identified:
- **Champions:** High recency, high frequency, high spenders
- **Loyal Customers:** Frequent buyers with decent monetary value
- **Potential Loyalists:** New customers with recent activity
- **At Risk:** Haven't purchased in a while
- **Lost:** Inactive for a long time

## 🧾 Summary of Key Insights
- 🏆 **Top 10% of customers contribute 52% of total revenue**, suggesting high revenue concentration.
- ⚠️ **29% of customers are At-Risk or Lost**, indicating a high churn risk but also opportunity for recovery.
- 📈 **Sales peak in November & December** due to seasonal promotions, while May–June see downturns.
- 🛍️ **Average Order Value (AOV)** is highest during peak months, implying bulk or high-value purchases.
- 💡 **5 customer segments** identified — with Loyal and Regular customers being key targets for retention and revenue growth.

## 📈 Seasonality & AOV Trends
- **Revenue spikes** in Nov-Dec (Christmas promotions)
- **Low seasons** observed in summer months (May–June)
- **AOV increases** significantly in Q4

## 🔎 Churn Rate Analysis
- **Churn rate calculated using customer inactivity (90+ days)**
- Identified customer loss patterns over quarters
- RFM segments "Lost" and "At Risk" correlate highly with churn

## 🌍 Purchase Behavior Across Regions
- Highest revenue from **United Kingdom** (home base)
- B2B vs B2C segmentation observed by invoice volume and AOV

## 🎯 Recommendations
1. **Loyalty Program:** Reward top-tier segments like Champions and Loyal Customers.
2. **Win-Back Campaigns:** Target "At Risk" customers with discounts and reminders.
3. **Seasonal Promotions:** Boost marketing in Q4 and low seasons to even out revenue.
4. **Bulk Order Incentives:** Encourage high-volume B2B customers with pricing strategies.

## 🔮 Future Work
- Apply clustering algorithms (e.g., K-Means) to validate RFM-based segments.
- Predict churn using classification models.
- Build a dashboard using Tableau or Power BI for real-time monitoring.

---

