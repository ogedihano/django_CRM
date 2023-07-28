import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password'

)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE femi_crm_app")

print("All Done!")

$ git config --global user.name "Your Name"
$ git config --global user.email "you@youraddress.com"
$ git config --global push.default matching
$ git config --global alias.co checkout
$ git init