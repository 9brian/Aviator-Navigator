
import requests, json
from pprint import pprint

# Don't think we need this
payload = {
    # 'region' : 'Marina, CA'
    # 'country_id' 'US'
}

endpoint = 'https://weatherdbi.herokuapp.com/data/weather/marina'

try:
    r = requests.get(endpoint, params=payload)
    data = r.json()
    pprint(data)
except:
    print('please try again')