# -*- coding: utf-8 -*-
"""
Function to webscrape Magicseaweed
"""
import requests
import numpy as np
from bs4 import BeautifulSoup
import lxml
import pandas as pd

#%%
# download
def get_soup_from_url(url: str):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')

    return soup

url_ms_sch = 'https://magicseaweed.com/Scheveningen-Nord-Surf-Report/145/'
ms_soup = get_soup_from_url(url_ms_sch)
#%%

## Get dates from table

## Get all height values

## Check for flats

## Get all periods




#%%

# #find primairy heights in html
# heights_prim_soup = ms_sch_soup.find_all('h4', class_ = 'nomargin font-sans-serif heavy')
#find periods in html
periods_soup = ms_soup.find_all('h4', class_ = 'nomargin font-sans-serif heavy')
#find heights in html
heights_prim_soup = ms_soup.find_all('span', class_ = 'msw-fc-s-h')

#Get floats from the data in list for primary period
ms_periods = []
for i in range(len(periods_soup)):
    data = periods_soup[i].text
    # if 'm' in data:
    #     ms_heights_prim.append(float(data.split('m')[0]))
    if 's' in data:
        ms_periods.append(float(data.split('s')[0]))

# #Get floats from the data in list for primary period
# ms_periods = []
# for i in range(len(periods_soup)):
#     data = periods_soup[i].text

#     # if 'm' in data:
#     #     ms_heights_prim.append(float(data.split('m')[0]))
#     if 's' in data:
#         ms_periods.append(float(data.split('s')[0]))

#%%
req = requests.get(url_ms_sch)
soup = BeautifulSoup(req.text, 'lxml')


#First just find table was used to find class of the table.
#table_data = soup.find_all('table')#, class_ = "table table-sm table-striped table-inverse table-tide")
class_prim_tb = 'table table-primary table-forecast allSwellsActive msw-js-table'
table_data = soup.find_all('table', class_ = class_prim_tb)

# headers = []
# for i in table_data[0].find_all('th'):
#     title = i.text
#     headers.append(title)

headers = ['time', 'height','empty1','height_prim','period_prim','empty2',
           'empty3','wind', 'empty4','empty5','temp','empty6']
df = pd.DataFrame(columns = headers)

# Find all data in the primary table and put this per row in list.
rows_txt = []
for j in table_data[0].find_all('tr'):
    row_data = j.find_all('td')
    rows_txt.append([tr.text for tr in row_data])

day = 0
data = np.zeros((8,12))
for count,row_text in enumerate(rows_text):
    if '12am' in row_text[0]:
        data[day,:12] = row_text[:12]
        data[day+1,:12] = rows_text[count+1,:12]
        data[day+2,:12] = rows_text[count+2,:12]
        data[day+3,:12] = rows_text[count+3,:12]
        data[day+4,:12] = rows_text[count+4,:12]
        data[day+5,:12] = rows_text[count+5,:12]
        data[day+6,:12] = rows_text[count+6,:12]
        data[day+7,:12] = rows_text[count+7,:12]
        day +=1
        
    # row = row_data[0].text
    # row_data = j.find_all('td')
    # row = [tr.text for tr in row_data]
    # length = len(df)
    # df.loc[length] = row


