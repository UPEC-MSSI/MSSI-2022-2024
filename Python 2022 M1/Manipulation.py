#PS C:\Users\ygoetgheluck\OneDrive - UPEC\M1\Programmation python\Programmation\Exercices>

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