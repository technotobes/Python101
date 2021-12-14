

class ShoppingList:
    def __init__(self, title, address):                                     
        self.title = title
        self.address = address
        self.grocery_items = []

    def add_item(self, item):
        self.grocery_items.append(item)

    def remove_item(self, item_index_to_remove):
        if item_index_to_remove >= 0 and item_index_to_remove < len(self.grocery_items):
            del self.grocery_items[item_index_to_remove]
        else:
            print("Invalid Index")

class GroceryItem: 
  def __init__(self, name, price, quanitity): 
    self.name = name
    self.price = price
    self.quantity = quanitity 