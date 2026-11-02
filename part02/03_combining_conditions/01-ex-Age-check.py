# Exercise: Age check
# Course: Python Programming MOOC 2026 (University of Helsinki)
# Section: Part 3 - Combining conditions

age = int(input("What is your age: "))

if age >= 5 and age <= 99:
    print(f"Ok, you're {age} years old")
elif age >= 0 and age <= 5:
    print("I suspect you can't write quite yet...")
else:
    print("That must be a mistake")