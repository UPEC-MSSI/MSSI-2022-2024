#Travail de Yann Goetgheluck MSSI 1
#Pour lancer le code veuillez enlevez les """ avant et après. 
"""
#Méthode de tricheur car on utilise pas l'un des caractère demandé. 
x = int(input("Veuillez choisir le nombre de ligne : "))
y = int(input("Veuillez choisir le nombre de caractère par ligne : "))
print(("+-+-+-+-\n")*x)
"""
"""
#On utilise toutes les données mais pas très honnêtement car on rend le 8 à 4. 
from operator import length_hint


x = int(input("Veuillez choisir le nombre de ligne : "))
y = int(input("Veuillez choisir le nombre de caractère par ligne : "))
i = 0
b = 0
y = y/2
for b in range(x):
    for y in range(x):
        print("+",end="-")
    print("")
"""     
"""
#Utilisation parfaite des données. Avec questions. 
x = int(input("Veuillez choisir le nombre de ligne : "))
y = int(input("Veuillez choisir le nombre de caractère par ligne : "))
compte = y
ligne = ""

#Fonction pour imprimé les symboles de manière alterné (+-).
def symbole():
	if (compte % 2 == 0):
		return "+"
	else: return "-"

#Imprimer x lignes et y colonnes de lignes de symboles alterné
for i in range(x):
    for w in range(compte):
        ligne = ligne+ symbole()
        compte = compte - 1
    print(ligne)
"""

#Utilisation parfaite des données.
import sys
x = int(sys.argv[1])
y = int(sys.argv[2])
ligne = ""
#Fonction pour imprimé les symboles de manière alterné (+-).
def symbole():
	if (y % 2 == 0):
		return "+"
	else: return "-"
#Imprimer x lignes et y colonnes de lignes de symboles alterné
for i in range(x):
    for w in range(y):
        ligne = ligne + symbole()
        y = y - 1
    print(ligne)