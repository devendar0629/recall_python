import sqlite3

# python sqlite3 sample

# connect to database
conn = sqlite3.connect('sample.db')

# create a cursor
# explanation: A cursor is a control structure that enables traversal over the records in a database. This can be used to retrieve data from a database.
cursor = conn.cursor()

