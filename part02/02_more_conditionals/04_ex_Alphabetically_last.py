# Exercise: Alphabetically last
# Course: Python Programming MOOC 2026 (University of Helsinki)
# Section: Part 2 - More conditionals

word1 = input("Please type in the 1st word: ")
word2 = input("Please type in the 2nd word: ")

if word1 < word2:
    print(f"{word2} comes alphabetically last.")
elif word1 > word2:
    print(f"{word1} comes alphabetically last.")
else:
    print("You gave the same word twice.")