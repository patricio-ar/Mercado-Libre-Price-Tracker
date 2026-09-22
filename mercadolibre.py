import json
import requests


def get_my_items():
    with open("tokens.json", "r", encoding="utf-8") as file:
        tokens = json.load(file)

    headers = {"Authorization": f"Bearer {tokens["access_token"]}"}
    url = f"https://api.mercadolibre.com/users/{tokens["user_id"]}/items/search"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error: the server answered {response.status_code}")
        return []
    return response.json()["results"]
products = get_my_items()
#print(products)

def get_item(item_id):
    with open("tokens.json", "r", encoding="utf-8") as file:
        tokens = json.load(file)
    headers = {"Authorization": f"Bearer {tokens["access_token"]}"}
    url = f"https://api.mercadolibre.com/items/{item_id}"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error: the server answered {response.status_code}")
        return None
    item = response.json()
    title_and_price = {"title":item["title"],"price":item["price"]}
    return title_and_price 