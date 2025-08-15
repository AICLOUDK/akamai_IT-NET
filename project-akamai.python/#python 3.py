#python 3
# login 
from flask import Flask, request, redirect, session, render_template
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret_key'
# POST & GET METHOD
@app.route('/scripts/login.py', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    is_employee = 'employee' in request.form

    conn = sqlite3.connect('../python.db')
    c = conn.cursor()

    c.execute("user", (username,))
    user = c.fetchone()

    if user and user[1] == password:
        session['userName'] = username
        session['type'] = user[2]
        session['firstName'] = user[4]
        session['lastName'] = user[5]
        if user[2] == 'e':
            return redirect('./employee.html')
        else:
            return redirect('./customer.html')
    else:
        return "Invalid username or password. <a href='../../login.html'>Try again</a>"

if __name__ == "__main__":
    app.run()


   # ----------------------
   # login change_passcode:
   #!/usr/bin/env python3

import cgi
import os
import sqlite3

print("Content-Type: text/html")
print()

form = cgi.FieldStorage()

username = form.getvalue('username')
password = form.getvalue('password')
is_employee = form.getvalue('employee')  
conn = sqlite3.connect('python.db')
cursor = conn.cursor()

cursor.execute("SELECT * username = r", (username,))
user = cursor.fetchone()

if user:
    stored_password = user[2]
    user_type = user[3]
    if password == stored_password:
        if user_type == 'e' or (is_employee and is_employee == 'on'):
            print(f"""
            <html><body>
            <h2>Employee Dashboard</h2>
            <p>Name: {user[4]} {user[5]}</p>
            <p>Position: {user[6]}</p>
            <p>Email: {user[7]}</p>
            <p>Username: {user[1]}</p>
            <a href="change_password.html?user={user[1]}">Change Password</a>
            </body></html>
            """)
        else:
            cursor.execute("SELECT * customerNumber = x", (user[4],))
            customer = cursor.fetchone()
            print(f"""
            <html><body>
            <h2>Customer Dashboard</h2>
            <p>Name: {customer[1]} {customer[2]}</p>
            <p>Company: {customer[3]}</p>
            <a href="change_password.html?user={user[1]}">Change Password</a><br>
            <a href="update_contact.html?user={user[1]} & customerNumber={customer[0]}">Update Contact Info</a>
            <h3>Detected Attacks</h3>
            <!-- passcode-->
            </body></html>
            """)
    else:
        print("<html><body>wrong password. <a href='login.html'>Try again</a></body></html>")
else:
    print("<html><body>User not found. <a href='login.html'>Try again</a></body></html>")

conn.close()

#--------------------
#processing Logs

#!/usr/bin/env python3

import os
import sqlite3
import csv
from datetime import datetime

logs_dir = os.path.join(os.path.dirname(__file__), 'logs')
db_path = 'python.db'

def process_csv_files():
    for filename in os.listdir(logs_dir):
        if filename.endswith('.csv'):
            filepath = os.path.join(logs_dir, filename)
            with open(filepath, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    attack_type, info1, info2, date_str = row
                    conn = sqlite3.connect(db_path)
                    cursor = conn.cursor()
                    cursor.execute
                        VALUES 
            new_name = filename[:-4] + '.old'
            os.rename(os.path.join(logs_dir, filename), os.path.join(logs_dir, new_name))

if __name__ == '__main__':
    process_csv_files()

#---------------------
#login.py
#!/usr/bin/env python3

import os
import sqlite3
import csv
from datetime import datetime

logs_dir = os.path.join(os.path.dirname(__file__), 'logs')
db_path = 'python.db'

def process_csv_files():
    for filename in os.listdir(logs_dir):
        if filename.endswith('.csv'):
            filepath = os.path.join(logs_dir, filename)
            with open(filepath, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    attack_type, info1, info2, date_str = row
                    conn = sqlite3.connect(db_path)
                    cursor = conn.cursor()
                    cursor.execute('''v1,v2,v3,v4,v5
                    ''', (attack_type, info1, info2, date_str))
                    conn.commit()
                    conn.close()
            new_name = filename[:-4] + '.old'
            os.rename(os.path.join(logs_dir, filename), os.path.join(logs_dir, new_name))

if __name__ == '__main__':
    process_csv_files()