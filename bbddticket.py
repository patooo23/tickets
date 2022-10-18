from operator import contains
from queue import Empty
import mysql.connector
from tkinter import messagebox as mb

class Area:
    def __init__ (self):
        self.conexion=mysql.connector.connect(host="localhost",user="root",
                                    passwd="Pato1234",database="Tickets")
        

    def insertar(self,nombre, email, telefono):
        con = self.conexion.cursor()
        #LOS NOMBRES DE COLUMNAS TAL CUAL COMO ESTAN EN LA BASE
        sql=f'''INSERT INTO area (nombre, email, telefono)
        VALUES('{nombre}','{email}','{telefono}')'''
        con.execute(sql)
        self.conexion.commit()
        con.close()
        mb.showinfo(title="area agregada",message="Se ha agregado una nueva area con éxito")
        

    def mostrar(self):
        con = self.conexion.cursor()
        sql="SELECT * FROM area"
        con.execute(sql)
        registro = con.fetchall()
        return registro

   

    def eliminarArea(self,id_area):
        con = self.conexion.cursor()
        sql=f'''DELETE FROM area where id_area = {id_area}'''
        con.execute(sql)
        self.conexion.commit()
        con.close()

#=========================================================================================================================


class Tipo_problema:
    def __init__ (self):
        self.conexion=mysql.connector.connect(host="localhost",user="root",
                                    passwd="Pato1234",database="Tickets")
        

    def insertar(self,nombre):
        con = self.conexion.cursor()
        #LOS NOMBRES DE COLUMNAS TAL CUAL COMO ESTAN EN LA BASE
        sql=f'''INSERT INTO tipo_problema (nombre)
        VALUES('{nombre}')'''
        con.execute(sql)
        self.conexion.commit()
        con.close()
        mb.showinfo(title="tipo de problema",message="Se ha agregado uno nuevo tipo de problema")
        

    def mostrar(self):
        con = self.conexion.cursor()
        sql="SELECT * FROM tipo_problema"
        con.execute(sql)
        registro = con.fetchall()
        return registro

   

    def eliminar_tipo_problema(self,id_tipo_problema):
        con = self.conexion.cursor()
        sql=f'''DELETE FROM tipo_problema where id_tipo_problema = {id_tipo_problema}'''
        con.execute(sql)
        self.conexion.commit()
        con.close()

#========================================================================================================================

class Articulo:
    def __init__ (self):
        self.conexion=mysql.connector.connect(host="localhost",user="root",
                                    passwd="Pato1234",database="Tickets")
        

    def insertar(self,nombre):
        con = self.conexion.cursor()
        #LOS NOMBRES DE COLUMNAS TAL CUAL COMO ESTAN EN LA BASE
        sql=f'''INSERT INTO articulo (nombre)
        VALUES('{nombre}')'''
        con.execute(sql)
        self.conexion.commit()
        con.close()
        mb.showinfo(title="articulo",message="Se ha agregado un nuevo articulo")
        

    def mostrar(self):
        con = self.conexion.cursor()
        sql="SELECT * FROM articulo"
        con.execute(sql)
        registro = con.fetchall()
        return registro

   

    def eliminar_articulo(self,id_articulo):
        con = self.conexion.cursor()
        sql=f'''DELETE FROM articulo where id_articulo = {id_articulo}'''
        con.execute(sql)
        self.conexion.commit()
        con.close()
