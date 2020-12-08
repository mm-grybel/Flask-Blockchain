import requests
from . import main


API_URL = 'https://api.coinbase.com/v2/prices/spot?currency=EUR'


@main.route('/')
def index():
    response = requests.get(API_URL)
    current_price = response.json()

    return current_price
