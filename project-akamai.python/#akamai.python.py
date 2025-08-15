#processing logs
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
                    cursor.execute(attack_type,i_1,i_2,i_3'''
                        
                    ''', (attack_type, info1, info2, date_str))
                    conn.commit()
                    conn.close()
            new_name = filename[:-4] + '.old'
            os.rename(os.path.join(logs_dir, filename), os.path.join(logs_dir, new_name))

if __name__ == '__main__':
    process_csv_files()