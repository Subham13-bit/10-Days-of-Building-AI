# =====================================
# DAY 1 - PYTHON PRACTICE CHALLENGES
# =====================================


# CHALLENGE 1: Find the Second Largest Unique Number

numbers = [10, 20, 40, 30, 40]

unique_numbers = set(numbers)
sorted_numbers = sorted(unique_numbers)

second_largest = sorted_numbers[-2]

print("Challenge 1: Second Largest Number")
print(second_largest)


# =====================================
# CHALLENGE 2: Count Word Frequency
# =====================================

words = ["AI", "Python", "ML", "AI", "Python", "AI"]

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nChallenge 2: Word Frequency")
print(frequency)


# =====================================
# CHALLENGE 3: Find Even Numbers
# =====================================

numbers = [12, 7, 9, 20, 15, 8, 3, 14]

even = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)

print("\nChallenge 3: Even Numbers")
print(even)

# =====================================
# CHALLENGE 4: Largest Number without max()
# =====================================

numbers = [10, 20, 40, 30, 40]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("\nChallenge 4: Largest Number")
print(largest)


# =====================================
# CHALLENGE 5: List Comprehension
# =====================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = [number for number in numbers if number % 2 == 0]

print("Challenge 5: Even Numbers using List Comprehension")
print(even)
