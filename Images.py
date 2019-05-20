from bs4 import BeautifulSoup as bs
import requests as rq
from PIL import Image
from io import BytesIO as by

searching = input("Enter Search Word: ")
paramater = {"q": searching}
req = rq.get("https://www.bing.com/images/search", params=paramater)
soup = bs(req.text, "html.parser")
links = soup.findAll("a", {"class" : "thumb"})

for l in links:
    imgHref= rq.get(l.attrs["href"])
    print("Url: ", l.attrs["href"])
    title=l.attrs["href"].split("/")[-1]
    img=Image.open(by(imgHref.content))
    img.save("./webImgs/"+title, img.format)

