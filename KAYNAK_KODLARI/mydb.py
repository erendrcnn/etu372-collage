# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'school_management_system',
	passwd = 'password'

	)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database

print("All Done!")