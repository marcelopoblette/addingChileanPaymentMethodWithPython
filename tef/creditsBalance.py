
from typing import ValuesView
import requests
from requests.api import post
from loginToken import logintoken

url = "https://apis.pagofacil.xyz/dev/balance"

headers = {
    "Accept": "application/json",
    "Authorization": logintoken()
}

response = requests.request("GET", url, headers=headers)

print("El balance de créditos es: $",format(response.json()["balance"],","))

#print(response.text)