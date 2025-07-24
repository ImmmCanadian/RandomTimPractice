import requests
from pprint import PrettyPrinter
from dotenv import load_dotenv
import os

#set the path to out current working directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Load environment variables from .env file
load_dotenv('secret.env')

# Access the API key
api_key = os.getenv('API_KEY')

BASE_URL = 'https://api.freecurrencyapi.com/v1'
END_POINT_LATEST = '/latest'
END_POINT_HISTORICAL = '/historical'

headers = {
        'apikey': f'{api_key}',
        'Accept': 'application/json',
    }

params = {
        'base_currency': f'EUR',
        'currencies': 'USD,CAD,CNY'
    }

exchange_rates_today = requests.get(BASE_URL+END_POINT_LATEST, headers=headers, params=params).json()

#print("Status Code:", exchange_rates_today.status_code)
#print("Response Text:", exchange_rates_today.text)
#exchange_rates_today.raise_for_status()  

params = {
        'base_currency': f'EUR',
        'currencies': 'USD,CAD,CNY',
        'date': '2024-08-21'
    }

exchange_rates_1_year_ago = requests.get(BASE_URL+END_POINT_HISTORICAL, headers=headers, params=params).json()

#print("Status Code:", exchange_rates_1_year_ago.status_code)
#print("Response Text:", exchange_rates_1_year_ago.text)
#exchange_rates_1_year_ago.raise_for_status()

for curr in exchange_rates_today['data'].keys():
    diff = exchange_rates_today['data'][curr]/exchange_rates_1_year_ago['data'][params['date']][curr]
    print(f"The difference between the EUR and {curr} has changed by {diff}% in the past year.")










