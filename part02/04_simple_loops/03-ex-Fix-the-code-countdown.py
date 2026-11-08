# Course: Python Programming MOOC 2026 (University of Helsinki)
# Section: Part 2 - Simple loops
# Exercise: Fix the code: Countdown

number = 5
print("Countdown!")
while True:
    print(number)
    number = number - 1
    if number == 0:
        break

print("Now!")