import requests
from pprint import PrettyPrinter
from dotenv import load_dotenv
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Load environment variables from .env file
load_dotenv('secret.env')

#Create our printer
printer = PrettyPrinter()

# Access the API key
api_key = os.getenv('NBA_API_KEY')

print(api_key)

BASE_URL = "https://api.balldontlie.io/v1"
END_POINT="/games"

def get(url, api_key):

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Accept': 'application/json',
    }

    params = {
        'seasons[]': [2024]
    }

    response = requests.get(url, headers=headers, params=params)

    print("Status Code:", response.status_code)
    #print("Response Text:", response.text)

    response.raise_for_status()  
    return response

data = get(BASE_URL + END_POINT, api_key).json()
games = data['data']

for game in games:
    print("-------------------------------------------------------")
    print(f"The home team {game['home_team']['full_name']} scored {game['home_team_score']}")
    print(f"The visiting team {game['visitor_team']['full_name']} scored {game['visitor_team_score']}")
    
print(len(games))




