# Samy Marchetti

import sys

nbBoucle = int(sys.argv[1])
nbHaut = int(sys.argv[1])
nbBas = 1

for x in range(nbBoucle):
	print(nbBas, "//", nbHaut)
	nbBas = nbBas + 1
	nbHaut = nbHaut - 1