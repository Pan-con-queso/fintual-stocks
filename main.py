import math
from datetime import datetime

class Stock:
    # dictionary of prices
    prices = {}
    name = ""

    def __init__(self,name):
        self.name = name 

    def add_price(self,date: datetime,price):
        self.prices[date] = price

    def price(self,date: datetime):
        return self.prices[date]


class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self,stock: Stock):
        self.stocks.append(stock)

    def profit(self,date1: datetime,date2: datetime):
        final_price = 0
        beginning_price = 0
        date_diff = abs((date2-date1).days)
        for i in range(len(self.stocks)):
            final_price = final_price + self.stocks[i].price(date2) 
            beginning_price = beginning_price + self.stocks[i].price(date1)
        return_portfolio = (final_price - beginning_price)/beginning_price
        years = date_diff/365 #we assume that a year = 365 days
        annualized_return = math.pow(1 + return_portfolio, 1/years) - 1
        return annualized_return
