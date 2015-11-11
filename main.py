from pageRank import pageRank
from crawler import crawler
from indexing import indexer
from scoring import scoring


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

myIndexer = indexer(mycrawler.urlSetDone)
myIndexer.runIndexing()
myIndexer.outputIndexToFile()

index = myIndexer.indexDict
myScoring = scoring(len(mycrawler.urlSetDone), index)
myScoring.calcScoreForQuery("and")