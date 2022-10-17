#!/usr/bin/env python3
#_*_ coding: utf-8 _*_

import os
import datetime
from clases.cls_Bdd import BaseDD
from clases.cls_SmartDB import Indicadores
from modulos.funciones import substr,  printlog 

SDB_Id_Servidor=1
SDB_Servidor='Ares'
SDB_Usuario= 'monitor'
SDB_Clave='Emilita01'
SDB_BDD='SmartDB'
SDB_Puerto='3306'
SDB_Motor= 'MariaDB'

tabla='Tbl_Indicadores'
SmartDB='SmartDB'

consulta="select count(*) from information_schema.tables where table_name = '" + tabla + "' and  Table_SCHEMA= '" + SmartDB +  "'"

dbConn_SmartDB=BaseDD(servidor=SDB_Servidor, usuario=SDB_Usuario, clave=SDB_Clave, db=SDB_BDD, puerto=SDB_Puerto, drver='', motor=SDB_Motor) 

a = dbConn_SmartDB.ejecutar_query(consulta)

#print(a[0][0])

Ind_=Indicadores(Id=1, Motor=SDB_Motor,conn=dbConn_SmartDB)

print(Ind_.valida_exist_tabla('Tbl_Indicadores'))

print(Ind_.insert)


#print(Ind_.Id)

#Ind_.lee_indicadores()

#print(Ind_.genera_sql_insert('tbl_mdb_p002'))

#print(Ind_.insert)

#Ind_.creaTabla('tbl_mdb_p002')


print(datetime.datetime(2022, 10, 17, 16, 3, 59, 793098))

query = "INSERT INTO tbl_mdb_p001(id,Motor,Id_Servidor,BDD,table_schema,size_db,free_space) VALUES (?,?,?,?,?,?,?)"
Data = ('1', 'MariaDB', '1', 'mysql','mysql', '2.547', '0.1')

print(query, Data)
dbConn_SmartDB.ejecutar_query_data(query,Data)


