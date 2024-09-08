class Restaurant:  #declaring a class
    def __init__(self, restaurant_name, cuisine_type):
        """ Initialise Attributes to describe a restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self): # this is 'method'. It's a function within a class
        print(f"\n The name of the restaurant is {self.restaurant_name}")
        print(f"\n The name of the cuisine is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"\n {self.restaurant_name} is open for business")

name = Restaurant('SeaFood Eaters', 'Crabs &  Prawns') # this is an instance or 'Object'
name.describe_restaurant()
name.open_restaurant()

