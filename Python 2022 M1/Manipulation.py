#PS C:\Users\ygoetgheluck\OneDrive - UPEC\M1\Programmation python\Programmation\Exercices>

"""
import sys
list = [0] * (len(sys.argv) -1)
for i in range(0,len(list)):
    list[i] = int(sys.argv[i+1])
print(list)
"""

#Exercice 1
"""
#A
list = ['3','6','8','5','10','3','7','6','3','2']
print(*list,sep="#")
"""
"""
#A2
list = [ 3, 6, 8, 5, 10, 3, 7, 6, 3, 2 ]
for i in range (0, len(list)-1):
    print(list[i], end="")
    print(" # ", end="")
print(list[len(list)-1])
"""
"""
#Affiche les valeurs de la tab entre les positions 0 et 9 avec un # pour les séparés
tab = [3, 6, 8, 5, 10, 3, 7, 6, 3, 2]
for x in tab[0:9] :
    print(x,end="#")
    x = x + 1
#Affiche simplement la valeur en position 10.
for x in tab[9:10]:
    print(x)
"""

"""
#B
tabl = [3,6,8,5,10,3,7,6,3,2]
tabl.reverse()
for x in tabl : 
    print(x, end=" ")
"""
"""
#C
tabl = [3, 6, 8, 5, 10, 3, 7, 6, 3, 2]
i = 0
for x in tabl:
    print(tabl[i])
    i = i + 1
"""
"""
#D
tabl = [3,6,8,5,10,3,7,6,3,2]
tabl.reverse()
print(tabl)
"""
"""
#E
list =  [3, 6, 8, 5, 10, 3, 7, 6, 3, 2]
list1 = list[-1:] + list[:-1]
list1 [0] = 0
somme = [x + y for x, y in zip(list, list1)]
print(somme)
"""

"""
#F
list =  [3, 6, 8, 5, 10, 3, 7, 6, 3, 2]
list = list[-1:] + list[:-1]
list [0] = 0
print(list)
"""
"""
#G
list =  [3, 6, 8, 5, 10, 3, 7, 6, 3, 2]
list = list[+1:] + list[:+1]
list [9] = 0
print(list)
"""
"""
#H
list =  [3, 6, 8, 5, 10, 3, 7, 6, 3, 2]
list = list[-1:] + list[:-1]
print(list)
"""


#i
list =  [3, 6, 8, 5, 10, 3, 7, 6, 3, 2]
list = list[+1:] + list[:+1]
print(list)

"""
#J
list =  [3, 6, 8, 5, 10, 3, 7, 6, 3, 2]
i = int(input ("Entrez une valeur : "))
list = list[+i:] + list[:+i]
print(list)
"""
"""
#K
list =  [3, 6, 8, 5, 10, 3, 7, 6, 3, 2]
i = int(input ("Entrez une valeur : "))
list = list[-i:] + list[:-i]
print(list)
"""
"""
#Exercice 2 
#a
list =  [3, 6, 8, 5, 10, 3, 7, 6, 3, 2]
print (sum(list))
"""
"""
#b
def prod(prod,list):
    for x in list : 
        prod*= x
    return prod
list =  [3, 6, 8, 5, 10, 3, 7, 6, 3, 2]
prod = prod(1,list)
print (prod)
"""

"""
#c
list = [3, 6, 8, 5, 10, 3, 7, 6, 3, 2]
moy = sum(list)/len(list)
print (moy)
"""
"""
#d
list = [3, 6, 8, 5, 10, 3, 7, 6, 3, 2]
max = max(list)
print(max)
"""

"""
#e
list = [3, 6, 8, 5, 10, 3, 7, 6, 3, 2]
min = min(list)
print(min)
"""
"""
#f
list = [3, 6, 8, 5, 10, 3, 7, 6, 3, 2]
a = int(input("Entrez la valeur recherché : "))
print(list.count(a))
"""
"""
#g
list = [3, 6, 8, 5, 10, 3, 7, 6, 3, 2]
max = max(list)
print(list.index(max))
"""

#Exercice 3

#1
#a
