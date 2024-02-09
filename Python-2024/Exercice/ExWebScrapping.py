import requests
from pyquery import PyQuery as pq
import pandas as pd
import re


coworking = []

# On récupère la réponse de la requête GET sur l'URL de la page
response = requests.get("https://www.leportagesalarial.com/coworking/")

# On vérifie le code de statut de la réponse (200 signifie succès)
rep = response.status_code
print(rep)

# On extrait le contenu HTML de la réponse
html = response.text

# On crée un objet PyQuery à partir du HTML
d = pq(html)

# On sélectionne les éléments qui contiennent les informations sur les espaces de coworking
fiches = d(".inner-post-entry")

# On parcourt les éléments sélectionnés
for fiche in fiches.items():
  # On crée un dictionnaire vide pour stocker les informations d'un espace de coworking
  data = {}
  # On extrait le texte de l'élément
  texte = fiche.text()
  # On utilise une expression régulière pour séparer le texte par le caractère ":"
  infos = re.split(":", texte)
  # On vérifie qu'il y a au moins deux parties dans le texte
  coworking.append(data)
# On crée un dataframe pandas à partir de la liste des espaces de coworking
df = pd.DataFrame(coworking)

# On affiche le dataframe
print(df)