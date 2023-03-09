from init import *
import sys

if not sys.argv[1].isdigit() or sys.argv[1] == 0:
    print("Enter a valid task ID")
    sys.exit()

result  = conn.execute("delete from tasks where id=?", sys.argv[1])

conn.commit()
print("Task set to completed")