import requests
from time import sleep
import pandas as pd

def calcul_intervalle(intervalle):
  if intervalle.isdigit():
    temps_attente = int(intervalle)
    print(f"[+] PAUSE DE {temps_attente} secondes")
    sleep(temps_attente)


list = []
request_counter = 0
while True:
  print(request_counter)
  if request_counter % 5 == 0 or request_counter == 0:
    continuer = input("5 Nouvelles requêtes ? (y/n) : ")
    if continuer == "n" :
      break
  else:
    pass

  intervalle = "1"
  calcul_intervalle(intervalle)

  response = requests.get("http://pubproxy.com/api/proxy")
  print(response.text)
  print(response.status_code)
  if response.status_code == 200:
    print("[+] Request 200")

    dico_json = response.json()

    country = dico_json["data"][0]["country"]
    
    if country == "US":
      list.append(dico_json["data"][0])

  request_counter += 1

df1 = pd.DataFrame(list)
df1