from init import *
import sys

if not sys.argv[1].isdigit() or sys.argv[1] == 0:    
    print("Enter a valid task ID")
    sys.exit()
result  = conn.execute("update tasks set status='pending' where id=?", (sys.argv[1],))

conn.commit()
if result.rowcount > 0:
    print("Task set to pending")
else:
    print("Invalid task ID")