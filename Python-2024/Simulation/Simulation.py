import csv
personnages = []

# Liste des personnages
with open("C:\Users\goetgheluck\OneDrive - UPEC\M2\Python\Simulation\Simulation.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    next(csv_reader)  # Ignore la première ligne du fichier (en-tête)
    for row in csv_reader:
        nom = row[0]
        force = int(row[1])
        endurance = int(row[2])
        pv = int(row[3])
        personnages.append((nom, force, endurance, pv))


# Choix du personnage1
J1 = input("Entrez votre nom : ")
print("Choisissez un personnage :")
for i, (nom, force, endurance, pv) in enumerate(personnages):
    print(f"{i + 1} - {nom} (force : {force}, endurance : {endurance}, PV : {pv})")

choix1 = int(input("Votre choix : "))

# Initialisation des variables
perso1 = personnages[choix1 - 1][0]
force1 = personnages[choix1 - 1][1]
endurance1 = personnages[choix1 - 1][2]
pv1 = personnages[choix1 - 1][3]

# Choix du personnage
J2 = input("Entrez votre nom : ")
print("Choisissez un personnage :")
for i, (nom, force, endurance, pv) in enumerate(personnages):
    print(f"{i + 1} - {nom} (force : {force}, endurance : {endurance}, PV : {pv})")

choix = int(input("Votre choix : "))
# Initialisation des variables
perso2 = personnages[choix - 1][0]
force2 = personnages[choix - 1][1]
endurance2 = personnages[choix - 1][2]
pv2 = personnages[choix - 1][3]


# Jeu
while pv1 > 0:
    # Attaque joueur 1
    att1 = force1
    pv2 -= att1

    # Affiche l'attaque
    msg1 = perso1 + " attaque " + perso2 + " qui perd " + str(att1) + " PV"
    msg2 = perso2 + " a maintenant " + str(pv2) + " PV"
    print('\n')

    # Vérifie les PV
    if pv2 <= 0:
        break

    # Attaque joueur 2
    att2 = force2
    pv1 -= att2

    # Affiche l'attaque
    msg1 = perso2 + " attaque " + perso1 + " qui perd " + str(att2) + " PV"
    msg2 = perso1 + " a maintenant " + str(pv1) + " PV"
    print()

    # Vérifie les PV
    if pv1 <= 0:
        break

# Détermine le vainqueur
if pv1 > 0:
    winner = J1
else:
    winner = J2

# Affiche le résultat
print()
print("Le gagnant est " + winner)
