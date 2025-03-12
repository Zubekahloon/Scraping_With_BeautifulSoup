import requests 
from bs4 import BeautifulSoup
import pandas as pd

page = 1

Data = []

process = True
while(process):

    responce = requests.get(f"https://books.toscrape.com/catalogue/page-{page}.html")
    soup = BeautifulSoup(responce.text, 'html.parser')
    #print(soup.title.text)
    if soup.title.text == "404 Not Found":
        process = False
    
    else:
        books = soup.find_all('li', class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
        for book in books:
            item ={}

            item['Title'] = book.find('img').attrs["alt"]

            item['Link'] = "https://books.toscrape.com/catalogue"+book.find('a').attrs["href"]

            item['Price'] = book.find('p', class_="price_color")

            item['Stock'] = book.find('p', class_="instock availability")

            Data.append(item)

    page += 1

df = pd.DataFrame(Data)
df.to_excel("bookss.csv")