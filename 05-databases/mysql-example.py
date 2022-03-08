import mysql.connector

db = mysql.connector.connect(
    host="localhost", user="test", password="test", database="python_example"
)

cursor = db.cursor()

# query = "INSERT INTO CHAT (send_from, send_to, message) VALUES ('john', 'peter', 'Hello there')"
#
# cursor.execute(query)
# db.commit()

select_query = "SELECT * FROM chat"
cursor.execute(select_query)
data = cursor.fetchall()

for row in data:
    print(row[1])

