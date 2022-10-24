from os import path
from tkinter import PhotoImage, IntVar, StringVar, Tk, Text, Toplevel, messagebox as mb
from tkinter.ttk import Button, Combobox, Entry, Frame, Label, Notebook, Scrollbar, Spinbox, Style, Treeview, Checkbutton
from tkinter.font import Font
from time import strftime
from clases import *


# region funciones

def posicionar_formulario(lista_label, lista_entry, button=None, column=0, row=1):
    row_label = row
    row_entry = row
    for i in lista_label:
        i.grid(column=column, row=row_label, padx=(24, 8), ipady=3, sticky='e')
        row_label += 1
    for i in lista_entry:
        i.grid(column=column+1, row=row_entry,
               padx=(8, 24), ipady=3, sticky='ew')
        row_entry += 1
    if button != None:
        button.grid(column=column+1, row=row_entry, padx=24, pady=(12, 8), ipadx=16, ipady=6, sticky='e')

def vaciar_entry(lista_entry):
    for i in lista_entry:
        i.delete(0, 'end')

def validar_obligatorios(lista_variables):
    for i in lista_variables:
        if i == '':
            mb.showerror('ERROR', 'Los campos marcados con * son obligatorios')
            return False
    else:
        return True

def crear_treeview(clase, treeview):
    for i in clase.mostrar():
        treeview.insert('', 'end', values=i)
        
def actualizar_treeview(clase, treeview):
    treeview.delete(*treeview.get_children())
    for i in clase.mostrar():
        treeview.insert('', 'end', values=i)
    actualizar_comboboxes()

def mostrar_usuario():
    global ventana_emergente
    if ventana_emergente != None:
        ventana_emergente.top.destroy()
    ventana_emergente = VentanaEmergente()
    WidgetsModificarUsuario(ventana_emergente.top)

def registrar_usuario():
    nombre = nombre_usuario.get().strip()
    apellido = apellido_usuario.get().strip()
    legajo = legajo_usuario.get().strip()
    email = email_usuario.get().strip()
    nombre_usuarioo = nombre_usuario_usuario.get().strip().lower() # esta variable tiene dos o porque no andaba el get del nombre
    contraseña = contraseña_usuario.get().strip()
    repetir_contraseña = repetir_contraseña_usuario.get().strip()
    
    if '@' not in email:
        mb.showerror('ERROR', 'Ingrese un email válido')
        return
    if len(contraseña) < 4:
        mb.showerror('ERROR', 'Las contraseña no debe tener menos de 4 dígitos')
        return
    if contraseña != repetir_contraseña:
        mb.showerror('ERROR', 'Las contraseñas no coinciden')
        return
    usuario = Usuario()
    for i in usuario.lista_usuarios():
        if i[0] == nombre_usuarioo:
            mb.showerror('ERROR', 'El nombre de usuario ya existe')
            return
    
    if validar_obligatorios((nombre, apellido, legajo, email, nombre_usuarioo, contraseña)):
        usuario.insertar(nombre, apellido, legajo, email, nombre_usuarioo, contraseña)
        vaciar_entry(widgets_registrarse.lista_entry)
        widgets_iniciar_sesion.lista_entry[1].delete(0, 'end')
        widgets_iniciar_sesion.lista_entry[1].insert(0, nombre_usuarioo)


def modificar_usuario():
    global ventana_emergente
    mensaje = mb.askyesno('Modificar Usuario', '¿Seguro desea modificar el usuario?')
    if mensaje == True:

        id_usuario = id_mod_usuario.get()
        nombre = nombre_mod_usuario.get().strip()
        apellido = apellido_mod_usuario.get().strip()
        legajo = legajo_mod_usuario.get().strip()
        email = email_mod_usuario.get().strip()
        activo = activo_mod_usuario.get()
        tipo = tipo_mod_usuario.get()
        if validar_obligatorios((nombre, apellido, legajo, email, tipo)):
            usuario = Usuario()
            tipo_usuario = TipoUsuario()
            id_tipo_usuario = tipo_usuario.obtener_id(tipo_mod_usuario.get())
            usuario.modificar(id_usuario, id_tipo_usuario, nombre, apellido, email, legajo, activo)
            vaciar_entry(widgets_registrarse.lista_entry)
            widgets_usuarios.actualizar_treeview()
            ventana_emergente.top.destroy()

#====================================================================================================================
def crear_ticket():    
    area = Area()
    tipo_problema = TipoProblema()
    id_usuario = usuario_actual.id_usuario                                 #ticket
    asunto = asunto_ticket.get().strip()
    id_area = area_ticket.get().strip()
    id_tipo_problema = tipo_problema_ticket.get().strip()
    codigo_hardware = codigo_hardware_ticket.get().strip()
    descripcion = widgets_crear_ticket.text.get('1.0', 'end').strip()
    if validar_obligatorios((asunto, id_area, id_tipo_problema, descripcion)):
        id_area = area.obtener_id(area_ticket.get())
        id_tipo_problema = tipo_problema.obtener_id(tipo_problema_ticket.get())
        fecha_inicio = strftime('%Y/%m/%d')
        hora_inicio = strftime('%H:%M:%S')
        ticket = Ticket()
        ticket.insertar(id_usuario, asunto, id_area, codigo_hardware, descripcion, fecha_inicio, hora_inicio, id_tipo_problema)
        vaciar_entry(widgets_crear_ticket.lista_entry[0:2])
        vaciar_entry(widgets_crear_ticket.lista_entry[3:4])
        widgets_crear_ticket.lista_entry[1].set('')
        widgets_crear_ticket.lista_entry[2].set('')
        widgets_crear_ticket.text.delete('1.0', 'end')
        widgets_mostrar_tickets.actualizar_treeview()


def mostrar_ticket():
    global ventana_emergente
    if ventana_emergente != None:
        ventana_emergente.top.destroy()
        
    ticket = Ticket()

    id_ticket = id_mod_ticket.get()
    datos = ticket.obtener_datos(id_ticket)
    lista_datos = [id_mod_ticket, usuario_mod_ticket, area_mod_ticket, estado_mod_ticket, prioridad_mod_ticket, tecnico_mod_ticket, 
                   tipo_problema_mod_ticket, asunto_mod_ticket, fecha_inicio_mod_ticket, fecha_cierre_mod_ticket,
                   descripcion_mod_ticket, codigo_hardware_mod_ticket, hora_inicio_mod_ticket, hora_cierre_mod_ticket]

    for i in range(len(datos)):
        lista_datos[i].set(datos[i])

    estado = Estado()
    usuario = Usuario()
    area = Area()
    prioridad = Prioridad()
    tipo_problema = TipoProblema()

    estado_mod_ticket.set(estado.obtener_nombre(estado_mod_ticket.get()))
    usuario_mod_ticket.set(usuario.obtener_campo('nombre_usuario', usuario_mod_ticket.get()))
    area_mod_ticket.set(area.obtener_nombre(area_mod_ticket.get()))
    prioridad_mod_ticket.set(prioridad.obtener_nombre(prioridad_mod_ticket.get()))
    tipo_problema_mod_ticket.set(tipo_problema.obtener_nombre(tipo_problema_mod_ticket.get()))
    tecnico_mod_ticket.set(usuario.obtener_campo('nombre_usuario', tecnico_mod_ticket.get()))
    

    ventana_emergente = VentanaEmergente()
    WidgetsModificarTicket(ventana_emergente.top)


def modificar_ticket():
    mensaje = mb.askyesno('Modificar Ticket', '¿Seguro desea modificar el ticket?')
    if mensaje == True:
        id_ticket = id_mod_ticket.get()
        id_area = area_mod_ticket.get()
        id_prioridad = prioridad_mod_ticket.get()
        id_estado = estado_mod_ticket.get()
        codigo_hardware = codigo_hardware_mod_ticket.get()
        id_tecnico = tecnico_mod_ticket.get()
        id_tipo_problema = id_mod_tipo_problema.get()
        if validar_obligatorios((id_area, id_prioridad, id_estado, id_tipo_problema, codigo_hardware)):
            ticket = Ticket()
            area = Area()
            prioridad = Prioridad()
            estado = Estado()
            usuario = Usuario()
            tipo_problema = TipoProblema()
            id_area = area.obtener_id(area_mod_ticket.get())
            id_prioridad = prioridad.obtener_id(prioridad_mod_ticket.get())
            id_estado = estado.obtener_id(estado_mod_ticket.get())
            id_tipo_problema = tipo_problema.obtener_id(tipo_problema_mod_ticket.get())
            if id_tecnico != '':
                id_tecnico = usuario.obtener_id(tecnico_mod_ticket.get())
            ticket.modificar(id_ticket, id_area, id_prioridad, id_estado, id_tipo_problema, id_tecnico, codigo_hardware)
            if id_estado == 5:
                fecha_cierre = strftime('%Y/%m/%d')
                hora_cierre = strftime('%H:%M:%S')
                ticket.archivar(id_ticket, fecha_cierre, hora_cierre)
            widgets_mostrar_tickets.actualizar_treeview()

def eliminar_ticket():
    mensaje = mb.askyesno("eliminar ticket", "¿seguro desea eliminar el ticket?")
    if mensaje == True:
        id_ticket = id_ticket.get()
        ticket = Ticket()
        ticket.eliminar(id_ticket)
        vaciar_entry(widgets_mostrar_tickets.lista_entry)
        actualizar_treeview(Ticket, widgets_mostrar_tickets.treeview)

#===============================================================================================================

def agregar_area():
    nombre = nombre_area.get().strip()
    email = email_area.get().strip()
    telefono = telefono_area.get().strip()
    area = Area()
    for i in area.lista_areas():
        if i[0].lower() == nombre.lower():
            mb.showerror('ERROR', 'Ya existe un área con ese nombre')
            return
    if validar_obligatorios((nombre,)):
        area = Area()
        area.insertar(nombre, email, telefono)
        vaciar_entry(widgets_areas.lista_entry)
        actualizar_treeview(area, widgets_areas.treeview)

def modificar_area():
    mensaje = mb.askyesno('Modificar Área', '¿Seguro desea modificar el área?')
    if mensaje == True:
        id_area = id_mod_area.get()
        nombre = nombre_mod_area.get().strip()
        email = email_mod_area.get().strip()
        telefono = telefono_mod_area.get().strip()
        area = Area()
        if nombre.lower() != area.obtener_nombre(id_area).lower():
            for i in area.lista_areas():
                if i[0].lower() == nombre.lower():
                    mb.showerror('ERROR', 'Ya existe un área con ese nombre')
                    return
        if validar_obligatorios((nombre,)):
            area = Area()
            area.modificar(id_area, nombre, email, telefono)
            actualizar_treeview(area, widgets_areas.treeview)

def eliminar_area():
    mensaje = mb.askyesno('Eliminar Área', '¿Seguro desea eliminar el área?')
    if mensaje == True:
        id_area = id_mod_area.get()
        area = Area()
        area.eliminar(id_area)
        vaciar_entry(widgets_areas.lista_entry_mod)
        for i in widgets_areas.lista_entry_mod:
            i.config(state='disabled')
        widgets_areas.button_eliminar.config(state='disabled')
        widgets_areas.button_modificar.config(state='disabled')
        actualizar_treeview(area, widgets_areas.treeview)


def agregar_tipo_problema():
    nombre = nombre_tipo_problema.get().strip()
    tipo_problema = TipoProblema()
    for i in tipo_problema.lista_tipos_problema():
        if i[0].lower() == nombre.lower():
            mb.showerror('ERROR', 'Ya existe un tipo de problema con ese nombre')
            return
    if validar_obligatorios((nombre,)):
        tipo_problema = TipoProblema()
        tipo_problema.insertar(nombre)
        vaciar_entry(widgets_tipos_problema.lista_entry)
        actualizar_treeview(tipo_problema, widgets_tipos_problema.treeview)

def modificar_tipo_problema():
    mensaje = mb.askyesno('Modificar Tipo de Problema', '¿Seguro desea modificar el tipo de problema?')
    if mensaje == True:
        id_tipo_problema = id_mod_tipo_problema.get()
        nombre = nombre_mod_tipo_problema.get().strip()
        tipo_problema = TipoProblema()
        if nombre.lower() != tipo_problema.obtener_nombre(id_tipo_problema).lower():
            for i in tipo_problema.lista_tipos_problema():
                if i[0].lower() == nombre.lower():
                    mb.showerror('ERROR', 'Ya existe un tipo de problema con ese nombre')
                    return
        if validar_obligatorios((nombre,)):
            tipo_problema.modificar(id_tipo_problema, nombre)
            actualizar_treeview(tipo_problema, widgets_tipos_problema.treeview)

def eliminar_tipo_problema():
    mensaje = mb.askyesno('Eliminar Tipo de Problema', '¿Seguro desea eliminar el tipo de problema?')
    if mensaje == True:
        id_tipo_problema = id_mod_tipo_problema.get()
        area = TipoProblema()
        area.eliminar(id_tipo_problema)
        vaciar_entry(widgets_tipos_problema.lista_entry_mod)
        widgets_tipos_problema.lista_entry_mod[0].config(state='disabled')
        widgets_tipos_problema.button_eliminar.config(state='disabled')
        widgets_tipos_problema.button_modificar.config(state='disabled')
        actualizar_treeview(area, widgets_tipos_problema.treeview)


def iniciar_sesion():
    global usuario_actual
    nombre_usuarioo = nombre_usuario_iniciar.get().lower()
    contraseña = contraseña_iniciar.get()
    usuario = Usuario()
    for i in usuario.lista_usuarios():
        if i[0] == nombre_usuarioo:
            # usuario.validar_contraseña(nombre_usuarioo, contraseña)
            break
    else:
        mb.showerror('ERROR', 'El nombre de usuario no existe')
        return
    
    if usuario.validar_contraseña(nombre_usuarioo, contraseña) != False:

        global widgets_areas
        global widgets_crear_ticket
        global widgets_mostrar_tickets
        global widgets_crear_pedido
        global widgets_usuarios
        global widgets_tipos_problema

        datos = usuario.mostrar_datos(nombre_usuarioo)
        
        usuario_actual = UsuarioActual(datos[0], datos[1], datos[2], datos[3], datos[4],
                                    datos[5], datos[6], datos[7], datos[8])

        notebook_contenido.forget(widgets_iniciar_sesion.frame)
        notebook_contenido.forget(widgets_registrarse.frame)

        widgets_crear_ticket = WidgetsCrearTicket()

        if usuario_actual.id_tipo_usuario == 1 or usuario_actual.id_tipo_usuario == 2:
            widgets_mostrar_tickets = WidgetsMostrarTickets()
            widgets_areas = WidgetsAreas()
            # widgets_crear_pedido = WidgetsCrearPedido()
            widgets_tipos_problema = WidgetsTiposProblema()
            if usuario_actual.id_tipo_usuario == 1:
                widgets_usuarios = WidgetsUsuarios()

    else:
        mb.showerror('ERROR', 'Contraseña incorrecta')

def crear_pedido():
    print('crear pedido')

def agregar_detalle_pedido():
    print('agregar detalle pedido')

def actualizar_listas():
    global lista_areas
    global lista_tipos_problema
    global lista_tipos_usuario
    global lista_tecnicos
    global lista_prioridades
    global lista_estados

    area = Area()
    areas = area.mostrar()

    lista_areas = []
    for i in areas:
        lista_areas.append(i[1])

    estado = Estado()
    estados = estado.mostrar()

    lista_estados = []
    for i in estados:
        lista_estados.append(i[1])

    tipo_problema = TipoProblema()
    tipos_problema = tipo_problema.mostrar()

    lista_tipos_problema = []
    for i in tipos_problema:
        lista_tipos_problema.append(i[1])

    tipo_usuario = TipoUsuario()
    tipos_usuario = tipo_usuario.mostrar()

    lista_tipos_usuario = []
    for i in tipos_usuario:
        lista_tipos_usuario.append(i[1])

    usuario = Usuario()
    tecnicos = usuario.mostrar_lista_tecnicos()

    lista_tecnicos = []
    for i in tecnicos:
        lista_tecnicos.append(i[0])

    prioridad = Prioridad()
    prioridades = prioridad.mostrar()

    lista_prioridades = []
    for i in prioridades:
        lista_prioridades.append(i[1])

    

def actualizar_comboboxes():
    actualizar_listas()

    widgets_crear_ticket.lista_entry[1].config(values=lista_areas)
    widgets_crear_ticket.lista_entry[2].config(values=lista_tipos_problema)

# endregion

# region principal

carpeta = path.dirname(path.realpath(__file__)[0:-7])
colores = ('#251D3A', '#2A2550', '#E04D01',
           '#FF7700', 'black', 'white', '#C3C3C3')
tamaño_fuente = [1]

ventana = Tk()
# ventana.geometry(f'{ventana.winfo_screenwidth()}x{ventana.winfo_screenheight()}')
ventana.geometry('960x540')
# ventana.geometry('1280x720')
ventana.minsize(640, 480)
ventana.title('Gestión de Tickets')
ventana.config(bg=colores[0])
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)
img_municipalidad = PhotoImage(file=carpeta+'/img/logo_muni.png')

fuente_titulo = Font(family='Segoe UI', size=int(18*tamaño_fuente[0]), slant='italic')
fuente_subtitulo = Font(family='Segoe UI', size=int(14*tamaño_fuente[0]))
fuente_pie = Font(family='Segoe UI', size=int(8*tamaño_fuente[0]))
fuente_button = Font(family='Segoe UI', size=int(12*tamaño_fuente[0]), weight='bold')
fuente_label = Font(family='Segoe UI', size=int(12*tamaño_fuente[0]))
fuente_notebook = Font(family='Segoe UI', size=int(14*tamaño_fuente[0]), weight='bold')

estilo = Style()
estilo.theme_use('alt')

estilo.configure('TCombobox', foreground=colores[4], arrowsize=15, arrowcolor=colores[0])
ventana.option_add('*TCombobox*Font', fuente_label)
ventana.option_add('*TCombobox*Listbox*Font', fuente_label)
estilo.configure('TEntry', foreground=colores[4])
ventana.option_add('*TEntry*Font', fuente_label)
estilo.configure('subtitulo.TEntry')
estilo.configure('TFrame', background=colores[0])
estilo.configure('TLabel', background=colores[0], foreground=colores[5], font=fuente_label)
estilo.configure('titulo.TLabel', background=colores[0], foreground=colores[6], font=fuente_titulo, justify='center')
estilo.configure('subtitulo.TLabel', background=colores[0], foreground=colores[5], font=fuente_subtitulo, justify='center')
estilo.configure('pie.TLabel', background=colores[0], foreground=colores[3], font=fuente_pie)
estilo.configure('TButton', background=colores[2], foreground=colores[5], focuscolor='none', font=fuente_button)
estilo.map('TButton', background=[('active', colores[3])])
estilo.configure('peligro.TButton', background='red', foreground=colores[5], focuscolor='none', font=fuente_button)
estilo.map('peligro.TButton', background=[('active', colores[3])])
estilo.configure('TNotebook', background=colores[1], borderwidth=0)
estilo.configure('TNotebook.Tab', foreground=colores[1], focuscolor='none', font=fuente_button)
estilo.map('TNotebook.Tab', background=[('selected', colores[0]), ('active', colores[5])],
           foreground=[('selected', colores[6])], font=[('selected', fuente_notebook)])
estilo.configure('Treeview', background=colores[5], foreground=colores[4], font=fuente_label)
estilo.configure('Treeview.Heading', background=colores[6], font=fuente_button)
estilo.configure('TScrollbar', arrowsize=15, arrowcolor=colores[0])
estilo.configure('TSpinbox', foreground=colores[4], arrowsize=15, arrowcolor=colores[0])
ventana.option_add('*TSpinbox*Font', fuente_label)
estilo.configure('TCheckbutton', background=colores[0], foreground=colores[4], font=fuente_label)
estilo.map('TCheckbutton', background=[('active', colores[0])])

notebook_contenido = Notebook(ventana)
notebook_contenido.grid(column=0, row=0, sticky='nsew')

label_pie = Label(ventana, style='pie.TLabel',
                  text='Municipalidad de Villa Carlos Paz')
label_pie.grid(column=0, row=1, columnspan=2, sticky='w')

# endregion

# region variables

usuario_actual = None
#=============================
nombre_area = StringVar()
email_area = StringVar()
telefono_area = StringVar()
id_mod_area = IntVar()
nombre_mod_area = StringVar()
email_mod_area = StringVar()
telefono_mod_area = StringVar()
# ===================================
id_mod_usuario = IntVar()
nombre_usuario = StringVar()
apellido_usuario = StringVar()
legajo_usuario = StringVar()
email_usuario = StringVar()
nombre_usuario_usuario = StringVar()
contraseña_usuario = StringVar()
repetir_contraseña_usuario = StringVar()
nombre_mod_usuario = StringVar()
apellido_mod_usuario = StringVar()
legajo_mod_usuario = StringVar()
email_mod_usuario = StringVar()
nombre_usuario_mod_usuario = StringVar()
contraseña_mod_usuario = StringVar()
activo_mod_usuario = IntVar()
tipo_mod_usuario = StringVar()
# ==========================================
nombre_usuario_iniciar = StringVar()
contraseña_iniciar = StringVar()
# ==========================================

asunto_ticket = StringVar()                                    #string var de tickets
area_ticket = StringVar()
prioridad_ticket = StringVar()
tipo_problema_ticket = StringVar()
codigo_hardware_ticket = StringVar()
descripcion_ticket = StringVar()

id_mod_ticket = StringVar()
estado_mod_ticket = StringVar()
asunto_mod_ticket = StringVar()
area_mod_ticket = StringVar()
prioridad_mod_ticket = StringVar()
codigo_hardware_mod_ticket = StringVar()
tecnico_mod_ticket = StringVar()
descripcion_mod_ticket = StringVar()
usuario_mod_ticket = StringVar()
tipo_problema_mod_ticket = StringVar()
fecha_inicio_mod_ticket = StringVar()
fecha_cierre_mod_ticket = StringVar()
hora_inicio_mod_ticket = StringVar()
hora_cierre_mod_ticket = StringVar()

lista_areas = []
lista_tipos_problema = []
lista_tipos_usuario = []
lista_prioridades = []
lista_tecnicos = []
lista_estados = []
lista_articulos = ['Mouse', 'Teclado', 'Monitor', 'Disco Duro', 'SSD']
#====================================
nombre_tipo_problema = StringVar()
id_mod_tipo_problema = IntVar()
nombre_mod_tipo_problema = StringVar()


# endregion

# region widgets


class WidgetsRegistrarse:
    def __init__(self):

        self.frame = Frame()
        self.frame.grid(column=0, row=0, sticky='nsew')
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure((1, 2, 3, 4, 5, 6, 7), weight=1)

        self.label_img_municipalidad = Label(
            self.frame, image=img_municipalidad)
        self.label_img_municipalidad.grid(column=2, row=1, rowspan=8)

        self.label_titulo = Label(
            self.frame, style='titulo.TLabel', text='Registrarse en el Sistema')
        self.label_titulo.grid(column=0, row=0, columnspan=3)

        self.lista_label = [
            Label(self.frame, text='Nombre *'),
            Label(self.frame, text='Apellido *'),
            Label(self.frame, text='Legajo *'),
            Label(self.frame, text='Email *'),
            Label(self.frame, text='Nombre de Usuario *'),
            Label(self.frame, text='Contraseña *'),
            Label(self.frame, text='Repetir Contraseña *')
        ]
        self.lista_entry = [
            Entry(self.frame, textvariable=nombre_usuario),
            Entry(self.frame, textvariable=apellido_usuario),
            Entry(self.frame, textvariable=legajo_usuario),
            Entry(self.frame, textvariable=email_usuario),
            Entry(self.frame, textvariable=nombre_usuario_usuario),
            Entry(self.frame, show='*', textvariable=contraseña_usuario),
            Entry(self.frame, show='*', textvariable=repetir_contraseña_usuario)
        ]

        self.button_registrarse = Button(
            self.frame, text='Registrarse', command=registrar_usuario, cursor='hand2')

        posicionar_formulario(
            self.lista_label, self.lista_entry, self.button_registrarse)

        notebook_contenido.add(self.frame, text='Registrarse')


class WidgetsIniciarSesion:
    def __init__(self):

        self.frame = Frame()
        self.frame.grid(column=0, row=0, sticky='nsew')
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure((1, 2, 3, 4, 5), weight=1)

        self.label_img_municipalidad = Label(self.frame, image=img_municipalidad)
        self.label_img_municipalidad.grid(column=2, row=1, rowspan=8)

        self.label_titulo = Label(self.frame, style='titulo.TLabel', text='Registrarse en el Sistema')
        self.label_titulo.grid(column=0, row=0, columnspan=3)

        self.lista_label = [
            Label(self.frame),
            Label(self.frame, text='Nombre de Usuario *'),
            Label(self.frame, text='Contraseña *'),
            Label(self.frame),
            Label(self.frame)
        ]
        self.lista_entry = [
            Label(self.frame),
            Entry(self.frame, textvariable=nombre_usuario_iniciar),
            Entry(self.frame, show='*', textvariable=contraseña_iniciar),
            Label(self.frame),
            Label(self.frame)
        ]

        self.button_iniciar_sesion = Button(self.frame, text='Iniciar Sesión', command=iniciar_sesion, cursor='hand2')

        posicionar_formulario(
            self.lista_label, self.lista_entry, self.button_iniciar_sesion)

        notebook_contenido.add(self.frame, text='Iniciar Sesión')


class WidgetsUsuarios:
    def __init__(self):

        self.frame = Frame()
        self.frame.grid(column=0, row=0, sticky='nsew')
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)

        self.label_titulo = Label(self.frame, style='titulo.TLabel', text='Usuarios')
        self.label_titulo.grid(column=0, row=0)

        self.frame_treeview = Frame(self.frame)
        self.frame_treeview.grid(
            column=0, row=1, padx=24, pady=(12, 8), sticky='nsew')
        self.frame_treeview.columnconfigure(0, weight=1)
        self.frame_treeview.rowconfigure(0, weight=1)

        self.columnas = ('id', 'tipo_usuario', 'nombre', 'apellido', 'legajo',
                         'email', 'activo', 'nombre_usuario')

        self.treeview = Treeview(self.frame_treeview, columns=self.columnas, height=20, show='headings')

        self.treeview.heading('id', text='ID')
        self.treeview.heading('tipo_usuario', text='Tipo de usuario')
        self.treeview.heading('nombre', text='Nombre')
        self.treeview.heading('apellido', text='Apellido')
        self.treeview.heading('legajo', text='Legajo')
        self.treeview.heading('email', text='Email')
        self.treeview.heading('activo', text='Activo')
        self.treeview.heading('nombre_usuario', text='Nombre de Usuario')

        self.treeview.column('id', minwidth=40, width=0)
        self.treeview.column('tipo_usuario', minwidth=40, width=0)
        self.treeview.column('nombre', minwidth=40, width=0)
        self.treeview.column('apellido', minwidth=40, width=0)
        self.treeview.column('legajo', minwidth=40, width=0)
        self.treeview.column('email', minwidth=40, width=0)
        self.treeview.column('activo', minwidth=40, width=0)
        self.treeview.column('nombre_usuario', minwidth=40, width=0)

        self.treeview.grid(column=0, row=0, sticky='nsew')

        self.scrollbar = Scrollbar( self.frame_treeview, command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        self.button_modificar = Button(self.frame, text='Modificar', command=mostrar_usuario, state='disabled', cursor='hand2')
        self.button_modificar.grid(column=0, row=2, padx=24, pady=(12, 8), ipadx=16, ipady=6, sticky='e')

        self.lista_variables_mod = [None, tipo_mod_usuario, nombre_mod_usuario, apellido_mod_usuario, legajo_mod_usuario,
                                    email_mod_usuario, activo_mod_usuario, nombre_usuario_mod_usuario]


        def item_seleccionado(event):
            self.button_modificar.config(state='normal')
            global ventana_emergente
            if ventana_emergente != None:
                ventana_emergente.top.destroy()
                
            try:
                for i in self.treeview.selection():
                    item = self.treeview.item(i)
                    record = item['values']
                    id_mod_usuario.set(record[0])
                for i in range(len(self.lista_variables_mod)):
                    if self.lista_variables_mod[i] != None:
                        self.lista_variables_mod[i].set(record[i])
            except:
                pass
        
        self.treeview.bind('<<TreeviewSelect>>', item_seleccionado)

        self.crear_treeview()

        notebook_contenido.add(self.frame, text='Usuarios')

    def crear_treeview(self):
        self.usuario = Usuario()
        self.tipo_usuario = TipoUsuario()
        self.lista_datos = self.usuario.mostrar()
        for i in self.lista_datos:
            l = list(i)
            l[1] = self.tipo_usuario.obtener_nombre(l[1])
            self.treeview.insert('', 'end', values=l)

    def actualizar_treeview(self):
        self.treeview.delete(*self.treeview.get_children())
        actualizar_comboboxes()
        self.crear_treeview()


class WidgetsModificarUsuario:
    def __init__(self, toplevel):

        self.frame = Frame(toplevel)
        self.frame.grid(column=0, row=0, sticky='nsew')
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure((1, 2, 3, 4, 5, 6, 7), weight=1)

        self.label_img_municipalidad = Label(
            self.frame, image=img_municipalidad)
        self.label_img_municipalidad.grid(column=2, row=1, rowspan=8)

        self.label_titulo = Label(self.frame, style='titulo.TLabel', text='Modificar Usuario')
        self.label_titulo.grid(column=0, row=0, columnspan=3)
        self.label_nombre_usuario = Label(self.frame, style='subtitulo.TLabel', text=nombre_usuario_mod_usuario.get())
        self.label_nombre_usuario.grid(column=0, row=1, columnspan=3)

        self.lista_label = [
            Label(self.frame, text='Nombre *'),
            Label(self.frame, text='Apellido *'),
            Label(self.frame, text='Legajo *'),
            Label(self.frame, text='Email *'),
            Label(self.frame, text='Tipo de Usuario *'),
            Label(self.frame, text='Activo *')
        ]
        self.lista_entry = [
            Entry(self.frame, textvariable=nombre_mod_usuario),
            Entry(self.frame, textvariable=apellido_mod_usuario),
            Entry(self.frame, textvariable=legajo_mod_usuario),
            Entry(self.frame, textvariable=email_mod_usuario),
            Combobox(self.frame, values=lista_tipos_usuario, textvariable=tipo_mod_usuario, state='readonly'),
            Checkbutton(self.frame, text='', variable=activo_mod_usuario)
        ]

        self.button_aceptar = Button(
            self.frame, text='Aceptar', command=modificar_usuario, cursor='hand2')

        posicionar_formulario(self.lista_label, self.lista_entry, self.button_aceptar, row=2)


class WidgetsAreas:
    def __init__(self):

        self.frame = Frame()
        self.frame.grid(column=0, row=0, sticky='nsew')
        self.frame.columnconfigure(0, weight=5)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure((1, 2, 3, 4, 7, 8, 9), weight=1)

        self.label_titulo = Label(self.frame, style='titulo.TLabel', text='Áreas')
        self.label_titulo.grid(column=0, row=0, columnspan=3)

        self.frame_treeview = Frame(self.frame)
        self.frame_treeview.grid(column=0, row=1, rowspan=10, padx=24, pady=(12, 8), sticky='nsew')
        self.frame_treeview.columnconfigure(0, weight=1)
        self.frame_treeview.rowconfigure(0, weight=1)

        self.columnas = ('id', 'nombre', 'email', 'telefono')

        self.treeview = Treeview(self.frame_treeview, columns=self.columnas, height=20, show='headings')

        self.treeview.heading('id', text='ID')
        self.treeview.heading('nombre', text='Nombre')
        self.treeview.heading('email', text='Email')
        self.treeview.heading('telefono', text='Teléfono')

        self.treeview.column('id', minwidth=40, width=0)
        self.treeview.column('nombre', minwidth=40, width=0)
        self.treeview.column('email', minwidth=40, width=0)
        self.treeview.column('telefono', minwidth=40, width=0)

        self.treeview.grid(column=0, row=0, sticky='nsew')

        self.scrollbar = Scrollbar(self.frame_treeview, command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        # 2ª columna

        self.lista_label_mod = [
            Label(self.frame, text='Nombre de Área *'),
            Label(self.frame, text='Email  '),
            Label(self.frame, text='Teléfono  ')
        ]
        self.lista_entry_mod = [
            Entry(self.frame, textvariable=nombre_mod_area, state='disabled'),
            Entry(self.frame, textvariable=email_mod_area, state='disabled'),
            Entry(self.frame, textvariable=telefono_mod_area, state='disabled')
        ]

        self.frame_button = Frame(self.frame)
        self.frame_button.columnconfigure((0, 1), weight=1)

        self.button_modificar = Button(self.frame_button, text='Modificar', command=modificar_area, state='disabled', cursor='hand2')
        self.button_modificar.grid(column=1, row=0, ipadx=16, ipady=6, sticky='e')
        self.button_eliminar = Button(self.frame_button, style='peligro.TButton', text='Eliminar', command=eliminar_area, state='disabled', cursor='hand2')
        self.button_eliminar.grid(column=0, row=0, ipadx=16, ipady=6, sticky='w')

        posicionar_formulario(self.lista_label_mod, self.lista_entry_mod, self.frame_button, column=1)

        self.label_nueva = Label( self.frame, style='titulo.TLabel', text='Nueva Área')
        self.label_nueva.grid(column=1, row=6, columnspan=2)

        self.lista_label = [
            Label(self.frame, text='Nombre de Área *'),
            Label(self.frame, text='Email  '),
            Label(self.frame, text='Teléfono  ')
        ]
        self.lista_entry = [
            Entry(self.frame, textvariable=nombre_area),
            Entry(self.frame, textvariable=email_area),
            Entry(self.frame, textvariable=telefono_area)
        ]

        crear_treeview(Area(), self.treeview)

        self.lista_variables_mod = [
            None, nombre_mod_area, email_mod_area, telefono_mod_area]

        def item_seleccionado(event):
            try:
                for i in self.treeview.selection():
                    item = self.treeview.item(i)
                    record = item['values']
                    id_mod_area.set(record[0])
                for i in range(len(self.lista_variables_mod)):
                    if self.lista_variables_mod[i] != None:
                        self.lista_variables_mod[i].set(record[i])
                self.button_eliminar.config(state='normal')
                self.button_modificar.config(state='normal')
                for i in self.lista_entry_mod:
                    i.config(state='normal')
            except:
                pass

        self.treeview.bind('<<TreeviewSelect>>', item_seleccionado)

        self.button_agregar = Button(
            self.frame, text='Agregar', command=agregar_area, cursor='hand2')

        posicionar_formulario(self.lista_label, self.lista_entry,
                              self.button_agregar, column=1, row=7)

        notebook_contenido.add(self.frame, text='Áreas')


class WidgetsCrearTicket:
    def __init__(self):

        self.frame = Frame()
        self.frame.grid(column=0, row=0, sticky='nsew')
        self.frame.columnconfigure((1, 2), weight=1)
        self.frame.rowconfigure((1, 2, 3, 4, 5, 6), weight=1)

        self.label_titulo = Label(
            self.frame, style='titulo.TLabel', text='Nuevo Ticket')
        self.label_titulo.grid(column=0, row=0, columnspan=2)

        self.lista_label = [
            Label(self.frame, text='Asunto *'),
            Label(self.frame, text='Área *'),
            Label(self.frame, text='Tipo de Problema *'),
            Label(self.frame, text='Código Hardware  '),
            Label(self.frame, text='Descripción *')
        ]

        self.frame_text = Frame(self.frame)
        self.frame_text.columnconfigure(0, weight=1)

        self.text = Text(self.frame_text, height=7, width=0, font=fuente_label)
        self.scrollbar = Scrollbar(self.frame_text, command=self.text.yview)
        self.text.config(yscrollcommand=self.scrollbar.set)
        self.text.grid(column=0, row=0, sticky='nsew')
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        self.lista_entry = [
            Entry(self.frame, textvariable=asunto_ticket),
            Combobox(self.frame, values=lista_areas, textvariable=area_ticket, state='readonly'),
            Combobox(self.frame, values=lista_tipos_problema, textvariable=tipo_problema_ticket, state='readonly'),
            Entry(self.frame, textvariable=codigo_hardware_ticket),
            self.frame_text
        ]

        self.button_crear = Button(self.frame, text='Crear', command=crear_ticket, cursor='hand2')

        posicionar_formulario(self.lista_label, self.lista_entry, self.button_crear)

        notebook_contenido.add(self.frame, text='Crear Ticket')


class WidgetsMostrarTickets:
    def __init__(self):
        self.frame = Frame()
        self.frame.grid(column=0, row=0, sticky='nsew')
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)

        self.label_titulo = Label( self.frame, style='titulo.TLabel', text='Tickets')
        self.label_titulo.grid(column=0, row=0, columnspan=2)

        self.frame_treeview = Frame(self.frame)
        self.frame_treeview.grid(
            column=0, row=1, padx=24, pady=(12, 8), sticky='nsew')
        self.frame_treeview.columnconfigure(0, weight=1)
        self.frame_treeview.rowconfigure(0, weight=1)

        self.columnas = ('numero', 'usuario', 'area', 'estado', 'prioridad',
                         'tecnico', 'asunto', 'fecha_inicio', 'hora_inicio')

        self.treeview = Treeview(self.frame_treeview, columns=self.columnas, height=20, show='headings')

        self.treeview.heading('numero', text='Nº')
        self.treeview.heading('usuario', text='Usuario')
        self.treeview.heading('area', text='Área')
        self.treeview.heading('estado', text='Estado')
        self.treeview.heading('prioridad', text='Prioridad')
        self.treeview.heading('tecnico', text='Técnico')
        self.treeview.heading('asunto', text='Asunto')
        self.treeview.heading('fecha_inicio', text='Fecha')
        self.treeview.heading('hora_inicio', text='Hora')

        self.treeview.column('numero', minwidth=40, width=0)
        self.treeview.column('usuario', minwidth=40, width=0)
        self.treeview.column('area', minwidth=40, width=0)
        self.treeview.column('estado', minwidth=40, width=0)
        self.treeview.column('prioridad', minwidth=40, width=0)
        self.treeview.column('tecnico', minwidth=40, width=0)
        self.treeview.column('asunto', minwidth=40)
        self.treeview.column('fecha_inicio', minwidth=40, width=40)
        self.treeview.column('hora_inicio', minwidth=40, width=40)

        
        def item_seleccionado(event):
            self.button_modificar.config(state='normal')
            if ventana_emergente != None:
                ventana_emergente.top.destroy()
            try:
                for i in self.treeview.selection():
                    item = self.treeview.item(i)
                    record = item['values']
                    id_mod_ticket.set(record[0])
            except:
                pass


        self.treeview.bind('<<TreeviewSelect>>', item_seleccionado)

        self.treeview.grid(column=0, row=0, sticky='nsew')

        self.scrollbar = Scrollbar(self.frame_treeview, command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        self.button_modificar = Button(self.frame, text='Mostrar', command=mostrar_ticket, state='disabled', cursor='hand2')
        self.button_modificar.grid(column=0, row=2, padx=24, pady=(12, 8), ipadx=16, ipady=6, sticky='e')

        
        self.crear_treeview()
        notebook_contenido.add(self.frame, text='Mostrar Tickets')

    def crear_treeview(self):
        self.ticket = Ticket()
        self.usuario = Usuario()
        self.area = Area()
        self.estado = Estado()
        self.prioridad = Prioridad()
        self.lista_datos = self.ticket.mostrar_resumido()
        for i in self.lista_datos:
            l = list(i)
            l[1] = self.usuario.obtener_campo('nombre_usuario', l[1])
            l[2] = self.area.obtener_nombre(l[2])
            l[3] = self.estado.obtener_nombre(l[3])
            l[4] = self.prioridad.obtener_nombre(l[4])
            l[5] = self.usuario.obtener_campo('nombre_usuario', l[5])
            self.treeview.insert('', 'end', values=l)

    def actualizar_treeview(self):
        self.treeview.delete(*self.treeview.get_children())
        actualizar_comboboxes()
        self.crear_treeview()


class WidgetsModificarTicket:
    def __init__(self, toplevel):

        self.frame = Frame(toplevel)
        self.frame.grid(column=0, row=0, sticky='nsew')
        self.frame.columnconfigure(1, weight=2)
        self.frame.columnconfigure((1,3,5), weight=1)
        self.frame.rowconfigure((1,2,3,4,5), weight=1)

        self.label_titulo = Label(self.frame, style='titulo.TLabel', text='Modificar Ticket')
        self.label_titulo.grid(column=0, row=0, columnspan=6)

        self.entry_asunto = Entry(self.frame, style='subtitulo.TEntry', textvariable=asunto_mod_ticket, state='readonly', font=fuente_button)
        self.entry_asunto.grid(column=0, row=1, columnspan=4, padx=24, ipady=3, sticky='ew')

        self.entry_hora = Entry(self.frame, textvariable=hora_inicio_mod_ticket, width=0, state='readonly')
        self.entry_hora.grid(column=4, row=1, padx=(24,8), ipady=3, sticky='ew')

        self.entry_fecha = Entry(self.frame, textvariable=fecha_inicio_mod_ticket, width=0, state='readonly')
        self.entry_fecha.grid(column=5, row=1, padx=(24,8), ipady=3, sticky='ew')

        if fecha_cierre_mod_ticket.get() != 'None':

            self.label_hora_fecha = Label(self.frame, text='Hora y Fecha de Cierre')
            self.label_hora_fecha.grid(column=2, row=2, columnspan=2, sticky='e')
            self.entry_hora_cierre = Entry(self.frame, textvariable=hora_cierre_mod_ticket, width=0, state='readonly')
            self.entry_hora_cierre.grid(column=4, row=2, padx=(24,8), ipady=3, sticky='ew')
            self.entry_fecha_cierre = Entry(self.frame, textvariable=fecha_cierre_mod_ticket, width=0, state='readonly')
            self.entry_fecha_cierre.grid(column=5, row=2, padx=(24,8), ipady=3, sticky='ew')

        self.combobox_estado = Combobox(self.frame, textvariable=estado_mod_ticket, values=lista_estados, state='readonly')
        self.combobox_estado.grid(column=0, row=2, columnspan=2, padx=(24,8), ipady=3, sticky='ew')

        self.lista_label = [
            Label(self.frame, text='Usuario  '),
            Label(self.frame, text='Área *')
        ]
        self.lista_entry = [
            Entry(self.frame, textvariable=usuario_mod_ticket, state='readonly'),
            Combobox(self.frame, textvariable=area_mod_ticket, values=lista_areas, state='readonly')
        ]
        self.lista_label_2 = [
            Label(self.frame, text='Tipo Problema *'),
            Label(self.frame, text='Código Hardware  ')
        ]
        self.lista_entry_2 = [
            Combobox(self.frame, textvariable=tipo_problema_mod_ticket, values=lista_tipos_problema, state='readonly'),
            Entry(self.frame, textvariable=codigo_hardware_mod_ticket)
        ]
        self.lista_label_3 = [
            Label(self.frame, text='Prioridad *'),
            Label(self.frame, text='Técnico  ')
        ]
        self.lista_entry_3 = [
            Combobox(self.frame, textvariable=prioridad_mod_ticket, values=lista_prioridades, state='readonly'),
            Combobox(self.frame, textvariable=tecnico_mod_ticket, values=lista_tecnicos, state='readonly')
        ]

        self.frame_text = Frame(self.frame)
        self.frame_text.columnconfigure(0, weight=1)

        self.text = Text(self.frame_text, height=12, width=0, font=fuente_label)
        self.text.insert('1.0', descripcion_mod_ticket.get())
        self.text.config(state='disabled')
        self.scrollbar = Scrollbar(self.frame_text, command=self.text.yview)
        self.text.config(yscrollcommand=self.scrollbar.set)
        self.text.grid(column=0, row=0, sticky='nsew')
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        self.frame_text.grid(column=0, row=5, columnspan=4, padx=24, ipady=3, sticky='ew')

        self.button_aceptar = Button(self.frame, text='Aceptar', command=modificar_ticket, cursor='hand2')

        posicionar_formulario(self.lista_label, self.lista_entry, row=3)
        posicionar_formulario(self.lista_label_2, self.lista_entry_2, column=2, row=3)
        posicionar_formulario(self.lista_label_3, self.lista_entry_3, column=4, row=3)

        self.button_modificar = Button(self.frame, text='Modificar', command=modificar_ticket, cursor='hand2')
        self.button_modificar.grid(column=4, row=6, columnspan=2, padx=24, pady=(12, 8), ipadx=16, ipady=6, sticky='e')


class WidgetsCrearPedido():
    def __init__(self):

        self.frame = Frame()
        self.frame.grid(column=0, row=0, sticky='nsew')
        self.frame.columnconfigure((1, 3), weight=1)
        self.frame.rowconfigure((1, 2, 3, 4, 5, 6), weight=1)

        self.label_titulo = Label(self.frame, style='titulo.TLabel', text='Nuevo Pedido de Abastecimiento')
        self.label_titulo.grid(column=0, row=0, columnspan=4)

        self.lista_label = [
            Label(self.frame, text='Artículo *'),
            Label(self.frame, text='Modelo *'),
            Label(self.frame, text='Cantidad *'),
            Label(self.frame, text='Descripción  ')
        ]

        self.frame_descripcion = Frame(self.frame)
        self.frame_descripcion.columnconfigure(0, weight=1)

        self.frame_text = Frame(self.frame)
        self.frame_text.columnconfigure(0, weight=1)

        self.text = Text(self.frame_text, height=7, width=0, font=fuente_label)
        scrollbar = Scrollbar(self.frame_text, command=self.text.yview)
        self.text.config(yscrollcommand=scrollbar.set)
        self.text.grid(column=0, row=0, sticky='nsew')
        scrollbar.grid(row=0, column=1, sticky='ns')


        self.lista_entry = [
            Combobox(self.frame, values=lista_articulos, state='readonly'),
            Entry(self.frame),
            Spinbox(self.frame, from_=1, to=9999),
            self.frame_text
        ]

        self.button_agregar_detalle = Button(
            self.frame, text='Agregar', command=agregar_detalle_pedido, cursor='hand2')

        posicionar_formulario(self.lista_label, self.lista_entry,
                              self.button_agregar_detalle, row=3)

        # 2ª columna

        self.lista_label_detalle = [
            Label(self.frame, text='Ticket Nº'),
            Label(self.frame, text='Código de Pedido *')
        ]

        self.lista_entry_detalle = [
            Entry(self.frame, state='readonly'),
            Entry(self.frame)
        ]

        posicionar_formulario(self.lista_label_detalle,
                              self.lista_entry_detalle, column=2, row=1)

        self.frame_detalle = Frame(self.frame)
        self.frame_detalle.grid(
            column=2, row=3, columnspan=2, rowspan=4, padx=24, pady=(12, 8), sticky='nsew')
        self.frame_detalle.columnconfigure(0, weight=1)
        self.frame_detalle.rowconfigure(0, weight=1)

        self.columnas = ('articulo', 'modelo', 'cantidad', 'descripcion')

        self.treeview = Treeview(
            self.frame_detalle, columns=self.columnas, height=0, show='headings')

        self.treeview.heading('articulo', text='Artículo')
        self.treeview.heading('modelo', text='Modelo')
        self.treeview.heading('cantidad', text='Cantidad')
        self.treeview.heading('descripcion', text='Descripción')

        self.treeview.column('articulo', minwidth=40, width=0)
        self.treeview.column('modelo', minwidth=40, width=0)
        self.treeview.column('cantidad', minwidth=40, width=0)
        self.treeview.column('descripcion', minwidth=40)

        def item_seleccionado(event):
            for i in self.treeview.selection():
                item = self.treeview.item(i)
                record = item['values']
                print(', '.join(record))

        self.treeview.bind('<<TreeviewSelect>>', item_seleccionado)

        self.treeview.grid(column=0, row=0, sticky='nsew')

        self.scrollbar = Scrollbar(
            self.frame_detalle, command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        self.button_crear = Button(
            self.frame, text='Crear', command=crear_pedido, cursor='hand2')
        self.button_crear.grid(column=3, row=7, padx=24, pady=(
            12, 8), ipadx=16, ipady=6, sticky='e')

        notebook_contenido.add(self.frame, text='Crear Pedido')

class WidgetsTiposProblema:
    def __init__(self):
        self.frame = Frame()
        self.frame.grid(column=0, row=0, sticky='nsew')
        self.frame.columnconfigure(0, weight=5)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure((2, 3, 5, 7), weight=1)

        self.label_titulo = Label(self.frame, style='titulo.TLabel', text='Tipos de Problema')
        self.label_titulo.grid(column=0, row=0, columnspan=3)
        self.label_subtitulo = Label(self.frame, style='subtitulo.TLabel', text='(Utilizados para clasificar Tickets)')
        self.label_subtitulo.grid(column=0, row=1, columnspan=3)

        self.frame_treeview = Frame(self.frame)
        self.frame_treeview.grid(column=0, row=2, rowspan=6, padx=24, pady=(12, 8), sticky='nsew')
        self.frame_treeview.columnconfigure(0, weight=1)
        self.frame_treeview.rowconfigure(0, weight=1)

        self.columnas = ('id', 'nombre')

        self.treeview = Treeview(self.frame_treeview, columns=self.columnas, height=20, show='headings')

        self.treeview.heading('id', text='ID')
        self.treeview.heading('nombre', text='Nombre')
        
        self.treeview.column('id', minwidth=40, width=0)
        self.treeview.column('nombre', minwidth=40, width=0)

        self.treeview.grid(column=0, row=0, sticky='nsew')

        self.scrollbar = Scrollbar(self.frame_treeview, command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        # 2ª columna

        self.lista_label_mod = [
            Label(self.frame, text='Tipo de Problema *')
        ]
        self.lista_entry_mod = [
            Entry(self.frame, textvariable=nombre_mod_tipo_problema, state='readonly')
        ]

        self.frame_button = Frame(self.frame)
        self.frame_button.columnconfigure((0, 1), weight=1)

        self.button_modificar = Button(self.frame_button, text='Modificar', command=modificar_tipo_problema, state='disabled', cursor='hand2')
        self.button_modificar.grid(column=1, row=0, ipadx=16, ipady=6, sticky='e')
        self.button_eliminar = Button(self.frame_button, style='peligro.TButton', text='Eliminar', command=eliminar_tipo_problema, state='disabled', cursor='hand2')
        self.button_eliminar.grid(column=0, row=0, ipadx=16, ipady=6, sticky='w')

        posicionar_formulario(self.lista_label_mod, self.lista_entry_mod, self.frame_button, column=1, row=3)

        self.label_nueva = Label( self.frame, style='titulo.TLabel', text='Nuevo Tipo de Problema')
        self.label_nueva.grid(column=1, row=5, columnspan=2)

        self.lista_label = [
            Label(self.frame, text='Tipo de Problema *')
        ]
        self.lista_entry = [
            Entry(self.frame, textvariable=nombre_tipo_problema)
        ]

        crear_treeview(TipoProblema(), self.treeview)

        self.lista_variables_mod = [None, nombre_mod_tipo_problema]

        def item_seleccionado(event):
            try:
                for i in self.treeview.selection():
                    item = self.treeview.item(i)
                    record = item['values']
                    id_mod_tipo_problema.set(record[0])
                for i in range(len(self.lista_variables_mod)):
                    if self.lista_variables_mod[i] != None:
                        self.lista_variables_mod[i].set(record[i])
                self.lista_entry_mod[0].config(state='normal')
                self.button_eliminar.config(state='normal')
                self.button_modificar.config(state='normal')
            except:
                pass

        self.treeview.bind('<<TreeviewSelect>>', item_seleccionado)

        self.button_agregar = Button(self.frame, text='Agregar', command=agregar_tipo_problema, cursor='hand2')

        posicionar_formulario(self.lista_label, self.lista_entry, self.button_agregar, column=1, row=7)

        notebook_contenido.add(self.frame, text='Tipos de Problema')

class VentanaEmergente:
    def __init__(self):
        self.top = Toplevel(ventana)
        self.top.config()
        self.top.geometry('800x600')
        self.top.title('Modificacion Usuario')
        self.top.columnconfigure(0, weight=1)
        self.top.rowconfigure(0, weight=1)

class UsuarioActual:
    def __init__(self, id_usuario, id_tipo_usuario, nombre, apellido,
                 legajo, email, activo, nombre_usuario, contraseña):
        self.id_usuario = id_usuario
        self.id_tipo_usuario = id_tipo_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
        self.email = email
        self.activo = activo
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña

# endregion

actualizar_listas()
ventana_emergente = None
widgets_iniciar_sesion = WidgetsIniciarSesion()
widgets_registrarse = WidgetsRegistrarse()
widgets_areas = None
widgets_mostrar_tickets = None
widgets_crear_pedido = None
widgets_usuarios = None
widgets_tipos_problema = None

# widgets_areas = WidgetsAreas()
# widgets_crear_ticket = WidgetsCrearTicket()
# widgets_mostrar_tickets = WidgetsMostrarTickets()
# widgets_crear_pedido = WidgetsCrearPedido()
# widgets_usuarios = WidgetsUsuarios()
# widgets_tipos_problema = WidgetsTiposProblema()

ventana.mainloop()
