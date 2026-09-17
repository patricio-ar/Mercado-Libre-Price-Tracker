from datetime import date


def add_product(products, name, price, target_price):
    product = {
        "name": name,
        "target_price": target_price,
        "history": [{"date": date.today().isoformat(), "price": price}]
    }
    products.append(product)


def current_price(product):
    return product["history"][-1]["price"]

