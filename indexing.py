__author__ = 'Alexander'
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
import requests
import collections as col

class indexer():
    def __init__(self, urlset):
        self.stopWoerter = ['d01', 'd02', 'd03', 'd04', 'd05', 'd06', 'd07', 'd08',
'a', 'also', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'do',
'for', 'have', 'is', 'in', 'it', 'of', 'or', 'see', 'so',
'that', 'the', 'this', 'to', 'we']
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
                    if wort not in self.stopWoerter:
                        try:
                            self.indexDict[wort.lower()][url] += 1
                        except KeyError:
                            self.indexDict[wort.lower()][url] = 1
            self.orderedIndexDict = col.OrderedDict(sorted(self.indexDict.items()))
            #print(self.indexDict)

    def outputIndexToFile(self):
        output_file = open('index.dat', 'w+')
        for word, loc in self.orderedIndexDict.items():
            doc_freq = 0
            for url, vorkommen in loc.items():
                doc_freq += vorkommen
            output_file.write("{0: <15} {1: <3}:  -> {2}\n".format(word, doc_freq, loc))

    def getIndexMatrix(self):
        df = pd.DataFrame(self.orderedIndexDict).fillna(0)
        return df