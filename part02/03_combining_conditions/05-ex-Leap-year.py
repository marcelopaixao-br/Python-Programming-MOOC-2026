# Exercise: Leap year
# Course: Python Programming MOOC 2026 (University of Helsinki)
# Section: Part 3 - Combining conditions

year = int(input("Type in a year: "))

if year % 400 == 0:
    print("That year is a leap year.")
elif year % 100 == 0:
    print("That year is not a leap year.")
elif year % 4 == 0:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")