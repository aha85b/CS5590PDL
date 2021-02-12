# Open the file
file = open("words.txt", "r")
dict_count = dict()
# This function loops inside the file
def readFile():
    for line in file:
        line = line.strip()
        words = line.split(" ")
        countWords(words)


# Looping to check if the word was added to dictionary or add it
def countWords(words):
    for word in words:
        if word in dict_count:
            dict_count[word] = dict_count[word] + 1
        else:
            dict_count[word] = 1
# Looping to print all words
def printResult():
    for result in list(dict_count.keys()):
        print(result, ":", dict_count[result])

# Run functions
readFile()
printResult()
file.close()

file = open('words.txt', 'w')

def writeinFile():
    for wr in dict_count:
        file.write(wr)
        file.write(": ")
        file.write(str(dict_count[wr]))
        file.write("\n")

# Run function to write over words.txt file
writeinFile()
file.close()