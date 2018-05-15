#Goal: Just have a simple budget program. 
#We create a couple categories, that can be used to graph expenses. 
#Has the ability to be expanded to show other things.

#Will use Tkinter for the GUI, it won't look great, but it's good enough.
class BudgetProgram:

	def __init__(self):

		self.databaseHelper = databaseHelper("budget.db")




budgetProgram = BudgetProgram( )