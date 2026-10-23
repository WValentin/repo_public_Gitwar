product_name = "computer"
product_price = 1500
product_price *= 1.10
product_quantity = 5

print(f"The new price is {product_price} euros for a {product_name}.")
print(f"There are {product_quantity} {product_name} left in stock at {product_price} euros each.")

purchase = int(input("Enter the number of computers you want to buy : "))
print(f"You have chosen to buy {purchase} {product_name} at {product_price} euros each.")


if purchase <= product_quantity:
    product_quantity -= purchase
    print(f"You have bought {purchase} {product_name} for {purchase * product_price} euros.")
    print(f"There are {product_quantity} {product_name} left in stock at {product_price} euros each.")
else:
    print(f"There are only {product_quantity} {product_name} left in stock, you cannot buy {purchase} {product_name}.")    
if product_quantity < 5:
    print("Please note: stock is low.")
    product_quantity += 10
    print(f"Stock has been replenished, there are now {product_quantity} {product_name} left at {product_price} euros each.")