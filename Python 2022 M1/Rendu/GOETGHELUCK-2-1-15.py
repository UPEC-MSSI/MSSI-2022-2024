#Travail de Yann Goetgheluck MSSI 1
#Pour lancer le code veuillez enlevez les """ avant et après. 

#La méthode while qui premet de faire le "gateau" jusqu'a 10 maximum. Minimum de ligne.
import sys
x = int(sys.argv[1])
i = 0
#Tant que i est inférieur à l'âge indiqué imprimer les le chiffre sans revenir à la ligne.
while i < x : 
    print("",i+1, end="")
    i = i+1
#Imprimer les symbole x fois + 1
print("")
print("", end=" ")
print(("| ")*x)
print ('-'*(2*x+1))
print ('+'*(2*x+1))
print ('-'*(2*x+1))


"""
#La méthode while qui premet de faire le "gateau" jusqu'a 10 maximum. Minimum de ligne. Avec les questions. 

x = int(input("Veuillez indiquer l'âge (max 9) : "))
i = 0
#Tant que i est inférieur à l'âge indiqué imprimer les le chiffre sans revenir à la ligne.
while i < x : 
    print("",i+1, end="")
    i = i+1
#Imprimer les symbole x fois + 1
print("")
print("", end=" ")
print(("| ")*x)
print ('-'*(2*x+1))
print ('+'*(2*x+1))
print ('-'*(2*x+1))
"""


#La méthode en for qui premet de faire le "gateau" jusqu'a 10 maximum

"""
#Imprimer étapes par étapes les caratères nécessaire x fois.
x = int(input("Veuillez indiquer l'âge (max 9) : "))
for i in range (1, x+1):
    print(" "+ str(i), end= "")
print("")
for i in range (0, x):
    print (" " + "|", end ="")
print("")
for i in range (0, x+x+1):
        print("-", end ="")
print("")
for i in range (0, x+x+1):
        print("+", end ="")
print("")
for i in range (0, x+x+1):
        print("-", end ="")
"""