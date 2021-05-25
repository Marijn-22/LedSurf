# -*- coding: utf-8 -*-
"""
Function to webscrape Magicseaweed
"""
import requests
import numpy as np
from bs4 import BeautifulSoup



#%%
# download 
def get_soup_from_url(url: str):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')

    return soup

url_ms_sch = 'https://magicseaweed.com/Scheveningen-Nord-Surf-Report/145/'
ms_soup = get_soup_from_url(url_ms_sch)
#%%


et



#%%

# #find primairy heights in html
# heights_prim_soup = ms_sch_soup.find_all('h4', class_ = 'nomargin font-sans-serif heavy')
#find periods in html
periods_soup = ms_sch_soup.find_all('h4', class_ = 'nomargin font-sans-serif heavy')
#find heights in html
heights_prim_soup = ms_sch_soup.find_all('span', class_ = 'msw-fc-s-h')


#Get floats from the data in list for primary period
ms_periods = []
for i in range(len(periods_soup)):
    data = periods_soup[i].text
    # if 'm' in data:
    #     ms_heights_prim.append(float(data.split('m')[0]))
    if 's' in data:
        ms_periods.append(float(data.split('s')[0]))
    
#Get floats from the data in list for primary period
ms_periods = []
for i in range(len(periods_soup)):
    data = periods_soup[i].text
    # if 'm' in data:
    #     ms_heights_prim.append(float(data.split('m')[0]))
    if 's' in data:
        ms_periods.append(float(data.split('s')[0]))
        