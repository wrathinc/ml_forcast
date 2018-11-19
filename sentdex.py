import MySQLdb
import pandas as pd 
import time
conn = MySQLdb.connect("localhost","root", "root", "dbname")

c = conn.cursor()
c.execute("SELECT * FROM twit ")

rows = c.fetchall()

#df = pd.read_sql('SELECT * FROM twit ', conn)

for row in rows:
	print row
