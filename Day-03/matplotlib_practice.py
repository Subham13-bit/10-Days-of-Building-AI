from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(Path(__file__).parent / "students.csv")

# Calculate each student's average marks
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

# 1. Bar chart: average marks by student
plt.figure(figsize=(10, 5))
plt.bar(df["Name"], df["Average"])
plt.title("Average Marks by Student")
plt.xlabel("Student")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Histogram: distribution of average marks
plt.figure(figsize=(8, 5))
plt.hist(df["Average"], bins=6, edgecolor="black")
plt.title("Distribution of Student Average Marks")
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()

# 3. Scatter plot: study hours vs average marks
plt.figure(figsize=(8, 5))
plt.scatter(df["Study_Hours"], df["Average"])
plt.title("Study Hours vs Average Marks")
plt.xlabel("Study Hours per Day")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.show()

# 4. Line chart: average marks by attendance
attendance_summary = df.groupby("Attendance")["Average"].mean().sort_index()

plt.figure(figsize=(8, 5))
plt.plot(attendance_summary.index, attendance_summary.values, marker="o")
plt.title("Average Marks by Attendance")
plt.xlabel("Attendance")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.show()