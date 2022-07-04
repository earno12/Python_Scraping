import requests; from bs4 import BeautifulSoup

# This will be a News Headline scraper for Google News
# This program only technically requires requests and BeautifulSoup to achieve its current purpose.

URL = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find("c-wiz")

titles = results.find_all("a", class_="DY5T1d RZIKme")

for title in titles:
    print(title.text.strip())