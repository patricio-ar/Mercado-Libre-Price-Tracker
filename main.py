import tracker
import storage


products = storage.load_products()

while True:


    print("=== Price Tracker ===")
    print("1. Add a product")
    print("2. Update a price")
    print("3. Show my products")
    print("4. Exit")

    option = input("Choose an option: ")

    if option == "1":
        name = (input ("Product name: "))
        price = int(input ("Current price: "))
        target_price = int(input ("Target price: "))
        tracker.add_product(products, name, price, target_price )
        storage.save_products(products)
        print("Product added!")

    elif option == "2":
        for number, product in enumerate(products, start=1):
            print(f"{number}. {product["name"]} - ${tracker.current_price(product)}")

        choice = int(input("Product number: "))
        product = products[choice-1]

        new_price = int(input("New price: "))
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
    
