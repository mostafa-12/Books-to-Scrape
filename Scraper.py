import requests
from bs4 import BeautifulSoup
import lxml
from urllib.parse import urljoin
from word2number import w2n
from Books import Book

def getBookDetails(url):
    page = requests.get(url).text
    src = BeautifulSoup(page,"lxml")
    bookTitle = src.find("div", attrs={"class" : "col-sm-6 product_main"}).find("h1").text
    category = src.find("ul", attrs={"class" : "breadcrumb"}).find_all("li")[2].text.strip()
    price = src.find("div", attrs={"class" : "col-sm-6 product_main"}).find("p",attrs={"class":"price_color"}).text[2:]
    Ninstock = src.find("div", attrs={"class" : "col-sm-6 product_main"}).find("p",attrs={"class":"instock availability"}).text.strip()
    stars = w2n.word_to_num(src.find("div", attrs={"class" : "col-sm-6 product_main"}).find("p",attrs={"class":"star-rating"})["class"][1])
    description = src.find("div",attrs={"id" : "product_description"}).find_next("p").text

    return Book(bookTitle,price,category,description,stars,Ninstock)

def getBooks(url):
    try:
        page = requests.get(url).text
        src = BeautifulSoup(page,"lxml")
        books= src.find("ol",class_="row").find_all("li","col-xs-6 col-sm-4 col-md-3 col-lg-3")
        return [f"https://books.toscrape.com/{book.a["href"]}" for book in books]
#Description - available - Product Information
    except ConnectionError as err :
        print("connection error ", err)
        print("*"*50)
        print("please check your connection and try again")
    except ValueError as err :
        print("value error: ", err)
        print("*" * 50)
        print("please enter correct input")
    except Exception as err :
        print("unexpected error: ", err)
        print("*" * 50)
