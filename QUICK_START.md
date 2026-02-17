# Quick Start Guide

## Getting Started in 5 Minutes

This guide will help you set up and explore the Supply Chain Analytics dashboard quickly.

---

## Prerequisites

**Power BI Desktop** (Free download from [Microsoft](https://powerbi.microsoft.com/desktop/))  
**Python 3.x** (Optional - only needed if regenerating data)  
**10 minutes** of your time

---

## Option 1: View the Dashboard (Easiest)

**Just want to see it?**

1. Download `SupplyChain.pbix` from this repository
2. Double-click to open in Power BI Desktop
3. Start exploring! Data is embedded—no setup needed.

**Navigation:**
- **Page 1:** Executive Overview (high-level KPIs)
- **Page 2:** Risk Intelligence (root cause analysis)
- **Page 3:** Mitigation Effectiveness (strategy ROI)
- **Page 4:** Operational Details (granular data)

**Tips:**
- Use slicers on the right to filter data
- Click any visual to cross-filter other charts
- Hover over data points for tooltips

---

## Option 2: Regenerate Data (For Customization)

**Want to modify the dataset?**

### Step 1: Run Python Preprocessing

```bash
# Clone the repository
git clone https://github.com/yourusername/supply-chain-analytics.git
cd supply-chain-analytics

# Install dependencies
pip install pandas numpy

# Run preprocessing script
python data_prep.py
```

**Output Files Generated:**
- `fact_shipments.csv` - Main fact table (10,000 rows)
- `dim_routes.csv` - Route dimension (41 rows)
- `dim_products.csv` - Product dimension (8 rows)
- `dim_disruptions.csv` - Disruption dimension (4 rows)

### Step 2: Reload Data in Power BI

1. Open `SupplyChain.pbix` in Power BI Desktop
2. **Home tab** → **Transform Data**
3. For each table, right-click → **Advanced Editor**
4. Update the file path to point to your new CSV files
5. Click **Close & Apply**

### Step 3: Refresh Dashboard

All visuals will automatically update with the new data!

---

## Understanding the Dashboard

### Page 1: Executive Overview

**What it shows:**
- Overall supply chain health
- 87.1% on-time delivery rate
- Average delay of 0.95 days
- Total cost: $113M across 10,000 shipments

**Key Insight:**
Most shipments (87%) have no disruptions. Focus on the 13% that do.

---

### Page 2: Risk Intelligence

**What it shows:**
- Which routes are riskiest (Suez has highest geopolitical risk)
- Which disruptions cause longest delays (Geopolitical Conflict: 12.9 days)
- Seasonal weather patterns (Q3 is worst)

**Key Insight:**
Risk is concentrated in specific routes. Suez route needs the most attention.

---

### Page 3: Mitigation Effectiveness

**What it shows:**
- Expedited Air Freight saves 2.83 days
- Applied to 100% of high-value products when disrupted
- Costs $48,980 premium but worth it for Semiconductors/Pharmaceuticals
- Re-routing adds 18.5 days but is unavoidable when routes are blocked

**Key Insight:**
Different mitigation strategies serve different purposes. Expediting works; re-routing is necessary damage control.

---

### Page 4: Operational Details

**What it shows:**
- Searchable table of all 10,000 shipments
- Filter to see only late deliveries
- Route and transportation mode breakdowns
- Export capability for offline analysis

**Key Insight:**
Drill down into specific shipments to investigate issues.

---

## Customization Guide

### Change Colors

1. Select any visual
2. **Format pane** → **Visual** → **Data colors**
3. Pick new colors from palette

### Add New Measures

1. **Modeling tab** → **New Measure**
2. Write DAX formula (see DATA_DICTIONARY.md for examples)
3. Click ✓ to save

### Modify Visuals

1. Click visual to select
2. **Visualizations pane** → Change chart type
3. **Fields pane** → Drag/drop new fields

### Add Pages

1. Click **+** at bottom of screen
2. Build new visuals
3. **Right-click page tab** → Rename

---

## Troubleshooting

### "Data source error"
**Fix:** Data files are embedded in .pbix. If you see this, the file may be corrupted. Re-download from GitHub.

### "Can't refresh data"
**Fix:** Power Query is trying to find CSV files. Either:
- **Option A:** Use the embedded data (don't refresh)
- **Option B:** Run `data_prep.py` and update file paths

### "Visuals show blank"
**Fix:** 
- Check if slicers are filtering out all data
- Click "Clear all filters" icon
- Reset to default view

### "DAX measure error"
**Fix:**
- Check measure name spelling
- Ensure all referenced columns exist
- Review formula syntax (see DATA_DICTIONARY.md)

---

## Advanced Features

### Drill-Through

1. Right-click any data point in Pages 1-3
2. Select **Drill through** → **Operational Details**
3. See related shipments in detailed table

### Bookmarks

1. Set visuals to desired state
2. **View tab** → **Bookmarks** → **Add**
3. Name it (e.g., "Late Shipments Only")
4. Return anytime by clicking bookmark

### Export Data

1. Click **...** on any visual
2. **Export data** → Choose format (Excel, CSV)
3. Analyze offline in your tool of choice

---

## Learning Path

**New to Power BI?** Follow this order:

1. **Explore Page 1** - Get comfortable with slicers and clicking visuals
2. **Read ANALYSIS.md** - Understand the business story
3. **Explore Pages 2-4** - See how data flows through different lenses
4. **Review DAX measures** - Learn advanced calculations (DATA_DICTIONARY.md)
5. **Customize something** - Change a color, add a card, modify a title
6. **Run Python script** - Understand the preprocessing pipeline

**Want to go deeper?**
- Review the star schema in Model View
- Study the DAX formulas in Measures
- Examine the Python preprocessing logic
- Read the detailed methodology in ANALYSIS.md

---

## Project Files Overview

```
supply-chain-analytics/
│
├── README.md                      # You are here
├── ANALYSIS.md                    # Detailed methodology & insights
├── DATA_DICTIONARY.md             # Complete data reference
├── QUICK_START.md                 # This guide
│
├── SupplyChain.pbix              # Power BI dashboard file
├── data_prep.py                   # Python preprocessing script
│
├── supply_chain_data.csv         # Original raw data
├── fact_shipments.csv            # Processed fact table
├── dim_routes.csv                # Route dimension
├── dim_products.csv              # Product dimension
└── dim_disruptions.csv           # Disruption dimension
```

---

## FAQ

**Q: Can I use this for my portfolio?**  
A: Yes! This project is open-source. Clone it, customize it, make it your own.

**Q: How do I share this with recruiters?**  
A: Three options:
1. Share GitHub link (they can download .pbix)
2. Publish to Power BI Service (free tier) and share link
3. Export to PDF and share static images

**Q: Can I modify the data?**  
A: Absolutely! Edit `data_prep.py` to change how data is processed, or create your own synthetic dataset.

**Q: Is this based on real data?**  
A: It's synthetically generated but designed to mimic real-world supply chain patterns (Suez Canal crisis, COVID-19 impacts, etc.).

**Q: How long did this take to build?**  
A: ~15-20 hours of development, refinement, and documentation.

**Q: What skills does this demonstrate?**  
A: 
- Data cleaning & ETL (Python)
- Data modeling (Star schema)
- Business intelligence (Power BI)
- Analytics (DAX, statistical thinking)
- Communication (storytelling, documentation)

---

## Next Steps

**Ready to build your own version?**

1. **Star this repository** (helps others find it!)
2. **Fork it** to your GitHub
3. **Customize** the dashboard with your ideas
4. **Share** your version (tag me!)
5. **Add to resume/portfolio** 

**Questions?**  
- Open an issue on GitHub
- Email me: your.email@example.com
- Connect on LinkedIn: [Your Profile]

---

**Happy analyzing!**

---

*Last updated: February 2026*