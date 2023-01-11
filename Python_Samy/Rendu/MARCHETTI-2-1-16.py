# Samy Marchetti
import sys

ligne = int(sys.argv[1])
colonne = int(sys.argv[2])
compteurCol = colonne # cette variable sert à compter le numéro de la colonne (indépendamment du nombre initial de colonne)

# cette fonction retourne le caractère correspondant à la colonne, avec un test de parité
def whatSymbol():
	if (compteurCol % 2 == 0):
		return "+"
	else: return "-"

# cette boucle écrit une ligne de la figure, en ajoutant à chaque fois le caractère correspondant avec whatSymbol()
ligneEcrite = ""
for x in range(colonne):
	ligneEcrite = ligneEcrite + whatSymbol()
	compteurCol = compteurCol - 1

# cette boucle répète l'impression de la ligne autant qu'il y a de ligne
while ligne > 0:
	print(ligneEcrite)
	ligne = ligne - 1