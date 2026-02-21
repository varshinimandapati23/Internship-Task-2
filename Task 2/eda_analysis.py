import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("../Task 1/cleaned_smartphones.csv")

# -----------------------------
# Basic Statistics
# -----------------------------
print("===== BASIC STATISTICS =====")
print("Total Models:", df.shape[0])
print("Average Price:", df["price"].mean())
print("Minimum Price:", df["price"].min())
print("Maximum Price:", df["price"].max())
print("Average RAM:", df["ram"].mean())
print("Average Battery:", df["battery_capacity"].mean())

print("\nFull Statistical Summary:")
print(df.describe())

# -----------------------------
# Price Distribution (Histogram)
# -----------------------------
plt.figure()
plt.hist(df["price"], bins=20)
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.title("Price Distribution")
plt.show()

# -----------------------------
# RAM vs Price (Scatter Plot)
# -----------------------------
plt.figure()
plt.scatter(df["ram"], df["price"])
plt.xlabel("RAM (GB)")
plt.ylabel("Price")
plt.title("RAM vs Price")
plt.show()

# -----------------------------
# Brand vs Average Price (Bar Chart)
# -----------------------------
brand_avg = df.groupby("brand_name")["price"].mean().sort_values(ascending=False)

plt.figure()
brand_avg.head(10).plot(kind="bar")
plt.title("Top 10 Brands by Average Price")
plt.ylabel("Average Price")
plt.xticks(rotation=45)
plt.show()

# -----------------------------
# Correlation Matrix
# -----------------------------
print("\n===== CORRELATION MATRIX =====")
corr_matrix = df.corr(numeric_only=True)
print(corr_matrix)

# -----------------------------
# Correlation Heatmap
# -----------------------------
plt.figure()
sns.heatmap(corr_matrix, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()