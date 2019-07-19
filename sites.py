from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import multiprocessing
import re
import warnings
warnings.filterwarnings("ignore")
def Site():
     driver = webdriver.PhantomJS(executable_path = "C:/Users/Bytewave/phantomjs/phantomjs/bin/phantomjs")
     driver.get('https://www.nseindia.com/live_market/dynaContent/live_watch/equities_stock_watch.htm')
     s = BeautifulSoup(driver.page_source)
     s.findAll('th')[0].get_text()
     rows=s.findAll('tr')
     for row in rows:
         row_td=row.find_all('td')    
     str_cells=str(row_td)
     list_rows = []
     for row in rows:
         cells = row.find_all('td')
         str_cells = str(cells)
         clean = re.compile('<.*?>')
         clean2 = (re.sub(clean, '',str_cells))
         list_rows.append(clean2)
     
     df=pd.DataFrame(list_rows)
     return(df)
def Site2():
     driver = webdriver.PhantomJS(executable_path = "C:/Users/Bytewave/phantomjs/phantomjs/bin/phantomjs")
     driver.get('https://www.bseindia.com/markets.html')
     s = BeautifulSoup(driver.page_source)
     s.findAll('th')[0].get_text()
     rows=s.findAll('tr')
     for row in rows:
        row_td=row.find_all('td')    
     str_cells=str(row_td)
     list_rows = []
     for row in rows:
        cells = row.find_all('td')
        str_cells = str(cells)
        clean = re.compile('<.*?>')
        clean2 = (re.sub(clean, '',str_cells))
        list_rows.append(clean2)
     df2=pd.DataFrame(list_rows)
     return(df2)

def Site3():
    driver = webdriver.PhantomJS(executable_path = "C:/Users/Bytewave/phantomjs/phantomjs/bin/phantomjs")
    driver.get('https://www.moneycontrol.com/stocksmarketsindia/')
    s = BeautifulSoup(driver.page_source)
    s.findAll('th')[0].get_text()
    rows=s.findAll('tr')
    for row in rows:
       row_td=row.find_all('td')    
       str_cells=str(row_td)
       list_rows = []
    for row in rows:
       cells = row.find_all('td')
       str_cells = str(cells)
       clean = re.compile('<.*?>')
       clean2 = (re.sub(clean, '',str_cells))
       list_rows.append(clean2)
    df3=pd.DataFrame(list_rows)
    return(df3)

if __name__=='__main__':
    PROCESSES=4
    with multiprocessing.Pool(PROCESSES) as pool:
        result = pool.apply_async(Site).get()
        print(result)
        result2=pool.apply_async(Site2).get()
        print(result2)
        result3=pool.apply_async(Site3).get()
        print(result3)
