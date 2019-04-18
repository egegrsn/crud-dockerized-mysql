from typing import List, Dict
from flask import Flask, render_template
import mysql.connector
import json

config = {
		'user': 'root',
		'password': 'root',
		'host': 'db',
		'port': '3306',
		'database': 'school'
	}

class Database:
	def connect(self):
		connection = mysql.connector.connect(**config)
		return connection
	
	def read(self, id):
		con = Database.connect(self)
		cursor = con.cursor()
		try: 
			if id == None:
				cursor.execute("SELECT * FROM students order by name asc")
			else: 
				cursor.execute("SELECT * FROM students where id = %s order by name asc", (id,))

			return cursor.fetchall()
		except:
			return ()
		finally:
			con.close()

	def insert(self,data):
		con = Database.connect(self)
		cursor = con.cursor()
		
		try:
			cursor.execute("INSERT INTO students(id,name,department) VALUES(NULL, %s, %s)", (data['name'],data['department'],))
			con.commit()
			
			return True
		except:
			con.rollback()
			
			return False
		finally:
			con.close()
			
	def update(self, id, data):
		con = Database.connect(self)
		cursor = con.cursor()
		
		try:
			cursor.execute("UPDATE students set name = %s, department = %s where id = %s", (data['name'],data['department'],id,))
			con.commit()
			
			return True
		except:
			con.rollback()
			
			return False
		finally:
			con.close()
		
	def delete(self, id):
		con = Database.connect(self)
		cursor = con.cursor()
		
		try:
			cursor.execute("DELETE FROM students where id = %s", (id,))
			con.commit()
			
			return True
		except:
			con.rollback()
			
			return False
		finally:
			con.close()
