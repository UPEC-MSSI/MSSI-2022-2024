import requests
import pandas as pd
from pyquery import PyQuery as pq
import re
# Import pour connaitre le path du fichier :
import os

# Fonction pour extraire des informations spécifiques d'une page :
def extract_info(page, key, offset):
    if key in page:
        info = page[page.index(key) + offset:]
        return info.strip()
    return ""

url = "https://www.leportagesalarial.com/coworking/"

# Récupérer le contenu HTML de la page :
response = requests.get(url)
contenu_html = response.text

# Utiliser PyQuery pour parser le contenu HTML :
doc = pq(contenu_html)

# Sélectionner les liens contenant "Paris" :
links = doc('a:contains("Paris")')

# Sélectionner tous les éléments 'img' :
images = doc('img')
# Compter le nombre d'images :
image_count = len(images)
print(f"Nombre d'images sur la page : {image_count}")

# Récupérer le meta title :
meta_title = doc('meta[name="title"]').attr('content')

# Vérifier si la longueur du meta title est inférieure à 150 caractères :
title_length_ok = len(meta_title) < 150 if meta_title else False

# Récupérer la meta description :
meta_description = doc('meta[name="description"]').attr('content')

data = []

# Boucler sur les liens sélectionnés et extraire les informations nécessaires :
for link in links:
    # Extraire l'URL du lien :
    link_url = link.attrib['href']
    # Extraire le texte du lien :
    link_name = link.text

    # Faire une requête HTTP GET pour obtenir le contenu de la page pointée par le lien :
    rep_image = requests.get(link_url)
    # Lire le contenu de la réponse et le stocker dans 'page_image' :
    page_image = rep_image.text
    # Utiliser PyQuery pour parcourir le contenu HTML de la page :
    page = pq(page_image)

    # Récupérer l'URL de l'image principale à partir de données récurrentes que l'on sait à propos de l'URL :
    match = re.search("\((.*)\)", link_name)
    images_extension = match.group(1) + ".jpg" if match else ""
    # Utiliser l'expression 'findall' pour trouver l'URL de l'image principale dans la page :
    url_image_principale = re.findall(f'img .*?src="(.*{images_extension})"', page_image)
    alt_image_principale = ""

    # Extraire d'autres informations de la page en utilisant la fonction 'extract_info' :
    adresse = extract_info(page, "Adresse : ", 10)
    tel = extract_info(page, "Téléphone", 12)
    acces = extract_info(page, "Accès", 8)
    site = extract_info(page, "Site", 7)
    twit = extract_info(page, "Twitter", 10)
    faceb = extract_info(page, "Facebook", 11)
    linkd = extract_info(page, "LinkedIn", 11)

    # Ajouter les informations récupérées à la liste 'data' :
    data.append([link_name, link_url, url_image_principale, alt_image_principale, adresse, tel, acces, site, faceb, twit, linkd])

# Créer un DataFrame à partir des données récupérées :
df = pd.DataFrame(data, columns=["Nom du lien", "URL", "Lien de l'image principale", "Description de cette image","Adresse", "Téléphone", "Accès", "Site", "Twitter", "Facebook", "LinkedIn"])

# Écrire les données dans un fichier xlsx :
df.to_excel("liens.xlsx", index=False)


########################################################################################################################################################################################################

"""
Petit élément en plus pour faciliter la récupération de l'excel
"""
# Obtenez le chemin absolu du répertoire de travail actuel
cwd = os.getcwd()
# Ajoutez le nom du fichier Excel pour obtenir le chemin complet
excel_file_path = os.path.join(cwd, "liens.xlsx")
print("Emplacement du fichier Excel:", excel_file_path)
