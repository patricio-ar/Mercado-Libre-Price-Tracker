# Price Tracker - Design

## Goal

A terminal program that tracks product prices over time and tells the user when a price
drops to or below the price they want to pay.

## Stages

- **Stage 1:** prices are entered by hand.
- **Stage 2:** the prices of the user's own Mercado Libre listings are read from the
  Mercado Libre API. The API only lets a personal application read the listings of its own
  account, so products from other sellers are still tracked by hand.

## Menu

```
=== Price Tracker ===
1. Add a product
2. Update a price
3. Show my products
4. Sync my Mercado Libre products
5. Exit
Choose an option:
```

1. **Add a product:** asks for the name, the current price and the target price. The current
   price becomes the first entry of the history, with today's date.
2. **Update a price:** lists the products with a number, the user picks one and types the new
   price. The program adds it to the history and prints whether the price went down, went up or
   did not change, and whether it is below the target price.
3. **Show my products:** for each product, the name, the current price, the target price and the
   full price history.
4. **Sync my Mercado Libre products:** reads every listing of the account. New listings are added
   as products; for listings already tracked, today's price is added to the history if it changed.
5. **Exit.**

Data is saved after every change, so nothing is lost if the program is closed unexpectedly.

## Files

| File | Responsibility |
|---|---|
| `main.py` | Menu and user input/output |
| `tracker.py` | Product logic: add, current price, update, find by item id |
| `storage.py` | Load and save `products.json` |
| `mercadolibre.py` | Mercado Libre API: token refresh, list of listings, title and price |
| `get_tokens.py` | Exchanges the authorization code for tokens (run once) |

Rules:
- Only `main.py` reads from the keyboard and prints the menu.
- `tracker.py` does not read or write files and does not use the network.
- `storage.py` and `mercadolibre.py` do not know about the menu.

## Data format

`products.json` is a list of products. Prices are whole numbers (Argentine pesos). Dates use
the `YYYY-MM-DD` format. Products that come from Mercado Libre also store their `item_id`.

```json
[
  {
    "name": "Wireless headphones",
    "target_price": 20000,
    "history": [
      {"date": "2026-09-16", "price": 25999},
      {"date": "2026-09-20", "price": 22999}
    ]
  }
]
```

## Error handling

- **Invalid number** (letters, empty, zero or negative): `Please enter a positive number.` and
  ask again.
- **Empty product name:** `Please enter a name.` and ask again.
- **Invalid menu option:** `Invalid option.` and show the menu again.
- **Invalid product number** (letters or out of range): `Invalid product.` and go back to the menu.
- **No products yet:** `You don't have any products yet.`
- **No `products.json` file:** start with an empty list.
- **API error:** print the status code and continue. If the access token expired, refresh it and
  retry once.

## Mercado Libre authentication

The program uses OAuth 2.0 with the Authorization Code flow:

1. The user authorizes the application in the browser and copies the authorization code.
2. `get_tokens.py` exchanges that code for an access token and a refresh token and saves them in
   `tokens.json`.
3. The access token lasts 6 hours. When a request fails because it expired, `mercadolibre.py`
   uses the refresh token to get a new one.

`credentials.json`, `tokens.json` and `products.json` are listed in `.gitignore`.

## Out of scope

Deleting or editing products, notifications, charts, prices of other sellers' listings,
multiple users.
