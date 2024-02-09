import random


# Liste des personnages
personnages = [
    ("Astérix", 50, 75, 100),
    ("Obélix", 100, 50, 150),
    ("Panoramix", 20, 100, 100),
    ("Abraracourcix", 60, 60, 120),
    ("Idéfix", 5, 5, 5),
    ("Assurancetourix", 1, 1, 1),
    ("Falbala", 40, 50, 80),
    ("Bonemine", 30, 60, 90),
]

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

# Liste des attaques
attaques1 = {
    "1" : (force1 *0.5, 1.0),
    "2" : (force1 *0.8, 1.2),
    "3" : (force1 *0.2, 0.8),
}
attaques2 = {
    "1" : (force1 *0.5, 1.0),
    "2" : (force1 *0.8, 1.2),
    "3" : (force1 *0.2, 0.8),
}

# Jeu
tour = 1
while pv1 > 0 and pv2 > 0:

    # Attaque joueur 1
    print("C'est le tour du joueur 1 (", J1, ")")

    # Choix de l'attaque
    print("Choisissez votre attaque :")
    for nom, (force, precision) in attaques1.items():
        print(f"{nom} (force : {force}, précision : {precision})")

    choix_attaque1 = input("Votre choix : ")

    # Calcul de l'attaque
    force1_attaque = attaques1[choix_attaque1][0]
    precision_attaque1 = attaques1[choix_attaque1][1]
    att1 = force1_attaque * random.uniform(precision_attaque1 - 0.2, precision_attaque1 + 0.2)
    pv2 -= att1

    # Affiche l'attaque
    msg1 = perso1 + " attaque " + perso2 + " avec " + choix_attaque1 + " (inflige " + str(att1) + " PV)"
    msg2 = perso2 + " a maintenant " + str(pv2) + " PV"
    print()

    # Vérifie les PV
    if pv2 > 0 : 
        # Attaque joueur 2
        print("C'est le tour du joueur 2 (", J2, ")")

        # Choix de l'attaque
        print("Choisissez votre attaque :")
        for nom, (force, precision) in attaques2.items():
            print(f"{nom} (force : {force}, précision : {precision})")

        choix_attaque2 = input("Votre choix : ")

        # Calcul de l'attaque
        force2_attaque = attaques2[choix_attaque2][0]
        precision_attaque2 = attaques2[choix_attaque2][1]
        att2 = force2_attaque * random.uniform(precision_attaque2 - 0.2, precision_attaque2 + 0.2)
        pv1 -= att2

        # Affiche l'attaque
        msg1 = perso2 + " attaque " + perso1 + " avec " + choix_attaque2 + " (inflige " + str(att2) + " PV)"
        msg2 = perso1 + " a maintenant " + str(pv1) + " PV"
        print()

        # Vérifie les PV
        if pv2 <= 0:
            break

        # Affiche le tour
        print("Fin du tour ", tour)
        tour += 1

# Détermine le vainqueur
if pv1 > 0:
    winner = perso1
else:
    winner = perso2

# Affiche le résultat
print()
print("Le gagnant est " + winner)
