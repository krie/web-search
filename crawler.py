from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

__author__ = 'Alexander'

class crawler():
    def __init__(self, seedfile):
        self.seedfile = seedfile
        self.urlSetDone = []     # Bereits besuchte URLs
        self.urlset = []
    def crawl(self):
        with open("seed.dat", "r") as fileInput:
            for zeile in fileInput:
                self.urlset.append(zeile)
        while(len(self.urlset) > 0):
            url = self.urlset.pop()
            print('Aktuelle URL: {}, noch {} im URLset'.format(url, len(self.urlset)))
            self.urlSetDone.append(url)
            r = requests.get(url)
            data = r.text
            soup = BeautifulSoup(data)
            for link in soup.findAll('a'):
                print('Link zu {} in url: {} gefunden'.format(link.get('href'), url))
                newUrl = urljoin(url, link.get('href'))
                if newUrl not in self.urlSetDone:
                    self.urlset.append(newUrl)

mycrawler = crawler("seed.dat")
mycrawler.crawl()