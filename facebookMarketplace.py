import argparse
import re

import requests
from bs4 import BeautifulSoup


def main():
    args = parseArgs()


def parseArgs():
    parser = argparse.ArgumentParser("online buy & sell helper")
    parser.add_argument("item", help="ex:beats solo3", type=str)
    args = parser.parse_args()

    return args

def constructUrl(args):
    item_name = args.item
    temp_name = item_name.split(str="")
    searchable_name = "";
    for word in temp_name:
        searchable_name += word + "%20"
    # searchable_name = searchable_name[:-3]
    return "https://www.facebook.com/marketplace/search?query=" + searchable_name

def startChecking(url):
    print("checking")
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        prices = soup.find_all('div', class_="_f3l _4x3g")
        print (prices)
    except Exception as e:
        print("error::", e)



if __name__ == "__main__":
    main()