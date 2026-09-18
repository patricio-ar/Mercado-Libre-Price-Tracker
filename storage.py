import json 
import os 


def save_products(products):
    with open("products.json", "w", encoding="utf-8") as file: 
        json.dump(products, file, indent = 2, ensure_ascii = False)


def load_products():
    if not os.path.exists("products.json"):
        return []
    else:
        with open("products.json", "r", encoding="utf-8") as file:
            return json.load(file)
