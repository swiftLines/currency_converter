import requests

API_KEY = 'fca_live_pGiyeq6fkpcyHda2s24UOTUCM3mjg4bsn8u5dLYe'
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

CURRENCIES = ['USD', 'CAD', 'EUR', 'AUD', 'CNY']

def convert_currency(base):
  currencies = ','.join(CURRENCIES)
  url = f'{BASE_URL}&base_currency={base}&currencies={currencies}'

