import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("results.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

print("===== BASIC EXPLORATION =====")

# 1 Matches
print("1. Total Matches:", df.shape[0])

# 2 Earliest and latest year
print("2. Earliest Year:", df["date"].dt.year.min())
print("   Latest Year:", df["date"].dt.year.max())

# 3 Unique countries
countries = pd.concat([df["home_team"], df["away_team"]]).unique()
print("3. Unique Countries:", len(countries))

# 4 Most frequent home team
print("4. Most Frequent Home Team:")
print(df["home_team"].value_counts().head(1))

# --------------------
# Goals Analysis
# --------------------
df["total_goals"] = df["home_score"] + df["away_score"]

print("\n===== GOALS ANALYSIS =====")

# 5 Average goals
print("5. Average Goals Per Match:", round(df["total_goals"].mean(),2))

# 6 Highest scoring match
highest = df.loc[df["total_goals"].idxmax()]
print("6. Highest Scoring Match:")
print(highest[["home_team","away_team","home_score","away_score","total_goals"]])

# 7 Home vs Away goals
print("7. Home Goals:", df["home_score"].sum())
print("   Away Goals:", df["away_score"].sum())

# 8 Most common total goals
print("8. Most Common Total Goals:", df["total_goals"].mode()[0])

# --------------------
# Match Results
# --------------------
def result(row):
    if row["home_score"] > row["away_score"]:
        return "Home Win"
    elif row["home_score"] < row["away_score"]:
        return "Away Win"
    else:
        return "Draw"

df["result"] = df.apply(result, axis=1)

print("\n===== MATCH RESULTS =====")

# 9 Percentage home wins
home_pct = (df["result"].value_counts(normalize=True)["Home Win"]) * 100
print("9. Home Win Percentage:", round(home_pct,2), "%")

# 10 Home advantage
if home_pct > 40:
    print("10. Yes, home advantage exists.")
else:
    print("10. No strong home advantage.")

# 11 Most wins historically
home_wins = df[df["result"]=="Home Win"]["home_team"]
away_wins = df[df["result"]=="Away Win"]["away_team"]

wins = pd.concat([home_wins, away_wins])

print("11. Top 10 Teams by Wins:")
print(wins.value_counts().head(10))

# --------------------
# Visualizations
# --------------------

# Histogram
df["total_goals"].hist(bins=15)
plt.title("Distribution of Goals Per Match")
plt.xlabel("Goals")
plt.ylabel("Matches")
plt.show()

# Bar chart outcomes
df["result"].value_counts().plot(kind="bar")
plt.title("Match Outcomes")
plt.show()

# Top 10 wins
wins.value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Teams by Wins")
plt.show()