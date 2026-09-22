from datetime import date


def add_product(products, name, price, target_price, item_id=None):
    product = {
        "name": name,
        "target_price": target_price,
        "history": [{"date": date.today().isoformat(), "price": price}]
    }
    if item_id is not None:
        product["item_id"] = item_id
    products.append(product)


def current_price(product):
    return product["history"][-1]["price"]


def update_price(product, new_price):
    old_price = current_price(product)
    product["history"].append({"date": date.today().isoformat(), "price": new_price})
    return new_price - old_price


def find_by_item_id(products, item_id):
    for product in products:
        if product.get("item_id") == item_id:
            return product
    return None
