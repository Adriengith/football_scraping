import urllib.request
import requests
import pandas as pd

from bs4 import BeautifulSoup


def scrapmeteo(url):
    """
    Scrap informations of temperature and rainfall of a city, by date.
    from https://www.historique-meteo.net/
    In : "url" : (string) : url of the page
    Out : "tmax", "rainfall" : (integers) temperature max, rainfall ; 99999 = NaN
    """
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    # scrap rows
    listtr = soup.select(".table tr")

    # find values
    for tr in listtr:
        listtd = tr.select("td")
        for td in listtd:
            if td.get_text() == "Température maximale":
                tmax = int(tr.select("b")[0].get_text().strip("°"))
                # print("tmax", type(tmax), tmax)
            if td.get_text() == "Précipitations":
                rainfall = int(tr.select("b")[0].get_text().strip("mm"))
                # print("rainfall", type(rainfall), rainfall)
    # default values
    if "rainfall" not in locals():
        rainfall = 99999
    if "tmax" not in locals():
        tmax = 99999
    return tmax, rainfall
    
    
    
    
    
    
def create_link_weather(place, date):
    if place == 'Paris':
        place = 'Paris-SG'

    
    esp = date.count("-")
    deb = 0
    if date.count("-")!=0:
        fin = date.index("-")
    else:
        fin = len(date)
    split_words = []
    
    for i in range(0, esp + 1):
        split_words.append(date[deb:fin])
        date=date[fin+1:]
        if date.count("-")!=0:
            fin = date.index("-")
        else:
            fin = len(date)

    # if split_words[1] == "Janvier":
    #     split_words[1] = "01"
    # elif split_words[1] == "Février":
    #     split_words[1] = "02"
    # elif split_words[1] == "Mars":
    #     split_words[1] = "03"
    # elif split_words[1] == "Avril":
    #     split_words[1] = "04"
    # elif split_words[1] == "Mai":
    #     split_words[1] = "05"
    # elif split_words[1] == "Juin":
    #     split_words[1] = "06"
    # elif split_words[1] == "Juillet":
    #     split_words[1] = "07"
    # elif split_words[1] == "Août":
    #     split_words[1] = "08"
    # elif split_words[1] == "Septembre":
    #     split_words[1] = "09"
    # elif split_words[1] == "Octobre":
    #     split_words[1] = "10"
    # elif split_words[1] == "Novembre":
    #     split_words[1] = "11"
    # elif split_words[1] == "Décembre":
    #     split_words[1] = "12"


    if place == "Lille": 	
        start_link = "https://www.historique-meteo.net/france/nord-pas-de-calais/lille/"
    elif place == "Paris-SG":
        start_link = "https://www.historique-meteo.net/france/ile-de-france/paris/"
    elif place == "Monaco":
        start_link = "https://www.historique-meteo.net/france/provence-alpes-c-te-d-azur/monaco/"
    elif place == "Lyon":
        start_link = "https://www.historique-meteo.net/france/rh-ne-alpes/lyon/"
    elif place == "Marseille":
        start_link = "https://www.historique-meteo.net/france/provence-alpes-c-te-d-azur/marseille/"
    elif place == "Rennes":
        start_link = "https://www.historique-meteo.net/france/bretagne/rennes/"
    elif place == "Lens":
        start_link = "https://www.historique-meteo.net/france/nord-pas-de-calais/lens/"
    elif place == "Montpellier":
        start_link = "https://www.historique-meteo.net/france/languedoc-roussillon/montpellier/"
    elif place == "Nice":
        start_link = "https://www.historique-meteo.net/france/provence-alpes-c-te-d-azur/nice/"
    elif place == "Metz":
        start_link = "https://www.historique-meteo.net/france/lorraine/metz/"
    elif place == "Saint-Étienne":
        start_link = "https://www.historique-meteo.net/france/rh-ne-alpes/saint-etienne/"
    elif place == "Bordeaux":
        start_link = "https://www.historique-meteo.net/france/aquitaine/bordeaux/"
    elif place == "Angers":
        start_link = "https://www.historique-meteo.net/france/pays-de-la-loire/angers/"
    elif place == "Reims":
        start_link = "https://www.historique-meteo.net/france/champagne-ardenne/reims/"
    elif place == "Strasbourg":
        start_link = "https://www.historique-meteo.net/france/alsace/strasbourg/"
    elif place == "Lorient":
        start_link = "https://www.historique-meteo.net/france/bretagne/lorient/"
    elif place == "Brest":
        start_link = "https://www.historique-meteo.net/france/bretagne/brest/"
    elif place == "Nantes":
        start_link = "https://www.historique-meteo.net/france/pays-de-la-loire/nantes/"
    elif place == "Nîmes":
        start_link = "https://www.historique-meteo.net/france/languedoc-roussillon/nimes/"
    elif place == "Dijon":
        start_link = "https://www.historique-meteo.net/france/bourgogne/dijon/"
    else:
        start_link = "PROBLEM"
    split_words = split_words[0].replace(" ", "/")

    
    link_weather = start_link + split_words +"/"
    return link_weather


#/2020/08/22/
