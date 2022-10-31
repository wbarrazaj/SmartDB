#!/usr/bin/env python3
#_*_ coding: utf-8 _*_
import pyodbc 

Servidor='193.168.1.85'
Database='Aquiles'
usuario='sa'

clave='Emilita01'

cnxn_str = ("DRIVER={SQL Server};" 
            "SERVER=193.168.1.85;" 
            "DATABASE=Aquiles;" 
            "UID=sa;" 
            "PWD=Emilita01;")
cnxn = pyodbc.connect(cnxn_str)


print ('Conexion Exitosa')

#cursor = conn.cursor()
#cursor.execute('SELECT 1')

#for i in cursor:
#    print(i)




