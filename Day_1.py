# sum_numbers.py

# Read input from the input.txt file
with open('input.txt', 'r') as file:
    input_data = file.read()

# Split the input string into a list of integers
numbers = list(map(int, input_data.split()))

# Calculate the sum of the numbers
total_sum = sum(numbers)
print("Hello")
# Write the output to the output.txt file
with open('output.txt', 'w') as file:
    file.write(f"The sum of the numbers is: {total_sum}")
