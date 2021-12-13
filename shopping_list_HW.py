
shopping_lists = []


class GroceryItem: 
  def __init__(self, name, price, quanitity): 
    self.name = name
    self.price = price
    self.quantity = quanitity 

class ShoppingList:
    def __init__(self, title, address):
        self.title = title
        self.address = address
        self.grocery_items = []

    def add_item(self, item):
        self.grocery_items.append(item)

    def add_item_diff_list(self, to_list, item):
        to_list.add_item(item)


def display_all_shopping_lists():
    print("Here are your current lists.")
    for index in range(0, len(shopping_lists)):
        shop_list = shopping_lists[index]
        print(f"{index + 1}. {shop_list.title}")


while True:
    print("Enter '1' to create a shopping list\nEnter '2' to add an item to a shopping list\nEnter '3' to display current lists and items\nEnter 'q' to quit")
    user_input = input("Enter command: ")
    if user_input == "1":
        user_input_list_title = input("Enter the name of store: ")
        user_input_list_address = input("Enter address of store: ")
        shopping_list = ShoppingList(user_input_list_title, user_input_list_address)
        shopping_lists.append(shopping_list)
    elif user_input == "2":
        display_all_shopping_lists()
        user_input_diff_title = int(input("Enter the index of list to add items to: "))
        for index in range(0, len(shopping_lists)):
            shop_choice = shopping_lists[user_input_diff_title - 1]
        user_input_grocery_item = input("Enter item name: ")
        user_input_grocery_price = input("Enter price of item: ")
        user_input_grocery_quantity = input("Enter quanitity of item: ")
        item = GroceryItem(user_input_grocery_item, user_input_grocery_price, user_input_grocery_quantity)
        shop_choice.add_item(item)
    elif user_input == "3":
        display_all_shopping_lists()
        list_choice = int(input("Enter the index of list to view items: "))
        for index in range(0, len(shopping_lists)):
            list = shopping_lists[list_choice - 1]
            list_name = list.title[index]
        for index in range(0, len(list.grocery_items)):
            grocery_item = list.grocery_items[index]
            print(f"\n\nShopping List for {list.title}\n{index + 1}. {grocery_item.name}\n\n")
    else:
        break


