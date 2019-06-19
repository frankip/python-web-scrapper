import ssl
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import urllib
import certifi
data_list = []
def another_link(link):
    req = urllib.request.Request(
        link, 
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )

    uClient = uReq(req, cafile=certifi.where())
    html_page = uClient.read()
    uClient.close()

    page_soup = soup(html_page, "html.parser")

    # Take each item card
    item_data = page_soup.findAll("div", {"class": "sku -gallery"})
    # mabaya_data = page_soup.findAll("div", {"class": "mabaya sku -gallery"})
    # offers_data = page_soup.findAll("div", {"class": "sku -gallery -has-offers"})

    

    # length of container
    print(len(item_data))
    # print(len(mabaya_data))
    # print(len(offers_data))

    # Loop through the container
    for data in item_data:
        item_link = (data.a["href"])

        item_brand_data = data.a.h2.findAll("span", {"class": "brand"})
        item_brand = item_brand_data[0].text.strip()

        item_name_data = data.a.h2.findAll("span", {"class": "name"})
        item_name = item_name_data[0].text.strip()

        item_price_data = data.a.findAll("span", {"class": "price"})
        item_price = int(item_price_data[0].select("span > span")[1]["data-price"])

        data_dict = {
            "name": item_name,
            "brand": item_brand,
            "price": item_price,
            "link": item_link
        }
        data_list.append(data_dict)
    return data_list
        