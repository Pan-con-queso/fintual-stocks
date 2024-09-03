from datetime import date
from main import Stock, Portfolio

def test_stock_price():
    test_stock = Stock("Test")
    date_1 = date(2019,8,6)
    test_stock.add_price(date_1,101.23)
    assert 101.23 == test_stock.price(date_1)

def test_portfolio_profit():
    test_stock = Stock("Test")
    date_1 = date(2021,8,6)
    date_2 = date(2024,8,5)
    test_stock.add_price(date_1,2000)
    test_stock.add_price(date_2,6750)
    portfolio = Portfolio()
    portfolio.add_stock(test_stock)
    assert portfolio.profit(date_1, date_2) == 0.5