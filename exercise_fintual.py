# Ejercicio Entrevista Fintual
import requests
from bs4 import BeautifulSoup
import json

request_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

def get_rows(code):
    r = requests.get('https://finance.yahoo.com/quote/'+code+"/history", headers=request_headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.find_all("table",class_="table yf-ewueuo noDl")[0]
    table_headers = []
    rows = []
    for i, row in enumerate(table.find_all("tr")):
        if i == 0:
            table_headers = [el.text.strip() for el in row.find_all('th')]
        else:
            rows.append(dict(zip(table_headers,[el.text.strip() for el in row.find_all('td')])))
    return rows

def scrape_stocks(code):
    array_stock = get_rows(code)
    for i in range(0,10):
        array_stock[i]['diff'] = float(array_stock[i]['Close      Close price adjusted for splits.']) - float(array_stock[i+1]['Close      Close price adjusted for splits.'])
    return array_stock[:10]

        
stocks_to_see = ["AAPL", "SBUX"]  

table = scrape_stocks("AAPL")
print (table)

#r_json = r.json()
""" for dato in r_json['results']:
    if dato['regular']:
        suma += float(dato['regular'])
        datos +=1 """