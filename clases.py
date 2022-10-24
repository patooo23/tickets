import mariadb
from tkinter import messagebox as mb

password = 'Pato1234'


class Usuario:
    def __init__(self,):
        self.conexion = mariadb.connect(host='localhost', user='root',
                                        passwd=password, database='Tickets')

    def insertar(self, nombre, apellido, legajo, email, nombre_usuario, contraseña):
        con = self.conexion.cursor()
        sql = f'''INSERT INTO usuario (nombre, apellido, legajo, email, nombre_usuario, contraseña)
        VALUES('{nombre}','{apellido}','{legajo}','{email}','{nombre_usuario}', '{contraseña}')'''
        con.execute(sql)
        self.conexion.commit()
        con.close()
        mb.showinfo(title='Usuario Creado',
                    message='Se ha registrado su usuario con éxito.\nAhora puede iniciar sesión')

    def mostrar(self):
        con = self.conexion.cursor()
        sql = 'SELECT * FROM usuario'
        con.execute(sql)
        registro = con.fetchall()
        return reversed(registro)

    def modificar(self, id_usuario, id_tipo_usuario, nombre, apellido, email, legajo, activo):
        con = self.conexion.cursor()
        sql = f'''UPDATE usuario SET nombre = '{nombre}', apellido = '{apellido}', 
        legajo = '{legajo}', email = '{email}', activo= '{activo}', id_tipo_usuario = {id_tipo_usuario}
        WHERE id_usuario ={id_usuario}'''
        con.execute(sql)
        self.conexion.commit()
        con.close()
        mb.showinfo(title='Usuario Modificado',
                    message=f'Se ha modificado el usuario {nombre} {apellido} con éxito')

    def modificar_contraseña(self, id_usuario, contraseña):
        con = self.conexion.cursor()
        sql = f'''UPDATE usuario SET contraseña = '{contraseña}'
        WHERE id_usuario ={id_usuario}'''
        con.execute(sql)
        self.conexion.commit()
        con.close()
        mb.showinfo(title='Contraseña Modificada',
                    message=f'Se ha modificado la contraseña con éxito')

    def eliminar(self, id_usuario):
        try:
            con = self.conexion.cursor()
            sql = f'''DELETE FROM usuario where id_usuario = {id_usuario}'''
            con.execute(sql)
            self.conexion.commit()
            con.close()
            mb.showinfo(title='Usuario Eliminado',
                        message='Se ha eliminado el usuario con éxito')
        except:
            mb.showerror(title='ERROR',
                        message=f'No se pudo eliminar el usuario')

    def lista_usuarios(self):
        con = self.conexion.cursor()
        sql = 'SELECT nombre_usuario FROM usuario'
        con.execute(sql)
        registro = con.fetchall()
        return registro

    def validar_contraseña(self, nombre_usuario, contraseña):
        con = self.conexion.cursor()
        sql = f'''SELECT contraseña FROM usuario where nombre_usuario = '{nombre_usuario}' '''
        con.execute(sql)
        registro = con.fetchall()
        if (registro[0][0] == contraseña):
            sql = f'''SELECT * FROM usuario where nombre_usuario = '{nombre_usuario}' '''
            con.execute(sql)
            registro = con.fetchall()
            return registro
        else:
            return False

    def obtener_campo(self, campo, id):
        con = self.conexion.cursor()
        sql = f'''SELECT {campo} FROM usuario where id_usuario = '{id}' '''
        con.execute(sql)
        registro = con.fetchall()
        try:
            return registro[0][0]
        except:
            return ''

    def mostrar_datos(self, nombre_usuario):
        con = self.conexion.cursor()
        sql = f'''SELECT * FROM usuario where nombre_usuario = '{nombre_usuario}' '''
        con.execute(sql)
        registro = con.fetchall()
        return registro[0]

    def mostrar_lista_tecnicos(self):
        con = self.conexion.cursor()
        sql = 'SELECT nombre_usuario FROM usuario where id_tipo_usuario = 2'
        con.execute(sql)
        registro = con.fetchall()
        return registro

    def obtener_id(self, nombre_usuario):
        con = self.conexion.cursor()
        sql = f'''SELECT id_usuario FROM Usuario where nombre_usuario = '{nombre_usuario}' '''
        con.execute(sql)
        registro = con.fetchall()[0][0]
        return registro

#===========================================================================================================================

class Ticket:
    def __init__(self,):
        self.conexion = mariadb.connect(host='localhost', user='root',
                                        passwd=password, database='Tickets')

    def insertar(self, id_usuario, asunto, id_area, codigo_hardware, descripcion, fecha_inicio, hora_inicio, id_tipo_problema):
        con = self.conexion.cursor()
        sql = f'''INSERT INTO Ticket (id_usuario, asunto, id_area, codigo_hardware, descripcion, fecha_inicio, hora_inicio, id_tipo_problema)
        VALUES({id_usuario},'{asunto}',{id_area}, '{codigo_hardware}','{descripcion}','{fecha_inicio}', '{hora_inicio}', {id_tipo_problema})'''
        con.execute(sql)
        self.conexion.commit()
        con.close()
        mb.showinfo(title='Ticket Creado',
                    message='Se ha creado un nuevo ticket con éxito')

    def mostrar(self):
        con = self.conexion.cursor()
        sql = 'SELECT * FROM Ticket'
        con.execute(sql)
        registro = con.fetchall()
        return registro

    def mostrar_resumido(self):
        con = self.conexion.cursor()
        sql = '''SELECT id_ticket, id_usuario, id_area, id_estado,
                id_prioridad, id_tecnico, asunto, fecha_inicio, hora_inicio FROM Ticket'''
        con.execute(sql)
        registro = con.fetchall()
        return reversed(registro)

    def modificar(self, id_ticket, id_area, id_prioridad, id_estado, id_tipo_problema, id_tecnico, codigo_hardware):
        con = self.conexion.cursor()
        sql = ''
        if id_tecnico != '':
            sql = f'''UPDATE ticket SET id_area={id_area}, id_prioridad={id_prioridad}, id_estado={id_estado}, id_tipo_problema={id_tipo_problema},
                    id_tecnico={id_tecnico}, codigo_hardware='{codigo_hardware}' WHERE id_ticket={id_ticket}'''
        else:
            sql = f'''UPDATE ticket SET id_area={id_area}, id_prioridad={id_prioridad}, id_estado={id_estado}, id_tipo_problema={id_tipo_problema},
                    codigo_hardware='{codigo_hardware}' WHERE id_ticket={id_ticket}'''
        con.execute(sql)
        self.conexion.commit()
        con.close()
        mb.showinfo(title='Ticket Modificado',
                    message=f'Se ha modificado el ticket Nº {id_ticket} con éxito')

    def archivar(self, id_ticket, fecha_cierre, hora_cierre):
        con = self.conexion.cursor()
        sql = f'''UPDATE Ticket SET id_estado=5, fecha_cierre='{fecha_cierre}', hora_cierre='{hora_cierre}'
                where id_ticket = {id_ticket}'''
        con.execute(sql)
        self.conexion.commit()
        con.close()
        mb.showinfo(title='Ticket Archivado',
                    message=f'Se ha archivado el ticket Nº {id_ticket}')

    def obtener_datos(self, id_ticket):
        con = self.conexion.cursor()
        sql = f'SELECT * FROM Ticket where id_ticket = {id_ticket}'
        con.execute(sql)
        registro = con.fetchall()
        return registro[0]
# =========================================================================================================================

class Area:
    def __init__(self):
        self.conexion = mariadb.connect(host='localhost', user='root',
                                        passwd=password, database='Tickets')

    def insertar(self, nombre, email, telefono):
        con = self.conexion.cursor()
        sql = f'''INSERT INTO area (nombre, email, telefono)
        VALUES('{nombre}','{email}','{telefono}')'''
        con.execute(sql)
        self.conexion.commit()
        con.close()
        mb.showinfo(title='Área Agregada',
                    message='Se ha agregado una nueva área con éxito')

    def mostrar(self):
        con = self.conexion.cursor()
        sql = 'SELECT * FROM area'
        con.execute(sql)
        registro = con.fetchall()
        return registro

    def modificar(self, id_area, nombre, email, telefono):
        con = self.conexion.cursor()
        sql = f'''UPDATE area SET nombre='{nombre}',email='{email}',telefono='{telefono}' WHERE id_area ={id_area}'''
        con.execute(sql)
        self.conexion.commit()
        con.close()
        mb.showinfo(title='Área Modificada',
                    message=f'Se ha modificado el área {nombre} con éxito')

    def obtener_id(self, nombre):
        con = self.conexion.cursor()
        sql = f'''SELECT id_area FROM area where nombre = '{nombre}' '''
        con.execute(sql)
        registro = con.fetchall()
        return registro[0][0]

    def eliminar(self, id_area):
        try:
            con = self.conexion.cursor()
            sql = f'''DELETE FROM area where id_area = {id_area}'''
            con.execute(sql)
            self.conexion.commit()
            con.close()
            mb.showinfo(title='Área Eliminada',
                        message='Se ha eliminado el área con éxito')
        except:
            mb.showerror(title='ERROR',
                        message=f'No se pudo eliminar el área')

    def lista_areas(self):
        con = self.conexion.cursor()
        sql = 'SELECT nombre FROM area'
        con.execute(sql)
        registro = con.fetchall()
        return registro

    def obtener_nombre(self, id):
        con = self.conexion.cursor()
        sql = f'''SELECT nombre FROM area where id_area = {id} '''
        con.execute(sql)
        registro = con.fetchall()
        return registro[0][0]
# =========================================================================================================================


class TipoProblema:
    def __init__(self):
        self.conexion = mariadb.connect(host='localhost', user='root',
                                        passwd=password, database='Tickets')

    def insertar(self, nombre):
        con = self.conexion.cursor()
        sql = f'''INSERT INTO tipo_problema (nombre)
        VALUES('{nombre}')'''
        con.execute(sql)
        self.conexion.commit()
        con.close()
        mb.showinfo(title='Tipo de Problema Agregado',
                    message='Se ha agregado un nuevo tipo de problema')

    def mostrar(self):
        con = self.conexion.cursor()
        sql = 'SELECT * FROM tipo_problema'
        con.execute(sql)
        registro = con.fetchall()
        return registro

    def eliminar(self, id_tipo_problema):
        try:
            con = self.conexion.cursor()
            sql = f'''DELETE FROM tipo_problema where id_tipo_problema = {id_tipo_problema}'''
            con.execute(sql)
            self.conexion.commit()
            con.close()
            mb.showinfo(title='Tipo de Problema Eliminado',
                        message=f'Se ha eliminado el tipo de problema')
        except:
            mb.showerror(title='ERROR',
                        message=f'No se pudo eliminar el tipo de problema')

    def modificar(self, id_tipo_problema, nombre):
        con = self.conexion.cursor()
        sql = f'''UPDATE tipo_problema SET nombre='{nombre}' WHERE id_tipo_problema ={id_tipo_problema}'''
        con.execute(sql)
        self.conexion.commit()
        con.close()
        mb.showinfo(title='Tipo de Problema Modificado',
                    message=f'Se ha modificado el tipo de problema {nombre} con éxito')

    def obtener_id(self, nombre):
        con = self.conexion.cursor()
        sql = f'''SELECT id_tipo_problema FROM tipo_problema where nombre = '{nombre}' '''
        con.execute(sql)
        registro = con.fetchall()
        return registro[0][0]

    def obtener_nombre(self, id):
        con = self.conexion.cursor()
        sql = f'''SELECT nombre FROM tipo_problema where id_tipo_problema = '{id}' '''
        con.execute(sql)
        registro = con.fetchall()
        return registro[0][0]

    def lista_tipos_problema(self):
        con = self.conexion.cursor()
        sql = 'SELECT nombre FROM tipo_problema'
        con.execute(sql)
        registro = con.fetchall()
        return registro

# ========================================================================================================================


class Articulo:
    def __init__(self):
        self.conexion = mariadb.connect(host='localhost', user='root',
                                        passwd=password, database='Tickets')

    def insertar(self, nombre):
        con = self.conexion.cursor()
        sql = f'''INSERT INTO articulo (nombre)
        VALUES('{nombre}')'''
        con.execute(sql)
        self.conexion.commit()
        con.close()
        mb.showinfo(title='Artículo Agregado',
                    message='Se ha agregado un nuevo artículo')

    def mostrar(self):
        con = self.conexion.cursor()
        sql = 'SELECT * FROM articulo'
        con.execute(sql)
        registro = con.fetchall()
        return registro

    def eliminar_articulo(self, id_articulo):
        try:
            con = self.conexion.cursor()
            sql = f'''DELETE FROM articulo where id_articulo = {id_articulo}'''
            con.execute(sql)
            self.conexion.commit()
            con.close()
        except:
            mb.showerror(title='ERROR',
                        message=f'No se pudo eliminar el artículo')

class TipoUsuario:
    def __init__(self):
        self.conexion = mariadb.connect(host='localhost', user='root',
                                        passwd=password, database='Tickets')

    def mostrar(self):
        con = self.conexion.cursor()
        sql = 'SELECT * FROM tipo_usuario'
        con.execute(sql)
        registro = con.fetchall()
        return registro

    def obtener_id(self, nombre):
        con = self.conexion.cursor()
        sql = f'''SELECT id_tipo_usuario FROM tipo_usuario where nombre = '{nombre}' '''
        con.execute(sql)
        registro = con.fetchall()
        return registro[0][0]

    def obtener_nombre(self, id):
        con = self.conexion.cursor()
        sql = f'''SELECT nombre FROM tipo_usuario where id_tipo_usuario = {id} '''
        con.execute(sql)
        registro = con.fetchall()
        return registro[0][0]
# =========================================================================================================================

class Estado:
    def __init__(self):
        self.conexion = mariadb.connect(host='localhost', user='root',
                                        passwd=password, database='Tickets')

    def obtener_nombre(self, id):
        con = self.conexion.cursor()
        sql = f'''SELECT nombre FROM estado where id_estado = {id} '''
        con.execute(sql)
        registro = con.fetchall()
        return registro[0][0]

    def mostrar(self):
        con = self.conexion.cursor()
        sql = 'SELECT * FROM Estado'
        con.execute(sql)
        registro = con.fetchall()
        return registro

    def obtener_id(self, nombre):
        con = self.conexion.cursor()
        sql = f'''SELECT id_estado FROM estado where nombre = '{nombre}' '''
        con.execute(sql)
        registro = con.fetchall()
        return registro[0][0]
# =========================================================================================================================

class Prioridad:
    def __init__(self):
        self.conexion = mariadb.connect(host='localhost', user='root',
                                        passwd=password, database='Tickets')

    def obtener_nombre(self, id):
        con = self.conexion.cursor()
        sql = f'''SELECT nombre FROM prioridad where id_prioridad = {id} '''
        con.execute(sql)
        registro = con.fetchall()
        return registro[0][0]

    def mostrar(self):
        con = self.conexion.cursor()
        sql = 'SELECT * FROM Prioridad'
        con.execute(sql)
        registro = con.fetchall()
        return registro

    def obtener_id(self, nombre):
        con = self.conexion.cursor()
        sql = f'''SELECT id_prioridad FROM prioridad where nombre = '{nombre}' '''
        con.execute(sql)
        registro = con.fetchall()
        return registro[0][0]
# =========================================================================================================================
