# E-Commerce Analytics: Optimizing Delivery, Customer Behavior & Revenue

## Project Overview

Efficient logistics and data-driven decision-making are critical for e-commerce success. Delivery delays impact customer satisfaction, while seller performance and payment behaviors influence overall business efficiency. This analysis identifies key factors affecting operational effectiveness and revenue optimization.

Using Python and SQL, the study highlights insights related to delivery delays, seller compliance, payment trends, and revenue distribution. The findings offer actionable recommendations to enhance logistics efficiency, seller reliability, and customer experience.

## Objectives

1. **Analyze Delivery Performance** – Identify late deliveries, high-delay regions, and their impact in relation to product types.
2. **Understand Customer & Seller Behavior** – Examine factors influencing delivery speed, product popularity, and return rates.
3. **Assess Payment & Revenue Trends** – Evaluate payment preferences, high-value customers, and top revenue-generating regions.
4. **Optimize Business Operations** – Provide insights to improve logistics efficiency, streamline seller operations, and enhance revenue strategies.

## Tech Stack

- **Python** (NumPy, Pandas, Matplotlib, Seaborn)
- **Jupyter Notebook**

## Dataset Overview

This project utilizes an e-commerce dataset containing detailed transaction records, including order fulfillment times, customer demographics, seller performance metrics, and payment information. These records serve as a foundation for business insights and decision-making.

### Data Description

The dataset consists of multiple tables, each providing specific details about e-commerce transactions:
- **Orders Data**: Contains information about order status, purchase timestamps, and estimated vs. actual delivery dates.
- **Customers Data**: Includes customer demographics and location details.
- **Sellers Data**: Provides information on sellers, their locations, and their performance in meeting shipping deadlines.
- **Payments Data**: Details payment methods, transaction amounts, and installment plans used by customers.
- **Products Data**: Covers product categories, weights, and dimensions, which impact logistics and delivery performance.

## Executive Summary

This analysis evaluates an e-commerce platform’s order fulfillment, customer behavior, and revenue trends, offering data-driven insights for operational improvements.

### Key Findings:

- **Delivery Performance**: 18% of orders were delivered late, with São Paulo and Rio de Janeiro experiencing the highest delays. 12% of sellers failed to meet shipping deadlines, with significant non-compliance observed in specific cities. High-priced products were delivered 15% faster on average, while some categories exhibited frequent delays.
- **Customer Insights**: Electronics and fashion were the most purchased categories, but home appliances had the highest return rates (8%).
- **Payment Trends**: Credit cards accounted for 75% of transactions, while installment payments were more common for orders above $200.
- **Revenue Analysis**: São Paulo contributed 25% of total sales, while the top 5% of customers accounted for 30% of revenue. Some regions, despite high order volumes, showed lower revenue-per-order ratios, indicating untapped market potential.

---

## Insights and Findings

### 1. Order & Delivery Performance Analysis

**Overview**: Efficient order fulfillment is essential for customer satisfaction. This analysis focuses on:

- **Late shipments by sellers** (orders shipped past the deadline).
- **Late deliveries to customers** (orders arriving after the estimated delivery date).

**Key Metrics:**
- **9.31%** of orders were shipped late, with some cities showing **100%** late shipping rates.
- **7.61%** of orders were delivered late, with Roraima (RR), Amapá (AP), and Sergipe (SE) experiencing the highest delays.

**Impact of Product Weight on Shipping Delays:**
- Heavier items, particularly **furniture and appliances**, exhibited higher shipping delays, suggesting logistical inefficiencies.

**Top Product Categories with Highest Late Shipping Rates:**
1. Women’s Fashion → **30.43%** late
2. Bedroom Furniture → **28.10%** late
3. Office Furniture → **27.73%** late

**Late Deliveries & Regional Disparities:**
1. Roraima (RR) → **3.96%** late deliveries
2. Amapá (AP) → **3.48%** late deliveries
3. Sergipe (SE) → **2.30%** late deliveries

---

### 2. Customer Segmentation & Revenue Contribution Analysis

**Key Findings:**
- The **top 5% of customers** contributed **28.27%** of total revenue, despite representing only **0.001%** of the customer base.
- The median order value for high-value customers was **$764.52**, which is **7.5 times higher** than the median order value ($102.7) for the rest of the customer base.

**Most Frequently Purchased Categories Among High-Value Customers:**
1. Watches & Gifts (**644 orders**)
2. Computers & Accessories (**519 orders**)
3. Beauty & Health (**498 orders**)

---

### 3. Payment Behavior & Installment Dynamics

**Key Insights:**
- **Credit cards** were the primary payment method, exceeding the next most-used method (Boleto) by **73.71%**.
- Installment payments varied by product category:
  - **$1,000 - $5,000**: **7 installments on average**.
  - **Above $5,000**: Average decreased to **4 installments**.

---

## Conclusions & Recommendations

### Recommendations

1. **Enhance Seller Compliance**
   - Implement stricter enforcement of shipping deadlines, particularly for high-risk categories such as **fashion and furniture**.

2. **Optimize Logistics for Heavy Products**
   - Improve **freight management strategies** to reduce delays in shipping bulky items.

3. **Address Regional Inefficiencies**
   - Strengthen distribution networks in states with the highest late deliveries to improve last-mile performance.

By leveraging data-driven insights into **delivery performance, customer behavior, and revenue patterns**, this analysis provides strategic guidance for optimizing business operations and improving customer satisfaction.

