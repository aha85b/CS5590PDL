# Take an input
num = input("Enter a Number: ")

# Must be Integer
num = int(num)

# Counter for counting steps
count = 0

# Loop if input is not Zero
while num != 0:
    # if input is dividable by 2
    if num%2 == 0:
        # Divide input by two
        num = int(num/2)
    else:
        # Subtract one, because the input is odd number
        num -= 1
    # Counter
    count += 1

# Print result
print(count)