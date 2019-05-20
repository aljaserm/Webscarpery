from bs4 import BeautifulSoup as bs
import requests as rq
from PIL import Image
from io import BytesIO as by
import os


def search():
    searching = input("Enter Search Word: ")
    folderName = searching.replace(" ", "_").lower()
    if not os.path.isdir(folderName):
        os.makedirs(folderName)
    paramater = {"q": searching}
    req = rq.get("https://www.bing.com/images/search", params=paramater)
    soup = bs(req.text, "html.parser")
    links = soup.findAll("a", {"class": "thumb"})

    for l in links:
        try:
            imgHref = rq.get(l.attrs["href"])
            print("Url: ", l.attrs["href"])
            title = l.attrs["href"].split("/")[-1]
            try:
                img = Image.open(by(imgHref.content))
                img.save("./"+folderName+"/" + title, img.format)
            except:
                print("Didn't Save")
        except:
            print("Didn't request")

    search()


search()
