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

        delta = 0
        while delta > 0.04:
            pi = pi * self.websiteMatrix



        print(pi)
        print(self.websiteMatrix)

