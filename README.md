# Global Supply Chain Disruption & Mitigation Analytics

**An end-to-end data analytics project analyzing 10,000 global shipments to identify disruption patterns and evaluate mitigation strategy effectiveness.**
## Live Dashboard

*Note: Requires Microsoft Edge or Chrome*

![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![DAX](https://img.shields.io/badge/DAX-orange?style=for-the-badge)

---

## Table of Contents
- [Project Overview](#project-overview)
- [Business Problem](#business-problem)
- [Key Insights](#key-insights)
- [Technical Stack](#technical-stack)
- [Dashboard Features](#dashboard-features)
- [Data Model](#data-model)
- [Methodology](#methodology)
- [How to Use](#how-to-use)
- [Future Enhancements](#future-enhancements)
- [Contact](#contact)

---

## Project Overview

This project simulates a real-world supply chain analytics scenario where a global logistics company needs to:
- Identify high-risk trade routes and disruption patterns
- Evaluate the effectiveness of mitigation strategies (expedited shipping, re-routing)
- Optimize decision-making for future disruptions

**Dataset:** [10,000 shipment records across major global trade routes (2023-2025)](https://www.kaggle.com/datasets/bertnardomariouskono/global-supply-chain-disruption-and-resilience)  
**Tools:** Python, Power BI, DAX, Star Schema Modeling  
**Deliverable:** 4-page interactive dashboard with prescriptive analytics

---

## Business Problem

Global supply chains face increasing disruptions from:
- **Geopolitical conflicts** (e.g., Suez Canal blockages)
- **Severe weather events** (typhoons, storms)
- **Port congestion**

**Business Questions:**
1. Which routes and products are most vulnerable to delays?
2. Do mitigation actions (expedited air freight, re-routing) actually reduce delivery times?
3. What is the ROI of proactive mitigation strategies?
4. How should the company prioritize mitigation resources?

---

## Key Insights

### 1. **Proactive Mitigation Works**
- Expedited Air Freight saves **2.83 days** on average for disrupted shipments
- Applied with **100% consistency** to high-value products (Semiconductors, Pharmaceuticals)
- Cost premium: $48,980 per shipment
- **ROI: Positive** when considering delay penalties and product value

### 2. **Re-routing Is Unavoidable, Not Optional**
- When geopolitical conflicts block routes, re-routing adds **18.48 days**
- All 368 Geopolitical Conflict shipments required re-routing (no alternative)
- This isn't mitigation failure—it's damage control when routes are physically inaccessible

### 3. **Risk Concentration**
- **Suez route:** Highest geopolitical risk (1,241 high-risk shipments)
- **Pacific route:** Vulnerable to severe weather (seasonal patterns identified)
- **Port Congestion:** Adds 3 days on average but responds well to expedited mitigation

### 4. **Strategic Product Prioritization**
- High-value products (Semiconductors, Pharmaceuticals) receive 100% expedited mitigation
- Lower-value products (Textiles, Raw Materials) use standard shipping even when disrupted
- This strategic allocation optimizes total cost vs. delay risk

---

## Technical Stack

### **Data Processing & ETL**
- **Python 3**: Data cleaning, transformation, feature engineering
- **Pandas & NumPy**: Data manipulation and calculated columns
- **Star Schema Design**: Fact and dimension tables for optimal query performance

### **Business Intelligence**
- **Power BI Desktop**: Interactive dashboard development
- **DAX (Data Analysis Expressions)**: 50+ custom measures for advanced calculations
- **Power Query**: Data shaping and preprocessing

### **Data Modeling**
- **Star Schema Architecture**:
  - 1 Fact Table: `Fact_Shipments` (10,000 records)
  - 4 Dimension Tables: `Dim_Routes`, `Dim_Products`, `Dim_Disruptions`, `Dim_Date`
- **Relationships**: Many-to-One with single filter direction
- **Performance Optimization**: Proper indexing via foreign keys

---

## Dashboard Features

### **Page 1: Executive Overview**
High-level KPIs for leadership decision-making
- Total shipments, on-time %, average delay, total cost
- Disruption trends over time
- Delivery status breakdown
- Interactive slicers for dynamic filtering

### **Page 2: Risk Intelligence**
Root cause analysis of delays and disruptions
- Risk distribution heatmap by route
- Geopolitical risk vs. delay correlation (scatter plot)
- Weather severity trends with seasonal patterns
- Top 10 high-risk routes with drill-down capability

### **Page 3: Mitigation Effectiveness**
Prescriptive analytics for strategy optimization
- **Key Finding:** Separated proactive mitigation (expedited) from forced mitigation (re-routing)
- Time saved and cost premium analysis
- Adoption rate by product category
- ROI calculation with business value quantification

### **Page 4: Operational Details**
Granular shipment tracking for operational teams
- Searchable, sortable table of all 10,000 shipments
- Conditional formatting for late deliveries and high delays
- Route performance comparison
- Export capability for offline analysis

---

## Data Model

```
┌─────────────────┐
│   Dim_Date      │
│  (Date Table)   │
└────────┬────────┘
         │
         │ 1:Many
         ▼
┌─────────────────────────────────────┐
│         Fact_Shipments              │
│  • Order_ID (PK)                   │
│  • Order_Date (FK)                 │◄─────┬
│  • Route_ID (FK)                   │      │
│  • Product_ID (FK)                 │      │
│  • Disruption_ID (FK)              │      │
│  • Delay_Days                      │      │
│  • Shipping_Cost_USD               │      │
│  • Geopolitical_Risk_Index         │      │
│  • Weather_Severity_Index          │      │
│  • Mitigation_Action_Taken         │      │
└─┬──────────┬──────────┬────────────┘      │
  │          │          │                    │
  │ Many:1   │ Many:1   │ Many:1            │ Many:1
  ▼          ▼          ▼                    ▼
┌──────────┐ ┌────────┐ ┌────────────┐ ┌──────────┐
│Dim_Routes│ │Dim_    │ │Dim_        │ │  (back   │
│          │ │Products│ │Disruptions │ │   to     │
└──────────┘ └────────┘ └────────────┘ │  Date)   │
                                        └──────────┘
```

---

## Methodology

### **1. Data Preprocessing (Python)**
```python
# Key transformations applied:
- Converted blank disruptions to "No Disruption" category
- Created risk level categories (Low/Medium/High) from continuous risk index
- Extracted time dimensions (Year, Quarter, Month)
- Calculated cost per day and delay cost metrics
- Built star schema with proper foreign key relationships
```

### **2. Analytical Approach**

**Initial Challenge:**
When comparing mitigation vs. no mitigation overall, results showed mitigation *increased* delays (by 8.11 days). This was counterintuitive.

**Root Cause Analysis:**
Discovered **selection bias**—mitigation actions were applied to:
- More severe disruptions (higher risk indices)
- More complex routes (longer base lead times)
- Higher-value products (where speed matters more)

**Solution:**
Separated analysis into two strategies:
1. **Proactive Mitigation** (Expedited Air Freight): Compare like-to-like within same disruption severity
2. **Forced Mitigation** (Re-routing): Recognize as unavoidable when routes are blocked

**Result:** Expedited Air Freight saves 2.83 days; Re-routing is necessary damage control.

### **3. Key DAX Measures**

```dax
// Time saved by expedited mitigation
Time Saved - Expedited = 
VAR StandardTime = 
    CALCULATE(
        AVERAGE(Fact_Shipments[Actual_Lead_Time_Days]),
        Fact_Shipments[Disruption_Event] <> "No Disruption",
        Fact_Shipments[Mitigation_Action_Taken] = "Standard Shipping"
    )
VAR ExpeditedTime = 
    CALCULATE(
        AVERAGE(Fact_Shipments[Actual_Lead_Time_Days]),
        Fact_Shipments[Mitigation_Action_Taken] = "Expedited Air Freight"
    )
RETURN StandardTime - ExpeditedTime
```

---

## How to Use

### **Prerequisites**
- Power BI Desktop (latest version)
- Python 3.x with pandas and numpy (for data preprocessing)

### **Setup Instructions**

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/supply-chain-analytics.git
cd supply-chain-analytics
```

2. **Run data preprocessing**
```bash
python data_prep.py
```
This generates:
- `fact_shipments.csv`
- `dim_routes.csv`
- `dim_products.csv`
- `dim_disruptions.csv`

3. **Open Power BI file**
- Open `SupplyChain.pbix` in Power BI Desktop
- Data is embedded, no refresh needed
- Explore the 4 dashboard pages

4. **Interact with the dashboard**
- Use slicers to filter by Year, Product, Route, Disruption
- Click visuals to cross-filter related charts
- Right-click data points to drill through to operational details
- Export data from tables for offline analysis

---

## Future Enhancements

### **Technical Improvements**
- [ ] Connect to live SQL database for real-time updates
- [ ] Implement incremental refresh for large datasets
- [ ] Add predictive analytics using Python visuals (ARIMA forecasting)
- [ ] Create mobile-optimized dashboard layout

### **Business Extensions**
- [ ] Add inventory cost modeling (carrying cost vs. stockout risk)
- [ ] Include carbon footprint analysis by transportation mode
- [ ] Integrate supplier performance metrics
- [ ] Build what-if scenario modeling for route planning

### **Advanced Analytics**
- [ ] Machine learning model to predict optimal mitigation action
- [ ] Clustering analysis to identify route similarities
- [ ] Sensitivity analysis on cost parameters
- [ ] Network analysis for multi-hop shipment optimization

---

## Key Learnings

### **Data Analytics Skills Demonstrated**
 **End-to-end pipeline**: Raw data → Cleaned data → Data model → Insights  
 **Critical thinking**: Identified and corrected for selection bias in analysis  
 **Business acumen**: Translated data findings into actionable recommendations  
 **Storytelling**: Created narrative-driven dashboard with clear insights  
 **Technical depth**: Advanced DAX, star schema, conditional formatting

### **Recruiter-Friendly Highlights**
- **Prescriptive Analytics**: Not just "what happened" but "what should we do"
- **ROI Quantification**: Demonstrated business value of mitigation strategies
- **Data Quality Awareness**: Caught and corrected misleading initial results
- **Professional Presentation**: Production-ready dashboard with polished visuals

---

## Contact

**Your Name**  
Email: your.email@example.com  
LinkedIn: [linkedin.com/in/Mercuryy200](https://linkedin.com/in/Mercuryy200)  
GitHub: [github.com/rima-nafougui](https://github.com/rima-nafougui)

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Dataset : [Global Supply Chain Disruption & Resilience](https://www.kaggle.com/datasets/bertnardomariouskono/global-supply-chain-disruption-and-resilience)
- Methodology influenced by supply chain management best practices
- Dashboard design follows Power BI visualization guidelines
