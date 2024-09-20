import math
from datetime import datetime
from typing import Tuple

class Stock:
    # dictionary of prices
    prices = {}
    name = ""

    def __init__(self,name):
        self.name = name 

    def add_price(self,date: datetime,price) -> None:
        self.prices[date] = price

    def price(self,date: datetime) -> float:
        return self.prices[date] 


class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self,stock: Stock) -> None:
        self.stocks.append(stock)

    def profit(self,date1: datetime,date2: datetime) -> float:
        date_diff = abs((date2-date1).days)
        start_price, end_price = self.__get_prices(date1,date2)
        return self.__get_annualized_return(date_diff, start_price, end_price)
    
    def __get_prices(self, date1: datetime,date2: datetime) -> Tuple[float, float]:
        final_price = 0
        beginning_price = 0
        for i in range(len(self.stocks)):
            final_price = final_price + self.stocks[i].price(date2) 
            beginning_price = beginning_price + self.stocks[i].price(date1)
        return beginning_price, final_price
    
    def __get_annualized_return(self, date_diff: datetime, beginning_price: float, end_price: float) -> float:
        return_portfolio = (end_price - beginning_price)/beginning_price
        years = date_diff/365 #we assume that a year = 365 days
        annualized_return = math.pow(1 + return_portfolio, 1/years) - 1
        return annualized_return

