# Exercise: FizzBuzz
# Course: Python Programming MOOC 2026 (University of Helsinki)
# Section: Part 3 - Combining conditions

number = int(input("Type in a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")