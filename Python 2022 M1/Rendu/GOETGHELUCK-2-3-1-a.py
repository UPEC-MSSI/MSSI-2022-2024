#Travail de Yann Goetgheluck MSSI 1
#Pour lancer le code veuillez enlevez les """ avant et après. 


#Exercice 1
#A

#Affiche les valeurs de la tab entre les positions 0 et 9 avec un # pour les séparés
tab = [3, 6, 8, 5, 10, 3, 7, 6, 3, 2]
for x in tab[0:9] :
    print(x,end="#")
    x = x + 1
#Affiche simplement la valeur en position 10.
for x in tab[9:10]:
    print(x)


"""
#Méthode efficace mais nécessite une syntaxte particulière qui n'est pas un tableau
#Et ne répond pas parfaitement au sujet, mais l'utilisation de sep pour séparateur est interressante. 

tab = ["3","6","8","5","10","3","7","6","3","2"]
for x in tabl : 
    print(x,sep='#')
"""