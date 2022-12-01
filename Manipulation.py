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
#B
tabl = [3,6,8,5,10,3,7,6,3,2]
tabl.reverse()
for x in tabl : 
    print(x, end=" ")
"""
"""
#C
tabl = [3,6,8,5,10,3,7,6,3,2]
for x in tabl : 
    print(x)
"""
"""
#D
tabl = [3,6,8,5,10,3,7,6,3,2]
tabl.reverse()
print(tabl)
"""