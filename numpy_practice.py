# =====================================
# PART 1: NUMPY BASICS
# =====================================

# Step 1: Import NumPy
import numpy as np

# Step 2: Create a NumPy array
marks = np.array([70, 80, 90, 60, 85])

# Step 3: Print the array
print("Student Marks:")
print(marks)

# Step 4: Add 5 marks to every student
updated_marks = marks + 5

print("Updated Marks:")
print(updated_marks)

# Step 5: Calculate average
average = np.mean(marks)

print("Average Marks:", average)

# Step 6: Find maximum and minimum marks
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))


# =====================================
# PART 2: NUMPY INDEXING AND SLICING
# =====================================

import numpy as np

marks = np.array([70, 80, 90, 60, 85, 95])

# Access individual elements
print("\n--- INDEXING ---")

print("First mark:", marks[0])
print("Third mark:", marks[2])
print("Last mark:", marks[-1])

# Access multiple elements
print("\n--- SLICING ---")

print("First three marks:", marks[0:3])
print("Last three marks:", marks[3:])
print("Every second mark:", marks[::2])


# =====================================
# PART 3: NUMPY MATHEMATICAL OPERATIONS
# =====================================

import numpy as np

marks = np.array([70, 80, 90, 60, 85, 95])

print("\n--- MATHEMATICAL OPERATIONS ---")

print("Total marks:", np.sum(marks))
print("Average marks:", np.mean(marks))
print("Highest marks:", np.max(marks))
print("Lowest marks:", np.min(marks))
print("Standard deviation:", np.std(marks))

# Adding and multiplying
print("\n--- ARRAY OPERATIONS ---")

print("Add 5:", marks + 5)
print("Subtract 5:", marks - 5)
print("Multiply by 2:", marks * 2)
print("Divide by 2:", marks / 2)


# =====================================
# PART 4: NUMPY MINI PROJECT
# Student Marks Analysis
# =====================================

import numpy as np

# Marks of 8 students
marks = np.array([45, 78, 90, 32, 88, 67, 95, 55])

print("\n===== STUDENT MARKS ANALYSIS =====")

# 1. Calculate average
average = np.mean(marks)
print("Class Average:", average)

# 2. Find highest marks
highest = np.max(marks)
print("Highest Marks:", highest)

# 3. Find lowest marks
lowest = np.min(marks)
print("Lowest Marks:", lowest)

# 4. Find students scoring above 70
above_70 = marks[marks > 70]
print("Students scoring above 70:", above_70)

# 5. Count students who passed (marks >= 40)
passed = marks[marks >= 40]
print("Number of students passed:", len(passed))

# 6. Count students who failed
failed = marks[marks < 40]
print("Number of students failed:", len(failed))

# 7. Increase everyone's marks by 5
updated_marks = marks + 5
print("Updated Marks:", updated_marks)
