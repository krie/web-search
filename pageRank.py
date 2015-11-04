__author__ = 'julian'
class pageRank:
    def __init__(self, websiteMatrix = []):
        self.websiteMatrix = websiteMatrix

    def calcRank(self):
        i = 0
        for row in self.websiteMatrix:
            # 1en zaehlen
            ones = 0
            for cell in row:
                if cell == 1:
                    ones = ones + 1

            # Uebergangswahrscheinlichkeiten berechnen
            j = 0
            for cell in row:
                if ones != 0:
                    if cell == 1:
                        self.websiteMatrix[i][j] = 1/ones
                else:
                    self.websiteMatrix[i][j] = 1/len(self.websiteMatrix)
                j = j + 1

            # Teleportation und Daempfung berechnen
            t = 0.05  # Teleportationsrate
            d = 1 - t  # Daempfungsfaktor

            j = 0
            for cell in row:
                self.websiteMatrix[i][j] = cell * d + t/len(self.websiteMatrix)
                j = j + 1
            i = i + 1


        # Wahrscheinlichkeitsvektor pi initialisieren
        pi = []
        for i in self.websiteMatrix:
            pi.append(1/len(self.websiteMatrix))
        print(pi)
        delta = 1
        while delta > 0.04:
            piOld = pi.copy()

            for i in range(0, len(pi)):
                sum = 0
                for j in range(0, len(pi)):
                    sum += piOld[j] * self.websiteMatrix[j][i]
                pi[i] = sum
            """
            i = 0
            pi[i] = piOld[0] * self.websiteMatrix[0][i]\
                    + piOld[1] * self.websiteMatrix[1][i]\
                    + piOld[2] * self.websiteMatrix[2][i]\
                    + piOld[3] * self.websiteMatrix[3][i]\
                    + piOld[4] * self.websiteMatrix[4][i]\
                    + piOld[5] * self.websiteMatrix[5][i]\
                    + piOld[6] * self.websiteMatrix[6][i]\
                    + piOld[7] * self.websiteMatrix[7][i]

            i = 1
            pi[i] = piOld[0] * self.websiteMatrix[0][i]\
                    + piOld[1] * self.websiteMatrix[1][i]\
                    + piOld[2] * self.websiteMatrix[2][i]\
                    + piOld[3] * self.websiteMatrix[3][i]\
                    + piOld[4] * self.websiteMatrix[4][i]\
                    + piOld[5] * self.websiteMatrix[5][i]\
                    + piOld[6] * self.websiteMatrix[6][i]\
                    + piOld[7] * self.websiteMatrix[7][i]

            i = 2
            pi[i] = piOld[0] * self.websiteMatrix[0][i]\
                    + piOld[1] * self.websiteMatrix[1][i]\
                    + piOld[2] * self.websiteMatrix[2][i]\
                    + piOld[3] * self.websiteMatrix[3][i]\
                    + piOld[4] * self.websiteMatrix[4][i]\
                    + piOld[5] * self.websiteMatrix[5][i]\
                    + piOld[6] * self.websiteMatrix[6][i]\
                    + piOld[7] * self.websiteMatrix[7][i]

            i = 3
            pi[i] = piOld[0] * self.websiteMatrix[0][i]\
                    + piOld[1] * self.websiteMatrix[1][i]\
                    + piOld[2] * self.websiteMatrix[2][i]\
                    + piOld[3] * self.websiteMatrix[3][i]\
                    + piOld[4] * self.websiteMatrix[4][i]\
                    + piOld[5] * self.websiteMatrix[5][i]\
                    + piOld[6] * self.websiteMatrix[6][i]\
                    + piOld[7] * self.websiteMatrix[7][i]

            i = 4
            pi[i] = piOld[0] * self.websiteMatrix[0][i]\
                    + piOld[1] * self.websiteMatrix[1][i]\
                    + piOld[2] * self.websiteMatrix[2][i]\
                    + piOld[3] * self.websiteMatrix[3][i]\
                    + piOld[4] * self.websiteMatrix[4][i]\
                    + piOld[5] * self.websiteMatrix[5][i]\
                    + piOld[6] * self.websiteMatrix[6][i]\
                    + piOld[7] * self.websiteMatrix[7][i]

            i = 5
            pi[i] = piOld[0] * self.websiteMatrix[0][i]\
                    + piOld[1] * self.websiteMatrix[1][i]\
                    + piOld[2] * self.websiteMatrix[2][i]\
                    + piOld[3] * self.websiteMatrix[3][i]\
                    + piOld[4] * self.websiteMatrix[4][i]\
                    + piOld[5] * self.websiteMatrix[5][i]\
                    + piOld[6] * self.websiteMatrix[6][i]\
                    + piOld[7] * self.websiteMatrix[7][i]

            i = 6
            pi[i] = piOld[0] * self.websiteMatrix[0][i]\
                    + piOld[1] * self.websiteMatrix[1][i]\
                    + piOld[2] * self.websiteMatrix[2][i]\
                    + piOld[3] * self.websiteMatrix[3][i]\
                    + piOld[4] * self.websiteMatrix[4][i]\
                    + piOld[5] * self.websiteMatrix[5][i]\
                    + piOld[6] * self.websiteMatrix[6][i]\
                    + piOld[7] * self.websiteMatrix[7][i]

            i = 7
            pi[i] = piOld[0] * self.websiteMatrix[0][i]\
                    + piOld[1] * self.websiteMatrix[1][i]\
                    + piOld[2] * self.websiteMatrix[2][i]\
                    + piOld[3] * self.websiteMatrix[3][i]\
                    + piOld[4] * self.websiteMatrix[4][i]\
                    + piOld[5] * self.websiteMatrix[5][i]\
                    + piOld[6] * self.websiteMatrix[6][i]\
                    + piOld[7] * self.websiteMatrix[7][i]

            delta = abs(pi[0] - piOld[0])\
                    + abs(pi[1] - piOld[1])\
                    + abs(pi[2] - piOld[2])\
                    + abs(pi[3] - piOld[3])\
                    + abs(pi[4] - piOld[4])\
                    + abs(pi[5] - piOld[5])\
                    + abs(pi[6] - piOld[6])\
                    + abs(pi[7] - piOld[7])\
            """
            delta = 0
            for k in range(0, len(pi)):
                delta += abs(pi[k] - piOld[k])


        print(self.websiteMatrix)
        print(pi)