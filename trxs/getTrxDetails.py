import requests
from login import login
import pprint

url = "https://api-dev.pgf.cl/trx-details/28338"

headers = {
    "Accept": "application/json",
    "Authorization": login()
}

response = requests.request("GET", url, headers=headers)

pprint.pprint(response.json())

"""
28217 vd
28082 vd
15858 vc 16-04-2020
18334 vc 24-07-2020
28221 vc 20-07-2021 verificationToken: 3dc916e9-83e6-45e4-9f73-9813fb2ff08f
"""