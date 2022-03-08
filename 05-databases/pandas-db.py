import mysql.connector
import pandas as pd

db = mysql.connector.connect(
    host="localhost", user="test", password="test", database="python_example"
)

query = pd.read_sql_query("SELECT * FROM chat", db)
df = pd.DataFrame(query)

print(df.shape)
print(df.info())

print(df.head())
