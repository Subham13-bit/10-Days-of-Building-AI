from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(Path(__file__).parent / "students.csv")

df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

# 1. Count plot: number of students in each city
sns.countplot(data=df, x="City")
plt.title("Number of Students by City")
plt.xlabel("City")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()

# 2. Box plot: compare marks across subjects
marks_df = df[["Math", "Science", "English"]]
sns.boxplot(data=marks_df)
plt.title("Marks Distribution by Subject")
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()

# 3. Heatmap: correlation between numerical columns
numeric_df = df[
    ["Math", "Science", "English", "Attendance", "Study_Hours", "Average"]
]

correlation = numeric_df.corr()

sns.heatmap(correlation, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()