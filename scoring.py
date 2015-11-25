import operator

__author__ = 'julian'
import math
import collections as col
import pandas as pd
pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

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

    def weight(self, tf, df):
        weightVal = 1 + math.log10(tf)
        weightVal = weightVal * math.log10(self.n/df)
        return weightVal

    def calcWeightMatrix(self):
        for column in list(self.indexList.columns):
            index = 0
            df = 0
            for val in self.indexList[column]:
                if(val > 0):
                    df += 1

            for val in self.indexList[column]:
                if(val > 0):
                    self.indexList[column][index] = self.weight(val, df)
                index += 1

    def calcDocLength(self):
        for index, row in self.indexList.iterrows():
            self.docLength[index] = row.values.dot(row.values)

    def calcScoreForQuery(self, query, pagerank):
        score = {}
        query = query.lower()
        terms = query.split(" ")
        queryWeight = []
        for column in list(self.indexList.columns):
            if column in terms:
                queryWeight.append(1)
            else:
                queryWeight.append(0)
        for index, row in self.indexList.iterrows():
            if (row.values.dot(queryWeight) > 0):
                score[index] = row.values.dot(queryWeight) / self.docLength[index] * pagerank[index];
        orderedScore = sorted(score.items(), key=operator.itemgetter(1), reverse=True)
        for item in orderedScore:
            print(item)




