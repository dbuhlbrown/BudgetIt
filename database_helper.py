import sqlite3
from sqlite3 import Error

class DatabaseHelper:

	connection = 0
	TABLE_NAMES = ["Categories","DailySpending","ItemsBought"]

	def __init__(self, file_name):

		print ("main")
		self.connection = self.create_connection(file_name)

	def create_connection(self, db_file):

		#Needs to discuss try, catch blocks.
		try:

			conn = sqlite3.connect(db_file)
			return conn

		except Error as e:
			print(e)

	#Make general return function
	def return_data( self, table_name):

		return self.execute_statement("SELECT * FROM '%s' " % table_name)

	def execute_statement(self, statement):

		cur = self.connection.cursor( )
	
		cur.execute(statement)

		rows = cur.fetchall()
		
		self.connection.commit( )


		return rows	

	#Return orders per customer id
	#def return_orders_for_customer(self, customer_ID):

	#	return self.execute_statement( "SELECT * FROM 'Order' WHERE customer_ID = %s" % customer_ID )


	#def return_total_raw_price( self ):

	#	return self.execute_statement("SELECT SUM(raw_cost) FROM 'Order'")


	#def insert_customer(self, customer):

	#	return self.execute_statement("INSERT INTO Customer (first_name, last_name, shipping_address, billing_address) VALUES ('%s','%s','%s','%s' );" % (customer.first_name, customer.last_name, customer.shipping_address, customer.billing_address) )