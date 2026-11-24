import numpy as np

# Student marks
marks = np.array([
    [85, 90, 78],
    [92, 88, 95],
    [67, 72, 70],
    [45, 55, 60],
    [80, 85, 89]
])

subjects = ["Maths", "Science", "English"]

print("STUDENT MARKS ANALYSIS")

# Overall statistics
print("\nTotal Marks:", np.sum(marks))
print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))

# Average marks for each student
student_averages = np.mean(marks, axis=1)

print("\nAverage marks of each student:")
print(student_averages)

# Average marks in each subject
subject_averages = np.mean(marks, axis=0)

print("\nSubject-wise averages:")
for i in range(len(subjects)):
    print(subjects[i], ":", subject_averages[i])

# Find topper
topper_index = np.argmax(student_averages)

print("\nTopper is Student", topper_index + 1)
print("Topper Average:", student_averages[topper_index])

# Students who scored above 75 average
print("\nStudents scoring above 75:")
print(student_averages[student_averages > 75])

# Standard deviation
print("\nStandard Deviation:", np.std(marks))