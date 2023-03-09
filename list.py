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

if arg and type(arg) == str:    
    if arg == 'completed':
        cursor = conn.execute("SELECT * FROM tasks where date=DATE(CURRENT_TIMESTAMP) and status='completed'")        
else:
    cursor = conn.execute("SELECT * FROM tasks where date=DATE(CURRENT_TIMESTAMP) and status='pending'")
for row in cursor:
    table.add_row([row[0], row[1] if len(row[1]) < 20 else row[1][:20]+'...', row[2] if len(row[2]) < 20 else row[2][:20]+'...', row[3],row[4]])

print(table)