from pprint import pprint
import time
from typing import ValuesView
import requests
from requests.api import post
from loginToken import logintoken
import random
import string
import pprint


urlTef = "https://apis.pagofacil.xyz/dev/tef"

payloadTef = {"tef": {
        "recipientData": {
            "rut": "15605114-4",
            "name": "Pepe Grillo",
            "email": "yomismo@cristiantala.cl"
        },
        "bankData": {
            "bankSBIFNumber": "037",
            "bankAccount": "3680210608"
        },
        "messageToAddressee": "Saldos Pago Facil ID2429",
        "id": ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)]),
        "amount": 100,
        "url" : "https://kr34t1v1ty/tefcallback.cl/"
        
    }}
headersTef = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": logintoken()
}

callbackUrl = {
    "url" : "https://kr34t1v1ty/tefcallback.cl/"
}

responseTef = requests.request("POST", urlTef, json=payloadTef, headers=headersTef )

pprint.pprint(responseTef.json())