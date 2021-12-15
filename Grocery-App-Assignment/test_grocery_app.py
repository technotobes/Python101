import unittest
from grocery_app_classes import ShoppingList
from grocery_app_classes import GroceryItem




class TestShoppingList(unittest.TestCase):

    def setUp(self):
        self.shopping_list = ShoppingList("Walmart", "123 st")
        self.grocery_items = []
        self.grocery_items.append(GroceryItem("eggs", 1, 1))
        self.grocery_items.append(GroceryItem("milk", 1, 1))

                
    # Test to add the same item to an existing list
    def test_adding_the_same_item(self):
        self.shopping_list.add_item((GroceryItem("eggs", 1, 1)))
        print(self.grocery_items)
        self.assertEqual(["eggs", "milk", "eggs"], self.grocery_items)
        
            
    


unittest.main()

