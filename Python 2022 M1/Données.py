#PS C:\Users\ygoetgheluck\OneDrive - UPEC\M1\Programmation python\Programmation\Exercices>
'''
#Exercice 1 
choix = True
while choix == True :
    y = int(input("Entrez le premier chiffre : "))
    g = int(input("Entrez le second chiffre : "))
    o = y + g
    print ("La somme de",y,"et de",g,"est", o) 
    choix = input("Recommencer ?" " O : " )

    if choix == "O"  : 
        choix = True
    else :
        choix = False
        print("Fin")
'''

#Exercice 2
""""
i = int(input("Entrez un nombre: "))

if (i % 2) == 0:
   print("{0} est Paire".format(i))
else:
   print("{0} est Impaire".format(i))
"""
"""
a = int(input("Entrez un nombre: "))
b = int(input("Entrez un nombre: "))
if a > b :
    print("Le nombre",a,"est le plus grand.")
else :
    if a<b : 
        print("Le nombre",b,"est le plus grand.")
    else :
        print("Les deux nombre sont égaux.")
"""
"""
a = int(input("Entrez un nombre: "))
b = int(input("Entrez un nombre: "))
c = int(input("Entrez un nombre: "))
if a > b > c:
    print(a,b,c)
else :
    if a < b < c : 
        print(c,b,a)
    else :
        if b < c < a :
            print(a,c,b)
        else : 
            if  a < c < b : 
                print(b,c,a)
            else : 
                if  c < a < b : 
                    print(b,a,c)
"""
"""
a = int(input("Entrez un nombre: "))
b = int(input("Entrez un nombre: "))
c = int(input("Entrez un nombre: "))
if a < b < c:
    print(a,b,c)
else :
    if a > b > c : 
        print(c,b,a)
    else :
        if b > c > a :
            print(a,c,b)
        else : 
            if  a > c > b : 
                print(b,c,a)
            else : 
                if  c > a > b : 
                    print(b,a,c)
"""
"""
a = int(input("Entrez un nombre: "))
b = int(input("Entrez un nombre: "))
c = int(input("Entrez un nombre: "))
d = int(input("Entrez un nombre: "))
moy = (a+b+c+d)/4
print(int(moy),float(moy))
"""
"""
#Exercice 3
choix = True
while choix == True :
    y = int(input("Entrez le premier chiffre : "))
    g = int(input("Entrez le second chiffre : "))
    a = (input("Entrez l'opérateur (+,*,/,-): "))
    if a == "+":
        print ("La somme de",y,"et de",g,"est", int(y+g) ) 
    else : 
        if a == "-":
            print ("La différence de",y,"et de",g,"est", int(y-g) )
        else : 
            if a == "*":
                print ("Le produit de",y,"et de",g,"est", int(y*g) )
            else : 
                if a == "/" and g == 0 :
                    print ("Le quotient de",y,"et de",g,"n'est pas calculable")
                else : 
                    print ("Le quotient de",y,"et de",g,"est", int(y/g) )
    
                    
                
    choix = input("Recommencer ?" " O : " )

    if choix == "O"  : 
        choix = True
    else :
        choix = False
        print("Fin")
"""
"""
#Exercice 4.1
import sys
num = 10
number_list = [i+1 for i in range(num)]

while number_list:
    print(number_list.pop(0))
"""

"""
#Exercice 4.2
import sys
num = 10
x = num
num = num - 1 
number_list = [i+1 for i in range(num)]

while number_list:        
    print(number_list.pop(0),end=",")
print (x)
"""
"""
#2
from turtle import end_fill
num = int(input("Entrez un nombre : "))
i = 1

for i in range(num) :
    if i<(num-1) : 
        print((i+1),end=",")
        i = i + 1
    else : 
        print(i+1)
"""
"""
#Exercice 4.3
import sys
num = int(sys.argv[1])
x = num
num = num - 1 
number_list = [i+1 for i in range(num)]

while number_list:        
    print(number_list.pop(0),end=",")
print (x)
"""

"""
#4
num = int(input("Entrez un nombre : "))
i = 0
for i in range(num) :
    if num-(num-1)<(num) : 
        print((num),end=",")
        num = num - 1
    else : 
        print(num)
"""
"""
#5
num = int(input("Entrez un nombre : "))
i = 1
for i in range(num):
    print((i+1),"//",num)
    i = i + 1
    num = num - 1
"""
"""
#6
import sys
num = 10
i = 1 
for i in range(1,num+1):
    if (i % 2) == 0 : 
        print(i)
    else : 
        pass
    i = i + 1
"""

"""
import sys
num = 10
i = 1 
for i in range(1,num):
    if (i % 2) == 0 : 
        print(i,end=",")
    else : 
        pass
    i = i + 1
if (num % 2) == 0 : 
    print(num)
else : 
    pass
"""


"""
#3
import sys
num = int(sys.argv[1])
x = num
num = num - 1 
number_list = [i+1 for i in range(num)]

while number_list:
    if (num % 2) == 0 :        
        print(number_list.pop(0),end=",")
    else : 
        pass
if (x % 2) == 0 :
    print(x)
else : 
    pass
"""

"""
#4
import sys
num = int(sys.argv[1])
x = num - ( num  - 1)
y = 1
for i in range(1,num-1) : 
    if (num % 2) == 0 : 
        print((num - (y)),end=",")
        y = y + 1
    else : 
        pass
if (num % 2) == 0 : 
    print(x)
else : 
    pass
"""
"""
#7
import sys
num = int(sys.argv[1])

"""

#Exercce 5
"""
#1 
import sys
x = int(sys.argv[1])
y = 0
r = 0
for i in range(11):
    r = x * y
    print (x,"x",y,"=",r)
    y = y + 1
"""

#2
import sys
x = int(sys.argv[1])
a = str(sys.argv[2])
y = 0
r = 0
if a == str('+') :
    for i in range(11):
        r = x + y
        print (x,"+",y,"=",r)
        y = y + 1


"""
#3
import sys
x = int(sys.argv[1])
y = 0
r = 0
for i in range(10):
    r = x - y
    print (x,"-",y,"=",r)
    y = y + 1
"""

"""
#Exercice 6
#1
import sys
"""