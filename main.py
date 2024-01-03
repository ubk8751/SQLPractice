import sqlite3

conn = sqlite3.connect(':memory:')

conn.execute('''CREATE TABLE Cars (
               CarNumber INTEGER PRIMARY KEY,
               Brand TEXT,
               Model TEXT,
               Color TEXT,
               PricePerDay INTEGER
           )''')

conn.execute('''CREATE TABLE Customers (
               CustomerNumber INTEGER PRIMARY KEY,
               Name TEXT,
               BirthDate DATE
           )''')

conn.execute('''CREATE TABLE Bookings (
               CustomerNumber INTEGER,
               CarNumber INTEGER,
               StartDate DATE,
               EndDate DATE
           )''')

cars_data = [
    (1, 'Peugeot', '208', 'Blue', 800),
    (2, 'Peugeot', '3008', 'Green', 700),
    (3, 'Volkswagen', 'Polo', 'Red', 600),
    (4, 'Volvo', 'V70', 'Silver', 1200),
    (5, 'Tesla', 'X', 'Black', 2000),
    (6, 'SAAB', '9-5', 'Green', 850),
    (7, 'Volvo', 'V40', 'Red', 900),
    (8, 'Fiat', '500', 'Black', 1050),
    (9, 'Volvo', 'V40', 'Green', 850),
    (10, 'Fiat', '500', 'Red', 950),
    (11, 'Volkswagen', 'Polo', 'Blue', 700),
    (12, 'BMW', 'M3', 'Black', 1599),
    (13, 'Volkswagen', 'Golf', 'Red', 1500)
]

bookings_data = [
    (6, 1, '2018-01-02', '2018-01-15'),
    (1, 1, '2018-01-03', '2018-01-05'),
    (3, 3, '2018-01-03', '2018-01-04'),
    (8, 5, '2018-01-04', '2018-01-30'),
    (10, 6, '2018-01-10', '2018-01-13'),
    (1, 1, '2018-01-20', '2018-01-25'),
    (13, 2, '2018-01-21', '2018-01-30'),
    (6, 3, '2018-01-22', '2018-01-30'),
    (2, 1, '2018-01-29', '2018-02-01'),
    (5, 2, '2018-02-02', '2018-02-06'),
    (1, 6, '2018-02-20', '2018-02-25'),
    (6, 7, '2018-02-21', '2018-02-24'),
    (3, 8, '2018-02-21', '2018-02-28'),
    (3, 10, '2018-02-22', '2018-02-26'),
    (12, 9, '2018-02-22', '2018-02-28'),
    (13, 10, '2018-03-01', '2018-03-10'),
    (1, 11, '2018-03-04', '2018-03-09'),
    (3, 10, '2018-03-11', '2018-03-14'),
    (6, 8, '2018-03-14', '2018-03-17'),
    (5, 9, '2018-03-14', '2018-03-30'),
    (12, 7, '2018-03-18', '2018-03-20'),
    (8, 6, '2018-03-18', '2018-04-02')
]

customers_data = [
    (1, 'Alice Andersson', '1990-05-05'),
    (2, 'Oscar Johansson', '1975-08-10'),
    (3, 'Nora Hansen', '1981-10-27'),
    (4, 'William Johansen', '2000-01-17'),
    (5, 'Lucía García', '1987-12-13'),
    (6, 'Hugo Fernández', '1950-03-16'),
    (7, 'Sofia Rossi', '1995-08-04'),
    (8, 'Francesco Russo', '2000-02-26'),
    (9, 'Olivia Smith', '1972-05-23'),
    (10, 'Oliver Jones', '1964-05-08'),
    (11, 'Shaimaa Elhawary', '1999-12-23'),
    (12, 'Mohamed Elshabrawy', '1997-11-07'),
    (13, 'Jing Wong', '1947-07-15'),
    (14, 'Wei Lee', '1962-09-29'),
    (15, 'Aadya Singh', '1973-01-01'),
    (16, 'Aarav Kumar', '1986-06-28'),
    (17, 'Louise Martin', '1994-04-22'),
    (18, 'Gabriel Bernard', '1969-12-01'),
    (19, 'Emma Smith', '1971-03-18'),
    (20, 'Noah Johnson', '1800-12-16'),
    (21, 'Alice Silva', '1988-12-04'),
    (22, 'Miguel Santos', '1939-12-29')
]

conn.executemany("INSERT INTO Cars (CarNumber, Brand, Model, Color, PricePerDay) VALUES (?, ?, ?, ?, ?)", cars_data)
conn.executemany("INSERT INTO Customers (CustomerNumber, Name, BirthDate) VALUES (?, ?, ?)", customers_data)
conn.executemany("INSERT INTO Bookings (CustomerNumber, CarNumber, StartDate, EndDate) VALUES (?, ?, ?, ?)", bookings_data)

conn.commit()

conn.close()
