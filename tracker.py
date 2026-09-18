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

def update_price(product, new_price):
    old_price =  current_price(product)
    product["history"].append({"date": date.today().isoformat(), "price": new_price})
    return new_price - old_price
