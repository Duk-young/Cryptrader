# Dukyoung Eom dukyoung.eom@stonybrook.edu
import os
import sqlite3

print(os.path.abspath(os.path.dirname(__file__)))

conn = sqlite3.connect('deomps5.db')

cur = conn.cursor()

# Create tables
cur.execute('''DROP TABLE IF EXISTS Products''')
cur.execute('''CREATE TABLE Products
               (maker Text, model Integer UNIQUE, type Text, PRIMARY KEY (model))''')

cur.execute('''DROP TABLE IF EXISTS PCs''')
cur.execute('''CREATE TABLE PCs
               (model Integer UNIQUE, speed REAL, RAM Integer, hd Integer, price Integer, PRIMARY KEY (model), FOREIGN KEY (model) REFERENCES Products)''')

cur.execute('''DROP TABLE IF EXISTS Laptops''')
cur.execute('''CREATE TABLE Laptops
               (model Integer UNIQUE, speed REAL, RAM Integer, hd Integer,screen Integer, price Integer, PRIMARY KEY (model), FOREIGN KEY (model) REFERENCES Products)''')

cur.execute('''DROP TABLE IF EXISTS Printers''')
cur.execute('''CREATE TABLE Printers
               (model Integer UNIQUE, color Integer, type Text,price Integer,PRIMARY KEY (model), FOREIGN KEY (model) REFERENCES Products)''')

# Insert rows of data

# PC
cur.execute("INSERT INTO Products VALUES ('Samsung',1, 'PC')")
cur.execute("INSERT INTO Products VALUES ('Samsung',2, 'PC')")
cur.execute("INSERT INTO Products VALUES ('Samsung',3, 'PC')")
cur.execute("INSERT INTO Products VALUES ('LG',4, 'PC')")
cur.execute("INSERT INTO Products VALUES ('Samsung',5, 'PC')")
cur.execute("INSERT INTO Products VALUES ('MSI',6, 'PC')")
cur.execute("INSERT INTO Products VALUES ('Apple',7, 'PC')")
cur.execute("INSERT INTO Products VALUES ('Apple',8, 'PC')")
cur.execute("INSERT INTO Products VALUES ('Samsung',9, 'PC')")
cur.execute("INSERT INTO Products VALUES ('Apple',10, 'PC')")

#Laptop
cur.execute("INSERT INTO Products VALUES ('Samsung',11, 'Laptop')")
cur.execute("INSERT INTO Products VALUES ('Samsung',12, 'Laptop')")
cur.execute("INSERT INTO Products VALUES ('MSI',13, 'Laptop')")
cur.execute("INSERT INTO Products VALUES ('LG',14, 'Laptop')")
cur.execute("INSERT INTO Products VALUES ('Samsung',15, 'Laptop')")
cur.execute("INSERT INTO Products VALUES ('MSI',16, 'Laptop')")
cur.execute("INSERT INTO Products VALUES ('Apple',17, 'Laptop')")
cur.execute("INSERT INTO Products VALUES ('LG',18, 'Laptop')")
cur.execute("INSERT INTO Products VALUES ('Samsung',19, 'Laptop')")
cur.execute("INSERT INTO Products VALUES ('MSI',20, 'Laptop')")

#Printer
cur.execute("INSERT INTO Products VALUES ('Samsung',21, 'Printer')")
cur.execute("INSERT INTO Products VALUES ('Samsung',22, 'Printer')")
cur.execute("INSERT INTO Products VALUES ('LG',23, 'Printer')")
cur.execute("INSERT INTO Products VALUES ('LG',24, 'Printer')")
cur.execute("INSERT INTO Products VALUES ('Samsung',25, 'Printer')")
cur.execute("INSERT INTO Products VALUES ('MSI',26, 'Printer')")
cur.execute("INSERT INTO Products VALUES ('LG',27, 'Printer')")
cur.execute("INSERT INTO Products VALUES ('LG',28, 'Printer')")
cur.execute("INSERT INTO Products VALUES ('Samsung',29, 'Printer')")
cur.execute("INSERT INTO Products VALUES ('Apple',30, 'Printer')")

#PC Specs
cur.execute("INSERT INTO PCs VALUES (1, 3.6, 8, 1000, 950000)")
cur.execute("INSERT INTO PCs VALUES (2, 3.2, 4, 500, 800000)")
cur.execute("INSERT INTO PCs VALUES (3, 3.5, 4, 500, 850000)")
cur.execute("INSERT INTO PCs VALUES (4, 3.6, 8, 1000, 900000)")
cur.execute("INSERT INTO PCs VALUES (5, 2.7, 4, 500, 700000)")
cur.execute("INSERT INTO PCs VALUES (6, 2.8, 4, 500, 750000)")
cur.execute("INSERT INTO PCs VALUES (7, 3.0, 4, 500, 850000)")
cur.execute("INSERT INTO PCs VALUES (8, 3.2, 8, 250, 800000)")
cur.execute("INSERT INTO PCs VALUES (9, 2.5, 4, 500, 750000)")
cur.execute("INSERT INTO PCs VALUES (10, 3.7, 16, 1000, 1050000)")

#Laptop Spces
cur.execute("INSERT INTO Laptops VALUES (11, 2.9, 8, 500, 15.6, 1200000)")
cur.execute("INSERT INTO Laptops VALUES (12, 3.7, 16, 1000, 17.2, 1700000)")
cur.execute("INSERT INTO Laptops VALUES (13, 3.0, 8, 500, 15.6, 1300000)")
cur.execute("INSERT INTO Laptops VALUES (14, 2.5, 4, 500, 13.3, 800000)")
cur.execute("INSERT INTO Laptops VALUES (15, 3.2, 4, 500, 15.6, 1200000)")
cur.execute("INSERT INTO Laptops VALUES (16, 3.2, 16, 500, 17.2, 1500000)")
cur.execute("INSERT INTO Laptops VALUES (17, 2.9, 8, 500, 15.6, 1100000)")
cur.execute("INSERT INTO Laptops VALUES (18, 2.5, 4, 500, 13.3, 900000)")
cur.execute("INSERT INTO Laptops VALUES (19, 2.8, 8, 500, 15.6, 1050000)")
cur.execute("INSERT INTO Laptops VALUES (20, 2.6, 8, 500, 15.6, 1000000)")

#Printer Specs
cur.execute("INSERT INTO Printers VALUES (21, 0, 'laser', 300000)")
cur.execute("INSERT INTO Printers VALUES (22, 0, 'ink-jet', 250000)")
cur.execute("INSERT INTO Printers VALUES (23, 1, 'laser', 450000)")
cur.execute("INSERT INTO Printers VALUES (24, 0, 'ink-jet', 350000)")
cur.execute("INSERT INTO Printers VALUES (25, 1, 'laser', 400000)")
cur.execute("INSERT INTO Printers VALUES (26, 0, 'ink-jet', 270000)")
cur.execute("INSERT INTO Printers VALUES (27, 1, 'laser', 370000)")
cur.execute("INSERT INTO Printers VALUES (28, 0, 'ink-jet', 260000)")
cur.execute("INSERT INTO Printers VALUES (29, 1, 'laser', 300000)")
cur.execute("INSERT INTO Printers VALUES (30, 0, 'ink-jet', 280000)")

# Save (commit) the changes
conn.commit()

cur = conn.cursor()
#for row in cur.execute('SELECT * FROM roles ORDER BY id'):
#    print(row)

#for row in cur.execute('SELECT * FROM users ORDER BY id'):
#    print(row)

# To see what these names are
print(__file__)
print(__name__)

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()