from typing import ValuesView
import requests
from requests.api import post
from loginToken import logintoken
import pprint




url = "https://apis.pagofacil.xyz/dev/availableBalance"

headers = {
    "Accept": "application/json",
    "Authorization": logintoken()
}

response = requests.request("GET", url, headers=headers)
print(response)
#print(format(numero, ','))

print("\nEl Saldo de tu Cuenta Pago Fácil es: $",format(response.json()["balance"],','),"\n")