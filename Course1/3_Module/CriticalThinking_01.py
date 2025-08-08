charge_food = int(input('Enter the charge for food: '))
tip = 18/100 * charge_food
print('The tip amount is: ', tip)
sales_tax = 7/100 * charge_food
print('The sales tax amount is: ', sales_tax)
total_amount = charge_food + tip + sales_tax
print('The total amount for the food alone is ${:d} and tip is ${:.2f} and sales tax is ${:.2f}'.format(charge_food, tip, sales_tax))
print('The total amount to be paid is: $', total_amount)
