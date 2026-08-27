**Online Shopping System**


**1. Objective**

To develop a Python-based Online Shopping System that allows users to manage products in a shopping cart, change product quantities, remove products, apply discounts, calculate the subtotal, calculate GST, and display the final bill.


**2. Input**

**The program accepts:**

Product name

Product price

Product quantity

Product to be removed

Updated product quantity

Discount percentage

GST percentage

**Menu choice**

The menu options are:

1 – Add Product

2 – Remove Product

3 – Change Quantity

4 – Apply Discount

5 – Calculate Subtotal

6 – Calculate GST

7 – Display Final Bill

8 – Exit

**3. Output**

**The program displays:**

Products added to the shopping cart

Products removed from the cart

Updated product quantities

Subtotal amount

Discount amount

GST amount

Final payable amount

Complete shopping bill

The calculations are performed using:

Subtotal = Sum of (Product Price × Quantity)

Discount Amount = Subtotal × Discount Percentage / 100

Amount After Discount = Subtotal − Discount Amount

GST Amount = Amount After Discount × GST Percentage / 100

Final Bill = Amount After Discount + GST Amount


**4. Algorithm**

1.Start.

2.Create an empty shopping cart to store product details.

3.Display the online shopping system menu.

**Read the user's choice.**

**If the choice is 1:**

Read the product name.
Read the product price.
Read the product quantity.
Add the product details to the shopping cart.
Display a confirmation message.


**If the choice is 2:**

Read the product name to be removed.
Search for the product in the shopping cart.
If the product is found, remove it.
Display a confirmation message.
If the product is not found, display an appropriate message.

**If the choice is 3:**

Read the product name.
Search for the product in the shopping cart.
If the product is found, read the new quantity.
Update the product quantity.
Display the updated quantity.


**If the choice is 4:**

Read the discount percentage.
Calculate the subtotal.
Calculate the discount amount.
Subtract the discount from the subtotal.

**If the choice is 5:**

Calculate the subtotal by multiplying the price of each product by its quantity.
Add the amounts of all products.
Display the subtotal.


**If the choice is 6:**

Calculate the amount after discount.
Calculate GST using the GST percentage.
Display the GST amount.


**If the choice is 7:**

Display all products with their prices and quantities.
Display the subtotal.
Display the discount amount.
Display the GST amount.
Display the final payable amount.


**If the choice is 8:**

Display the exit message.

Stop the program.

If an invalid choice is entered, display an appropriate error message.

Repeat the menu until the user chooses the Exit option.

5.Stop.


**5. Time Complexity**

O(n)

Where n is the number of products in the shopping cart.

Operations such as calculating the subtotal, applying the discount, calculating GST, and displaying the final bill may require traversing all products in the cart. Therefore, the overall time complexity is O(n).

Adding a product is O(1) when using a dictionary, while searching for or removing a product can be O(n) depending on the implementation.
