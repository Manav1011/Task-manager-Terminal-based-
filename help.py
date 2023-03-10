from prettytable import PrettyTable


# Create a new table object
table = PrettyTable()

table.field_names = ["command","work"]
table.add_row(["task add","To add a new task"])
table.add_row(["task done [ID]","Set a task as completed"])
table.add_row(["task open [ID]","Set a task as pending"])
table.add_row(["task show [ID]","Detailed task view"])
table.add_row(["task list","Current day's pending tasks"])
table.add_row(["task list completed","Current day's completed tasks"])
table.add_row(["task list kalna","Yesterday's tasks"])
table.add_row(["task list paramdivas","Day before yesterday's tasks"])

print(table)
