__author__ = 'julian'
import math
class scoring:
    def __init__(self, n, indexList):
        self.n = n
        self.indexList = indexList
        self.weigthMatrix = indexList
        self.docLength = [0] * n
        self.calcWeightMatrix()
        self.calcDocLength()

    def termFreq(self,t, d):
        return self.indexList[t][d]

    def docFreq(self, t):
        return len(self.indexList[t])

    def weight(self, t, d):
        return (1 + math.log10(self.termFreq(t, d))) * math.log10(self.n/self.docFreq(t))


    def calcWeightMatrix(self):
        for wort, docs in self.indexList.items():
            for doc, freq in docs.items():
                self.weigthMatrix[wort][doc] = self.weight(wort, doc)

    def calcDocLength(self):
        for wort, docs in self.weigthMatrix.items():
            for doc, weight in docs.items():
                self.docLength[doc] = self.docLength[doc] + weight * weight


    def calcScoreForQuery(self, query):
        score = [0] * self.n
        terms = query.split(" ")
        for term in terms:
            for doc, weight in self.weigthMatrix[term].items():
                score[doc] = weight * 1
        print(score)



