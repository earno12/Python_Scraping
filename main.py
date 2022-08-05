import requests; from bs4 import BeautifulSoup

# This will be a News Headline scraper for Google News
# This program only technically requires requests and BeautifulSoup to achieve its current purpose.

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}

URL = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen"

page = requests.get(URL, headers)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find("c-wiz")

titles = results.find_all("a", class_="DY5T1d RZIKme")

with open("news05Aug.txt", "w") as external_file:
    for title in titles:
        print(title.text.strip(), file=external_file)
    external_file.close()

    #print(title.text.strip())
    #newsArticle = title.text.strip()
