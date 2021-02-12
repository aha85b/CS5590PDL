


# Take input from user, the number of students
numOfStudents = input("Enter Number of Student: ")

# Convert input to integer
numOfStudents = int(numOfStudents)

# Create two lists, one list to save inputs in feet and another one to list calculated values in cm
listfeet = []
listcm =[]

# Loop to insert input from user and calculated values
i = 0
while i < numOfStudents:
    # Insert function into feet
    listfeet.insert(i, float(input("Enter Height in Feet: ")))
    # Insert function into cm
    listcm.insert(i, format(listfeet[i] * 30.48, '.2f'))
    # Loop until students number equals number of lists
    i+=1

# Print users input values of height
print(listfeet)

# Print calculated vales that converted to cm
print(listcm)