from init import *
import sys


title = input("Title: ")
print("Description:",end=' ',flush=True)
desc= sys.stdin.read()
status = "pending"

conn.execute("Insert into tasks (title, description, status) values(?,?,?)",(title,desc,status))
conn.commit()
print()
print()
print("Task added.")