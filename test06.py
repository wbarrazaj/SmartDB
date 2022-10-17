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

#print(consulta)

dbConn_SmartDB=BaseDD(servidor=SDB_Servidor, usuario=SDB_Usuario, clave=SDB_Clave, db=SDB_BDD, puerto=SDB_Puerto, drver='', motor=SDB_Motor) 


Ind_=Indicadores(Id=1, Motor=SDB_Motor,conn=dbConn_SmartDB)

print(Ind_.valida_exist_tabla('Tbl_Indicadores'))



#Ind_.lee_indicadores()
