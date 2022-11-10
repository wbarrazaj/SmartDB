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



Comando =  'redis-cli'
Servidor =  "Aquiles"
Usuario = "monitor"
Clave = "Emilita01"
Puerto = 6379
Comando_REDIS = "INFO MEMORY"
Comando_REDIS_Split  = Comando_REDIS.split()

mensaje = [Comando,"-h", Servidor, "--user",Usuario, "--pass",Clave ,"-p" ,str(Puerto)]

for xx_comando in Comando_REDIS_Split :
    mensaje.append(xx_comando)

result = subprocess.Popen(mensaje,text=True,stdout=subprocess.PIPE)

i=0
for linea in result.stdout  :   
    if i>0 :
        Parametros, Valores = linea.rstrip().split(":")
        print(Parametros, Valores)
        i+=1
    else : 
        i+=1

