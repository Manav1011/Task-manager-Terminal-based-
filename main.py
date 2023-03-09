import sqlite3

# Connect to a new SQLite database file
conn = sqlite3.connect('my_database.db')

# Create a new table
try:
    conn.execute('''CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    date DATE DEFAULT CURRENT_DATE
    );''')
except Exception as e:
    print("You have already intitalized the app")

# Insert some data into the table
# conn.execute("INSERT INTO tasks (title, description) VALUES (?, ?)", ('New task', 'Just a demo task'))
# Commit the changes
conn.commit()

# Query the database and print the results
cursor = conn.execute("SELECT * FROM tasks  ")
for row in cursor:
    print(row)

# Close the database connection
conn.close()