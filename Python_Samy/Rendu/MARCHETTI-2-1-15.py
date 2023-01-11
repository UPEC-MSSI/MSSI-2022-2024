# Samy Marchetti
import sys

nbLigne = int(sys.argv[1]) # nombre de ligne
nbEspace = nbLigne * 2 - 2 # nombre d'espace initial

i = 1 # nombre d'étoile de chaque côté sur une même ligne

# cette boucle va écrire une ligne tant que le nombre d'espace est supérieur à 0
while (nbEspace > 0):
	nbEspace = nbEspace - 2 
	print("*" * i, " " * nbEspace, "*" * i)
	i = i + 1

# on rajoute la ligne suivante car la ligne 11 vient avant l'écriture de la ligne, et il en manquera donc une
print("*" * (nbLigne * 2))