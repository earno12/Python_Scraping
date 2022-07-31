from urllib.error import URLError
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

URL = "https://www.newegg.com/p/pl?N=100011693%204814%204131%20600038493%20600038497%20600545605%20601354671%201100858365%204808%20601193224%20600038463%20600640786%20600521287%20600038519%2050001077&PageSize=96&Order=1"

page = requests.get(URL, headers)
soup = BeautifulSoup(page.content, "html.parser")
print(soup)

#results = soup.find("c-wiz")

#titles = results.find_all("a", class_="DY5T1d RZIKme")

#with open("news01Jul.txt", "w") as external_file:
    #for title in titles:
        #print(title.text.strip(), file=external_file)
    #external_file.close()

    #print(title.text.strip())
    #newsArticle = title.text.strip()
