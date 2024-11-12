# Pràctica 1 - Tipologia i cicle de vida de les dades
Assignatura: M2.851 / Semestre: 2024-1 / Data: 12-11-2024
## Autors
 * Victor Marmol Romero - vmarmolro@uoc.edu
 * Joan Sabaté Terrón - jsabatete@uoc.edu
## Lloc web escollit
https://www.3cat.cat/tv3/cuines/receptes/
## Enllaç DOI Zenodo
El dataset ha estat publicat a Zenodo amb [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14054272.svg)](https://doi.org/10.5281/zenodo.14054272)

## Descripció del repositori
El repositori consta de la carpeta dataset que conté les dades que obtenim dels diferents programes, la carpeta source que conté els programes, dins d'aquesta la carpeta Segmentacio que conté els programes que hem utilitzat per a comprovar cada part del programa principal, el README i el document pdf. Els fitxers que podem trobar en aquest repositori són:
 * /dataset/receptes.csv: fitxer amb el joc de dades.
 * /dataset/urls.txt: urls de totes les pàgines web.
 * /source/Cuines.py: Fitxer principal i codi del programa.
 * /source/requirements.txt: Llista de paquets utilitzats.
 * /source/Segmentacio/Desdeurl.py: Programa per a obtenir el fitxer receptes.csv des d'el fitxer urls.txt
 * source/Segmentacio/PasapaginesCuines.py: Programa per a observar com el navegador pasa les pagines per a fer webscrapping tenint en compte que la paginació és dinàmica i dona errors.
 * source/Segmentacio/UnaRecepta.py: Programa que amb el link d'una recepta extreu tota la informació que extreu el programa Cuines.py. Serveix per comprovar que passa am les receptes que donen error.
## Instruccions
Per a obtenir el dataset hem d'executar el programa Cuines.py i aquest s'encarregarà de produir el fitxer urls.txt amb totes les urls de les receptes que tindrà el nostre dataset i el fitxer receptes.csv amb tot el dataset.
És important saber que necessitem una connexió a internet i tenir instal·lat els navegadors Microsoft Edge o Google Chrome per a executar el programa Cuines.py.
També cal destacar que el temps d'execució és molt llarg i tediós però estem parlant d'aconseguir extreure dades de gairebé 8000 receptes amb una paginació dinàmica.

De tota manera, es recomana llegir la memòria per entendre bé cada part del programa.
