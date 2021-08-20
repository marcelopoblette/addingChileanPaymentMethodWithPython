from typing import ValuesView
import requests
from requests.api import post
from login import login
import pprint

url = "https://apis-dev.pgf.cl/trxs/28221/nullification/status"

querystring = {"verificationToken":"3dc916e9-83e6-45e4-9f73-9813fb2ff08f"}

headers = {
    "Accept": "application/json",
    "Authorization": login()
}

response = requests.request("GET", url, headers=headers, params=querystring)

pprint.pprint(response.json())