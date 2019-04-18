from typing import List, Dict
from flask import Flask, flash, render_template, redirect, url_for, request, session
import mysql.connector
import json
from database import Database

config = {
		'user': 'root',
		'password': 'root',
		'host': 'db',
		'port': '3306',
		'database': 'school'
	}

app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = Database()


@app.route('/')
def index():
	data = db.read(None)
	return render_template('index.html', data = data)

@app.route('/add/')
def add():
	return render_template('add.html')

@app.route('/addstudent', methods = ['POST', 'GET'])
def addstudent():
	if request.method == 'POST' and request.form['save']:
		if db.insert(request.form):
			flash("A new student has been added!")
		else:
			flash("A new student can not be added!")
			
		return redirect(url_for('index'))
	else:
		return redirect(url_for('index'))


@app.route('/update/<int:id>/')
def update(id):
	data = db.read(id);
	
	if len(data) == 0:
		return redirect(url_for('index'))
	else:
		session['update'] = id
		return render_template('update.html', data = data)

@app.route('/updatestudent', methods = ['POST'])
def updatestudent():
	if request.method == 'POST' and request.form['update']:
		
		if db.update(session['update'], request.form):
			flash('A student has been updated!')
		   
		else:
			flash('The student can not be updated!')
		
		session.pop('update', None)
		
		return redirect(url_for('index'))
	else:
		return redirect(url_for('index'))
	
@app.route('/delete/<int:id>/')
def delete(id):
	data = db.read(id);
	
	if len(data) == 0:
		return redirect(url_for('index'))
	else:
		session['delete'] = id
		return render_template('delete.html', data = data)

@app.route('/deletestudent', methods = ['POST'])
def deletestudent():
	if request.method == 'POST' and request.form['delete']:
		
		if db.delete(session['delete']):
			flash('A student has been deleted')
		   
		else:
			flash('The student can not be deleted')
		
		session.pop('delete', None)
		
		return redirect(url_for('index'))
	else:
		return redirect(url_for('index'))


if __name__ == '__main__':
	app.run(host='0.0.0.0')
