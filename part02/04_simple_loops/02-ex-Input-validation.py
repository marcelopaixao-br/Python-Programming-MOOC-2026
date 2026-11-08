# Course: Python Programming MOOC 2026 (University of Helsinki)
# Section: Part 2 - Simple loops
# Exercise: Input validation

from math import sqrt

while True:
    number = int(input("Type in a number: "))
    
    if number == 0:
        break
    elif number < 0:
        print("Invalid number")
    else:
        print(sqrt(number))

print("Exiting...")