__author__ = 'Alexander'
from crawler import crawler
from bs4 import BeautifulSoup
import numpy as np
import requests
import collections as col

class indexer():
    def __init__(self, urlset):
        self.urlSetDone = []
        self.urlset = urlset
        self.indexDict = col.defaultdict(dict)

    def runIndexing(self):
        while(self.urlset):
            url = self.urlset.pop()
            #print(url)
            self.urlSetDone.append(url)
            r = requests.get(url)
            data = r.text
            soup = BeautifulSoup(data)
            texts = soup.get_text()
            texts = texts.replace("\n", " ")
            texts = texts.replace('.', " ")
            texts = texts.replace(',', " ")
            texts = texts.replace('!', " ")
            texts = texts.replace('?', " ")
            texts = texts.split(" ")
            #print(texts)
            url = url.rsplit('/',1)[-1]
            for wort in texts:
                if(wort != ""):
                    try:
                        self.indexDict[wort.lower()][url] += 1
                    except KeyError:
                        self.indexDict[wort.lower()][url] = 1
            self.orderedIndexDict = col.OrderedDict(sorted(self.indexDict.items()))
            #print(self.indexDict)

mycrawler = crawler("seed.dat")
mycrawler.crawl()
#mycrawler.getUebergangsMatrix()

indexer = indexer(mycrawler.urlSetDone)
indexer.runIndexing()
for word, loc in indexer.orderedIndexDict.items():
    doc_freq = 0
    for url, vorkommen in loc.items():
        doc_freq += vorkommen
    print("{0: <15} {1: <3}:  -> {2}".format(word, doc_freq, loc))