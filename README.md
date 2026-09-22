# Mercado Libre Price Tracker

This Python project was created for anyone who wants to track the price of products on Mercado Libre.

## Functions

- **Add a product:** you can add a product with its name, its target price and its initial price.
- **Update a price:** every time the price changes, use option 2 to update it. The date is filled in automatically and the price is entered manually.
- **Show my products:** you can see the price evolution of any product, and whether the current price is below or above the target price.
- **Sync my Mercado Libre products:** the program connects to the Mercado Libre API, reads every listing of your account, adds the new ones and saves today's price of the ones you already track. The access token is refreshed automatically when it expires.

## How to use

You must have Python installed.

1. Open the terminal on Windows.
2. Change the directory to the project folder:

```bash
cd "C:\Users\...\price-tracker"
```

3. Run the program:

```bash
python main.py
```

You will see this:

```
=== Price Tracker ===
1. Add a product
2. Update a price
3. Show my products
4. Sync my Mercado Libre products
5. Exit
```

Every product you add and every price you update is saved in `products.json`, where you can modify or delete the price history of any product.

## Mercado Libre setup

To use option 4 you need your own Mercado Libre application (the API only lets an account read its own listings).

1. Create an application at https://developers.mercadolibre.com.ar. Use your own repository URL as the redirect URI, enable the *Authorization Code* and *Refresh Token* flows, and give it read access to listings.
2. Create a `credentials.json` file in this folder:

```json
{
  "client_id": "YOUR_APP_ID",
  "client_secret": "YOUR_CLIENT_SECRET"
}
```

3. Open this address in your browser (with your own app id and redirect URI), authorize the application, and copy the `code=TG-...` value from the address bar:

```
https://auth.mercadolibre.com.ar/authorization?response_type=code&client_id=YOUR_APP_ID&redirect_uri=YOUR_REDIRECT_URI
```

4. Run `python get_tokens.py` and paste that code. It saves `tokens.json`, and from then on the program refreshes the token by itself.

`credentials.json`, `tokens.json` and `products.json` are listed in `.gitignore`, so your keys and your data never reach GitHub.

## Next update

Tracking products from other sellers: the API does not allow it for a personal application, so those products are still added and updated by hand.