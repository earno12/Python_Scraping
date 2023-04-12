import re
import requests
from bs4 import BeautifulSoup
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
nltk.download('wordnet')
nltk.download('stopwords')

# This will be a News Headline scraper for Google News
# This program only requires requests and BeautifulSoup to achieve its current purpose.

# sets up headers
# considers CORS
# uses GET method
# uses a Mozilla Firefox user-agent
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}

# the World news URL for Google News
URL = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen"

output_filename = input("Enter a filename for your results: ")

page = requests.get(URL).text # gets the source of the URL and renders as text

soup = BeautifulSoup(page, "html.parser") # passes text to BeautifulSoup

results = soup.find_all("h4") # finds all h4 HTML tags

# opens a new text file with the user chosen name in write mode
# builds an array of the h4 tags
# strips the h4 tags to get the news article names
# writes the article names to the text file
# saves the text file and closes it
with open(f"{output_filename}.txt", "w") as external_file:
    for result in results:
        print(result.text.strip(), file=external_file)
    external_file.close()

def count_unique_words(output_filename):
    with open(f"{output_filename}.txt", 'r') as file:
        text = file.read()
        words = text.split()

        # Get the NLTK stopword list
        stop_words = set(stopwords.words('english'))

        # Create a WordNetLemmatizer object
        lemmatizer = WordNetLemmatizer()

        word_counts = {}
        for word in words:
            word = word.lower()
            # Remove all punctuation characters from the word
            word = "".join([char for char in word if char not in string.punctuation])
            palestinian_regex = re.compile(r'palestini.*')
            canadian_regex = re.compile(r'canadi.*')
            if len(word) > 4 and word not in stop_words:
                if word == "russian":
                    word = "russia"
                elif palestinian_regex.match(word):
                    word = "palestine"
                elif word == "ukrainian":
                    word = "ukraine"
                elif word == "israeli":
                    word = "israel"
                elif canadian_regex.match(word):
                    word = "canada"
                else:
                    # Lemmatize the word using WordNetLemmatizer algorithm
                    pos = wordnet.synsets(word)[0].pos() if wordnet.synsets(word) else 'v'
                    word = lemmatizer.lemmatize(word, pos=pos)
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
        with open("word_count.txt", "w") as word_count_file:
            sorted_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
            for word, count in sorted_counts:
                if count > 6:
                    print(f"{word}: {count}", file=word_count_file)
            word_count_file.close()

count_unique_words(output_filename)