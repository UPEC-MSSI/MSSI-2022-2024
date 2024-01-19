"""
Le but de ce code est de répondre à l'exercice demandé par Monjour en cours de Python en M2:
https://colab.research.google.com/drive/1-BF-K6fmbB8uqIADs9gsf3odLBCZfPGG?usp=sharing#scrollTo=GKxoEJgp3JV5
Discord: @armetz
à rendre pour 28/01
"""
from pyquery import PyQuery as pq
import pandas
import requests

#Requête HTML sur le site 
response = requests.get("https://www.leportagesalarial.com/coworking/")

#Le check à supprimer? je n'en vois pas l'utilité
if response.status_code == 200:
	htmltxt = response.text

htmlsrc = pq(htmltxt)
coworkings = htmlsrc('ul').eq(5) #Pour sélectionner la liste des coworkings parisiens.

listecoworkings = []

for li in coworkings.find('li'):
    li_query = pq(li)

    #Texte / Nom
    li_text = li_query.text()
    #Il faut garder ce qui vient avant les ':', càd le nom de l'espace de coworking
    phrase = li_text.split(':')
    li_text = phrase[0].strip()

    #Lien / href
    li_link = li_query.find('a')
    href = li_link.attr('href')

    lignecoworking = {'Nom': li_text, 'Lien': href}
    listecoworkings.append(lignecoworking)

# Pense-bête pour récupérer les attributs spécifique
"""
print(listecoworkings[2]['Nom'])
print(listecoworkings[5]['Lien'])
"""


#On exporte le dictionaire listecoworkings dans un excel
df = pandas.DataFrame(listecoworkings, columns=['Nom', 'Lien'])
df.to_excel('listecoworkings.xlsx', index=False)

# Boucle pour itérer sur tout les liens dans listecoworking et non l'excel (plus simple)
for x in range(len(listecoworkings)):
	officeLink = listecoworkings[x]['Lien']

	#Partie où l'on va récuperer les infos
	response2 = requests.get(officeLink)

	htmltxt2 = response2.text
	htmlsrc2 = pq(htmltxt2)

	#Récuperer le titre
	pageTitle = htmlsrc2('title').text()
	#Récuperer le lien de l'image principale (Image principale en h2, sur tag src)
	imgLink = htmlsrc2('h2.src').text()
	#Récuperer la description (du 1er au 4ème tag p)
