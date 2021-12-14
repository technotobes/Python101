

def display_all_shopping_lists(shopping_lists):
    print("_____________________________________________________")
    print("Here are your current lists.")
    for index in range(0, len(shopping_lists)):
        shop_list = shopping_lists[index]
        print(f"{index + 1}. {shop_list.title}")
    print("_____________________________________________________")


def display_all_items(grocery_items):
    for index in range(0, len(list.grocery_items)):
        grocery_item = list.grocery_items[index]
        print(f"\n{index + 1}. {grocery_item.name}")  


# def display_specific_list(shopping_lists, list_choice):
#     for index in range(0, len(shopping_lists)):
#         list = shopping_lists[list_choice - 1]
#     print(f"Shopping List for {list.title}")
