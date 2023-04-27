# import module
import requests
import pandas as pd
from bs4 import BeautifulSoup
  
# link for extract html data
def getdata(url):
    r = requests.get(url)
    return r.text

def spy(link):
    htmldata = getdata(link)
    soup = BeautifulSoup(htmldata, 'html.parser')
    soup = soup.find_all("p")
    return soup
    # dictionary = dict()
    # soup = BeautifulSoup(htmldata, 'html.parser')
    # data = ''
    # for data in soup.find_all("h2"):
    #     text = data.get_text()
    #     for data in soup.find_all("p"):
    #         key = (data.get_text())
    #         dictionary[text] = key
    # return dictionary

if __name__ == '__main__':
    link = input("Link: ")
    print(spy(link))
    