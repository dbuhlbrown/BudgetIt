#Just a class to hold the daily_spending values

class DailySpending:

	def __init__(self):

		self.ID = 0
		self.date = ""
		self.total_spent = 0
		self.day_of_the_week = 0
		self.worked = False

	def set_values(self, ID, date, total_spent, day_of_the_week, worked):

		self.ID = ID
		self.date = date
		self.total_spent = total_spent
		self.day_of_the_week = day_of_the_week
		self.worked = worked

	def print_data(self):

		print "Date: " + self.date + " Total Spent: " + str( self.total_spent ) + " Day of the week: " + self.day_of_the_week + " Worked: " + str(self.worked)
