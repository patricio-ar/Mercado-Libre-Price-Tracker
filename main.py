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
        print("Coming soon...")
    elif option == "3":
        if len(products) == 0:
            print("You don't have any products yet.")
        else: 
            for product in products:
                print(f"Product name: {product["name"]} - Current price: ${tracker.current_price(product)}")
    elif option == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
    
