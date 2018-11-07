
from flask import Flask, render_template
import sql_client_class
import psycopg2
import json

app = Flask(__name__)

@app.route('/client/<id>')
def client(id):
	client = sql_client_class.SqlClient.getClient(id)
	return json.dumps({'client_id':client[0][0], 'name':client[0][1], 'email':client[0][2], 'city':client[0][3]})

@app.route('/allclients')
def get_all_clients():

	return render_template("allclients.html",
		allclients=sql_client_class.SqlClient.show_clients())

@app.route('/clientmonth')
def client_month():

	return render_template("allclients.html", 
		allclients=sql_client_class.SqlClient.show_clients_per_month('2018-07'))

@app.route('/clientsnocredits')
def clients_credits():

	return render_template("allclients.html", 
		allclients=sql_client_class.SqlClient.show_clients_no_credits('2018-07'))

@app.route('/creditsnoclients')
def credits_noclients():

	return render_template("allclients.html", 
		allclients=sql_client_class.SqlClient.show_clients_no_credits('2018-07'))

if __name__ =='__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)