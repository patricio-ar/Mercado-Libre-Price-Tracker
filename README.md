# Mercado Libre Price Tracker

This Python project was created for anyone who wants to track the price of products on Mercado Libre.

## Functions

- **Add a product:** you can add a product with its name, its target price and its initial price.
- **Update a price:** every time the price changes, use option 2 to update it. The date is filled in automatically and the price is entered manually.
- **Show my products:** you can see the price evolution of any product, and whether the current price is below or above the target price.

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
4. Exit
```

Every product you add and every price you update is saved in `products.json`, where you can modify or delete the price history of any product.

## Next update

We are on the way to connecting the Mercado Libre API. You will be able to paste a product link and the price will be updated automatically, and you will still be able to modify every parameter in the `products.json` file.

https://auth.mercadolibre.com.ar/authorization?response_type=code&client_id=2060633006307395&redirect_uri=https://github.com/patricio-ar/Mercado-Libre-Price-Tracker