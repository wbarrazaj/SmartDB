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



for ListaServer in resultado_Servidores:
    Motor = ListaServer[0]
    Id_Servidor = ListaServer[1]
    Servidor = ListaServer[2]
    Usuario = ListaServer[3]
    Clave = ListaServer[4]
    BDD = ListaServer[5]
    Puerto = ListaServer[6]


    consulta_Indicadores="select Id_Indicadores, Motor, Tipo, Consulta, Fecha, Tabla, Estructura from Tbl_Indicadores where Motor='MariaDB';"
    resultado_Indicadores=dbConn_SmartDB.ejecutar_query(consulta_Indicadores) 

    dbConn=BaseDD(servidor=Servidor, usuario=Usuario, clave=Clave, db=BDD, puerto=Puerto, drver='', motor=Motor)

    printlog('Servidor-------> ' + Servidor)

    Status=Indicadores(Id=0, Motor=dbConn.Motor,conn=dbConn_SmartDB)

    dbConn.ejecutar_query('select 1;')
    
    #print(dbConn.Estado)

    if dbConn.Estado==0:
        printlog ('Base de Datos UP :  Servidor ---> ' + dbConn.ServidorDB )
        Status.insert_tbl_Estado_BDD(0, Motor,Id_Servidor,BDD, 'UP')
        printlog ("\tTabla--->"+ "tbl_mdb_p000")
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
    else : 
        printlog ('Base de Datos Down :  Servidor ---> ' + dbConn.ServidorDB )
        Status.insert_tbl_Estado_BDD(0, Motor,Id_Servidor,BDD, 'DOWN')
        printlog ("\tTabla--->"+ "tbl_mdb_p000")

#dbConn.close()
dbConn_SmartDB.close()
printlog ("Termino .-- ")