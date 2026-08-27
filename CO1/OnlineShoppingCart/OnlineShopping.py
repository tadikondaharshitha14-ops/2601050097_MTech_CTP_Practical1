cart = {}

DISCOUNT_PERCENT = 10
GST_PERCENT = 18

while True:

    print("\n===== ONLINE SHOPPING SYSTEM =====")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Change Quantity")
    print("4. Apply Discount")
    print("5. Calculate Subtotal")
    print("6. Calculate GST")
    print("7. Display Final Bill")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    # Add Product
    if choice == 1:

        product = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter quantity: "))

        if product in cart:
            cart[product]["quantity"] += quantity
            print("Product quantity updated successfully.")

        else:
            cart[product] = {
                "price": price,
                "quantity": quantity
            }

            print("Product added successfully.")

    # Remove Product
    elif choice == 2:

        product = input("Enter product name to remove: ")

        if product in cart:
            del cart[product]
            print("Product removed successfully.")

        else:
            print("Product not found.")

    # Change Quantity
    elif choice == 3:

        product = input("Enter product name: ")

        if product in cart:

            quantity = int(input("Enter new quantity: "))

            if quantity > 0:
                cart[product]["quantity"] = quantity
                print("Quantity updated successfully.")

            else:
                print("Quantity must be greater than 0.")

        else:
            print("Product not found.")

    # Apply Discount
    elif choice == 4:

        if len(cart) == 0:
            print("Cart is empty.")

        else:
            subtotal = 0

            for product, details in cart.items():
                subtotal += details["price"] * details["quantity"]

            discount = subtotal * DISCOUNT_PERCENT / 100

            print("\n--- DISCOUNT DETAILS ---")
            print("Subtotal:", subtotal)
            print("Discount Percentage:", DISCOUNT_PERCENT, "%")
            print("Discount Amount:", discount)

    # Calculate Subtotal
    elif choice == 5:

        if len(cart) == 0:
            print("Cart is empty.")

        else:
            subtotal = 0

            for product, details in cart.items():
                amount = details["price"] * details["quantity"]
                subtotal += amount

            print("\nSubtotal:", subtotal)

    # Calculate GST
    elif choice == 6:

        if len(cart) == 0:
            print("Cart is empty.")

        else:
            subtotal = 0

            for product, details in cart.items():
                subtotal += details["price"] * details["quantity"]

            discount = subtotal * DISCOUNT_PERCENT / 100
            amount_after_discount = subtotal - discount
            gst = amount_after_discount * GST_PERCENT / 100

            print("\n--- GST DETAILS ---")
            print("Amount After Discount:", amount_after_discount)
            print("GST Percentage:", GST_PERCENT, "%")
            print("GST Amount:", gst)

    # Display Final Bill
    elif choice == 7:

        if len(cart) == 0:
            print("Cart is empty.")

        else:
            subtotal = 0

            print("\n========== FINAL BILL ==========")
            print("Product\t\tPrice\tQuantity\tAmount")

            for product, details in cart.items():

                price = details["price"]
                quantity = details["quantity"]
                amount = price * quantity

                subtotal += amount

                print(product, "\t\t", price, "\t",
                      quantity, "\t\t", amount)

            discount = subtotal * DISCOUNT_PERCENT / 100
            amount_after_discount = subtotal - discount
            gst = amount_after_discount * GST_PERCENT / 100
            final_amount = amount_after_discount + gst

            print("--------------------------------")
            print("Subtotal:", subtotal)
            print("Discount (", DISCOUNT_PERCENT, "%):", discount)
            print("Amount After Discount:", amount_after_discount)
            print("GST (", GST_PERCENT, "%):", gst)
            print("Final Bill:", final_amount)
            print("================================")

    # Exit
    elif choice == 8:

        print("Thank you for shopping!")
        print("Program ended.")
        break

    # Invalid Choice
    else:

        print("Invalid choice. Please try again.")
