
import pandas as pd

# Step 1: Load the dataset
from pathlib import Path

df = pd.read_csv(Path(__file__).parent / "students.csv")

# Step 2: Display the first 5 rows
print("\nFIRST 5 STUDENTS")
print(df.head())

# Step 3: Display the last 5 rows
print("\nLAST 5 STUDENTS")
print(df.tail())

# Step 4: Check the number of rows and columns
print("\nDATASET SHAPE")
print(df.shape)

# Step 5: Display column names
print("\nCOLUMN NAMES")
print(df.columns)

# Step 6: Understand data types and missing values
print("\nDATASET INFORMATION")
df.info()

# Step 7: Statistical summary
print("\nSTATISTICAL SUMMARY")
print(df.describe())

# Step 8: Check missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Step 9: Check duplicate rows
print("\nDUPLICATE ROWS")
print(df.duplicated().sum())

# Step 10: Count students by gender
print("\nSTUDENTS BY GENDER")
print(df["Gender"].value_counts())

# Step 11: Count students by city
print("\nSTUDENTS BY CITY")
print(df["City"].value_counts())

# Step 12: Show students who scored 90 or more in Math
print("\nSTUDENTS WITH MATH MARKS >= 90")
print(df[df["Math"] >= 90][["Name", "Math"]])

# Step 13: Show students with attendance below 80
print("\nSTUDENTS WITH ATTENDANCE BELOW 80")
print(df[df["Attendance"] < 80][["Name", "Attendance"]])

# Step 14: Find the student with the highest Math score
top_math_student = df.loc[df["Math"].idxmax(), ["Name", "Math"]]

print("\nHIGHEST MATH SCORE")
print(top_math_student)

# Step 15: Calculate average marks for each subject
subject_averages = df[["Math", "Science", "English"]].mean()

print("\nAVERAGE MARKS BY SUBJECT")
print(subject_averages)

# Step 16: Calculate each student's total and average marks
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

print("\nTOP 5 STUDENTS BY AVERAGE")
print(df.sort_values("Average", ascending=False)[["Name", "Total", "Average"]].head())

# Step 17: Check the relationship between study hours and average marks
print("\nCORRELATION: STUDY HOURS AND AVERAGE MARKS")
print(df["Study_Hours"].corr(df["Average"]))