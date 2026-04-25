# ⚽ International Football Analysis (1872-2024)

## 📊 Project Overview
This project analyzes **49,287 international football matches** spanning **154 years** (1872-2026) to uncover patterns in goal scoring, home advantage, and team performance using Python data analysis.

**Dataset:** [International Football Results from Kaggle](https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017)

## 🛠️ Technologies Used
- Python 3.7+
- Pandas (Data manipulation)
- Matplotlib (Data visualization)
- Git & GitHub (Version control)

## 📁 Repository Structure
football-analysis/
├── analysis.py # Main analysis script
├── results.csv # Match results (3.7M rows)
├── goalscorers.csv # Individual goal scorer data
├── shootouts.csv # Penalty shootout records
├── former_names.csv # Country name changes
├── international-football-results-from-1872-to-2017.zip # Original dataset
├── README.md # Project documentation
└── venv/ # Python virtual environment


## 🚀 Getting Started

### Clone the Repository
```bash
git clone https://github.com/kbrown3695/football-analysis.git
cd football-analysis

## Install Dependencies

# Create and activate virtual environment (already included)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install pandas matplotlib

## Run the Analysis
python analysis.py

## 📈 Analysis & Results

1️⃣ Basic Exploration
Question	Answer	Code Logic
Total matches	49,287	df.shape[0]
Date range	1872 - 2026	df["date"].dt.year.min() / .max()
Unique countries	333	pd.concat([df["home_team"], df["away_team"]]).unique()
Most frequent home team	Brazil (614 matches)	df["home_team"].value_counts().head(1)

# Sample code for basic exploration
import pandas as pd

df = pd.read_csv("results.csv")
df["date"] = pd.to_datetime(df["date"])

print(f"Total Matches: {df.shape[0]}")
print(f"Date Range: {df['date'].dt.year.min()} - {df['date'].dt.year.max()}")

2️⃣ Goals Analysis

# Create total goals column
df["total_goals"] = df["home_score"] + df["away_score"]

3️⃣ Match Results & Home Advantage

def match_result(row):
    if row["home_score"] > row["away_score"]:
        return "Home Win"
    elif row["home_score"] < row["away_score"]:
        return "Away Win"
    else:
        return "Draw"

df["result"] = df.apply(match_result, axis=1)

## Result Type	Percentage	Count

Home Win	48.91%	24,108 matches
Away Win	29.58%	14,581 matches
Draw	21.51%	10,598 matches

✅ Home Advantage Conclusion: With 48.91% home wins vs. the expected 33.33% (if results were random), home advantage is statistically significant and exists in international football.

4️⃣ Top 10 Winning Teams Historically
Rank	Team	Total Wins
1	🇧🇷 Brazil	670
2	🏴󠁧󠁢󠁥󠁮󠁧󠁿 England	623
3	🇩🇪 Germany	597
4	🇦🇷 Argentina	588
5	🇸🇪 Sweden	541
6	🇰🇷 South Korea	536
7	🇲🇽 Mexico	511
8	🇫🇷 France	476
9	🇮🇹 Italy	475
10	🇭🇺 Hungary	470

# Calculate total wins (home + away)
home_wins = df[df["result"]=="Home Win"]["home_team"]
away_wins = df[df["result"]=="Away Win"]["away_team"]
total_wins = pd.concat([home_wins, away_wins]).value_counts().head(10)

📊 Visualizations

The script generates three key visualizations:

1. Distribution of Goals Per Match
Histogram showing frequency of different total goal counts

Most common: 2 goals per match

Right-skewed distribution (most matches have 0-4 goals)

2. Match Outcomes Bar Chart
Compares Home Wins, Away Wins, and Draws

Visually demonstrates home advantage

3. Top 10 Teams by Total Wins
Horizontal/vertical bar chart of winningest teams

Shows Brazil's historical dominance

# Generate all visualizations
import matplotlib.pyplot as plt

# Histogram
df["total_goals"].hist(bins=15)
plt.title("Distribution of Goals Per Match")
plt.show()

# Outcome bar chart
df["result"].value_counts().plot(kind="bar")
plt.title("Match Outcomes")
plt.show()

# Top teams
total_wins.head(10).plot(kind="bar")
plt.title("Top 10 Teams by Wins")
plt.show()

💡 Key Insights Summary

🏠 Home Advantage is Real: Teams win 48.91% of matches at home

⚽ Typical Match: Most common result has exactly 2 total goals

🇧🇷 Brazilian Dominance: Brazil leads all nations with 670 historical wins

📈 Goal Trends: Average 2.94 goals per match across 154 years

🌍 Global Reach: Data covers 333 unique countries/nations

🎯 Record Performance: Australia's 31-0 victory stands as the biggest margin

🔄 Complete Output from Analysis
===== BASIC EXPLORATION =====
1. Total Matches: 49287
2. Earliest Year: 1872 | Latest Year: 2026
3. Unique Countries: 333
4. Most Frequent Home Team: Brazil (614 matches)

===== GOALS ANALYSIS =====
5. Average Goals Per Match: 2.94
6. Highest Scoring Match: Australia 31 - 0 American Samoa
7. Home Goals: 86,426 | Away Goals: 58,192
8. Most Common Total Goals: 2.0

===== MATCH RESULTS =====
9. Home Win Percentage: 48.91%
10. Yes, home advantage exists.
11. Top Team by Wins: Brazil (670 wins)

🎓 Learning Outcomes
This exercise demonstrates:

Data loading with pandas (CSV files)

Data cleaning (date conversion, column creation)

Exploratory analysis (summary statistics, aggregations)

Data transformation (custom functions with apply)

Visualization (histograms, bar charts)

Version control (Git/GitHub workflow)

📧 Contact & Submission
Exercise: Artificial Intelligence - Exercise 1
Author: Nicholas Mureti Mwenda
GitHub: kbrown3695/football-analysis

📜 License
This project uses the Kaggle International Football Results dataset. Dataset is available for public use under Kaggle's terms.