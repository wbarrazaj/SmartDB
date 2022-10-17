import mysql

conn = mysql.connector.connect(
   user='monitor', password='Emilita01', host='Ares', database='SmartDB')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL query to INSERT a record into the database.
sql = "select * from Tbl_Servidor;"

try:
   # Executing the SQL command
   cursor.execute(sql)

   # Commit your changes in the database
   conn.commit()

except:
   # Rolling back in case of error
   conn.rollback()

# Closing the connection
conn.close()
