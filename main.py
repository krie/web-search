from pageRank import pageRank
__author__ = 'Alexander'

testMatrix = [[0, 1, 1, 1, 0],
              [0, 0, 1, 0, 1],
              [0, 0, 0, 1, 1],
              [0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0]]

myRank = pageRank(testMatrix)
myRank.calcRank()
