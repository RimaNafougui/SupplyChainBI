# Data Dictionary

## Overview

This document provides detailed descriptions of all tables, columns, and measures used in the Supply Chain Analytics project.

---

## Table of Contents
1. [Fact Tables](#fact-tables)
2. [Dimension Tables](#dimension-tables)
3. [DAX Measures](#dax-measures)
4. [Data Types & Formats](#data-types--formats)

---

## Fact Tables

### Fact_Shipments

**Description:** Central fact table containing one row per shipment order with associated metrics and foreign keys.

**Grain:** One row = One shipment order

**Row Count:** 10,000

| Column Name | Data Type | Description | Example Values | Notes |
|------------|-----------|-------------|----------------|-------|
| Order_ID | Text | Unique identifier for shipment | ORD-A5C7A8D7 | Primary Key |
| Order_Date | Date | Date order was placed | 2024-04-05 | Links to Dim_Date |
| Origin_City | Text | Shipment origin city and country | "Shanghai, CN" | Part of route definition |
| Destination_City | Text | Shipment destination city and country | "Los Angeles, US" | Part of route definition |
| Route_Type | Text | Classification of trade route | Pacific, Suez, Atlantic, Intra-Asia, Commodity | Links to Dim_Routes |
| Transportation_Mode | Text | Method of transport | Sea, Air, Rail, Road | Affects cost and speed |
| Product_Category | Text | Type of goods shipped | Semiconductors, Pharmaceuticals, etc. | Links to Dim_Products |
| Base_Lead_Time_Days | Integer | Standard shipping time under normal conditions | 18 | Benchmark for delay calculation |
| Scheduled_Lead_Time_Days | Integer | Expected delivery time with buffer | 21 | Includes buffer for contingencies |
| Actual_Lead_Time_Days | Integer | Realized delivery time | 18 | Key performance metric |
| Delay_Days | Integer | Difference between actual and scheduled time | 0 | Negative = early, Positive = late |
| Delivery_Status | Text | On-time or late classification | On Time, Late | Based on scheduled vs actual |
| Disruption_Event | Text | Primary cause of delay if any | Port Congestion, Geopolitical Conflict, Severe Weather, No Disruption | Links to Dim_Disruptions |
| Geopolitical_Risk_Index | Decimal | Political instability score for route | 0.81 | Range: 0.0 to 1.0 (higher = riskier) |
| Weather_Severity_Index | Decimal | Weather conditions during transit | 8.9 | Range: 0 to 10 (higher = more severe) |
| Inflation_Rate_Pct | Decimal | Economic inflation rate affecting costs | 1.83 | Percentage |
| Shipping_Cost_USD | Decimal | Final cost of shipping including surcharges | 1611.81 | USD currency |
| Order_Weight_Kg | Integer | Weight of shipment in kilograms | 1781 | Used for capacity planning |
| Mitigation_Action_Taken | Text | Response action to disruption | Expedited Air Freight, Re-routing, Standard Shipping | Strategy implemented |
| On_Time_Flag | Integer | Binary indicator for on-time delivery | 1 (on-time), 0 (late) | For quick aggregations |
| Cost_Per_Day | Decimal | Shipping cost divided by actual lead time | 89.55 | Efficiency metric |
| Risk_Level | Text | Categorized geopolitical risk | Low, Medium, High | Based on risk index bucketing |
| Order_Quarter | Text | Quarter of order date | 2024Q2 | Time dimension |
| Order_Month | Integer | Month number of order date | 4 | 1-12 |
| Order_Year | Integer | Year of order date | 2024 | Time dimension |
| Route_ID | Integer | Foreign key to Dim_Routes | 1 | Lookup reference |
| Product_ID | Integer | Foreign key to Dim_Products | 1 | Lookup reference |
| Disruption_ID | Integer | Foreign key to Dim_Disruptions | 1 | Lookup reference |

---

## Dimension Tables

### Dim_Date

**Description:** Date dimension table for time intelligence.

**Row Count:** 731 (2024-01-01 to 2025-12-31)

| Column Name | Data Type | Description | Example Values |
|------------|-----------|-------------|----------------|
| Date | Date | Unique date | 2024-04-05 |
| Year | Integer | Calendar year | 2024 |
| Quarter | Text | Quarter of year | Q2 |
| Month | Text | Month name | April |
| Month Number | Integer | Month as number | 4 |
| Week Number | Integer | ISO week number | 14 |
| Day | Integer | Day of month | 5 |
| Weekday | Text | Day of week | Friday |
| Year-Quarter | Text | Combined year-quarter | 2024-Q2 |
| Year-Month | Text | Combined year-month | 2024-04 |

**Relationships:**
- Dim_Date[Date] → Fact_Shipments[Order_Date] (One to Many)

---

### Dim_Routes

**Description:** Dimension table for route definitions.

**Row Count:** 41 unique route combinations

| Column Name | Data Type | Description | Example Values |
|------------|-----------|-------------|----------------|
| Route_ID | Integer | Unique identifier | 1, 2, 3... |
| Route_Type | Text | Classification of route | Pacific, Suez, Atlantic, Intra-Asia, Commodity |
| Origin_City | Text | Starting city and country | "Shanghai, CN" |
| Destination_City | Text | Ending city and country | "Los Angeles, US" |

**Relationships:**
- Dim_Routes[Route_ID] → Fact_Shipments[Route_ID] (One to Many)

**Key Routes:**
- **Pacific:** Asia to North America (e.g., Shanghai to Los Angeles)
- **Suez:** Asia/Middle East to Europe via Suez Canal (e.g., Shenzhen to Rotterdam)
- **Atlantic:** Europe to North America (e.g., Hamburg to New York)
- **Intra-Asia:** Regional Asian routes (e.g., Tokyo to Singapore)
- **Commodity:** South America to Asia (e.g., Santos to Shanghai)

---

### Dim_Products

**Description:** Product category dimension.

**Row Count:** 8 product categories

| Column Name | Data Type | Description | Example Values |
|------------|-----------|-------------|----------------|
| Product_ID | Integer | Unique identifier | 1, 2, 3... |
| Product_Category | Text | Type of goods | Semiconductors, Pharmaceuticals, Consumer Electronics, Auto Parts, Raw Materials, Textiles, Perishable Foods |

**Relationships:**
- Dim_Products[Product_ID] → Fact_Shipments[Product_ID] (One to Many)

**Product Groupings:**
- **High-Value:** Semiconductors, Pharmaceuticals (always get expedited mitigation)
- **Medium-Value:** Consumer Electronics, Auto Parts
- **Low-Value:** Textiles, Raw Materials, Perishable Foods

---

### Dim_Disruptions

**Description:** Disruption event types.

**Row Count:** 4 disruption categories

| Column Name | Data Type | Description | Example Values |
|------------|-----------|-------------|----------------|
| Disruption_ID | Integer | Unique identifier | 1, 2, 3, 4 |
| Disruption_Event | Text | Type of disruption | No Disruption, Port Congestion, Geopolitical Conflict (Route Diversion), Severe Weather (Typhoon/Storm) |
| Is_Disrupted | Text | Binary flag | Yes, No |

**Relationships:**
- Dim_Disruptions[Disruption_ID] → Fact_Shipments[Disruption_ID] (One to Many)

**Disruption Frequency:**
- **No Disruption:** 87.3% of shipments
- **Port Congestion:** 5.7%
- **Geopolitical Conflict:** 5.2%
- **Severe Weather:** 1.7%

---

## DAX Measures

### Basic Measures

#### Total Shipments
```dax
Total Shipments = COUNTROWS(Fact_Shipments)
```
**Purpose:** Count total number of shipment records  
**Usage:** Primary KPI, denominator for percentages

#### On-Time Shipments
```dax
On-Time Shipments = 
CALCULATE(
    COUNTROWS(Fact_Shipments),
    Fact_Shipments[Delivery_Status] = "On Time"
)
```
**Purpose:** Count shipments delivered on schedule  
**Usage:** Performance tracking

#### Late Shipments
```dax
Late Shipments = 
CALCULATE(
    [Total Shipments],
    Fact_Shipments[Delivery_Status] = "Late"
)
```
**Purpose:** Count delayed shipments  
**Usage:** Problem identification

#### On-Time %
```dax
On-Time % = 
DIVIDE(
    [On-Time Shipments],
    [Total Shipments],
    0
)
```
**Purpose:** Calculate on-time delivery rate  
**Usage:** Primary performance KPI  
**Format:** Percentage

#### Avg Delay Days
```dax
Avg Delay Days = 
ROUND(AVERAGE(Fact_Shipments[Delay_Days]), 1)
```
**Purpose:** Average delay across all shipments  
**Usage:** Performance metric  
**Format:** Number with 1 decimal

---

### Risk Analysis Measures

#### Disrupted Shipments
```dax
Disrupted Shipments = 
CALCULATE(
    [Total Shipments],
    Fact_Shipments[Disruption_Event] <> "No Disruption"
)
```
**Purpose:** Count shipments that faced disruptions  
**Usage:** Risk analysis denominator

#### High Risk Shipments
```dax
High Risk Shipments = 
CALCULATE(
    [Total Shipments],
    Fact_Shipments[Geopolitical_Risk_Index] > 0.6
)
```
**Purpose:** Count shipments in high-risk zones  
**Usage:** Risk concentration analysis

#### Medium Risk Shipments
```dax
Medium Risk Shipments = 
CALCULATE(
    [Total Shipments],
    Fact_Shipments[Geopolitical_Risk_Index] > 0.3,
    Fact_Shipments[Geopolitical_Risk_Index] <= 0.6
)
```
**Purpose:** Count shipments in medium-risk zones  
**Usage:** Risk distribution

#### Low Risk Shipments
```dax
Low Risk Shipments = 
CALCULATE(
    [Total Shipments],
    Fact_Shipments[Geopolitical_Risk_Index] <= 0.3
)
```
**Purpose:** Count shipments in low-risk zones  
**Usage:** Baseline comparison

#### Avg Geopolitical Risk
```dax
Avg Geopolitical Risk = 
AVERAGE(Fact_Shipments[Geopolitical_Risk_Index])
```
**Purpose:** Average political stability risk  
**Usage:** Trend analysis  
**Format:** 3 decimals

#### Avg Weather Severity
```dax
Avg Weather Severity = 
AVERAGE(Fact_Shipments[Weather_Severity_Index])
```
**Purpose:** Average weather conditions  
**Usage:** Seasonal pattern identification  
**Format:** 1 decimal

#### Risk Score
```dax
Risk Score = 
([Avg Geopolitical Risk] * 0.6) + ([Avg Weather Severity] / 10 * 0.4)
```
**Purpose:** Composite risk indicator  
**Usage:** Route prioritization  
**Weights:** 60% geopolitical, 40% weather

---

### Mitigation Effectiveness Measures

#### Expedited Shipments
```dax
Expedited Shipments = 
CALCULATE(
    [Total Shipments],
    Fact_Shipments[Mitigation_Action_Taken] = "Expedited Air Freight"
)
```
**Purpose:** Count shipments using air freight  
**Usage:** Mitigation adoption tracking

#### Rerouted Shipments
```dax
Rerouted Shipments = 
CALCULATE(
    [Total Shipments],
    Fact_Shipments[Mitigation_Action_Taken] = "Re-routing"
)
```
**Purpose:** Count shipments that were re-routed  
**Usage:** Forced mitigation tracking

#### Standard Disrupted Shipments
```dax
Standard Disrupted Shipments = 
CALCULATE(
    [Total Shipments],
    Fact_Shipments[Disruption_Event] <> "No Disruption",
    Fact_Shipments[Mitigation_Action_Taken] = "Standard Shipping"
)
```
**Purpose:** Count disrupted shipments without active mitigation  
**Usage:** Control group for comparison

#### Avg Lead Time - Expedited
```dax
Avg Lead Time - Expedited = 
CALCULATE(
    AVERAGE(Fact_Shipments[Actual_Lead_Time_Days]),
    Fact_Shipments[Mitigation_Action_Taken] = "Expedited Air Freight"
)
```
**Purpose:** Average total time for expedited shipments  
**Usage:** Performance comparison  
**Expected:** ~19.4 days

#### Avg Lead Time - Standard (Disrupted)
```dax
Avg Lead Time - Standard (Disrupted) = 
CALCULATE(
    AVERAGE(Fact_Shipments[Actual_Lead_Time_Days]),
    Fact_Shipments[Disruption_Event] <> "No Disruption",
    Fact_Shipments[Mitigation_Action_Taken] = "Standard Shipping"
)
```
**Purpose:** Average total time for standard disrupted shipments  
**Usage:** Baseline for mitigation comparison  
**Expected:** ~22.2 days

#### Time Saved - Expedited
```dax
Time Saved - Expedited = 
VAR StandardTime = [Avg Lead Time - Standard (Disrupted)]
VAR ExpeditedTime = [Avg Lead Time - Expedited]
RETURN
    StandardTime - ExpeditedTime
```
**Purpose:** Calculate days saved by expediting  
**Usage:** Key mitigation effectiveness metric  
**Expected:** ~2.8 days

#### Avg Cost - Expedited
```dax
Avg Cost - Expedited = 
CALCULATE(
    AVERAGE(Fact_Shipments[Shipping_Cost_USD]),
    Fact_Shipments[Mitigation_Action_Taken] = "Expedited Air Freight"
)
```
**Purpose:** Average cost of expedited shipping  
**Usage:** ROI calculation  
**Expected:** ~$53,000

#### Avg Cost - Standard (Disrupted)
```dax
Avg Cost - Standard (Disrupted) = 
CALCULATE(
    AVERAGE(Fact_Shipments[Shipping_Cost_USD]),
    Fact_Shipments[Disruption_Event] <> "No Disruption",
    Fact_Shipments[Mitigation_Action_Taken] = "Standard Shipping"
)
```
**Purpose:** Baseline shipping cost  
**Usage:** Cost comparison  
**Expected:** ~$4,150

#### Expedited Cost Premium
```dax
Expedited Cost Premium = 
[Avg Cost - Expedited] - [Avg Cost - Standard (Disrupted)]
```
**Purpose:** Extra cost of expediting  
**Usage:** ROI denominator  
**Expected:** ~$48,980

#### Cost Per Day Saved
```dax
Cost Per Day Saved = 
DIVIDE([Expedited Cost Premium], [Time Saved - Expedited], 0)
```
**Purpose:** Cost efficiency of mitigation  
**Usage:** Budget justification  
**Expected:** ~$17,300/day

#### Expedited Adoption Rate
```dax
Expedited Adoption Rate = 
VAR HighValueDisrupted = 
    CALCULATE(
        [Total Shipments],
        Fact_Shipments[Product_Category] IN {"Semiconductors", "Pharmaceuticals"},
        Fact_Shipments[Disruption_Event] <> "No Disruption"
    )
VAR HighValueExpedited = 
    CALCULATE(
        [Total Shipments],
        Fact_Shipments[Product_Category] IN {"Semiconductors", "Pharmaceuticals"},
        Fact_Shipments[Mitigation_Action_Taken] = "Expedited Air Freight"
    )
RETURN
    DIVIDE(HighValueExpedited, HighValueDisrupted, 0)
```
**Purpose:** % of high-value products getting expedited treatment  
**Usage:** Strategy consistency check  
**Expected:** 100%

#### Avg Lead Time - Rerouted
```dax
Avg Lead Time - Rerouted = 
CALCULATE(
    AVERAGE(Fact_Shipments[Actual_Lead_Time_Days]),
    Fact_Shipments[Mitigation_Action_Taken] = "Re-routing"
)
```
**Purpose:** Average time for re-routed shipments  
**Usage:** Understand forced mitigation cost  
**Expected:** ~40.7 days

#### Rerouting Time Penalty
```dax
Rerouting Time Penalty = 
[Avg Lead Time - Rerouted] - [Avg Lead Time - Standard (Disrupted)]
```
**Purpose:** Additional time from re-routing  
**Usage:** Quantify route closure impact  
**Expected:** ~18.5 days

---

## Data Types & Formats

### Standard Formats Used

| Metric Type | Format | Example |
|-------------|--------|---------|
| Percentages | 0.0% or 0% | 87.1% |
| Currency | $#,##0 | $48,980 |
| Days | 0.0 | 2.8 |
| Counts | #,##0 | 10,000 |
| Risk Index | 0.00 | 0.81 |
| Dates | MM/DD/YYYY | 04/05/2024 |

### Color Coding Standards

**Status Indicators:**
- Green (#10B981): Good performance, on-time
- Red (#EF4444): Poor performance, late, high risk
- Orange (#F59E0B): Warning, medium risk
- Blue (#1E3A8A): Neutral, informational

**Risk Levels:**
- Low Risk: Green background
- Medium Risk: Orange background
- High Risk: Red background

---

## Data Quality Notes

### Known Limitations
1. **Simulated Data:** Dataset is synthetically generated to simulate real-world patterns
2. **Simplified Costs:** Actual logistics costs involve more variables than captured
3. **Binary Outcomes:** Delivery status simplified to on-time/late (no partial delays)
4. **Limited Weather Detail:** Weather severity is indexed, not specific storm types

### Data Validation Rules
- No negative delays except where shipments arrived early
- All foreign keys have matching dimension records
- Shipping costs always positive
- Lead time >= delay days
- Risk indices bounded 0.0 to 1.0
- Weather severity bounded 0 to 10

### Assumptions
- $100 per day delay penalty (used in ROI calculations)
- Product value hierarchy: Semiconductors > Pharmaceuticals > Electronics > Auto Parts > Materials > Textiles
- All timestamps in UTC
- Currency in USD

---

**Document Version:** 1.0  
**Last Updated:** February 2026  
**Maintained By:** [Your Name]