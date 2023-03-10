from init import *
import sys

if not sys.argv[1].isdigit() or sys.argv[1] == 0:
    print("Enter a valid task ID")
    sys.exit()

title = input("Title: ")
print("Description:",end=' ',flush=True)
desc= sys.stdin.read()
status = "pending"

result  = conn.execute("update tasks set title=?,description=?,status=?,date=DATE(CURRENT_TIMESTAMP) where id=?", (title,desc,status,sys.argv[1]))

conn.commit()
if result.rowcount > 0:
    print()
    print("Task Updated")
else:
    print("Invalid task ID")