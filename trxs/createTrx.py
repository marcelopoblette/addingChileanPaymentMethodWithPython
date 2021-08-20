import requests
import hashlib
import hmac
import json
import time
import webbrowser
import tokens
import pprint


encoding = 'utf-8'
x_account_id = tokens.tokenServiceDev #Put your Token Service
x_amount = str(b'1000000', encoding)
x_currency = str(b'CLP', encoding)
x_reference = str(time.time()) #Just a random number as an example 
x_customer_email = str(b'correo@correo.cl', encoding)
x_url_complete = str(b'https://www.pagofacil.cl', encoding)
x_url_cancel = str(b'https://www.pagofacil.cl', encoding)
x_url_callback = str(b'https://callback.domain.com', encoding)
x_shop_country = str(b'CL', encoding)
x_session_id = str(b'1', encoding) #Just a random number as an example 



object='x_account_id'+x_account_id+'x_amount'+x_amount+'x_currency'+x_currency+'x_customer_email'+x_customer_email+'x_reference'+x_reference+'x_session_id'+x_session_id+'x_shop_country'+x_shop_country+'x_url_callback'+x_url_callback+'x_url_cancel'+x_url_cancel+'x_url_complete'+x_url_complete
payload = object.encode('utf-8')
key = tokens.tokenSecretDev #Put your Token Secret


# Generate the hash.
signature = hmac.new(key,payload,hashlib.sha256).hexdigest()
x_signature =  signature
url = tokens.dev # Put the Enviroment Endpoint (dev or Prod)
payload = {
  'x_account_id' : x_account_id ,
  'x_amount' : int(x_amount), 
  'x_currency' : x_currency, 
  'x_reference' : x_reference , 
  'x_customer_email' : x_customer_email, 
  'x_url_complete' : x_url_complete, 
  'x_url_cancel' : x_url_cancel, 
  'x_url_callback' : x_url_callback ,
  'x_shop_country' : x_shop_country, 
  'x_session_id' : x_session_id, 
  'x_signature' : x_signature 
}

jpayload = json.dumps(payload)
headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }

response = requests.request("POST", url, data=jpayload, headers=headers)
"""
0 gateway
1 webpay
2 khipu max 5mm
3 multicaja
4 pago 46
5 mach
"""
chosenPayUrl = response.json()['data']['payUrl'][1]['url']  # here you choose your payUrl
pprint.pprint(response.json())#Here you can see the response
webbrowser.open(chosenPayUrl)