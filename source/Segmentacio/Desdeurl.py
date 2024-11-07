# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 12:17:40 2024

@author: vmarm
"""

from bs4 import BeautifulSoup 
import requests
import csv

with open("C:/Users/vmarm/OneDrive/Documentos/Paradoxes/UOC/03-. Tipologia i cicle de les dades/PRACTIQUES/PRAC1/Dades estalvi/urls_final.txt", "r") as f:
    urls = csv.reader(f, delimiter = ",")
    
    
    llistaReceptes = []
    numrecepta = 0
    numreceptes = 3975
    
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,\
        */*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch, br",
        "Accept-Language": "en-US,en;q=0.8",
        "Cache-Control": "no-cache",
        "dnt": "1",
        "Pragma": "no-cache",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
    }
    
    for linkRecepta, img_url, numpag in urls:
        numrecepta += 1
        
        page = requests.get(linkRecepta, headers=headers)
        soupPage = BeautifulSoup(page.content, features="html.parser")
        
        # Obtenim el nom de la recepta
        try:
            nomRecepta = soupPage.find_all("h1")[1]
            nomRecepta = nomRecepta.string
        except:
            try:
                nomRecepta = soupPage.find("h1")
                nomRecepta = nomRecepta.string
            except:
                nomRecepta = None
        print(nomRecepta)
        print("(",numrecepta,"/",numreceptes,")\n")
        
        # Obtenim els tags
        try:
            div_tags = soupPage.find("div", class_ = "llistat-tags")
            a_tags = div_tags.find_all("a")
            Etiquetes = [tag.string for tag in a_tags]
        except:
            Etiquetes = None
    #    print(Etiquetes)
        
        # Obtenim la info basica
        try:
            div_info = soupPage.find("div", class_ = "span4 informacio-basica")
        except:
            div_info = None
        
        # Obtenim la dificultat
        try:
            Dificultat_bloc = div_info.find("span", string="Dificultat: ")
            Dificultat = Dificultat_bloc.next_sibling.strip()
        except:
            Dificultat = None
            
        # Obtenim el temps
        try:
            Temps_bloc = div_info.find("span", string="Temps: ")
            Temps = Temps_bloc.next_sibling.strip()        
        except:
            Temps = None
        
        # Obtenim la dieta
        try:
            Dieta_bloc = div_info.find("span", string="Dieta: ")
            Dieta = Dieta_bloc.next_sibling.string
        except:
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
            Ingredients = None
        #    print(Ingredients)

        # Obtenim la preparacio
        try:
            preparacio = soupPage.find("h2", string="PREPARACIÓ")
            pasos = preparacio.find_next_sibling().find_all(["li", "p", "div"])
            Preparacio = [pas.string for pas in pasos]
        except:
            Preparacio = None
    #    print(Preparacio)
        
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
        #afegim a la llista de diccionaris
    
        llistaReceptes.append(recepta)
    
    # Creem l'arxiu csv i exportem tota la llista de diccionaris
    with open('receptes.csv', mode='w', newline='', encoding='utf-8') as arxiu_csv:
        camps=llistaReceptes[0].keys()
        escriptor_csv = csv.DictWriter(arxiu_csv, fieldnames=camps)
        
        escriptor_csv.writeheader()
        escriptor_csv.writerows(llistaReceptes)
    #'''