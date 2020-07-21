# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 20:54:45 2019

@author: emill
"""


from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
import requests
import pandas as pd


url = "https://www.bilbasen.dk/brugt/bil?fuel=0&yearfrom=0&yearto=0&pricefrom=0&priceto=10000000&mileagefrom=-1&mileageto=10000001&includeengroscvr=true&includeleasing=true&free=vw%20touran&page={page_number}"
page_number=1
uclient = uReq(url)

df = pd.DataFrame(columns=['pris', 'km','year','hk','kml', 'kmt','Grøn ejerudgift','model navn',
                           'region','beskrivelse', 'annonce'])
page_html = uclient.read()
uclient.close()
page_soup = soup(page_html, "html.parser")

number_cars = str(page_soup.find("li", {"class":"active "}))
numbs = number_cars.find("Alle ")
start = number_cars.find("Alle ") + len("Alle ") +1
end = number_cars.find("\r",start) -2
number = int(number_cars[start:end])

i = 0
page_number = 0
while i < number:
    counter_plus = 0
    counter_exclusive = 0
    page_number=page_number +1
    url = "https://www.bilbasen.dk/brugt/bil?fuel=0&yearfrom=0&yearto=0&pricefrom=0&priceto=10000000&mileagefrom=-1&mileageto=10000001&includeengroscvr=true&includeleasing=true&free=vw%20touran&page={page_number}"   
    uclient = uReq(url)
    page_html = uclient.read()
    uclient.close()
    page_soup = soup(page_html, "html.parser")
    containers_plus = page_soup.findAll("div", {"class":"row listing listing-plus bb-listing-clickable"})   
    containers_exclusive = page_soup.findAll("div", {"class":"row listing listing-exclusive bb-listing-clickable"})   
    for contain in containers_plus:
        tester = contain
        test_km = int(tester.findAll("div", {"class":"col-xs-2 listing-data "})[1].text.strip().replace(".",""))
        test_year = int(tester.findAll("div", {"class":"col-xs-2 listing-data "})[2].text.strip())
        test_pris = tester.find("div", {"class":"col-xs-3 listing-price "}).text.strip()
        var = str(tester.findAll("span", {"class":"variableDataColumn"}))
        hk = int(var[var.find("hk=")+len("hk=")+1:var.find("HK")-1])
        kml = float(var[var.find("kml=")+len("kml=")+1:var.find("km/l")-1].replace(",","."))
        kmt = float(var[var.find("kmt=")+len("kmt=")+1:var.find("sek")-1].replace(",","."))
        ejerudgift = int(var[var.find("data-moth=")+len("data-moth=")+1:var.find("pr.")-1].replace(".",""))
        model_name = tester.find("a",{"class":"listing-heading darkLink"}).text
        region = tester.find("div", {"class":"col-xs-2 listing-region "}).text.strip()
        desc = tester.find("div", {"class":"listing-description expandable-box"}).text.strip()
        annonce = 'plus'
        
        df2=pd.DataFrame([[test_pris, test_km, test_year, hk, kml, kmt,ejerudgift,model_name,region,desc, annonce]]
        ,columns=['pris', 'km','year','hk','kml', 'kmt','Grøn ejerudgift','model navn',
                                   'region','beskrivelse', 'annonce'])
        df= df.append(df2)
    for contain in containers_exclusive:
        tester = contain
        test_km = int(tester.findAll("div", {"class":"col-xs-2 listing-data "})[1].text.strip().replace(".",""))
        test_year = int(tester.findAll("div", {"class":"col-xs-2 listing-data "})[2].text.strip())
        test_pris = tester.find("div", {"class":"col-xs-3 listing-price "}).text.strip()
        var = str(tester.findAll("span", {"class":"variableDataColumn"}))
        hk = int(var[var.find("hk=")+len("hk=")+1:var.find("HK")-1])
        kml = float(var[var.find("kml=")+len("kml=")+1:var.find("km/l")-1].replace(",","."))
        kmt = float(var[var.find("kmt=")+len("kmt=")+1:var.find("sek")-1].replace(",","."))
        ejerudgift = int(var[var.find("data-moth=")+len("data-moth=")+1:var.find("pr.")-1].replace(".",""))
        model_name = tester.find("a",{"class":"listing-heading darkLink"}).text
        region = tester.find("div", {"class":"col-xs-2 listing-region "}).text.strip()
        desc = tester.find("div", {"class":"listing-description expandable-box"}).text.strip()
        annonce = 'plus'
        
        df2=pd.DataFrame([[test_pris, test_km, test_year, hk, kml, kmt,ejerudgift,model_name,region,desc, annonce]]
        ,columns=['pris', 'km','year','hk','kml', 'kmt','Grøn ejerudgift','model navn',
                                   'region','beskrivelse', 'annonce'])
        df= df.append(df2)
    i=i+len(containers_plus)+len(containers_exclusive)
    print(i)
