import requests; from bs4 import BeautifulSoup

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
