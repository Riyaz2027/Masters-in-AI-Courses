class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0.0, quantity=0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self, customer_name="none", date="January 1, 2020"):
        self.customer_name = customer_name
        self.date = date
        self.cart_items = []
    
    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)
        print(f"Item '{ItemToPurchase.name}' added to cart.")

    def remove_item(self, item):
        for cart_item in self.cart_items:
            if cart_item.name == item.name:
                self.cart_items.remove(cart_item)
                print(f"{item.name} has been removed from your cart.")
                return
        print(f"{item.name} not found in cart. Nothing removed.")
    
    def modify_item(self, ItemToPurchase):
        for item in self.cart_items:
            if item.name == ItemToPurchase.name:
                if ItemToPurchase.description is not None:
                    item.description = ItemToPurchase.description
                if ItemToPurchase.price is not None:
                    item.price = ItemToPurchase.price
                if ItemToPurchase.quantity is not None:
                    item.quantity = ItemToPurchase.quantity
                print(f"Item '{ItemToPurchase.name}' has been modified.")
                return
        print(f"{ItemToPurchase.name} not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = sum(item.quantity for item in self.cart_items)
        return total_quantity
    
    def get_cost_of_cart(self):
        total_cost = sum(item.price * item.quantity for item in self.cart_items)
        return total_cost
    
    def print_total(self):
        print("OUTPUT SHOPPING CART")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}\n")
            for item in self.cart_items:
                if hasattr(item, 'name') and hasattr(item, 'quantity') and hasattr(item, 'price'):
                    total_price = item.price * item.quantity
                    print(f"{item.name} {item.quantity} @ ${item.price} = ${total_price}")
            print(f"\nTotal: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print(f"{self.customer_name}'s Shopping Cart - {self.date}\n")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.name}: {item.description}")

def print_menu():
    menu = (
        "\nMENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
    )
    print(menu)

if __name__ == "__main__":
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")
    cart = ShoppingCart(customer_name, current_date)
    while True:
        print_menu()
        choice = input("Choose an option:\n")
        if choice == 'a':
            print("ADD ITEM TO CART")
            item_name = input("Enter the item name:\n")
            item_description = input("Enter the item description:\n")
            item_price = float(input("Enter the item price:\n"))
            item_quantity = int(input("Enter the item quantity:\n"))
            item = ItemToPurchase(item_name, item_description, item_price, item_quantity)
            cart.add_item(item)
        elif choice == 'r':
            print("REMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove:\n")
            item = ItemToPurchase(name=item_name)
            cart.remove_item(item)
        elif choice == 'c':
            print("CHANGE ITEM QUANTITY")
            item_name = input("Enter the item name:\n")
            new_description = input("Enter the new item description (or leave blank to keep unchanged):\n")
            new_price_input = input("Enter the new price (or leave blank to keep unchanged):\n")
            new_quantity_input = input("Enter the new quantity (or leave blank to keep unchanged):\n")

            # Handle optional description, price, and quantity
            item_description = new_description if new_description.strip() != "" else None
            item_price = float(new_price_input) if new_price_input.strip() != "" else None
            item_quantity = int(new_quantity_input) if new_quantity_input.strip() != "" else None
            updated_item = ItemToPurchase(item_name, item_description, item_price, item_quantity)
            cart.modify_item(updated_item)
        elif choice == 'i':
            cart.print_descriptions()
        elif choice == 'o':
            cart.print_total()
        elif choice == 'q':
            break
        else:
            print("Invalid option. Please try again.")