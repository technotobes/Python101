import unittest

shopping_lists = []

class GroceryItem: 
  def __init__(self, name): 
    self.name = name



class TestShoppingList(unittest.TestCase):

    def setUp(self):
        self.grocery_items = []
        self.grocery_items.append(GroceryItem("eggs"))
        self.grocery_items.append(GroceryItem("milk"))
        self.grocery_items.append(GroceryItem("eggs"))

        
        
    # Test to add the same item to an existing list
    def test_adding_the_same_item(self):
        if 2 in set([self.grocery_items.count(n) for n in self.grocery_items]):
            self.assertTrue()


unittest.main()