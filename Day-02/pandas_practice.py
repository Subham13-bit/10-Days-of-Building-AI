import pandas as pd
from pathlib import Path
print(pd.__version__)

# DAY 2 - PANDAS PRACTICE

# PART 1: CREATE A SERIES

marks = pd.Series([85, 90, 78, 95, 88])

print("STUDENT MARKS:")
print(marks)


# PART 2: CREATE A DATAFRAME

data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Rohan"],
    "Age": [20, 21, 20, 22, 21],
    "Marks": [85, 90, 78, 95, 88]
}

df = pd.DataFrame(data)

print("\nSTUDENT DATAFRAME:")
print(df)


# PART 3: ACCESS COLUMNS

print("\nSTUDENT NAMES:")
print(df["Name"])

print("\nSTUDENT MARKS:")
print(df["Marks"])


# PART 4: BASIC INFORMATION

print("\nDATAFRAME SHAPE:")
print(df.shape)

print("\nDATAFRAME COLUMNS:")
print(df.columns)

print("\nDATAFRAME INFORMATION:")
print(df.info())

print("\nSTATISTICAL SUMMARY:")
print(df.describe())


# =====================================
# PART 5: READING CSV FILES
# =====================================

# Read CSV file
df = pd.read_csv(Path(__file__).parent / "students.csv")

# Display complete dataset
print("\nCOMPLETE DATASET:")
print(df)

# Display first 5 rows
print("\nFIRST 5 ROWS:")
print(df.head())

# Display last 3 rows
print("\nLAST 3 ROWS:")
print(df.tail(3))

# Display number of rows and columns
print("\nDATASET SHAPE:")
print(df.shape)


# =====================================
# PART 6: PANDAS FILTERING
# =====================================


df = pd.read_csv(Path(__file__).parent / "students.csv")

# Students scoring above 80
high_scorers = df[df["Marks"] > 80]

print("\nSTUDENTS SCORING ABOVE 80:")
print(high_scorers)

# Students scoring below 80
low_scorers = df[df["Marks"] < 80]

print("\nSTUDENTS SCORING BELOW 80:")
print(low_scorers)

# Students from Bhubaneswar
bhubaneswar_students = df[df["City"] == "Bhubaneswar"]

print("\nSTUDENTS FROM BHUBANESWAR:")
print(bhubaneswar_students)

# Part 8: Grouping data by city

city_average = df.groupby("City")["Marks"].mean()
print("Average marks by city:")
print(city_average)

city_count = df.groupby("City")["Name"].count()
print("\nNumber of students in each city:")
print(city_count)

# Part 9: Handling missing values

print("Checking missing values:")
print(df.isnull().sum())

# Fill missing marks with the average marks
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Remove rows with missing values
df_cleaned = df.dropna()

print("\nCleaned dataset:")
print(df_cleaned)

# Part 10: Creating new columns

df["Result"] = df["Marks"].apply(
    lambda marks: "Pass" if marks >= 40 else "Fail"
)

print("Dataset with Result column:")
print(df)

# Part 11: Exporting data to CSV

output_path = Path(__file__).parent / "students_processed.csv"

df.to_csv(output_path, index=False)

print("Dataset successfully exported!")
print("Saved at:", output_path)