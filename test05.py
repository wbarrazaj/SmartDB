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

printlog ("Inicio .-- ")

dbConn_SmartDB=BaseDD(servidor=SDB_Servidor, usuario=SDB_Usuario, clave=SDB_Clave, db=SDB_BDD, puerto=SDB_Puerto, drver='', motor=SDB_Motor) 

consulta_Servidores="select Motor, Id_Servidor, fn_Servidor(ID_Servidor) as Servidor, Usuario, Clave, BDD, Puerto from " + SDB_BDD + ".Tbl_Conexion where fn_Servidor(Id_Servidor) in ('Ares','Apolo')"

resultado_Servidores=dbConn_SmartDB.ejecutar_query(consulta_Servidores)

for aaa in resultado_Servidores:
    Motor = aaa[0]
    Id_Servidor = aaa[1]
    Servidor = aaa[2]
    Usuario = aaa[3]
    Clave = aaa[4]
    BDD = aaa[5]
    Puerto = aaa[6]


    consulta_Indicadores="select Id_Indicadores, Motor, Tipo, Consulta, Fecha, Tabla, Estructura from Tbl_Indicadores where Motor='MariaDB';"
    resultado_Indicadores=dbConn_SmartDB.ejecutar_query(consulta_Indicadores) 

    dbConn=BaseDD(servidor=Servidor, usuario=Usuario, clave=Clave, db=BDD, puerto=Puerto, drver='', motor=Motor)

    printlog('Servidor-------> ' + Servidor)

    for a in resultado_Indicadores :

        resultado=dbConn.ejecutar_query(a[3])
        id = a[0] 
        fecha_ejecucion = datetime.datetime.now()
        printlog ("\tTabla--->"+ a[5])
        Ind_=Indicadores(Id=id, Motor=dbConn.Motor,conn=dbConn_SmartDB)
        try:
            for exec_cons in resultado :
                Dato = [Ind_.Id, Ind_.Motor,Id_Servidor,BDD,fecha_ejecucion]
                for exec_y in range(Ind_.cant_campos-5):
                    Dato.append(exec_cons[exec_y])
                Ind_.insert_tbl(Dato,Ind_.Id)
            
                
        except ValueError as er:
                printlog (er)

printlog ("Termino .-- ")