def calculate_discount(price, discount_percentage):
    # Check if the discount percentage is valid
    if discount_percentage < 0 or discount_percentage > 100:
        return "Error: Discount percentage must be between 0 and 100."
    
    # Apply discount only if it is 20% or higher
    if discount_percentage >= 20:
        discounted_price = price - (price * discount_percentage / 100)
        return discounted_price
    else:
        return price  # Return the original price if the discount is less than 20%


# Prompt the user to enter price and discount percentage
price = float(input("Enter the price: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Call the function and print the result
result = calculate_discount(price, discount_percentage)
print(f"Final price after discount: {result}")
