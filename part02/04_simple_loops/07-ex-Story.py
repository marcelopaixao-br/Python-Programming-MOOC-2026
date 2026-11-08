# Exercise: Story (Part 2)
# Course: Python Programming MOOC 2026 (University of Helsinki)
# Section: Part 2 - Simple loops

story = []
previous_word = ""

while True:
    word = input("Type in a word: ")
    
    # Condition to end the loop: if the user types "end" or repeats the previous word
    if word == "end" or word == previous_word:
        break
        
    # The .append() method adds the typed word to the end of the 'story' list
    story.append(word)
    previous_word = word

# The " ".join(story) method joins all elements of the list into a single string, 
# separating each word with a blank space (" ")
full_story = " ".join(story)
print(full_story)