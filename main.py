from init import *

# Create a new table
try:
    conn.execute('''CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    date DATE DEFAULT CURRENT_DATE,
    status VARCHAR(10) NOT NULL CHECK (status IN ('pending', 'completed')),
    posted INTEGER
    );''')
except Exception as e:
    print("You have already initialized the app")

# Insert some data into the table
# conn.execute("")
# Commit the changes
conn.commit()

# Query the database and print the results

# Close the database connection
conn.close()