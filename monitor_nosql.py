#!/usr/bin/env python3
#_*_ coding: utf-8 _*_

import subprocess
import sys
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

consulta_Servidores="select Motor, Id_Servidor, fn_Servidor(ID_Servidor) as Servidor, Usuario, Clave, BDD, Puerto from " + SDB_BDD + ".Tbl_Conexion where fn_Servidor(Id_Servidor) in ('Aquiles')"

resultado_Servidores=dbConn_SmartDB.ejecutar_query(consulta_Servidores)

for ListaServer in resultado_Servidores:
    Motor = ListaServer[0]
    Id_Servidor = ListaServer[1]
    Servidor = ListaServer[2]
    Usuario = ListaServer[3]
    Clave = ListaServer[4]
    BDD = ListaServer[5]
    Puerto = ListaServer[6]

Comando =  'redis-cli'
Comando_REDIS = "INFO MEMORY"
Comando_REDIS_Split  = Comando_REDIS.split()
comand_conec_redis = [Comando,"-h", Servidor, "--user",Usuario, "--pass",Clave ,"-p" ,str(Puerto)]

consulta_Indicadores="select Id_Indicadores, Motor, Tipo, Consulta, Fecha, Tabla, Estructura from Tbl_Indicadores where Motor='Redis';"
resultado_Indicadores=dbConn_SmartDB.ejecutar_query(consulta_Indicadores) 



for a in resultado_Indicadores :
    comand_conec_redis = [Comando,"-h", Servidor, "--user",Usuario, "--pass",Clave ,"-p" ,str(Puerto)]
    id = a[0] 
    fecha_ejecucion = datetime.datetime.now()
    printlog ("\tTabla--->"+ a[5])
    Ind_=Indicadores(Id=id, Motor=Motor,conn=dbConn_SmartDB)
    print(Ind_.Consulta)
    Comando_REDIS_Split = Ind_.Consulta.split()

    for xx_comando in Comando_REDIS_Split :
        comand_conec_redis.append(xx_comando)


    resultado_redis = subprocess.Popen(comand_conec_redis,text=True,stdout=subprocess.PIPE)
    resultado=[]
    i=0
    for linea in resultado_redis.stdout  :   
        if i>0 :
            resultado_xx = linea.rstrip().split(":")
            resultado.append(resultado_xx)
            i+=1
        else : 
            i+=1

    for exec_cons in resultado :
        Dato = [Ind_.Id, Ind_.Motor,Id_Servidor,BDD,fecha_ejecucion,Ind_.Consulta]

        for exec_y in range(Ind_.cant_campos-6):
            Dato.append(exec_cons[exec_y])
        Ind_.insert_tbl(Dato,Ind_.Id)
        #print(Dato)
        #except ValueError as er:
        #printlog (er)


printlog ("Termino .-- ")
