from readline import insert_text
from modulos.funciones import substr,  printlog 
import datetime
import sqlite3
import pymysql


class Indicadores():
    def __init__(self, Motor, Id, conn):
            self.Id = Id
            self.Motor =  Motor
            self.Tipo = ''
            self.Descripcion = ''
            self.Consulta = '' 
            self.Fecha = ''
            self.Tabla = ''
            self.Estructura = ''
            self.conn=conn
            self.insert = ''
            self.cant_campos = 0
            self.lee_indicadores()

      
    def valida_exist_tabla(self, tabla):
        conn=self.conn
        #print(conn)
        esquema='SmartDB'
        cons="select count(*) from information_schema.tables where table_name = '" + tabla + "' and  Table_SCHEMA= '" + esquema +  "';"         
        r = conn.ejecutar_query(cons)

        print(r)

        if r[0]==1:
            return 1
        else :
            return 0

    def creaTabla (self, tabla):
        conn=self.conn
        id_= str(self.Id)
        cons= "select Estructura from Tbl_Indicadores where Id =" + id_ + " and Motor ='" + self.Motor + "';"
        a=conn.ejecutar_query(cons)
        cre_table=a[0]+ ';'
        print(cre_table)
        a=conn.ejecutar_query(cre_table)

    def lee_indicadores (self):
        try:
            conn=self.conn
            id_= str(self.Id)
            consult= "select Id_Indicadores, Motor, Tipo, Descripcion, Consulta, Fecha, Tabla,  Estructura from Tbl_Indicadores where Id_Indicadores =" + id_ + " and Motor ='" + self.Motor + "';"
            print(consult)
            resp_ = conn.ejecutar_query(consult)
            self.Id=resp_[0]
            #print(self.Id)
            #self.Id, self.Motor, self.Tipo, self.Descripcion, self.Consulta, self.Fecha, self.Tabla , self.Estructura = resp
            self.insert=self.__genera_sql_insert(self.Tabla)
            #print(self.Id, self.Motor, self.Tipo, self.Descripcion, self.Consulta, self.Fecha, self.Tabla , self.Estructura,self.insert )
        except ValueError as err :
            print(err)
        
    def __genera_sql_insert(self, tabla):
        conn=self.conn
        esquema='SmartDB'
        
        consulta="select column_name as column_name from information_schema.columns where table_name = '" + tabla + "' and Table_SCHEMA= '" + esquema + "' order by ordinal_position;"

        resp = conn.ejecutar_query(consulta)

        campos = ''
        campos2 = ''
        count = 0 

        for a in resp:
            campos = campos + a[0] + ','
            campos2 = campos2 + '?,'
            count=count+1
    

        self.cant_campos = count 
        ins_txt = 'INSERT INTO ' + tabla + '(' + substr(campos.strip(),0,len(campos.strip())-1) + ') VALUES (' + substr(campos2.strip(),0,len(campos2.strip())-1) + ')'

        return ins_txt

    def insert_tbl(self, Datos, id ):
        cur = self.conn.cursor()
        table = self.Tabla
        query = self.insert 
        cur.execute(query, Datos)
        self.conn.commit()

    def insert_tbl_Estado_BDD (self, id, Motor,Servidor,BDD, estado):
        fecha_ejecucion= datetime.datetime.now()
        tabla='tbl_mdb_p000'
        self.Tabla=tabla
        self.insert= self.__genera_sql_insert(self.Tabla)
        self.id=id
        Dato = [self.id, Motor,Servidor,BDD,fecha_ejecucion, estado ]
        self.insert_tbl(Dato, id) 









