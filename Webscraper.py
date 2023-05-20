import requests, csv, pandas as pd, pprint, time
from bs4 import BeautifulSoup
import pandas as pd

# review_dict = {"name": [], "date": [], "Metascore": [], "User Score": [], "review": []}

# Find names
# titles = soup.find_all("a", class_="title")
# for list in titles:
# review_dict["name"].append(list.find("h3").text)
# review_dict["url"].append(list.find(href=True))


# Find Url
def web(Npages):
    url = (
        "https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?year_selected=2010&distribution=&sort=desc&view=condensed&page="
        + str(Npages)
    )
    user_agent = {"User-agent": "Mozilla/5.0"}
    response = requests.get(url, headers=user_agent)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def scrapper(soup, review_dict):
    info = soup.find_all("tr")
    for tr in info:
        td = tr.find_all("td")
        for td in td[1].find_all("a", {"class": "title"}):
            review_dict["name"].append(td.find("h3"))
        td = tr.find_all("td")
        for td in td[1].find_all("a", {"class": "title"}, href=True):
            review_dict["url"].append(td["href"])


def page(soup):
    pages = soup.find_all("li", {"class": "page last_page"})
    Npages = pages[0].find("a").text
    return Npages


def main():
    review_dict = {"name": [], "url": []}
    i = 0
    while i < int(page(web(0))):
        scrapper(web(i), review_dict)
        print(review_dict["name"])
        time.sleep(10)
        i = i + 1


main()
