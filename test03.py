import sqlite3

data = [
    ("MARIADB","Ares","root","Emilita01","Prueba","3306"),
    ("MARIADB","Apolo","root","Emilita01","mysql","3306"),
    ("SQLSERVER","servidorPandora","","","",""),
    ("MYSQL","servidorNicaragua","","","",""),
    ("MYSQL","servidorGuatemala","","","","")
        ]

con = sqlite3.connect("SmartDB.db")
cur = con.cursor()
#cur.execute("CREATE TABLE Tbl_Conexion(Motor, Servidor, usuario, clave , BDD, puerto)") 
res = cur.execute("SELECT name FROM sqlite_master") 
a = res.fetchone()
print(a)
cur.executemany("INSERT INTO Tbl_Conexion VALUES(?, ?, ?, ?, ?, ?)", data) 
con.commit()

for row in cur.execute("SELECT * FROM Tbl_Conexion"):
    print(row)

con.close()



