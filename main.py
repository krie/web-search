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

index = myIndexer.getIndexMatrix()
myScoring = scoring(len(mycrawler.getFinalUrlset()), index)

running = True
while running:
    eingabe = input("Nach welchen Wörtern wollen Sie suchen?:\n\t ")
    if (eingabe == "exit"):
        running = False
    else:
        myScoring.calcScoreForQuery(eingabe, myRank.ranking)
        print("\n")