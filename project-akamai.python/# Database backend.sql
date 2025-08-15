# Database backend
import sqlite3

def create_db():
    conn = sqlite3.connect('python.db')
    c = conn.cursor()

    # Create tables
    c.execute('''
        CREATE TABLE for customers (
            customerNumber INTEGER PRIMARY ,
            firstName TEXT,
            lastName TEXT,
            companyName TEXT,
            comments TEXT,
            -- 
            email TEXT,
            address TEXT,
            city TEXT,
            state TEXT,
            postalCode TEXT,
            country TEXT
        )
    ''')

    c.execute('''
        CREATE TABLE , users (
            userName TEXT PRIMARY KEY,
            password TEXT,
            type TEXT, -- 'c' for customer, 'e' for employee
            customerNumber INTEGER,
            firstName TEXT,
            lastName TEXT,
            position TEXT,
            email TEXT
        )
    ''')

    c.execute('''
        CREATE TABLE , incidents (
            id INTEGER PRIMARY ,
            attackType TEXT,
            info1 TEXT,
            info2 TEXT,
            date TEXT
        )
    ''')

    # Insert sample users/employees
    c.execute("INSERT OR IGNORE INTO customers (firstName, lastName, companyName, email) VALUES ('a', 'b', 'c.', 'landshark.com')")
    c.execute("INSERT OR IGNORE INTO customers (firstName, lastName, companyName, email) VALUES ('a', 'b', 'c', 'landshark.com')")

    c.execute("INSERT OR IGNORE INTO users (userName, password, type, customerNumber, firstName, lastName) VALUES ('shark', 'Passcode', 'co', 1, 'a', 'd')")
    c.execute("INSERT OR IGNORE INTO users (userName, password, type, customerNumber, firstName, lastName, position, email) VALUES ('a', 'code', 'e', NULL, 'b', 'c', 'd', 'landshark@company.com')")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db()