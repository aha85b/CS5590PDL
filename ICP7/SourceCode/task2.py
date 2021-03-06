import urllib

import nltk
from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
from nltk import word_tokenize, pos_tag, ne_chunk
#nltk.download()


# Create input.txt file if not already created
file = open('input.txt', 'a+', encoding='utf-8')

# Extract Data from url link
url = "https://en.wikipedia.org/wiki/Google"
content = urllib.request.urlopen(url)

# Parse HTML document
soup = BeautifulSoup(content, "html.parser")
body = soup.find('div', {'class': 'mw-parser-output'})
file.write(str(body.text))




# Read from file
sentence = open('input.txt', encoding="utf8").read()

# Breaking a stream of text up Slide#18
sentence_tokens = nltk.sent_tokenize(sentence)
word_tokens = nltk.word_tokenize(sentence)
print(word_tokens)

print("\n Tokenization ")

# Print first 6 sentence
sentence_token_count = 0
for sent_token in sentence_tokens:
    sentence_token_count += 1
    if sentence_token_count < 7:
        print("sent token:", sent_token)
        print(sentence_token_count)

# Print first 6 words from first sentence
word_token_count = 0
for word_token in word_tokens:
    word_token_count += 1
    if word_token_count < 7:
        print("word token:", word_token)

# Classifying the words in a text(corpus) into their parts of speech and labeling them Slide#20&21
print("\n POS ")

word_token_count = 0
for word_token in word_tokens:
    word_token_count += 1
    if word_token_count < 7:
        print(nltk.pos_tag(word_token))


# Reducing injected words to their stem Silde#23
print("\n Stemming ")

p_stemmer = PorterStemmer()
l_stemmer = LancasterStemmer()
s_stemmer = SnowballStemmer('english')

word_token_count = 0
for word_token in word_tokens:
    word_token_count += 1
    if word_token_count < 7:
        print(p_stemmer.stem(word_token), l_stemmer.stem(word_token), s_stemmer.stem(word_token))


# Determining the part of speech of a word Slide#25
print("\n Lemmatization ")

lemmatizer = WordNetLemmatizer()

word_token_count = 0
for word_token in word_tokens:
    word_token_count += 1
    if word_token_count < 6:
            print("Lemmatizer:", lemmatizer.lemmatize(word_token), ",    With POS=a:",
                  lemmatizer.lemmatize(word_token, pos="a"))



# Print them as bigram and trigram orders slide#30&31
print("\n Trigram ")

sent_token_count = 0
for sentence_token in sentence_tokens:
    sent_token_count += 1
    if sent_token_count < 2:
        token = nltk.word_tokenize(sentence_token)
        bigrams = list(ngrams(token, 2))
        trigrams = list(ngrams(token, 3))
        print("The text:", sentence[:100], "\nword_tokenize:", token, "\nbigrams:", bigrams, "\ntrigrams", trigrams)


# Named entity recognition Slide#28
print("\n NER ")

sent_token_count = 0
for sentence_token in sentence_tokens:
    sent_token_count += 1
    if sent_token_count < 3:
        print(ne_chunk(pos_tag(word_tokenize(sentence_token))))


