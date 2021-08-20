from typing import ValuesView
import requests
from requests.api import post
import pprint

def login():
    url = "https://apis-dev.pgf.cl/users/login"
    payload = {
        "username": "YOUR-EMAIL", #put your e-mail
        "password": "YOUR_PASSWORD"#put your password
        }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
        }
    response = requests.request("POST", url, json=payload, headers=headers)
    atj = response.json()["data"]["access_token_jwt"]
    return atj

#jwt = login()
