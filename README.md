# Strategic Workforce Planning & Headcount Optimization Engine

> End-to-end HR analytics system that turns raw employee data into hiring decisions.

---

## What This Project Does
- Audits department-wise headcount using Excel
- Runs SQL queries to find overloaded teams, high attrition departments, and salary-performance gaps
- Cleans and processes IBM HR data using Python
- Simulates attrition risk using Monte Carlo (10,000 scenarios)
- Recommends optimal hiring plan using Linear Programming (PuLP + GLPK)
- Visualizes everything on a Google Looker Studio dashboard
- Presents results via a live Streamlit app

---

## Why These Techniques

- **Workload Ratio** — measures if a team has more work than it can handle
- **Monte Carlo Simulation** — runs thousands of random scenarios to forecast how many employees might leave
- **Linear Programming** — finds the cheapest hiring plan that still meets all department needs
- **People Analytics** — uses data to make HR decisions instead of guesswork

---

## Tech Stack
`Python` `MySQL` `Excel` `PuLP` `Google Looker Studio` `Streamlit`

---

## Dataset
IBM HR Analytics — 1,470 employees, 35 features
Download from [Kaggle](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset) — not included in repo

---

## Project Structure
- `python/` — cleaning, ratio analysis, Monte Carlo, optimization, Streamlit app
- `assets/` — charts and visualizations
- `headcount_audit.xlsx` — Excel audit file

---

## Author
**Afra Aquil** | B.Tech CS, Jamia Hamdard University
[LinkedIn](https://linkedin.com/in/afraaquil12) · [GitHub](https://github.com/afraaquil)
