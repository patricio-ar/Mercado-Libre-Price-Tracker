# Price Tracker (Stage 1) — Learning Plan

> **How to use this plan:** this is a *learning* plan. The author writes all the
> code; Claude guides, answers questions and reviews. Tasks give goals, hints
> and checks — not finished solutions. Mark steps with `[x]` when done.

**Goal:** A terminal program to track product prices by hand and warn when a
price is at or below the target price.

**Architecture:** `main.py` talks to the user (menu, input, printing).
`tracker.py` holds the logic on a list of product dictionaries. `storage.py`
loads and saves that list as JSON.

**Tech Stack:** Python 3.13, standard library only (`json`, `datetime`), Git, GitHub.

**Spec:** `docs/design.md`

## Global Constraints

- Python 3.13 standard library only — no `pip install`.
- Prices are whole numbers (`int`), pesos, no cents.
- Dates are strings in `YYYY-MM-DD` format.
- Data file name: `products.json`; it must never be committed (listed in `.gitignore`).
- Only `main.py` uses `input()`. `tracker.py` never opens files. `storage.py` never prints menus.
- User messages must match the spec text exactly.
- All commands run inside the `price-tracker` folder.

## Shared names (every task uses these)

```
storage.py
  load_products() -> list          # returns [] if products.json does not exist
  save_products(products) -> None  # writes the list to products.json

tracker.py
  add_product(products, name, price, target_price) -> None
  current_price(product) -> int                    # last price in history
  update_price(product, new_price) -> int          # adds to history, returns new - old

main.py
  ask_positive_number(message) -> int
  main()
```

Product dictionary shape:

```python
{"name": "Auriculares JBL", "target_price": 20000,
 "history": [{"date": "2026-09-16", "price": 25999}]}
```

---

### Task 1: Setup — Git, GitHub and first commit

**Files:** Create `.gitignore`

**You learn:** what a repository and a commit are; basic terminal commands.

- [ ] **Step 1: Create a GitHub account** at https://github.com (do it yourself in the browser; choose a professional username, you will show it to employers).
- [ ] **Step 2: Tell Git who you are** (use the same email as GitHub):
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "your-email@example.com"
  git config --global init.defaultBranch main
  ```
- [ ] **Step 3: Open a terminal in the `price-tracker` folder and create the repository:**
  ```bash
  git init
  ```
  Expected: `Initialized empty Git repository in ...`
- [ ] **Step 4: Create `.gitignore`** with these two lines:
  ```
  products.json
  __pycache__/
  ```
- [ ] **Step 5: Check and commit:**
  ```bash
  git status
  git add .
  git commit -m "Add design, plan and gitignore"
  ```
  Expected: `git status` lists `.gitignore` and `docs/`; after the commit, `git log --oneline` shows 1 commit.

---

### Task 2: The menu loop

**Files:** Create `main.py`

**You learn:** `print`, `input`, `while` loops, `if`/`elif`/`else`, functions.

**Goal:** show the menu again and again until the user chooses 4.

- [ ] **Step 1:** Write a function `main()` with a `while True:` loop that prints the menu exactly as in the spec and reads the option with `input("Choose an option: ")`.
- [ ] **Step 2:** Options:
  - `"1"`, `"2"`, `"3"` → for now print `Coming soon...`
  - `"4"` → print `Goodbye!` and stop the loop (hint: `break`)
  - anything else → print `Invalid option.`
- [ ] **Step 3:** At the bottom of the file, call the function:
  ```python
  if __name__ == "__main__":
      main()
  ```
  (Ask Claude what this line means — it's a good question.)
- [ ] **Step 4: Check:** run `python main.py` and try `1`, `7`, `hello`, then `4`.
  Expected: `Coming soon...`, `Invalid option.`, `Invalid option.`, `Goodbye!` and the program ends.
- [ ] **Step 5: Commit:**
  ```bash
  git add main.py
  git commit -m "Add menu loop"
  ```

---

### Task 3: Add and show products (in memory)

**Files:** Create `tracker.py`; Modify `main.py`

**You learn:** lists, dictionaries, `import`, `datetime`, `for` loops, f-strings.

- [ ] **Step 1:** In `tracker.py`, write `add_product(products, name, price, target_price)`. It builds a dictionary with the shape above and appends it to `products`. Today's date as text:
  ```python
  from datetime import date
  date.today().isoformat()   # "2026-09-16"
  ```
- [ ] **Step 2:** In `tracker.py`, write `current_price(product)` that returns the price of the **last** item in `history` (hint: index `-1`).
- [ ] **Step 3:** In `main.py`, `import tracker`, create `products = []` before the loop, and make option `1` ask for name, price and target price, then call `tracker.add_product(...)` and print `Product added!`. For now convert numbers with `int(input(...))` — letters will crash it; Task 6 fixes that.
- [ ] **Step 4:** Make option `3` print every product like this (or `You don't have any products yet.` if the list is empty):
  ```
  1. Auriculares JBL
     Current price: $25999 | Target: $20000
     History: 2026-09-16 $25999
  ```
- [ ] **Step 5: Check:** run it, choose `3` (empty message), add two products, choose `3` again.
  Expected: both products listed with numbers 1 and 2.
- [ ] **Step 6: Commit:** `git add main.py tracker.py` then `git commit -m "Add and show products"`

---

### Task 4: Save and load with JSON

**Files:** Create `storage.py`; Modify `main.py`

**You learn:** files, `with open(...)`, the `json` module, `os.path.exists`.

- [ ] **Step 1:** In `storage.py`, write `save_products(products)` using `json.dump(products, file, indent=2, ensure_ascii=False)` inside `with open("products.json", "w", encoding="utf-8") as file:`.
- [ ] **Step 2:** Write `load_products()`. If `products.json` does not exist, return `[]`; otherwise open it with `"r"` and return `json.load(file)`.
- [ ] **Step 3:** In `main.py`, `import storage`; replace `products = []` with `products = storage.load_products()`, and call `storage.save_products(products)` right after adding a product.
- [ ] **Step 4: Check:** add a product, choose `4`, run `python main.py` again, choose `3`.
  Expected: the product is still there. Open `products.json` in the editor and compare it with the spec's data format. Run `git status`: `products.json` must **not** appear.
- [ ] **Step 5: Commit:** `git add main.py storage.py` then `git commit -m "Save products to JSON file"`

---

### Task 5: Update a price and compare

**Files:** Modify `tracker.py`, `main.py`

**You learn:** return values, comparisons, `abs()`.

- [ ] **Step 1:** In `tracker.py`, write `update_price(product, new_price)`: remember the old price (`current_price`), append `{"date": today, "price": new_price}` to `history`, return `new_price - old_price`.
- [ ] **Step 2:** In `main.py`, option `2`:
  1. If there are no products, print `You don't have any products yet.` and go back to the menu.
  2. Show the numbered list, ask `Product number: ` and pick the product (number 1 is index 0).
  3. Ask the new price, call `tracker.update_price(...)`, then save.
  4. Print depending on the difference:
     - negative → `📉 The price went down $X!` (X is positive: use `abs()`)
     - positive → `📈 The price went up $X.`
     - zero → `➖ The price did not change.`
  5. If the new price `<=` target price, also print `🎉 It's below your target price — time to buy!`
- [ ] **Step 3:** Make option `3` show the full history, e.g. `History: 2026-09-16 $25999, 2026-09-20 $22999` (hint: build a list of strings, then `", ".join(...)`).
- [ ] **Step 4: Check:** product at 25999 with target 20000. Update to 22999 → "went down $3000". Update to 24000 → "went up $1001". Update to 24000 → "did not change". Update to 19999 → "went down" **and** the 🎉 message. Close and reopen: history has 5 prices.
- [ ] **Step 5: Commit:** `git add main.py tracker.py` then `git commit -m "Update prices and compare"`

---

### Task 6: Handle wrong input

**Files:** Modify `main.py`

**You learn:** `try`/`except ValueError`, loops that repeat until input is valid, `strip()`.

- [ ] **Step 1:** Write `ask_positive_number(message)`: loop forever; try `int(input(message))`; if it raises `ValueError` **or** the number is `<= 0`, print `Please enter a positive number.` and ask again; otherwise return it.
- [ ] **Step 2:** Use `ask_positive_number` for price, target price and new price (replace every `int(input(...))`).
- [ ] **Step 3:** Product name: ask again while the name is empty after `.strip()`.
- [ ] **Step 4:** Product number in option `2`: if it is not a number or not between 1 and the number of products, print `Invalid product.` and go back to the menu.
- [ ] **Step 5: Check:** try price `abc`, `-5`, `0`, empty; name with only spaces; product number `0`, `99`, `x`.
  Expected: the program never crashes and shows the spec messages.
- [ ] **Step 6: Commit:** `git add main.py` then `git commit -m "Handle invalid input"`

---

### Task 7: README and upload to GitHub

**Files:** Create `README.md`

**You learn:** Markdown, remote repositories, `git push`.

- [ ] **Step 1:** Write `README.md` in English with: title, one-sentence description, features list, how to run (`python main.py`), an example of the menu, and "Next: Stage 2 — automatic prices from Mercado Libre".
- [ ] **Step 2:** Commit: `git add README.md` then `git commit -m "Add README"`
- [ ] **Step 3:** On github.com, click **New repository**, name it `price-tracker`, **Public**, and do **not** add a README (you already have one).
- [ ] **Step 4:** Connect and upload (GitHub shows your exact URL):
  ```bash
  git remote add origin https://github.com/YOUR-USERNAME/price-tracker.git
  git push -u origin main
  ```
  A browser window may ask you to log in to GitHub — do it yourself.
- [ ] **Step 5: Check:** refresh the GitHub page. Expected: your files and README are visible, `products.json` is not, and the commit history shows all your commits. 🎉
