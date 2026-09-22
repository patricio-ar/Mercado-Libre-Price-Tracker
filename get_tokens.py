import requests
import json


with open("credentials.json", "r", encoding="utf-8") as credentials:
    values = json.load(credentials)

auth_code = input("Code: ")

data = {"grant_type":"authorization_code", "client_id": values["client_id"], "client_secret": values["client_secret"], "code": auth_code, "redirect_uri": "https://github.com/patricio-ar/Mercado-Libre-Price-Tracker"}
response = requests.post("https://api.mercadolibre.com/oauth/token", data=data)
print(response.status_code)

if response.status_code == 200:
    token_data = response.json()
    print(list(token_data))
    with open ("tokens.json", "w", encoding="utf-8") as tokens:
        json.dump(token_data, tokens, indent=2, ensure_ascii=False)