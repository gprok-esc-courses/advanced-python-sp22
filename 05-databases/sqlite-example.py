import sqlite3

db = sqlite3.connect('skype_clone.db')

# db.execute("""
#             CREATE TABLE chat
#             (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#             send_from TEXT, send_to TEXT, message TEXT)
#            """)

# db.execute("INSERT INTO chat (send_from, send_to, message) VALUES ('john', 'peter', 'Hello there')")
# db.commit()

cursor = db.cursor()
result = cursor.execute("SELECT * FROM chat")
for row in result:
    print(row)
