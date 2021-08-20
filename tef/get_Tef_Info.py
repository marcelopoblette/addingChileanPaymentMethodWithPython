from typing import KeysView, ValuesView
import requests
from requests.api import post
from loginToken import logintoken
import pprint

url = "https://apis.pagofacil.xyz/dev/tef/6efa5e8a-754c-432e-b544-9c32082c8214"
#6efa5e8a-754c-432e-b544-9c32082c8214
#226937de-1106-4978-b786-d3cdf08f28a7
headers = {
    "Accept": "application/json",
    "Authorization": logintoken()
}

response = requests.request("GET", url, headers=headers)

pprint.pprint(response.json()["tefResponse"])