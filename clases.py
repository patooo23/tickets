import mariadb
from tkinter import messagebox as mb


class Usuario:
    def __init__ (self,):
        self.conexion = mariadb.connect(host="localhost", user="root",
                                    passwd="Pato1234", database="Tickets")

    def insertar(self, nombre, apellido, legajo, email, nombre_usuario, contraseña):
        con = self.conexion.cursor()
        #LOS NOMBRES DE COLUMNAS TAL CUAL COMO ESTAN EN LA BASE
        sql=f'''INSERT INTO usuario (nombre, apellido, legajo, email, nombre_usuario, contraseña)
        VALUES('{nombre}','{apellido}','{legajo}''{email}','{nombre_usuario}', '{contraseña}')'''
        con.execute(sql)
        self.conexion.commit()
        con.close()
        mb.showinfo(title="usuario creado",message="Se ha agregado un nuevo usuario con éxito")

    def mostrar(self):
        con = self.conexion.cursor()
        sql="SELECT * FROM usuario"
        con.execute(sql)
        registro = con.fetchall()
        return registro

    def modificar(self, id_usuario, nombre, apellido, legajo, email, nombre_usuario):
        con = self.conexion.cursor()
        #LOS NOMBRES DE COLUMNAS TAL CUAL COMO ESTAN EN LA BASE
        sql=f'''UPDATE usuario SET nombre = '{nombre}', apellido = '{apellido}', 
        legajo = '{legajo}', email = '{email}', nombre_usuario ='{nombre_usuario}'
        WHERE id_usuario ={id_usuario}'''
        con.execute(sql)
        self.conexion.commit()
        con.close()
        mb.showinfo(title="usuario modificado",message=f"Se ha modificado el usuario {nombre} con éxito")
        
    def modificar_contraseña(self, id_usuario, contraseña):
        con = self.conexion.cursor()
        #LOS NOMBRES DE COLUMNAS TAL CUAL COMO ESTAN EN LA BASE
        sql=f'''UPDATE usuario SET contraseña = '{contraseña}'
        WHERE id_usuario ={id_usuario}'''
        con.execute(sql)
        self.conexion.commit()
        con.close()
        mb.showinfo(title="contraseña modificada",message=f"Se ha modificado la contraseña con éxito")


    def eliminar(self,id_usuario):
        con = self.conexion.cursor()
        sql=f'''DELETE FROM usuario where id_usuario = {id_usuario}'''
        con.execute(sql)
        self.conexion.commit()
        con.close()
        mb.showinfo(title="usuario eliminado",message="Se ha eliminado el usuario con éxito")

#=======================================================================================================================
class Area:
    def __init__ (self,):
        self.conexion = mariadb.connect(host="localhost", user="root",
                                    passwd="Pato1234", database="Tickets")

    def insertar(self, nombre, email, telefono):
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

    def modificar(self, id_area, nombre, email, telefono):
        con = self.conexion.cursor()
        #LOS NOMBRES DE COLUMNAS TAL CUAL COMO ESTAN EN LA BASE
        sql=f'''UPDATE area SET nombre='{nombre}',email='{email}',telefono='{telefono}' WHERE id_area ={id_area}'''
        con.execute(sql)
        self.conexion.commit()
        con.close()
        mb.showinfo(title="area modificada",message=f"Se ha modificado el area {nombre} con éxito")
        


    def eliminar(self,id_area):
        con = self.conexion.cursor()
        sql=f'''DELETE FROM area where id_area = {id_area}'''
        con.execute(sql)
        self.conexion.commit()
        con.close()
        mb.showinfo(title="area eliminada",message="Se ha eliminado el area con éxito")

#=========================================================================================================================


class TipoProblema:
    def __init__ (self):
        self.conexion=mariadb.connect(host="localhost",user="root",
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
        self.conexion=mariadb.connect(host="localhost",user="root",
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
