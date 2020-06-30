import sqlite3 as sql

#aqui = "./A_Login/"
	
connection = sql.connect('database.db')
c = connection.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS logins(
	id integer primary key autoincrement,
	login varchar(255) not null unique,
	username varchar(255) not null,
	senha varchar(32) not null,
	bio text,
	dinheiro int(255) DEFAULT 100
	)""")
