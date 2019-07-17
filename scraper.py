import scrapy


class BricketSpider(scrapy.Spider):
    name="brickset_spider"
    start_urls = ['http://brickset.com/sets/year-2016']
    
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url = input("Enter website url")

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
print(page_soup)




