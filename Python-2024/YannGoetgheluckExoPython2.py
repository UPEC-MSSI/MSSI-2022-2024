import pandas as pd
import requests
import dns.resolver
import os

#Print tout le fichier
df = pd.read_csv('D:\ygoetgheluck\Python\liste.csv')


#Extraire que les noms des lieux de coworking
df['Noms'] = df['Nom'].str.split(':').str[0]
#Extraire les CP
df['CP'] = df['Nom'].str.extract(r'(\d{5})')
#Extraire les lignes de métro
df['Lignes de Métro'] = df['Accès'].str.extractall(r'(\d+)').groupby(level=0).agg('-'.join)

#Extraire les numéro de téléphone 
df["Téléphone"].fillna("0")
def portable(value):
    if type(value)== float : 
        value = str(value)
    if type(value)==str :  
        if value.startswith(('06', '07')):
            return "Portable"
        else:
            return ""
        
def fixe(value):
    if type(value)== float : 
        value = str(value)
    if type(value)==str :  
        if value.startswith(('01')):
            return "Fixe"
        else:
            return ""


        
df['Portable'] = df['Téléphone'].apply(portable)
df['Fixe'] = df['Téléphone'].apply(fixe)

nom = df['Noms']
cp = df['CP']
lignes = df['Lignes de Métro']
tel = df['Téléphone']
port = df['Portable']
fix = df['Fixe']


# Vérifier le code 200 du site avec un timeout de 10 secondes
def check_code_200(url):
    try:
        # On envoie une requête GET à l'URL avec le paramètre timeout
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Cette ligne déclenchera une exception pour les codes d'erreur HTTP
        return 200
    except requests.exceptions.RequestException as e:
        # En cas d'erreur ou de dépassement du timeout, renvoyer "Error"
        return "Error"

# Fonction pour récupérer les enregistrements MX
# Fonction pour récupérer les enregistrements MX avec gestion d'erreur
def get_mx_records(site):
    try:
        mx_records = dns.resolver.resolve(site, 'MX')
        return ', '.join([record.exchange.to_text() for record in mx_records])
    except dns.resolver.NoAnswer:
        return ""
    except dns.resolver.NXDOMAIN:
        return ""
    except dns.resolver.LifetimeTimeout:
        return "Timeout"
    except dns.resolver.DNSException:
        return "DNS Exception"



df['Code 200'] = df['Site'].apply(check_code_200)
resp = df['Code 200']

# Appliquer la fonction get_mx_records pour créer la colonne MX
df['MX'] = df['Site'].apply(get_mx_records)
mx = df['MX']

#Concatener les frames
df_concat = pd.concat([nom, cp, lignes, tel, port, fix, resp, mx], axis=1)

#Enlever les NaN
df = df.dropna()


print(df_concat)
df.to_excel("Propre.xlsx", index=False)

"""
Petit élément en plus pour faciliter la récupération de l'excel
"""
# Obtenez le chemin absolu du répertoire de travail actuel
cwd = os.getcwd()
# Ajoutez le nom du fichier Excel pour obtenir le chemin complet
excel_file_path = os.path.join(cwd, "Propre.xlsx")
print("Emplacement du fichier Excel:", excel_file_path)
