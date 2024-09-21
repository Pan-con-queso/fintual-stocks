import pytest
from datetime import date
from main import Stock, Portfolio

def test_stock_price():
    test_stock = Stock("Test")
    date_1 = date(2019,8,6)
    test_stock.add_price(date_1,101.23)
    assert 101.23 == test_stock.get_price(date_1)

def test_portfolio_profit():
    test_stock = Stock("Test")
    date_1 = date(2021,8,6)
    date_2 = date(2024,8,5)
    test_stock.add_price(date_1,2000)
    test_stock.add_price(date_2,6750)
    portfolio = Portfolio()
    portfolio.add_stock(test_stock)
    assert portfolio.profit(date_1, date_2) == 0.5

def test_integrations_scraper():
    apple_stock = Stock("AAPL")
    prices = apple_stock.get_prices()
    assert len(prices)==0
    apple_stock.load_prices(10)
    prices = apple_stock.get_prices()
    assert len(prices)==10

def test_integrations_scraper_fail():
    with pytest.raises(Exception):
        apple_stock = Stock("OWO")
        apple_stock.load_prices(10)