# Exercise: The next leap year
# Course: Python Programming MOOC 2026 (University of Helsinki)
# Section: Part 2 - Simple loops

year = int(input("Type in a year: "))
current_year = year

while True:
    current_year += 1
    
    if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
        print(f"The next leap year after {year} is {current_year}")
        break