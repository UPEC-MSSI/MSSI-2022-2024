#Travail de Yann Goetgheluck MSSI 1
#Pour lancer le code veuillez enlevez les """ avant et après. 


#Méthode la plus efficace, avec question. 
#L'utilisateur entre les données qu'il veut lister de manière croissante. 
import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
#Crée une liste des nombre pour faciliter la présentation croissante. 
list = [a,b,c]
list = sorted(list)
print(*list,sep=' ')


#Première méthode trouvée
"""
#Demande 3 chiffre à l'utilisateur et les places en fonction de leur valeur à chaque fois grâce aux différents if qui propose toutes les possibilités. 
#Gros inconvénient de cette méthode : Impossible pour une grande quantité de nombre. 
import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
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