import pprint
from typing import ValuesView
import requests
from requests.api import post
from loginToken import logintoken

url = "https://apis.pagofacil.xyz/dev/validations/BankAccount"

payload = {
    "bankData": {
        "bankSBIFNumber": "016",
        "bankAccount": "46745556"
    },
    "rut": "14025496-7"
}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "18bec3b1-cbc6-4820-ad2e-fb142efa7f75"
    #logintoken()
}

response = requests.request("POST", url, json=payload, headers=headers)

pprint.pprint(response.json())