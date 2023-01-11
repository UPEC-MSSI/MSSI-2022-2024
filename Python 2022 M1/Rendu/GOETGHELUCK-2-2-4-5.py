#Travail de Yann Goetgheluck MSSI 1

#Affiche simplement le numéro entré par l'utilisateur et 1 séparé de //. Sachant que
#ces deux valeurs font le chemin inverse pour afficher 2 suites séparés de //, une 
#une croissante et une décroissante. 
import sys
num = int(sys.argv[1])
i = 1
for i in range(num):
    print((i+1),"//",num)
    i = i + 1
    num = num - 1
