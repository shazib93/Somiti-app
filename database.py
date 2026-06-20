import sqlite3

# database file বানাও
conn = sqlite3.connect("somiti.db")
cursor = conn.cursor()

# members table বানাও
cursor.execute("""
    CREATE TABLE IF NOT EXISTS members (
        id INTEGER PRIMARY KEY,
        naam TEXT,
        amount INTEGER,
        month TEXT
    )
""")

conn.commit()
conn.close()
print("Database ready!")
import sqlite3

conn = sqlite3.connect("somiti.db")
cursor = conn.cursor()

# member data যোগ করো
cursor.execute("INSERT INTO members (naam, amount, month) VALUES (?, ?, ?)", ("Shipon", 500, "June"))
cursor.execute("INSERT INTO members (naam, amount, month) VALUES (?, ?, ?)", ("Rajon", 300, "June"))
cursor.execute("INSERT INTO members (naam, amount, month) VALUES (?, ?, ?)", ("Habib", 500, "June"))
cursor.execute("INSERT INTO members (naam, amount, month) VALUES (?, ?, ?)", ("Billal", 200, "June"))

conn.commit()
conn.close()
print("Data added!")