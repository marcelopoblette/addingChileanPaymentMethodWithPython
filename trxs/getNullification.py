from typing import ValuesView
import requests
from requests.api import post
from login import login
import pprint

url = "https://apis-dev.pgf.cl/trxs/28338/nullification/"

headers = {
    "Accept": "application/json",
    "Authorization": login()
}

response = requests.request("GET", url, headers=headers)

pprint.pprint(response.json())