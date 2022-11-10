#!/usr/bin/env python3
#_*_ coding: utf-8 _*_

import subprocess
import sys
import os
import datetime
from clases.cls_Bdd import BaseDD
from clases.cls_SmartDB import Indicadores
from modulos.funciones import substr,  printlog 


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

