from pprint import pprint
from typing import ValuesView
import requests
from requests.api import post

def logintoken():
    urlLoginToken = "https://apis.pagofacil.xyz/dev/loginToken"
    payloadLoginToken = {
        "email": "email",
        "apiToken": "apiToken" 
       
        }
    headersLoginToken = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    responseLoginToken = requests.request("POST", urlLoginToken, json=payloadLoginToken, headers=headersLoginToken)
    atj = responseLoginToken.json()["access_token_jwt"]
    return atj

jwt = logintoken()
#pprint(logintoken())
