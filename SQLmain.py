import sqlite3

from constants import data, tables
from dbtools import create_table, insert_into_table

conn = sqlite3.connect(':memory:')

for table in tables:
    create_table(conn, table, data[table]["struct"])
    insert_into_table(conn, table, data[table]["struct"].keys(), data[table]["data"])

query = '''
SELECT Customers.CustomerNumber, Customers.Name, Bookings.CarNumber, Bookings.StartDate, Bookings.EndDate 
FROM Customers
INNER JOIN Bookings ON Customers.CustomerNumber = Bookings.CustomerNumber;
'''

# Run queries here
cursor = conn.execute(query)
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.commit()

conn.close()
