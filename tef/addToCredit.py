import requests
from requests.api import post
from loginToken import logintoken
import pprint

url = "https://apis.pagofacil.xyz/dev/addToCreditBalance"

payload = {"amount": 200}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": logintoken()
}

response = requests.request("POST", url, json=payload, headers=headers)

pprint.pprint(response.json())