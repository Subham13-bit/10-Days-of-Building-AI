from pathlib import Path
import pandas as pd
import numpy as np

# Load the dataset from the same folder as this Python file
data_path = Path(__file__).parent / "students.csv"
df = pd.read_csv(data_path)

# Display the dataset
print("STUDENT PERFORMANCE DATA")
print(df.head())

# Check dataset size
print("\nDATASET SHAPE")
print(df.shape)

# Check missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Check duplicate rows
print("\nDUPLICATE ROWS")
print(df.duplicated().sum())

# Calculate total and average marks
subjects = ["Math", "Science", "English"]

df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1)

# Assign a grade based on average marks
def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "Fail"

df["Grade"] = df["Average"].apply(calculate_grade)

# Pass if average is at least 40
df["Status"] = np.where(df["Average"] >= 40, "Pass", "Fail")

# Rank students: 1 is the highest average
df["Rank"] = df["Average"].rank(
    ascending=False,
    method="dense"
).astype(int)

# Display the top 5 students
print("\nTOP 5 STUDENTS")
print(
    df.sort_values("Rank")[
        ["Name", "Total", "Average", "Grade", "Status", "Rank"]
    ].head()
)

# Display grade counts
print("\nGRADE DISTRIBUTION")
print(df["Grade"].value_counts().sort_index())

# Display overall class average
print("\nCLASS AVERAGE")
print(df["Average"].mean())


import matplotlib.pyplot as plt
import seaborn as sns

# 1. Top 5 students bar chart
top_students = df.sort_values(
    "Average", ascending=False
).head(5)

plt.figure(figsize=(9, 5))
sns.barplot(
    data=top_students,
    x="Name",
    y="Average"
)
plt.title("Top 5 Students by Average Marks")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig(Path(__file__).parent / "top_5_students.png")
plt.show()


# 2. Distribution of student averages
plt.figure(figsize=(9, 5))
sns.histplot(df["Average"], bins=7, kde=True)
plt.title("Distribution of Student Average Marks")
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig(Path(__file__).parent / "marks_distribution.png")
plt.show()


# 3. Correlation heatmap
numeric_data = df[
    ["Math", "Science", "English", "Attendance",
     "Study_Hours", "Average"]
]

correlation = numeric_data.corr()

plt.figure(figsize=(9, 6))
sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    vmin=-1,
    vmax=1
)
plt.title("Student Performance Correlation Heatmap")
plt.tight_layout()
plt.savefig(Path(__file__).parent / "correlation_heatmap.png")
plt.show()

# Save complete student analysis
output_path = Path(__file__).parent / "student_performance_report.csv"

df.sort_values("Rank").to_csv(output_path, index=False)

print("\nREPORT SAVED SUCCESSFULLY!")
print(output_path)