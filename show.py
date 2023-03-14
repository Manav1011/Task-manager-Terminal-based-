from init import *
import sys

if not sys.argv[1].isdigit() or sys.argv[1] == 0:
    print("Enter a valid task ID")
    sys.exit()

result  = conn.execute("Select * from tasks where id=?", [sys.argv[1],])

for i in result:
    print(f"Task ID: {i[0]}")
    print(f"Task Title: {i[1]}")
    print(f"Task Status: {i[4]}")
    print(f"Task Date: {i[3]}")        
    print(f"Task Description".center(20,'-'))
    print(i[2])