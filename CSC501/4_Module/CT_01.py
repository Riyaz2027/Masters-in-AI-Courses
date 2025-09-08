class ItemToPurchase():
    item_name = "none"
    item_price = 0.0
    item_quantity = 0

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.item_quantity * self.item_price:.2f}")

i = 0
j = int(input("Enter the number of items to purchase: "))
items = []
while i < j:
    item_name = input("Enter the item name: ")
    item_price = float(input("Enter the item price: "))
    item_quantity = int(input("Enter the item quantity: "))
    item = ItemToPurchase()
    item.item_name = item_name
    item.item_price = item_price
    item.item_quantity = item_quantity
    items.append(item)
    i += 1

for item in items:
    item.print_item_cost()

# Calculate total cost of items
total_cost = 0.0
for item in items:
    total_cost += item.item_quantity * item.item_price

print(f"Total: ${total_cost:.2f}")



