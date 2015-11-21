__author__ = 'julian'


class pageRank:
    def __init__(self, websiteMatrix=[]):
        self.websiteMatrix = websiteMatrix

    def calcRank(self):
        i = 0
        for row in self.websiteMatrix:
            # 1en zaehlen
            ones = 0
            for cell in row:
                if cell == 1:
                    ones += 1

            # Uebergangswahrscheinlichkeiten berechnen
            j = 0
            for cell in row:
                if ones != 0:
                    if cell == 1:
                        self.websiteMatrix[i][j] = 1 / ones
                else:
                    self.websiteMatrix[i][j] = 1 / len(self.websiteMatrix)
                j = j + 1

            # Teleportation und Daempfung berechnen
            t = 0.05  # Teleportationsrate
            d = 1 - t  # Daempfungsfaktor

            j = 0
            for cell in row:
                self.websiteMatrix[i][j] = cell * d + t / len(self.websiteMatrix)
                j = j + 1
            i = i + 1

        # Wahrscheinlichkeitsvektor pi initialisieren
        pi = []
        for i in self.websiteMatrix:
            pi.append(1 / len(self.websiteMatrix))

        output_file = open('pageRank.dat', 'w+')

        # PageRank berechnen
        delta = 1
        l = 0
        while delta > 0.04:
            output_file.write("PageRank Step {0}:\n".format(l))
            for elem in pi:
                output_file.write("{0:.4f} ".format(elem))
            if(l != 0):
                output_file.write("\nDelta: {0:.4f}".format(delta))
            output_file.write("\n\n")

            piOld = pi.copy()
            for i in range(0, len(pi)):
                pi[i] = 0  # pi muss zurueckgesetzt werden!
                for j in range(0, len(pi)):
                    pi[i] += piOld[j] * self.websiteMatrix[j][i]

            delta = 0  # delta muss zurueckgesetzt werden!
            for k in range(0, len(pi)):
                delta += abs(pi[k] - piOld[k])
            l += 1
        iter = 1
        self.ranking = {}
        output_file.write("PageRank Step {0}:\n".format(l))
        for elem in pi:
            output_file.write("{0:.4f}\t".format(elem))
            self.ranking["d0"+str(iter)+".html"] = elem
            iter += 1
        if(l != 0):
            output_file.write("\nDelta: {0:.4f}\n".format(delta))