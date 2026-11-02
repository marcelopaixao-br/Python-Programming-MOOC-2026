# Exercise: Greater than or equal to
# Course: Python Programming MOOC 2026 (University of Helsinki)
# Section: Part 2 - More conditionals

number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in another number: "))

if number1 > number2:
    print(f"The greater number was: {number1}")
elif number2 > number1:
    print(f"The greater number was: {number2}")
else:
    print("The numbers are equal!")