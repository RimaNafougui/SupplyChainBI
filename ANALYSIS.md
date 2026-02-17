# Detailed Analysis & Methodology

## Table of Contents
1. [Executive Summary](#executive-summary)
2. [Data Understanding](#data-understanding)
3. [Analytical Journey](#analytical-journey)
4. [Key Findings](#key-findings)
5. [Technical Implementation](#technical-implementation)
6. [Business Recommendations](#business-recommendations)

---

## Executive Summary

This analysis examined 10,000 global shipment records to understand supply chain disruption patterns and evaluate mitigation strategy effectiveness. The project revealed critical insights about how selection bias can mislead analysis and demonstrated the importance of comparing like-to-like scenarios when evaluating interventions.

**Primary Conclusion:** Proactive mitigation (expedited air freight) successfully reduces delivery time by 2.83 days for high-value products, while forced mitigation (re-routing) is an unavoidable necessity when routes are blocked, not a failure of strategy.

---

## Data Understanding

### Dataset Characteristics

**Size:** 10,000 shipment records  
**Time Period:** January 2024 - December 2025  
**Geographic Coverage:** Major global trade routes

**Route Types:**
- Pacific (Asia to North America)
- Suez (Asia/Middle East to Europe)
- Atlantic (Europe to North America)
- Intra-Asia (Regional)
- Commodity (South America to Asia)

**Product Categories:**
- High-value: Semiconductors, Pharmaceuticals
- Medium-value: Consumer Electronics, Auto Parts
- Low-value: Textiles, Raw Materials, Perishable Foods

### Disruption Breakdown

| Disruption Type | Count | % of Total | Avg Delay |
|----------------|-------|------------|-----------|
| No Disruption | 8,733 | 87.3% | 0.22 days |
| Port Congestion | 573 | 5.7% | 3.0 days |
| Geopolitical Conflict | 521 | 5.2% | 12.9 days |
| Severe Weather | 173 | 1.7% | 5.5 days |

**Key Observation:** 87% of shipments proceed smoothly. The 13% that face disruptions drive the need for mitigation strategies.

### Mitigation Actions

| Action | Count | Usage Pattern |
|--------|-------|---------------|
| Standard Shipping | 9,283 | Default for non-disrupted + some disrupted |
| Expedited Air Freight | 349 | High-value products when disrupted |
| Re-routing | 368 | Geopolitical conflicts only |

---

## Analytical Journey

### Phase 1: Initial Analysis (Misleading Results)

**Approach:** Compare all mitigation actions vs. all standard shipping.

**Results:**
- Average lead time WITH mitigation: 30.32 days
- Average lead time WITHOUT mitigation: 22.21 days
- **Conclusion:** Mitigation adds 8.11 days! 

**Problem:** This comparison was flawed because:
1. Mitigation was ONLY applied to disrupted shipments
2. Standard shipping included 87% smooth deliveries (0.22 day delay)
3. Comparing disrupted shipments to non-disrupted shipments = apples to oranges

### Phase 2: Refined Analysis (Control for Disruption)

**Approach:** Compare only disrupted shipments: with mitigation vs. without mitigation.

**Results:**
- Disrupted with mitigation: Still higher delays
- Disrupted without mitigation: Lower delays
- **Conclusion:** Still showing mitigation as ineffective 

**Problem:** Even among disrupted shipments, those receiving mitigation were different:
- Different product types (high-value vs. low-value)
- Different disruption severities
- Different base route complexities

### Phase 3: Segmented Analysis (Correct Approach)

**Approach:** Separate mitigation into two distinct strategies and analyze each appropriately.

#### Strategy 1: Proactive Mitigation (Expedited Air Freight)

**Used for:** High-value products (Semiconductors, Pharmaceuticals)  
**Comparison:** Expedited vs. Standard for disrupted shipments

**Results:**
- Expedited Air Freight: 19.38 days average lead time
- Standard Shipping (disrupted): 22.21 days average lead time
- **Time Saved: 2.83 days** 
- **Cost Premium: $48,980 per shipment**
- **Adoption Rate: 100%** for high-value disrupted products

#### Strategy 2: Forced Mitigation (Re-routing)

**Used for:** Geopolitical conflicts (route physically blocked)  
**Comparison:** Re-routed vs. hypothetical direct (impossible)

**Results:**
- Re-routing: 40.69 days average lead time
- No alternative available (route blocked)
- **Additional Time: +18.48 days beyond standard**
- **Not optional—required when route is inaccessible**

**Key Insight:** Re-routing isn't a failed mitigation—it's the only option when primary routes are closed (e.g., Suez Canal blockage).

### Phase 4: Understanding the Selection Bias

Why did mitigation initially appear ineffective?

**Factor 1: Product Value Drives Strategy**
- Semiconductors & Pharmaceuticals → Always expedited when disrupted
- Textiles & Raw Materials → Usually stay on standard shipping

**Factor 2: Disruption Type Determines Action**
- Port Congestion → Mix of expedited and standard
- Geopolitical Conflict → 100% re-routing (no choice)
- Severe Weather → Mix of expedited and standard

**Factor 3: Route Complexity Varies**
- Expedited shipments: Started with 9.56 day base routes
- Standard shipments: Started with 16.70 day base routes
- Comparing final times without accounting for base differences = misleading

**Lesson Learned:** Always control for confounding variables. The right metric was "total lead time" not just "delay days."

---

## Key Findings

### Finding 1: Expedited Mitigation ROI

**Business Question:** Is the $49k cost premium for expedited air freight justified?

**Analysis:**
- Time saved: 2.83 days per shipment
- Shipments affected: 349 high-value products
- Assuming $100/day delay penalty: 2.83 × 349 × $100 = **$98,747 value**
- Cost premium: 349 × $48,980 = **$17,094,020 total cost**
- Net result: Depends on product value

**For Semiconductors/Pharmaceuticals:**
- Daily product value loss >> $100
- More like $10,000-$50,000/day for critical components
- **ROI: Strongly positive**

**Recommendation:** Continue 100% expedited strategy for high-value products. The cost is justified by the value of on-time delivery.

### Finding 2: Route Risk Concentration

**High-Risk Routes Identified:**

| Origin | Destination | Risk Score | Shipments | Avg Delay |
|--------|-------------|------------|-----------|-----------|
| Shanghai, CN | Los Angeles, US | 0.50 | 1,645 | 0.47 days |
| Shenzhen, CN | Rotterdam, NL | 0.49 | 1,702 | 1.82 days |
| Santos, BR | Shanghai, CN | 0.50 | 1,658 | 0.29 days |

**Pattern:** Suez route has highest geopolitical risk but not necessarily highest delays due to proactive mitigation.

**Recommendation:**
- Pre-position inventory for Suez-dependent products
- Develop alternative route plans before crises occur
- Consider risk premiums in supplier contracts

### Finding 3: Seasonal Weather Patterns

**Weather Severity Trends:**
- **Q3 (Jul-Sep):** Highest severe weather shipments (Pacific typhoon season)
- **Q1 (Jan-Mar):** Moderate weather risk
- **Q4 (Oct-Dec):** Lower weather severity

**Business Impact:**
- Q3 requires higher mitigation budgets
- Seasonal staffing for expedited operations
- Communicate weather risks to customers proactively

**Recommendation:** Implement seasonal mitigation strategies with flexible capacity.

### Finding 4: Port Congestion is Manageable

**Data:**
- Port Congestion adds only 3.0 days on average
- Responds well to expedited mitigation (2.9 days with expedited vs. 3.0 with standard)
- Most predictable disruption type

**Recommendation:**
- Port congestion should trigger expedited mitigation selectively
- Monitor port utilization rates proactively
- Build relationships with air freight providers for surge capacity

---

## Technical Implementation

### Data Model Design

**Star Schema Rationale:**
- Optimizes query performance for aggregations
- Simplifies DAX measure creation
- Enables flexible slicing and dicing
- Industry standard for BI applications

**Fact Table: Fact_Shipments**
- Grain: One row per shipment order
- 10,000 records
- Contains metrics (delay days, cost, risk indices)
- Foreign keys to all dimension tables

**Dimension Tables:**
1. **Dim_Date:** Time intelligence (366 days for 2024-2025)
2. **Dim_Routes:** 41 unique route combinations
3. **Dim_Products:** 8 product categories
4. **Dim_Disruptions:** 4 disruption types (including "No Disruption")

### Advanced DAX Patterns Used

**1. Context Transition**
```dax
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

**2. Complex Filtering**
```dax
Disrupted Shipments = 
CALCULATE(
    [Total Shipments],
    Fact_Shipments[Disruption_Event] <> "No Disruption"
)
```

**3. Percentage Calculations with Safety**
```dax
On-Time % = 
DIVIDE(
    [On-Time Shipments],
    [Total Shipments],
    0  // Returns 0 if denominator is 0
)
```

### Python Preprocessing Pipeline

**Key Transformations:**

```python
# 1. Handle missing values
df['Disruption_Event'] = df['Disruption_Event'].fillna('No Disruption')

# 2. Create calculated columns
df['Cost_Per_Day'] = df['Shipping_Cost_USD'] / df['Actual_Lead_Time_Days']

# 3. Categorize continuous variables
df['Risk_Level'] = pd.cut(
    df['Geopolitical_Risk_Index'],
    bins=[0, 0.3, 0.6, 1.0],
    labels=['Low', 'Medium', 'High']
)

# 4. Extract time dimensions
df['Order_Quarter'] = df['Order_Date'].dt.to_period('Q').astype(str)
df['Order_Month'] = df['Order_Date'].dt.month
df['Year_Month'] = df['Order_Date'].dt.strftime('%Y-%m')

# 5. Build dimension tables
dim_routes = df[['Route_Type', 'Origin_City', 'Destination_City']].drop_duplicates()
dim_routes['Route_ID'] = range(1, len(dim_routes) + 1)

# 6. Merge foreign keys
df = df.merge(dim_routes, on=['Route_Type', 'Origin_City', 'Destination_City'])
```

**Benefits:**
- Cleaner Power BI data model
- Faster dashboard performance
- Reusable preprocessing for future datasets
- Version control for data transformations

---

## Business Recommendations

### Immediate Actions (0-3 months)

**1. Formalize Mitigation Triggers**
Create decision matrix for when to expedite:

| Condition | Action | Rationale |
|-----------|--------|-----------|
| High-value product + Any disruption | Expedite | Always justified by product value |
| Medium-value + Geopolitical conflict | Re-route (required) | No alternative |
| Medium-value + Port congestion | Evaluate case-by-case | Cost vs. customer impact |
| Low-value + Weather | Standard | Cost savings outweigh delay |

**2. Enhance Monitoring**
- Real-time geopolitical risk tracking (e.g., subscribe to risk intelligence services)
- Weather forecast integration for Pacific routes (Q3 focus)
- Port congestion API integration (live data feeds)

**3. Customer Communication**
- Proactive alerts when high-risk shipments are in transit
- Transparent delay estimates based on historical data
- Mitigation options with cost trade-offs

### Medium-term Initiatives (3-12 months)

**1. Optimize Inventory Positioning**
- Pre-position safety stock for Suez-dependent routes
- Regional distribution centers to reduce reliance on single routes
- Calculate optimal safety stock levels using delay probability distributions

**2. Supplier Diversification**
- Identify alternative suppliers on lower-risk routes
- Negotiate risk-sharing clauses in contracts
- Build dual-sourcing for critical components

**3. Predictive Analytics**
- Machine learning model to predict disruption likelihood
- Automated mitigation recommendations based on real-time conditions
- What-if scenario planning tool for route disruptions

### Long-term Strategic Changes (12+ months)

**1. Route Network Redesign**
- Reduce dependency on Suez route (highest geopolitical risk)
- Develop multi-modal transport options (sea + air hybrid)
- Invest in alternative route infrastructure

**2. Product-Route Optimization**
- Match high-value products to most reliable routes
- Avoid high-risk routes for time-sensitive shipments
- Dynamic routing based on current conditions

**3. Financial Instruments**
- Delay insurance for high-value shipments
- Hedging strategies for fuel cost volatility (impacts expedited air freight)
- Performance-based carrier contracts

---

## Conclusion

This analysis demonstrates how critical thinking and proper analytical methodology transform misleading initial results into actionable business insights. By recognizing selection bias and segmenting mitigation strategies appropriately, we uncovered that:

1. **Proactive mitigation works** and delivers ROI for high-value products
2. **Forced mitigation** (re-routing) is an unavoidable necessity, not a failure
3. **Strategic prioritization** of mitigation resources is already happening effectively
4. **Future opportunities** exist in predictive analytics and route optimization

The dashboard provides ongoing monitoring capability and supports data-driven decision-making for supply chain operations.

---

**Document Version:** 1.0  
**Last Updated:** February 2026  
**Author:** Rima Nafougui