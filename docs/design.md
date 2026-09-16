# Price Tracker — Design (Stage 1)

**Date:** 2026-09-16
**Type:** learning project — the author writes the code, Claude guides

## Goal

A terminal program that tracks product prices over time and says when a price
drops below the price you want to pay. It is a first Python project, published
on GitHub, built step by step to learn the basics.

## Stages

- **Stage 1 (this design):** prices are typed in by hand.
- **Stage 2 (later, separate design):** prices come automatically from the
  Mercado Libre API. The API needs a developer account and authentication
  (tested on 2026-09-16: requests without a login return `403`).
  Stage 2 adds one new file, `mercadolibre.py`, without rewriting Stage 1.

## What the program does

A menu shown in the terminal, repeated until the user chooses Exit:

```
=== Price Tracker ===
1. Add a product
2. Update a price
3. Show my products
4. Exit
Choose an option:
```

1. **Add a product** — asks for name, current price and target price.
   Saves the current price as the first entry in the history, with today's date.
2. **Update a price** — lists the products with a number, the user picks one
   and types the new price. The program adds it to the history and prints:
   - `📉 The price went down $X!` if it is lower than the last price
   - `📈 The price went up $X.` if it is higher
   - `➖ The price did not change.` if it is equal
   - `🎉 It's below your target price — time to buy!` if the new price is less
     than or equal to the target price
3. **Show my products** — for each product: name, current price (last in
   history), target price, and all previous prices with their dates.
   If there are no products: `You don't have any products yet.`
4. **Exit** — saves and closes.

Data is saved to the file after every change, so nothing is lost if the
program is closed unexpectedly.

## Files

```
price-tracker/
├── main.py        → menu: prints options, reads input, calls tracker functions
├── tracker.py     → logic: add product, update price, compare prices
├── storage.py     → load_products() and save_products() using JSON
├── products.json  → saved data (created automatically, not uploaded to GitHub)
├── .gitignore     → tells Git to ignore products.json
└── README.md      → project description for GitHub
```

Rules for the files:
- Only `main.py` uses `input()` and `print()` for the menu.
- `tracker.py` does not read or write files; `storage.py` does not know about menus.

## Data format (`products.json`)

A list of products. Prices are whole numbers (Argentine pesos, no cents).
Dates use the format `YYYY-MM-DD`.

```json
[
  {
    "name": "Auriculares JBL",
    "target_price": 20000,
    "history": [
      {"date": "2026-09-16", "price": 25999},
      {"date": "2026-09-20", "price": 22999}
    ]
  }
]
```

## Error handling

- **Invalid number** (letters, empty, negative or zero): print
  `Please enter a positive number.` and ask again.
- **Invalid menu option** (e.g. `7` or `hello`): print `Invalid option.` and
  show the menu again.
- **Invalid product number** in "Update a price": print `Invalid product.` and
  go back to the menu.
- **No `products.json` file** (first run): start with an empty list.
- **Empty product name**: ask again.

## Checking that it works

After each learning step, the author runs `python main.py` and tries the new
feature by hand, including wrong input. Automated tests are out of scope for
Stage 1 and may be added later as a learning step.

## Learning path

1. Setup: project folder, GitHub account, Git configuration, first commit
2. Menu loop (`print`, `input`, `while`)
3. Add products (lists, dictionaries)
4. Save and load (`json`, files)
5. Update and compare prices (functions, `if`/`else`, dates)
6. Wrong input (`try`/`except`)
7. README and upload Stage 1 to GitHub

Each step ends with: run it, see it work, commit.

## Out of scope for Stage 1

Deleting or editing products, automatic price updates, notifications, charts,
multiple users, a graphical or web interface.
