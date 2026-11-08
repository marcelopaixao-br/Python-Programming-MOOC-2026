# Exercise: Working with numbers (Parts 1 to 4)
# Course: Python Programming MOOC 2026 (University of Helsinki)
# Section: Part 2 - Simple loops

count = 0
total_sum = 0
positives = 0
negatives = 0

print("Please type in integer numbers. Type in 0 to finish.")

while True:
    number = int(input("Number: "))
    
    # 0 is the sentinel value to exit the loop
    if number == 0:
        break
        
    # Increment total numbers typed
    count += 1
    # Add to the cumulative sum
    total_sum += number
    
    # Check if the number is positive or negative
    if number > 0:
        positives += 1
    else:
        negatives += 1

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {total_sum}")

# Calculate and print the mean only if at least one number was entered
if count > 0:
    mean = total_sum / count
    print(f"The mean of the numbers is {mean}")
    
print(f"Positive numbers {positives}")
print(f"Negative numbers {negatives}")