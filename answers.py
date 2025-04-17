def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

# user input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(original_price, discount)

    if discount >= 20:
        print(f"Discount applied! The final price is: ${final_price:.2f}")
    else:
        print(f"No significant discount applied. The price remains: ${final_price:.2f}")

except ValueError:
    print("Invalid input! Please enter numeric values for price and discount.")
