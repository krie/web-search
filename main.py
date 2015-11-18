from pageRank import pageRank
from crawler import crawler
from indexing import indexer
from scoring import scoring


mycrawler = crawler("seed.dat")
mycrawler.crawl()

myMatrix = mycrawler.getUebergangsMatrix()
myRank = pageRank(websiteMatrix=myMatrix)
myRank.calcRank()

myIndexer = indexer(mycrawler.getFinalUrlset())
myIndexer.runIndexing()
myIndexer.outputIndexToFile()

index = myIndexer.indexDict
myScoring = scoring(len(mycrawler.getFinalUrlset()), index)

again = "j"
while again == "j":
    queryString = input("Suchbegriff(e): ")
    myScoring.calcScoreForQuery(queryString)

    again = input("Neue Suche? j/n: ")
    print()