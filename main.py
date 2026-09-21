import tracker
import storage


def ask_positive_number(message):
    while True:
        try:
            number = int(input(message))
            if number > 0:
                return number
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a positive number.")


products = storage.load_products()

while True:


    print("=== Price Tracker ===")
    print("1. Add a product")
    print("2. Update a price")
    print("3. Show my products")
    print("4. Exit")

    option = input("Choose an option: ")

    if option == "1":
        name = input ("Product name: ").strip()
        while name == "":
            print("Please enter a name.")
            name = input("Product name: ").strip()
        price = ask_positive_number("Current price: ")
        target_price = ask_positive_number("Target price: ")
        tracker.add_product(products, name, price, target_price )
        storage.save_products(products)
        print("Product added!")

    elif option == "2":
        if len(products) == 0:
            print("You don't have any products yet.")
            continue

        for number, product in enumerate(products, start=1):
            print(f"{number}. {product["name"]} - ${tracker.current_price(product)}")

        try:
            choice = int(input("Product number: "))
        except ValueError:
            print ("Invalid product.")
            continue
        if choice < 1 or choice > len(products):    
            print("Invalid product.")
            continue

        product = products[choice-1]

        new_price = ask_positive_number("New price: ")
        difference = tracker.update_price(product, new_price)

        storage.save_products(products)
        if difference < 0:
            print(f"The price went down ${abs(difference)}")
        elif difference > 0:
            print(f"The price went up ${difference}.")
        else:
            print("The price did not change.")

        if new_price <= product["target_price"]:
            print("It's below your target price")
        
    elif option == "3":
        if len(products) == 0:
            print("You don't have any products yet.")
        else: 
            for product in products:
                print(f"Product name: {product["name"]} - Current price: ${tracker.current_price(product)} - Target: ${product["target_price"]}")
                for entry in product["history"]:
                    print(f"{entry["date"]}: ${entry["price"]}")
                

    elif option == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
    
