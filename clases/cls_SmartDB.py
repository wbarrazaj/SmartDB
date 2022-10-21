from readline import insert_text
from modulos.funciones import substr,  printlog 
import datetime
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
            self.__lee_indicadores()

      
    def valida_exist_tabla(self, tabla):
        conn=self.conn
        esquema='SmartDB'
        cons="select count(*) from information_schema.tables where table_name = '" + tabla + "' and  Table_SCHEMA= '" + esquema +  "';"         
        r = conn.ejecutar_query(cons)
        
        if r[0][0]==1:
            return 1
        else :
            return 0

    def creaTabla (self, tabla):
        conn=self.conn
        id_= str(self.Id)
        cons= "select Estructura from Tbl_Indicadores where Id_Indicadores =" + id_ + " and Motor ='" + self.Motor + "';"
        a=conn.ejecutar_query(cons)
        print(a[0])
        cre_table=str(a[0])+ ';'
        print(cre_table)
        a=conn.ejecutar_query(cre_table)

    def __lee_indicadores (self):
        try:
            conn=self.conn
            id_= str(self.Id)
            _consult= "select Id_Indicadores, Motor, Tipo, Descripcion, Consulta, Fecha, Tabla,  Estructura from SmartDB.Tbl_Indicadores where Id_Indicadores =" + id_ + " and Motor ='" + self.Motor + "';"
            resp_ = conn.ejecutar_query(_consult)
            if self.Id == 0:
                #conn.close()
                pass
            else : 
                self.Id, self.Motor, self.Tipo, self.Descripcion, self.Consulta, self.Fecha, self.Tabla , self.Estructura = resp_[0]
                self.insert=self.genera_sql_insert(self.Tabla)
                #conn.close()
        except ValueError as err :
            print(err)
        
    def genera_sql_insert(self, tabla):
        conn=self.conn
        esquema='SmartDB'
        
        consulta="select column_name as column_name from information_schema.columns where table_name = '" + tabla + "' and Table_SCHEMA= '" + esquema + "' order by ordinal_position;"

        resp = conn.ejecutar_query(consulta)

        campos = ''
        campos2 = ''
        count = 0 

        for a in resp:
            campos = campos + a[0] + ','
            campos2 = campos2 + '%s,'
            count=count+1
    

        self.cant_campos = count 
        ins_txt = 'INSERT INTO ' + tabla + '(' + substr(campos.strip(),0,len(campos.strip())-1) + ') VALUES (' + substr(campos2.strip(),0,len(campos2.strip())-1) + ')'
        #conn.close()
        return ins_txt

    def insert_tbl(self, Datos, id ):
        conn=self.conn
        table = self.Tabla
        query = self.insert 
        conn.ejecutar_query_data(query, Datos)
        #conn.close()

    def insert_tbl_Estado_BDD (self, id, Motor,Servidor,BDD, estado):
        fecha_ejecucion= datetime.datetime.now()
        tabla='tbl_mdb_p000'
        self.Tabla=tabla
        self.insert= self.genera_sql_insert(self.Tabla)
        self.id=id
        Dato = [self.id, Motor,Servidor,BDD,fecha_ejecucion, estado ]
        self.insert_tbl(Dato, id) 









