# DAY 1 - PYTHON PRACTICE
# 10 Days of Building AI Challenge
# =====================================

print("Welcome to Day 1 of my AI Challenge!")

# 1. Variables
name = "Subham"
age = 21
interest = "Artificial Intelligence"

print("\nMy name is:", name)
print("My age is:", age)
print("My interest is:", interest)

# 2. Lists
skills = ["Python", "NumPy", "Pandas", "Machine Learning"]

print("\nMy skills:")
for skill in skills:
    print("-", skill)

# 3. Dictionary
student = {
    "name": "Subham",
    "branch": "CSE (AI-ML)",
    "year": 3,
    "cgpa": 8.8
}

print("\nStudent Details:")
print(student)

# 4. List Comprehension
numbers = range(1, 11)

squares = [n**2 for n in numbers]

print("\nSquares:", squares)
