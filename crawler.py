from urllib.parse import urljoin

from bs4 import BeautifulSoup
import numpy as np
import requests
import collections as col

__author__ = 'Alexander'

class crawler():
    def __init__(self, seedfile):
        self.seedfile = seedfile
        self.urlSetDone = []     # Bereits besuchte URLs
        self.urlset = []
        self.uebergangsListe = col.defaultdict(dict)

    def crawl(self):
        with open("seed.dat", "r") as fileInput:
            alist = fileInput.read().splitlines()
            for line in alist:
                self.urlset.append(line)
        while(self.urlset):
            url = self.urlset.pop()
            #print('Aktuelle URL: {}, noch {} im URLset'.format(url, len(self.urlset)))
            self.urlSetDone.append(url)
            r = requests.get(url)
            data = r.text
            soup = BeautifulSoup(data)
            self.uebergangsListe[url][url] = 0
            for link in soup.findAll('a'):
                #print('Link zu {} in url: {} gefunden'.format(link.get('href'), url))
                newUrl = urljoin(url, link.get('href'))
                self.uebergangsListe[url][newUrl] = 1
                neueUrl = True
                for doneUrl in self.urlSetDone:
                    if(newUrl == doneUrl):
                        neueUrl = False
                if(neueUrl):
                    for todoUrl in self.urlset:
                        if(newUrl == todoUrl):
                            neueUrl = False
                if(neueUrl):
                    self.urlset.append(newUrl)

    def getUebergangsMatrix(self):
        matrix = np.zeros(shape=(len(self.urlSetDone), len(self.urlSetDone)));
        geordneteListe = col.OrderedDict(sorted(self.uebergangsListe.items()))
        #print(geordneteListe)
        for seite, links in geordneteListe.items():
            seiteIndex = list(geordneteListe.keys()).index(seite)
            for link, value in links.items():
                linkIndex = list(geordneteListe.keys()).index(link)
                matrix[seiteIndex, linkIndex] = value
        return matrix
