#c:\Users\ygoetgheluck\OneDrive - UPEC\M1\Programmation python\Programmation\Exercices\Exercice 1.py' 
#Exercice 1
#1
""""
i = 0
for i in range (4):
    print("*"*4)
"""
"""
#2
i = 0
for i in range (3):
    print("*"*3)
"""
"""
#3
i = 0
t = int(input("Indiquez la taille du carré : "))
for i in range (t):
    print("*"*t)
"""

#Exercice 2 
#1 / 1 
"""
x = int(input("Veuillez indiquer l'âge (max 9 : "))
i = 0
for i in range(x):
    print (" ",x,'\n',"", "|"* x, '\n',"---"*x,'\n',"+++"*x )
"""

"""
#1 / 3 While
from asyncore import loop
x = int(input("Veuillez indiquer l'âge (max 9 : "))
i = 0

while i < x : 
    print("",i+1, end="")
    i = i+1
loop
print("")
print("", end=" ")
print(("| ")*x)
print ('-'*(2*x+1))
print ('+'*(2*x+1))
print ('-'*(2*x+1))
"""

"""
Exercice 3 : For
import sys 
x = int(sys.argv[1])
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
"""
#Exercice 4 /1 
x = 5
i=1
for i in range(x):
    print('*'*i)
"""

"""
#Exercice 4 /1 
from asyncore import loop
x = 4 
i = 0
while i < x:
    print("*"*x)
    x = x - 1 
loop
"""
"""
#Exercice 5
x = 4 
y = x
i = 1
for i in range(x) :
    print("_"*(x-1),"*"*(i))
    x = x - 1
    i = i - 1
print ("*"*y)
"""
""""
#Exercice 6
x = 4 
y = x
i = 1
for i in range(x) :
    print(" "*(x-1),"*"*(i))
    x = x - 1
    i = i - 1
print ("*"*y)
"""
"""
#Exercice 7
x = 4
i = 0
for i in range(x):
    print(" "*i,"*"*x)
    x = x - 1
    i = i+1
"""
"""
#Exercice 8 : for
x = 1
i = 3
y = 5
for x in range(y):
    print("*"*x," "*i)
    x = x + 1 
    i = i - 1

x = 3
i = 1
y = 4
for i in range(y) : 
    print (" "*i,"*"*x)
    x = x - 1
    i = i + 1
"""
#Exercice 8 : while 
    
"""
#Exercice 9
x = 1
i = 3
y = 5
for x in range(y):
    print("!"*x," "*i)
    x = x + 1 
    i = i - 1

x = 3
i = 1
y = 4
for i in range(y) : 
    print (" "*i,"!"*x)
    x = x - 1
    i = i + 1
"""

#Exercice 9 : while 

"""
#Excercic 10
x = 1
i = 3
w = 0
y = 5
for w in range(y):
    print(" "*w,"*"*x," "*i)
    i = i - 1
    w = w + 1

x = 1
i = 4
w = 0
y = 5
for w in range(y):
    print(" "*i,"*"*x," "*w)
    i = i - 1
    w = w + 1
"""

"""
#Exercice 11
x = 6 
i = 2
print ("*"*x)
(print("*"," "*i,"*"))
(print("*"," "*i,"*"))
(print("*"," "*i,"*"))
(print("*"," "*i,"*"))
print ("*"*x)
"""
"""
#Exercice 12
x = 6
i = 0
for i in range (x):
    print(" "*i,"*"*x)
    i = i + 1
"""
"""
#Exercice 13 : while
from asyncore import loop
x = 5
i = 0
while i <= x:
    print("=*=*=")
    i = i + 1
    if i < x : print("*=*=*")
    i = i + 1
loop
"""
"""
#Exercice 14 : while
from asyncore import loop
x = 5
i = 0
while i <= x:
    print("X-X-X")
    i = i + 1
    if i < x : print("-X-X-")
    i = i + 1
loop
"""
"""
#Exercice 15
x = 4
i = 1
y = 0
for y in range (x-1):
    print("*"*i," "*x,"*"*i)
    i = i + 1
    x = x - 2
    y = y + 1
print ("*"*i*2)
"""
"""
#15 : 1
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
"""
#15 : 2
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
#15 : 3
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
"""
#Exercice 16
x = int(input("Veuillez choisir le nombre de ligne : "))
y = int(input("Veuillez choisir le nombre de caractère par ligne : "))
print(("+-+-+-+-\n")*x)
"""
"""
#Exercice 16 Best
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
"""

"""
#Exercice 17
import sys
x = int(sys.argv[1])
 
"""