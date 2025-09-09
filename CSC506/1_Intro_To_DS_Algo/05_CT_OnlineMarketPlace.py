# searching for a specific item in a large online marketplace database using a linear search algorithm
class ItemToPurchase:
    def __init__(self, name=None, price=None, quantity=None, description=None):
        self.name = name
        self.price = price
        self.description = description
    def __str__(self):
        return f"{self.name}'s Price : ${self.price}" 
    
class OnlineMarketPlace:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def search_item(self, item_name):
        for item in self.items: 
            if item.name == item_name: # LInear search performed here
                return item
        return None
# Main program to test the online marketplace search functionality.
if __name__ == '__main__':
    marketplace = OnlineMarketPlace()
    items = [
        ItemToPurchase("Laptop", 999.99, description="A high-performance laptop"),
        ItemToPurchase("Iphone", 499.99, description="A latest model smartphone"),
        ItemToPurchase("Headphone", 199.99, description="Noise-cancelling headphones")
    ]
    for item in items:
        marketplace.add_item(item)
    search_name = input("Enter the name of the item to search: ")
    found_item = marketplace.search_item(search_name)
    if found_item:
        print("Item found:")
        print(found_item)
    else:
        print("Item not found in the marketplace.")

