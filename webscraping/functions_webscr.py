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
class_prim_tb = 'table table-primary table-forecast allSwellsActive msw-js-table' #name changes so not used
table_data = soup.find_all('table')#, class_ = class_prim_tb)
primairy_table = table_data[2]
# headers = []
# for i in table_data[0].find_all('th'):
#     title = i.text
#     headers.append(title)

headers = ['time', 'height','empty1','height_prim','period_prim','empty2',
           'empty3','wind', 'empty4','empty5','temp','empty6']
df = pd.DataFrame(columns = headers)

# Find all data in the primary table and put this per row in list.
rows_txt = []
for j in primairy_table.find_all('tr'):
    row_data = j.find_all('td')
    rows_txt.append([tr.text for tr in row_data])

day = 0
data = np.zeros((8*7,12))
for count,row_text in enumerate(rows_txt):
    if len(row_text)>1 and'12am' in row_text[0]:
        
        for i in range(12):
            #Get time
            time_raw = rows_txt[count+i][0]
            if 'am' in time_raw:
                time = float(time_raw.split('am')[0])
            elif 'pm' in time_raw:
                time = float(time_raw.split('pm')[0])
            elif 'Noon' in time_raw:
                time = 12.0
            else:
                print('No correct time found for day {}. Time column '\
                      'found is {}.'.format(day,time_raw))
                print('\n So time set to 0.')
                time = 0
                
            #Get height
            height_raw = rows_txt[count+i][1]
            if '-' in height_raw and 'm' in height_raw:
                h_str = height_raw.split('-')[-1]
                height = float(h_str.split('m')[0])
            elif 'Flat' in height_raw:
                height = 0
            else:
                print('No correct height found for day {}. Height column '\
                      ' found is {}.'.format(day, height_raw))
                print('\n So height set to 0.')
                height = 0
                
            #Get period
            
            #fill data in table
            data[day+i,0] = day
            data[day+i,1] = time
            data[day+i,2] = height
                
        # data[day,:12] = row_text[:12]
        # data[day+1,:12] = rows_txt[count+1,:12]
        # data[day+2,:12] = rows_txt[count+2,:12]
        # data[day+3,:12] = rows_txt[count+3,:12]
        # data[day+4,:12] = rows_txt[count+4,:12]
        # data[day+5,:12] = rows_txt[count+5,:12]
        # data[day+6,:12] = rows_txt[count+6,:12]
        # data[day+7,:12] = rows_txt[count+7,:12]
        day +=1
        
    # row = row_data[0].text
    # row_data = j.find_all('td')
    # row = [tr.text for tr in row_data]
    # length = len(df)
    # df.loc[length] = row


