# Exercise: Repeat password
# Course: Python Programming MOOC 2026 (University of Helsinki)
# Section: Part 2 - Simple loops

password1 = input("Password: ")
password2 = input("Repeat password: ")

while True:
    if password1 == password2:
        print("User account created!")
        break
    else:
        print("They do not match!")
        password2 = input("Repeat password: ")