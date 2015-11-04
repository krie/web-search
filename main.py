from pageRank import pageRank
from crawler import crawler

__author__ = 'Alexander'


testMatrix = [[0, 1, 1, 1, 0, 0, 0, 0],
              [1, 0, 1, 1, 1, 0, 0, 0],
              [1, 1, 0, 1, 1, 0, 0, 0],
              [1, 1, 1, 0, 1, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0]]

mycrawler = crawler("seed.dat")
mycrawler.crawl()
myMatrix = mycrawler.getUebergangsMatrix()
myRank = pageRank(websiteMatrix=myMatrix)
myRank.calcRank()
