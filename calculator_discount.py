# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. 
# The function should take the original price (price) and the discount percentage (discount_percent) as parameters. 
# If the discount is 20% or higher, apply the discount; otherwise, return the original price.
#Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. 
# Print the final price after applying the discount, or if no discount was applied, print the original price.


def calculate_discount(price, discount_percent):
    # check if we can get a discount(20% or more)
    if discount_percent >= 20:
        # calculate how much we can save
        discount_amount = price * (discount_percent / 100)  
        # substract the savings from original price
        final_price = price - discount_amount
        return final_price
    else:
        # Return original price if discount is less than 20%
        return price
    
# Get input from user - e.g. shopping for a toy
original_price = float(input("Enter original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))
    
# Calcuate final price using function
final_price = calculate_discount(original_price, discount_percent)

# Test the results
# print(f"The final price is: {final_price}")

# printing the final price after applying the discount, 
# or if no discount was applied, print the original price.
if discount_percent >= 20:
    print(f"You got a {discount_percent}% discount appllied!")
    print(f"Original price: {original_price:.2f}")
    print(f"Final price: {final_price:.2f}")
else:
    print(f"Discount not given ({discount_percent}% less than 20%), too small.")
    print(f"Origina price: {original_price:.2f}")

    
    
    
    