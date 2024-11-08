# -*- coding: utf-8 -*-
"""
@author: Joan i Victor
"""

from bs4 import BeautifulSoup 
import requests
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import random
from datetime import datetime, timezone

# Modificar User Agent

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3", 
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
]

# Definir els headers

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,\
    */*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "en-US,en;q=0.8",
    "Cache-Control": "no-cache",
    "dnt": "1",
    "Pragma": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": random.choice(user_agents)
}
    
# Web a la que accedim
pagina="https://www.3cat.cat/tv3/cuines/receptes/"

# Obtenim la pàgina sencera i creem un objecte beautiful soup per treballar-hi
page= requests.get(pagina, headers=headers)
soupPage= BeautifulSoup(page.content, features="html.parser")

# Obtenir el numero de pagines que diu la web que te de receptes
ultimaPagina = soupPage.find("p", class_="numeracio")
ultimaPagina = ultimaPagina.text.split(" ")[3]
ultimaPagina = int(ultimaPagina)
print("Tenim un total de", ultimaPagina, "pagines! \n")

# Definim la funció que extreu les receptes
def extreure_receptes(website, numpag):
    # Busquem totes les receptes que s'han carregat a la pagina
    receptes = website.find_all("div", class_ = "M-destacat cuines T-cuinesTema")
    # Per a cada recepta
    for recepta in receptes:
        # trobem el nom i la imatge
        nom = recepta.find("a", {"class": "titol--a"})
        img = recepta.find("img", class_="foto")
        # guardem la url
        pagina_url = "https://www.3cat.cat" + nom["href"]
        try:
            # guardem la foto
            pagina_img = img["src"]
        except:
            # si no hi ha foto no guardar res
            pagina_img = None
        # afegir la info en la llista urls
        urls.append((pagina_url, pagina_img, numpag))

# Inicialitzem la llista de les urls i l'iterador
urls = []
i = 1

# Obrim el navegador i accedim a la pagina
try:
    driver = webdriver.Edge()
except:
    try:
        driver = webdriver.Chrome()
    except:
        print("Has d'instal·lar Edge o Chrome!")
        return
driver.get(pagina)
#driver.fullscreen_window()

# Esperem un segon per a que carregui
time.sleep(1)

# Rebutjem les cookies
cookies = driver.find_element(By.ID, "didomi-notice-disagree-button")
cookies.click()

# Guardem i imprimim el temps d'inici
iniciurl = datetime.now(timezone.utc)
print(iniciurl, "\n")

# Iniciem el bucle per a cada pagina
while i <= ultimaPagina:
    # crearem un beautifulsoup de la pagina
    website = BeautifulSoup(driver.page_source, features="html.parser")
    # trobem el número de pàgina que ens diu l'html
    paginacio = website.find("p", class_="numeracio")
    paginacio = paginacio.string.split(" ")[1]
    print("Estem a la pagina:", paginacio, "de", ultimaPagina, "\n")
    # apliquem la funcio extreure_receptes
    extreure_receptes(website, paginacio)
    # si no estem a la ultima pagina passar de pagina
    if i != ultimaPagina:
        try:
            seguent = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.R-seg a[title='Següent']")))
            seguent.click()
        except:
            # si no tenim el boto de passar pagina sortir del bucle
            break
        # Esperar per a que sembli una navegacio mes humana
        time.sleep(random.uniform(1, 4))
    # passar de pagina
    i += 1

# Tancar el navegador
driver.quit()

# imprimir el numero d'iteracions 
print("Hem fet", i, "iteracions\n")

# Guardar i imprimir el temps de finalitzacio
finalurl = datetime.now(timezone.utc)
print(finalurl, "\n")
# Imprimir el temps que hem trigat
print("Hem trigat", finalurl-iniciurl, "per aconseguir les urls\n")

# Guardar i imprimir el numero de receptes
numreceptes = len(urls)
print("Tenim", numreceptes, "receptes.")

# Guardar les urls, fotos i numero de pagina en un .txt
with open('urls.txt', 'w') as f:
    for url, img, numpag in urls:
        f.write(f"{url}, ")
        f.write(f"{img}, ")
        f.write(f"{numpag}\n")

# inicialitzem la llista de receptes i l'iterador del seguent bucle        
llistaReceptes = []
numrecepta = 0

iniciwebscrapping = datetime.now(timezone.utc)
print(iniciwebscrapping)

# Per a cada fila de les urls
for linkRecepta, img_url, numpag in urls:
    # Modifiquem l'iterador
    numrecepta += 1
    # Entrem a la pagina i creem un beautifulsoup
    page = requests.get(linkRecepta, headers=headers)
    soupPage = BeautifulSoup(page.content, features="html.parser")
    
    # Obtenim el nom de la recepta
    try:
        nomRecepta = soupPage.find_all("h1")[1]
        nomRecepta = nomRecepta.string
    except:
        # Les receptes més antigues tenen el nom al primer h1 de la pagina
        try:
            nomRecepta = soupPage.find("h1")
            nomRecepta = nomRecepta.string
        except:
            # Si no trobem el nom guardem un buit
            nomRecepta = None
    # Donem feedback a la consola d'on ens trobem
    print(nomRecepta)
    print("(",numrecepta,"/",numreceptes,")\n")
    
    # Obtenim els tags
    try:
        div_tags = soupPage.find("div", class_ = "llistat-tags")
        a_tags = div_tags.find_all("a")
        Etiquetes = [tag.string for tag in a_tags]
    except:
        # Si no, guardem un buit
        Etiquetes = None
#    print(Etiquetes)
    
    # Obtenim la info basica
    try:
        div_info = soupPage.find("div", class_ = "span4 informacio-basica")
    except:
        # Si no, guardem un buit
        div_info = None
    
    # Obtenim la dificultat
    try:
        Dificultat_bloc = div_info.find("span", string="Dificultat: ")
        Dificultat = Dificultat_bloc.next_sibling.strip()
    except:
        # Si no, guardem un buit
        Dificultat = None
        
    # Obtenim el temps
    try:
        Temps_bloc = div_info.find("span", string="Temps: ")
        Temps = Temps_bloc.next_sibling.strip()        
    except:
        # Si no, guardem un buit
        Temps = None
    
    # Obtenim la dieta
    try:
        Dieta_bloc = div_info.find("span", string="Dieta: ")
        Dieta = Dieta_bloc.next_sibling.string
    except:
        # Si no, guardem un buit
        Dieta = None
    
#    print(Dificultat)
#    print(Temps)
#    print(Dieta)
    
    # Obtenim els ingredients
    try:
        div_ingredients = soupPage.find("div", class_ = "ingredients")
        li_ingredients = div_ingredients.find_all(["li", "p"])
        Ingredients = [ingredient.get_text(strip = True) for ingredient in li_ingredients]
    except:
        # Si no, guardem un buit
        Ingredients = None
#    print(Ingredients)

    # Obtenim la preparacio
    try:
        preparacio = soupPage.find("h2", string="PREPARACIÓ")
        pasos = preparacio.find_next_sibling().find_all(["li", "p", "div"])
        Preparacio = [pas.string for pas in pasos]
    except:
        # Si no, guardem un buit
        Preparacio = None
#    print(Preparacio)
    
    # Obtenim la fotografia
    try:
        Imatge = img_url
    except:
        # Si no, guardem un buit
        Imatge = None
#    print(Imatge)
    
    # Creem el diccionari
    recepta = {
        "Nom":nomRecepta,
        "Link":linkRecepta,
        "Pagina": numpag,
        "Imatge": img_url,
        "Dificultat": Dificultat,
        "Temps": Temps,
        "Dieta": Dieta,
        "Ingredients": Ingredients,
        "Preparacio": Preparacio,
        "Tags": Etiquetes
        }
    
    # Afegim a la llista de diccionaris
    llistaReceptes.append(recepta)

# Guardar i imprimir el temps de finalitzacio
finalwebscrapping = datetime.now(timezone.utc)
print(finalwebscrapping, "\n")
# Imprimir el temps que hem trigat
print("Hem trigat", finalwebscrapping-iniciwebscrapping, "per aconseguir fer el webscrapping\n")

# Creem l'arxiu csv i exportem tota la llista de diccionaris
with open('receptes.csv', mode='w', newline='', encoding='utf-8') as arxiu_csv:
    camps=llistaReceptes[0].keys()
    escriptor_csv = csv.DictWriter(arxiu_csv, fieldnames=camps)
    
    escriptor_csv.writeheader()
    escriptor_csv.writerows(llistaReceptes)
