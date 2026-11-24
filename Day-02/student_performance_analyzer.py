
import pandas as pd
import numpy as np
from pathlib import Path

# 1. Load dataset
file_path = Path(__file__).parent / "students.csv"
df = pd.read_csv(file_path)

print("=" * 45)
print("       STUDENT PERFORMANCE ANALYZER")
print("=" * 45)

# 2. Basic dataset information
print("\nDataset Overview")
print("Total Students:", len(df))
print("Average Marks:", round(df["Marks"].mean(), 2))
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

# 3. NumPy statistical analysis
marks = df["Marks"].to_numpy()

print("\nNumPy Statistics")
print("Median:", np.median(marks))
print("Standard Deviation:", round(np.std(marks), 2))

# 4. Categorize students
def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "Fail"

df["Grade"] = df["Marks"].apply(calculate_grade)

# 5. Identify performance
df["Status"] = np.where(df["Marks"] >= 40, "Pass", "Fail")

# 6. Rank students
df["Rank"] = df["Marks"].rank(
    ascending=False,
    method="dense"
).astype(int)

# 7. Display top three students
print("\nTop 3 Students")
top_students = df.sort_values(
    by="Marks",
    ascending=False
).head(3)

print(top_students[["Name", "Marks", "Grade", "Rank"]])

# 8. Identify students needing improvement
print("\nStudents Needing Improvement")
weak_students = df[df["Marks"] < 70]
print(weak_students[["Name", "Marks"]])

# 9. City-wise performance
print("\nCity-wise Average Marks")
print(df.groupby("City")["Marks"].mean().round(2))

# 10. Grade distribution
print("\nGrade Distribution")
print(df["Grade"].value_counts())

# 11. Export final report
output_path = Path(__file__).parent / "student_performance_report.csv"
df.to_csv(output_path, index=False)

print("\nReport exported successfully!")
print("File:", output_path)
