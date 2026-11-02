# Exercise: The elder
# Course: Python Programming MOOC 2026 (University of Helsinki)
# Section: Part 2 - More conditionals

name1 = input("What is you name Person 1: ")
age1 = int(input("How old are you Person 1: "))
name2 = input("What is your name Person 2: ")
age2 = int(input("How old are you Person 2: "))

if age1 > age2:
    print(f"The elder is {name1}")
elif age1 < age2:
    print(f"The elder is {name2}") 
else:
    print(f"{name1} and {name2} are the same age")