import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Relay (INT id AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), level VARCHAR(255), sender VARCHAR(255), message VARCHAR(255))")
sql = "INSERT INTO customers (name, level, sender, message) VALUES (%s, %s, %s, %s)"
val = [
  ('Peter', '0', '1' , 'hello'),
  ('Amy', '1', '2', 'hello'),
]
mycursor.executemany(sql, val)
mydb.commit()
