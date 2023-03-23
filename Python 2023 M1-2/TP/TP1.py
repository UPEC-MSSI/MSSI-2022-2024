#C:\Users\ygoetgheluck\OneDrive - UPEC\M1\Programmation python\Python-2023-M2

#Exercice 1
def trouver_plus_grand(liste):
    plus_grand = liste[0]  # On suppose que le premier élément est le plus grand
    for element in liste:
        if element > plus_grand:
            plus_grand = element
    return plus_grand
"""
liste = [5, 2 , 5 , 6,10,5]
print(trouver_plus_grand(liste))
"""
#Exercice 2 
def perfect_number(n):
    somme_div = 0
    for i in range(1, n):
        if n%i == 0 :
            somme_div += i
    if somme_div == n :
        return True
    else : return False

""""
n = 496
print(perfect_number(n))
"""

 #Exercice 3
def all_perfect_number(n):
    result=[]
    for i in range(1, n):
        if perfect_number(i) == True :
            result.append(i)
    return result


"""  
n = 9999
print(all_perfect_number(n))       
"""

#Exercice 4
def factorielle(n):
    r = 1
    for i in range(1,n+1):
        r = r * i  
    return r

"""
n = 8
print(factorielle(n))
"""

#Exercice 5 : 
def lisse(list):
    for i in range (1, len(list)):
        if list[i]-list[i-1] == 1:
            continue
        else :
            return False
    return True

"""
list = [0,1,2,3,4,5,6,7,8]
print(lisse(list))
"""

#Exercice 6
def fizzbuzz():
    for i in range (1,200):
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        elif i%3 == 0 : 
            print("Fizz")
        elif i%5 == 0 :
            print("Buzz")
        else : print(i)
        i += i
    return ''
"""
print(fizzbuzz())
"""

#Exercice 7
def factorielle_rec(n):
    if n == 0:
        return 1
    else:
        return n * factorielle_rec(n - 1)
"""
print(factorielle_rec(8))
"""

#Exercice 8 
def fib(n):
    if n == 0 :
        return 0
    elif n <= 1 :
        return 1
    else : 
        return  fib(n-1) + fib(n-2)

"""        
print(fib(10))
"""

#Exercice 9 
def pi(n):
    pi = 0
    sign = 1
    div = 1
    for i in range(n):
        terme = 4 / div
        pi += sign * terme
        div += 2
        sign *= -1
    return pi

"""
print(pi(10000))
"""

#Exercice 10
def plateau(list):
    len_max = 0
    longueur = 1
    for i in range(1, len(list)):
        if list[i] == list[i-1]:
            longueur += 1
        else:
            len_max = max(len_max, longueur)
            longueur = 1
    len_max = max(len_max, longueur)
    return len_max
"""
List = [1, 1, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1, 1, 1]
print(plateau(List))
"""