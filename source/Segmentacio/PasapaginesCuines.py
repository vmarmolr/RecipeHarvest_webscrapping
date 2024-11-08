# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:43:39 2024

@author: vmarm
"""

from bs4 import BeautifulSoup 
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By

import random

# Web a la que accedim
pagina="https://www.3cat.cat/tv3/cuines/receptes/"


ultimaPagina = 529
i = 1

driver = webdriver.Chrome()
driver.get(pagina)
time.sleep(1)

cookies = driver.find_element(By.ID, "didomi-notice-disagree-button")
cookies.click()

while i <= 20: #ultimaPagina:
    website = BeautifulSoup(driver.page_source, features="html.parser")
    paginacio = website.find("p", class_="numeracio")
    paginacio = paginacio.string.split(" ")[1]
    print("Estem a la pagina:", paginacio, "de", ultimaPagina, "\n")
    if i != ultimaPagina:
        try:
            seguent = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.R-seg a[title='Següent']")))
            seguent.click()
        except:
            break
        time.sleep(random.uniform(2, 4))
    i += 1
