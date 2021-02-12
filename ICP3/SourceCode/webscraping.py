from bs4 import BeautifulSoup # Import BeatifulSoup
from requests import get # Import get request

# Link to the website
html = get("https://en.wikipedia.org/wiki/Deep_learning")
soup = BeautifulSoup(html.content, "html.parser")

# Create file if not already created
file = open("content.txt", 'w')

# Print title
print(soup.title.string)

# Looping to find all a links <a> html
for link in soup.find_all('a'):
    # Write to file
    file.write(str(link.get('href')))
    file.write("\n")

file.close()