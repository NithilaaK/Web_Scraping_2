from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import time
from selenium import webdriver

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome("/Users/anand/Downloads/chromedriver_win32 (2)/chromedriver.exe")
browser.get(START_URL)
time.sleep(10)
dwarf_data = []
soup = bs(browser.page_source, "html.parser")
temp_list = []

def scrape():
    star_table = soup.find_all('table')
    table_rows = star_table[7].find_all('tr')
    for tr in table_rows:
        td_tag = tr.find_all('td')
        row = [i.text.rstrip() for i in td_tag]
        temp_list.append(row)

    Name = []
    Distance = []
    Mass = []
    Radius = []

    for i in range(1,len(temp_list)):
        Name.append(temp_list[i][0])
        Distance.append(temp_list[i][5])
        Mass.append(temp_list[i][7])
        Radius.append(temp_list[i][8])

    df2 = pd.DataFrame(list(zip(Name,Distance,Mass,Radius)),columns=['Name','Distance','Mass','Radius'])
    df2.set_index('Name', inplace=True)
    df2.to_csv('dwarfStars.csv')
scrape()