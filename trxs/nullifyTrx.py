import requests
from login import login
import pprint


import requests
url = "https://apis-dev.pgf.cl/trxs/28338/nullification"

payload = {
    "amount": 5000000,
    "type": "total",
    "nullifyTbk": True
}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": login()
}

response = requests.request("POST", url, json=payload, headers=headers)

pprint.pprint(response.json())