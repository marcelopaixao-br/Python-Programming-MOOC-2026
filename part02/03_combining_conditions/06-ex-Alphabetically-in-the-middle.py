# Exercise: Alphabetically in the middle
# Course: Python Programming MOOC 2026 (University of Helsinki)
# Section: Part 3 - Combining conditions

letter1 = input("Please type in the 1st letter: ")
letter2 = input("Please type in the 2nd letter: ")
letter3 = input("Please type in the 3rd letter: ")

if (letter2 <= letter1 <= letter3) or (letter3 <= letter1 <= letter2):
    middle = letter1
elif (letter1 <= letter2 <= letter3) or (letter3 <= letter2 <= letter1):
    middle = letter2
else:
    middle = letter3

print(f"The letter in the middle is {middle}")