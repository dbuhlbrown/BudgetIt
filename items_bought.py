#Just a class to hold the items_bought data

class ItemsBought:

	def __init__(self):

		self.ID = 0
		self.item_name = ""
		self.category_name = ""
		self.price = ""
	
	def set_values(self, ID, item_name, category_name, price):

		self.ID = ID
		self.item_name = item_name
		self.category_name = category_name
		self.price = price

	def print_data(self):

		print "Item Name: " + self.item_name + " Category: " + self.category_name + " Price: " + str( self.price )

