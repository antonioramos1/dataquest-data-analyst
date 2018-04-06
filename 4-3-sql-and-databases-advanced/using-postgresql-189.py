## 3. Psycopg2 ##

import psycopg2

con = psycopg2.connect('dbname=dq user=dq')
cur = con.cursor()
print(cur)
con.close()

## 4. Creating a table ##

import psycopg2

con = psycopg2.connect('dbname=dq user=dq')
cur = con.cursor()
query= '''CREATE TABLE notes
            (
            id INTEGER PRIMARY KEY,
            body TEXT,
            title TEXT
        );'''
cur.execute(query)
con.close()

## 5. SQL Transactions ##

import psycopg2

con = psycopg2.connect('dbname=dq user=dq')
cur = con.cursor()
query = '''
        CREATE TABLE notes(
        id INTEGER PRIMARY KEY,
        body TEXT,
        title TEXT
        )'''
cur.execute(query)
con.commit()
con.close()


## 6. Autocommitting ##

con = psycopg2.connect('dbname=dq user=dq')
con.autocommit = True
cursor = con.cursor()
query='''CREATE TABLE facts
        (
         id INTEGER PRIMARY KEY,
         country TEXT,
         value INTEGER);'''
cursor.execute(query)
con.close()

## 7. Executing queries ##

con = psycopg2.connect('dbname=dq user=dq')
cur = con.cursor()
query = '''INSERT INTO notes
            VALUES (1, 'Do more missions on Dataquest.', 'Dataquest reminder');'''
cur.execute(query)
cur.execute('SELECT * FROM notes')
rows = cur.fetchall()
print(rows)
con.close()



## 8. Creating a database ##

con = psycopg2.connect('dbname=dq user=dq')
con.autocommit = True
cur = con.cursor()
query='CREATE DATABASE income OWNER dq;'
cur.execute(query)
con.close()

## 9. Deleting a database ##

con = psycopg2.connect('dbname=dq user=dq')
con.autocommit = True
cur = con.cursor()
cur.execute('DROP DATABASE income;')
con.close()