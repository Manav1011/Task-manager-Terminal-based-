from init import *
from prettytable import PrettyTable
import sys

# Create a new table object
table = PrettyTable()

table.field_names = ["id", "title", "description", "date","status"]

try:
    arg = sys.argv[1]
except Exception as e:
    arg = False
cursor = None
if arg and type(arg) == str:    
    if arg == 'completed':
        cursor = conn.execute("SELECT * FROM tasks where date=DATE(CURRENT_TIMESTAMP) and status='completed'")
    elif arg == 'kalna':
        cursor = conn.execute("SELECT * FROM tasks where date=date('now', '-1 day')")
    elif arg == 'paramdivas':
        cursor = conn.execute("SELECT * FROM tasks where date=date('now', '-2 day')")
    elif arg == 'date':
        print("Use yyyy-mm-dd format")
        date = input("Enter the date: ")
        cursor = conn.execute("SELECT * FROM tasks where date=?",(date,))
    else:
        print("Provide a valid argument")
        sys.exit()
else:
    cursor = conn.execute("SELECT * FROM tasks where date=DATE(CURRENT_TIMESTAMP) and status='pending'")

rows = cursor.fetchall()
if rows is not None and len(rows) > 0:
    for row in rows:
        table.add_row([row[0], row[1].replace('\n','') if len(row[1]) < 40 else row[1][:40]+'...'.replace('\n',''), row[2].replace('\n','') if len(row[2]) < 40 else row[2][:40]+'...'.replace('\n',''), row[3],row[4]])
    print()
    print(table)
else:
    print("No Records Found")
