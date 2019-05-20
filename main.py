from bs4 import BeautifulSoup as bs
import requests as rq

searching = input("Enter Search Word: ")
paramater = {"q": searching}
req = rq.get("https://www.bing.com/search", params=paramater)

soup = bs(req.text, "html.parser")
result = soup.find("ol", {"id": "b_results"})
links = result.findAll("li", {"class", "b_algo"})

for l in links:
    text=l.find("a").text
    href=l.find("a").attrs["href"]
    if text and href:
        print(text)
        print(href)
        # get parent
        # print("Summary: ", l.find("a").parent.parent.find("p").text)
        # get children
        # children=l.children
        # for c in children:
        #     print("child: ", c)
        #get sibling
        children=l.find("h2")
        print("next Sibling: ", children.next_sibling)

# print(soup.prettify())
