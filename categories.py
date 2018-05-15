#Just a class to hold the daily_spending values

class Categories:

	def __init__(self):

		self.ID = ""
		self.name = ""


	def set_values(self, ID, name):
		
		self.ID = ID
		self.name = name

	def print_data(self):

		print "Name: " + self.name
		 