import json

import requests


API = "https://api.mercadolibre.com"


def load_tokens():
    with open("tokens.json", "r", encoding="utf-8") as file:
        return json.load(file)


def save_tokens(tokens):
    with open("tokens.json", "w", encoding="utf-8") as file:
        json.dump(tokens, file, indent=2, ensure_ascii=False)


def refresh_access_token():
    """Ask for a new access token using the refresh token. Tokens last 6 hours."""
    tokens = load_tokens()

    with open("credentials.json", "r", encoding="utf-8") as file:
        credentials = json.load(file)

    data = {
        "grant_type": "refresh_token",
        "client_id": credentials["client_id"],
        "client_secret": credentials["client_secret"],
        "refresh_token": tokens["refresh_token"]
    }
    response = requests.post(f"{API}/oauth/token", data=data)
    if response.status_code != 200:
        print(f"Error: could not refresh the token ({response.status_code})")
        return None

    new_tokens = response.json()
    save_tokens(new_tokens)
    return new_tokens["access_token"]


def get(url):
    """GET with the access token. If the token expired, refresh it and try again."""
    tokens = load_tokens()
    headers = {"Authorization": f"Bearer {tokens["access_token"]}"}
    response = requests.get(url, headers=headers)

    # Mercado Libre answers 401 or 403 when the token expired
    if response.status_code in (401, 403):
        access_token = refresh_access_token()
        if access_token is None:
            return None
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error: the server answered {response.status_code}")
        return None

    return response.json()


def get_my_items():
    """Return the item ids of every listing of the account."""
    tokens = load_tokens()
    item_ids = []
    offset = 0

    while True:
        url = f"{API}/users/{tokens["user_id"]}/items/search?offset={offset}&limit=50"
        data = get(url)
        if data is None:
            return item_ids

        item_ids = item_ids + data["results"]
        offset = offset + 50
        if offset >= data["paging"]["total"]:
            return item_ids


def get_item(item_id):
    """Return the title and the price of one listing, or None if it fails."""
    item = get(f"{API}/items/{item_id}")
    if item is None:
        return None
    return {"title": item["title"], "price": item["price"]}
