import math
import requests
from datetime import datetime
from typing import List, Optional, Tuple, TypedDict
from bs4 import BeautifulSoup

class StockData(TypedDict):
    Date: datetime 
    Open: float 
    High: float 
    Low: float 
    Close: float
    Adj_Close: float 
    Volume: float 
    diff: Optional[float]     


class Stock:
    # dictionary of prices
    prices = {}
    name = ""

    def __init__(self,name):
        self.name = name 
        self.prices = {}

    def add_price(self,date: datetime,price) -> None:
        """
        Add Price for a certain date
        """
        self.prices[date] = price

    def load_prices(self, n_days: int) -> List[int]:
        array_stock = self.__get_last_rows(n_days)
        print(array_stock)
        for i in range(n_days):
            date = datetime.strptime(array_stock[i]['Date'], '%b %d, %Y').strftime('%Y-%m-%d')
            self.prices[date] = array_stock[i]['Close      Close price adjusted for splits.']

    def get_price(self,date: datetime) -> float:
        return self.prices[date] 


    def get_prices(self):
        return self.prices 

    def __get_last_rows(self, n_days) -> List[StockData]:
        request_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
        try:
            r = requests.get('https://finance.yahoo.com/quote/'+self.name+"/history", headers=request_headers)
            soup = BeautifulSoup(r.text, 'html.parser')
            table = soup.find_all("table",class_="table yf-ewueuo noDl")[0]
            table_headers = []
            rows = []
            for i, row in enumerate(table.find_all("tr")):
                if i == 0:
                    table_headers = [el.text.strip() for el in row.find_all('th')]
                elif i <= n_days:
                    rows.append(dict(zip(table_headers,[el.text.strip() for el in row.find_all('td')])))
                else:
                    break
            return rows
        except Exception as e:
            print(e)


class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self,stock: Stock) -> None:
        self.stocks.append(stock)

    def profit(self,date1: datetime,date2: datetime) -> float:
        date_diff = abs((date2-date1).days)
        start_price, end_price = self.__get_portfolio_prices(date1,date2)
        return self.__get_annualized_return(date_diff, start_price, end_price)
    
    def __get_portfolio_prices(self, date1: datetime,date2: datetime) -> Tuple[float, float]:
        final_price = 0
        beginning_price = 0
        for i in range(len(self.stocks)):
            final_price = final_price + self.stocks[i].get_price(date2) 
            beginning_price = beginning_price + self.stocks[i].get_price(date1)
        return beginning_price, final_price
    
    def __get_annualized_return(self, date_diff: datetime, beginning_price: float, end_price: float) -> float:
        return_portfolio = (end_price - beginning_price)/beginning_price
        years = date_diff/365 #we assume that a year = 365 days
        annualized_return = math.pow(1 + return_portfolio, 1/years) - 1
        return annualized_return

