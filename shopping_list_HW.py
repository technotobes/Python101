
from GroceryApp_classes import ShoppingList
from GroceryApp_classes import GroceryItem
from utils import display_all_shopping_lists
# from utils import display_all_items


# Shopping List (Obj) that are made from Shopping List Class
shopping_lists = []


def display_all_items():
    for index in range(0, len(shopping_lists)):
        list = shopping_lists[list_choice - 1]
        print(f"Shopping List for {list.title}")
        if len(list.grocery_items) == 0:
            print("(no items)") 
    for index in range(0, len(list.grocery_items)):
        grocery_item = list.grocery_items[index]
        print(f"\n{index + 1}. {grocery_item.name}")  


while True:
    print("_____________________________________________________")
    print("")
    print("Enter '1' to create a shopping list")
    print("Enter '2' to add an item to a shopping list")
    print("Enter '3' to display current lists and items")
    print("Enter '4' to delete a list")
    print("Enter '5' to delete an item from a list")
    print("Enter 'q' to quit")
    print("_____________________________________________________")
    user_input = input("Enter command: ")

    try:

            # Creating a new list/store(obj)
        if user_input == "1":
            user_input_list_title = input("Enter the name of store: ")
            user_input_list_address = input("Enter address of store: ")
            shopping_list = ShoppingList(user_input_list_title, user_input_list_address)    # User input will create object of shopping list, and object will be appended to array (shopping_lists)
            shopping_lists.append(shopping_list)

        # Adding an item to a list/store, after user chooses which list to add to
        elif user_input == "2":
            display_all_shopping_lists(shopping_lists)
            user_input_index = int(input("Enter the index of list to add items to: "))      
            shop_choice = shopping_lists[user_input_index - 1]                              
            user_input_grocery_item = input("Enter item name: ")
            user_input_grocery_price = float(input("Enter price of item: "))
            user_input_grocery_quantity = input("Enter quanitity of item: ")
            item = GroceryItem(user_input_grocery_item, user_input_grocery_price, user_input_grocery_quantity)
            shop_choice.add_item(item)

        # Display Stores and items
        elif user_input == "3":     
            display_all_shopping_lists(shopping_lists)

            # User chooses which list before items are displayed
            list_choice = int(input("Enter the index of list to view items: "))
            print("")
            print("_____________________________________________________")
            display_all_items()    

        # Deleting a store/list(obj) from shopping_lists array
        elif user_input == "4":     
            display_all_shopping_lists(shopping_lists)
            store_choice = int(input("Enter the index of list you wish to delete: "))
            del shopping_lists[store_choice - 1]
            

        # Deleting an item from a particular store/list(obj)
        elif user_input == "5":
            display_all_shopping_lists(shopping_lists)
            list_choice = int(input("Enter the index of the list you wish to modify: ")) # Generates a value error if input is a letter
            print("")
            print("_____________________________________________________")
            display_all_items()
            item_choice = int(input("Enter the index of what item you would like to delete: "))
            list.remove_item(item_choice - 1)

        else:
            break

    except:
        print("Please enter a valid choice.")

