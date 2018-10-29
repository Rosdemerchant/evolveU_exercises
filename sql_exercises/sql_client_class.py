import psycopg2

class SqlClient:
	

	def __init__(self, id, name, email, city, birth_year, credits=None):
		self.id = id
		self.name = name
		self.email = email
		self.city = city
		self.birth_year = birth_year
		self.credits = credits

	@staticmethod
	def client_sql_queries(sql):
		allClients=[]
		conn = psycopg2.connect('dbname=evolveu')
		cur = conn.cursor()
		cur.execute(sql)

		rows = cur.fetchall()
		for row in rows:
			allClients.append(SqlClient(row[0], row[1], row[2], row[3], row[4], row[5]))

		cur.close()
		conn.close()

		return allClients
	
	@staticmethod
	def credit_sql_queries_two(sql):
		allCredits=[]
		conn = psycopg2.connect('dbname=evolveu')
		cur = conn.cursor()
		cur.execute(sql)

		rows = cur.fetchall()
		for row in rows:
			allCredits.append(SqlClient(row[0], row[1], row[2], row[3], row[4], row[5]))

		cur.close()
		conn.close()

		return allCredits

	@staticmethod
	def show_clients():
		return SqlClient.client_sql_queries("""SELECT *, null from clients""")	
	
	@staticmethod
	def return_allclient():
		return SqlClient.allClients

	@staticmethod
	def show_clients_per_month(month):
		return SqlClient.client_sql_queries("""SELECT clients.*,credits.credits from clients join credits on clients.client_id = credits.client_id where credits.month = '2018-07' """)

	@staticmethod
	def return_allclient():
		return SqlClient.allCredits

	@staticmethod
	def show_clients_no_credits(month):
		allcredits=[]
		return SqlClient.credit_sql_queries_two("""SELECT credits.*, null  from clients right join credits on clients.client_id = credits.client_id where clients.client_id is null;""")

