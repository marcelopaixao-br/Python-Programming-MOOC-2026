# Exercise: PIN and number of attempts
# Course: Python Programming MOOC 2026 (University of Helsinki)
# Section: Part 2 - Simple loops

attempts = 0

while True:
    PIN = input("PIN: ")
    attempts += 1
    
    if PIN == "4321":
        # Check if it was guessed on the very first try
        if attempts == 1:
            print("Correct! It only took you one single attempt!")
        else:
            print(f"Correct! It took you {attempts} attempts")
        break
    else:
        print("Wrong")