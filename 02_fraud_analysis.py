import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("fraud_data.csv")

# Data Cleaning
df.dropna(inplace=True)

# Total transactions
total = len(df)
print("Total Transactions:", total)

# Fraud vs Legitimate count
fraud_count = df["Is_Fraud"].value_counts()
print("\nFraud vs Legitimate:\n", fraud_count)

# Total fraud transactions
fraud_total = df[df["Is_Fraud"] == 1].shape[0]
print("\nTotal Fraud Transactions:", fraud_total)

# Visualization - Pie Chart
plt.figure()
fraud_count.plot(kind="pie", autopct='%1.1f%%', labels=["Legitimate","Fraud"])
plt.title("Fraud Distribution")
plt.ylabel("")
plt.savefig("fraud_pie_chart.png")

# Visualization - Bar Graph
plt.figure()
fraud_count.plot(kind="bar")
plt.title("Fraud vs Legitimate Transactions")
plt.xlabel("Type (0=Legit, 1=Fraud)")
plt.ylabel("Count")
plt.savefig("fraud_bar_chart.png")

print("\nCharts saved successfully!")
