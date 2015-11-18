import operator

__author__ = 'julian'
import math
import collections as col

class scoring:
    def __init__(self, n, indexList):
        self.n = n
        self.indexList = indexList
        self.weigthMatrix = indexList
        self.docLength = {}
        self.calcWeightMatrix()
        self.calcDocLength()

    def termFreq(self,t, d):
        return self.indexList[t][d]

    def docFreq(self, t):
        return len(self.indexList[t])

    def weight(self, t, d):
        weightVal = 1 + math.log10(self.termFreq(t, d))
        weightVal = weightVal * math.log10(self.n/self.docFreq(t))
        #return ((1 + math.log10(self.termFreq(t, d))) * math.log10(self.n/self.docFreq(t)))
        return weightVal

    def calcWeightMatrix(self):
        for wort, docs in self.indexList.items():
            for doc, freq in docs.items():
                self.weigthMatrix[wort][doc] = self.weight(wort, doc)

    def calcDocLength(self):
        for wort, docs in self.weigthMatrix.items():
            for doc, weight in docs.items():
                if doc in self.docLength:
                    self.docLength[doc] +=  weight * weight
                else:
                    self.docLength[doc] =  weight * weight


    def calcScoreForQuery(self, query):
        score = {}
        terms = query.split(" ")
        for term in terms:
            for doc, weight in self.weigthMatrix[term].items():
                score[doc] = weight * 1
        orderedScore = sorted(score.items(), key=operator.itemgetter(1))
        print(orderedScore)



