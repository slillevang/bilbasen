# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:28:28 2019

@author: Emil

Functions getting relevant info for cars

"""

import numpy as np

def get_km(tester):
    try: 
        test_km = float(tester.findAll("div", {"class":"col-xs-2 listing-data"})[1].text.strip().replace(".",""))
    except:
        test_km = np.nan            
    return test_km

def get_id(tester):
    str_test = str(tester.findAll("div", {"class":"compare-cars-container"}))
    begin = str_test.find("data-listingid=") + len("data-listingid=") + 1 
    end = str_test.find(">")-1
    ID_var = str_test[begin:end]
    return ID_var

def get_year(tester):
    try:
        test_year = float(tester.findAll("div", {"class":"col-xs-2 listing-data"})[2].text.strip())
    except:
        test_year = np.nan
    return test_year


def get_price(tester):
    try:
        test_pris = tester.find("div", {"class":"col-xs-3 listing-price"}).text.strip()
        test_pris = float(test_pris[0:test_pris.find(" kr")].replace(".",""))
    except:
        test_pris = np.nan
    return test_pris

def get_var(tester):
        var = str(tester.findAll("span", {"class":"variableDataColumn"}))
        try:
            hk = float(var[var.find("hk=")+len("hk=")+1:var.find("HK")-1])
            kml = float(var[var.find("kml=")+len("kml=")+1:var.find("km/l")-1].replace(",","."))
            kmt = float(var[var.find("kmt=")+len("kmt=")+1:var.find("sek")-1].replace(",","."))
            ejerudgift = float(var[var.find("data-moth=")+len("data-moth=")+1:var.find("pr.")-1].replace(".",""))
        except:
            hk = np.nan
            kml = np.nan
            kmt = np.nan
            ejerudgift = np.nan
        return(hk,kml,kmt,ejerudgift)            

def get_model_region(tester):
    try:
        model_name = tester.find("a",{"class":"listing-heading darkLink"}).text
        region = tester.find("div", {"class":"col-xs-2 listing-region"}).text.strip()
        letters = ['ø','æ','å','Ø','Æ','Å']
        replace_letters = ['oe','ae','aa','Oe','Ae','AA']
        desc = tester.find("div", {"class":"listing-description expandable-box"}).text.strip()
        for i in range(len(letters)):
            region = region.replace(letters[i],replace_letters[i])
            desc = desc.replace(letters[i],replace_letters[i])
        if type(tester.find("span", {"class":"listing-label"})) == type(None):
            buy_leas = 'Koeb'
        else:
            buy_leas ='Leasing' 
    except:
        model_name = "Missing"
        region = "Missing"
        desc = "Missing"
        if type(tester.find("span", {"class":"listing-label"})) == type(None):
            buy_leas = 'Koeb'
        else:
            buy_leas ='Leasing' 
    return model_name, region, desc, buy_leas

def get_hyperlink(tester):
    start_str = 'www.bilbasen.dk'
    test = str(tester.findAll("a", {"class":"listing-heading darkLink"}))
    outs=test[test.find('href=')+len('href=')+1:test.find('>')-1]
    tjekker = start_str + outs
    return tjekker

