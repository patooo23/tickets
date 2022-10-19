from os import path
from tkinter import PhotoImage, IntVar, StringVar, Tk, Text, messagebox as mb
from tkinter.ttk import Button, Combobox, Entry, Frame, Label, Notebook, Scrollbar, Spinbox, Style, Treeview
from tkinter.font import Font
from turtle import bgcolor
from clases import *


#region funciones

def posicionar_formulario(lista_label, lista_entry, button=None, column=0, row=1):
    row_label = row
    row_entry = row
    for i in lista_label:
        i.grid(column=column, row=row_label, padx=(24, 8), ipady=3, sticky='e')
        row_label += 1
    for i in lista_entry:
        i.grid(column=column+1, row=row_entry, padx=(8, 24), ipady=3, sticky='ew')
        row_entry += 1
    if button != None:
        button.grid(column=column+1, row=row_entry, padx=24, pady=(12,8), ipadx=16, ipady=6, sticky='e')

def text_con_scrollbar(frame):

    frame_text = Frame(frame)
    frame_text.columnconfigure(0, weight=1)

    text = Text(frame_text, height=7, width=0, font=fuente_label)
    scrollbar = Scrollbar(frame_text, command=text.yview)
    text.config(yscrollcommand=scrollbar.set)
    text.grid(column=0, row=0, sticky='nsew')
    scrollbar.grid(row=0, column=1, sticky='ns')

    return frame_text

def vaciar_entry(lista_entry):
    for i in lista_entry:
        i.delete(0, 'end')

def actualizar_treeview(clase, treeview):
    treeview.delete(*treeview.get_children())
    for i in clase.mostrar():
        treeview.insert('', 'end', values=i)

def registrar_usuario():
    nombre = nombre_usuario.get()
    apellido = apellido_usuario.get()
    legajo = legajo_usuario.get()
    email =email_usuario.get()
    nombre_usuarioo = nombre_usuario_usuario.get()#esta variable tiene dos o porque no andaba el get del nombre
    contraseña = contraseña_usuario.get()
    usuario = Usuario()
    usuario.insertar(nombre, apellido, legajo, email, nombre_usuarioo, contraseña)
    vaciar_entry(widgets_usuarios)
    actualizar_treeview(usuario, widgets_usuarios.treeview)

#=========================================================================================
def agregar_area():
    nombre = nombre_area.get()
    email = email_area.get()
    telefono = telefono_area.get()
    area = Area()
    area.insertar(nombre, email, telefono)
    vaciar_entry(widgets_areas.lista_entry)
    actualizar_treeview(area, widgets_areas.treeview)

def modificar_area():
    id_area = id_mod_area.get()
    nombre = nombre_mod_area.get()
    email = email_mod_area.get()
    telefono = telefono_mod_area.get()
    area = Area()
    area.modificar(id_area, nombre, email, telefono)
    vaciar_entry(widgets_areas.lista_entry)
    actualizar_treeview(area, widgets_areas.treeview)

def eliminar_area():
    mensaje = mb.askyesno("eliminar area", "¿seguro desea eliminar el area?")
    if mensaje == True:
        id_area = id_mod_area.get()
        area = Area()
        area.eliminar(id_area)
        vaciar_entry(widgets_areas.lista_entry)
        actualizar_treeview(area, widgets_areas.treeview)

        


def crear_ticket():
    print('crear ticket')

def modificar_ticket():
    print('modificar ticket')

def crear_pedido():
    print('crear pedido')

def agregar_detalle_pedido():
    print('agregar detalle pedido')

lista_areas = ['Palacio', 'Administracion',
              'Computos', 'Modernizacion', 'Cultura', 'Turismo']

lista_prioridades = ['Baja', 'Media', 'Alta']

lista_tecnicos = ['Oscar', 'Camilo', 'Agustin']

lista_articulos = ['Mouse', 'Teclado', 'Monitor', 'Disco Duro', 'SSD']

lista_estados = []

#endregion

#region principal

carpeta = path.dirname(path.realpath(__file__)[0:-7])
colores = ('#251D3A', '#2A2550', '#E04D01', '#FF7700', 'black', 'white', '#C3C3C3')
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
img_municipalidad = img_municipalidad.subsample(2, 2)

fuente_titulo = Font(family='Segoe UI', size=int(18*tamaño_fuente[0]), slant='italic')
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
estilo.configure('TFrame', background=colores[0])
estilo.configure('TLabel', background=colores[0], foreground=colores[5], font=fuente_label)
estilo.configure('titulo.TLabel', background=colores[0], foreground=colores[6], font=fuente_titulo, justify='center')
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


notebook_contenido = Notebook(ventana)
notebook_contenido.grid(column=0, row=0, sticky='nsew')

label_pie = Label(ventana, style='pie.TLabel', text='Municipalidad de Villa Carlos Paz')
label_pie.grid(column=0, row=1, columnspan=2, sticky='w')

#endregion

#region variables

nombre_area = StringVar()
email_area = StringVar()
telefono_area = StringVar()
id_mod_area = IntVar()
nombre_mod_area = StringVar()
email_mod_area = StringVar()
telefono_mod_area = StringVar()
#===================================
nombre_usuario = StringVar()
apellido_usuario = StringVar()
legajo_usuario = StringVar()
email_usuario = StringVar()
nombre_usuario_usuario = StringVar()
contraseña_usuario = StringVar()
nombre_mod_usuario = StringVar()
apellido_mod_usuario = StringVar()
legajo_mod_usuario = StringVar()
email_mod_usuario = StringVar()
nombre_usuario_mod_usuario = StringVar()
contraseña_mod_usuario = StringVar()
#==========================================
#endregion

#region widgets

def widgets_registrarse(self):

    self.frame_registrarse = Frame()
    self.frame_registrarse.grid(column=0, row=0, sticky='nsew')
    self.frame_registrarse.columnconfigure(1, weight=1)
    self.frame_registrarse.columnconfigure(2, weight=1)
    self.frame_registrarse.rowconfigure((1,2,3,4,5,6,7), weight=1)

    self.label_img_municipalidad = Label(self.frame_registrarse, image=img_municipalidad)
    self.label_img_municipalidad.grid(column=2, row=1, rowspan=8)

    self.label_titulo = Label(self.frame_registrarse, style='titulo.TLabel', text='Registrarse en el Sistema')
    self.label_titulo.grid(column=0, row=0, columnspan=3)

    self.lista_label_registrarse = [
        Label(self.frame_registrarse, text='Nombre *'),
        Label(self.frame_registrarse, text='Apellido *'),
        Label(self.frame_registrarse, text='Legajo *'),
        Label(self.frame_registrarse, text='Email *'),
        Label(self.frame_registrarse, text='Nombre de Usuario *'),
        Label(self.frame_registrarse, text='Contraseña *'),
        Label(self.frame_registrarse, text='Repetir Contraseña *')
    ]
    self.lista_entry_registrarse = [
        Entry(self.frame_registrarse, textvariable= nombre_usuario),
        Entry(self.frame_registrarse, textvariable= apellido_usuario),
        Entry(self.frame_registrarse, textvariable= legajo_usuario ),
        Entry(self.frame_registrarse, textvariable= email_usuario),
        Entry(self.frame_registrarse, textvariable= nombre_usuario_usuario),
        Entry(self.frame_registrarse, show='*', textvariable= contraseña_usuario),
        Entry(self.frame_registrarse, show='*')
    ]

    self.button_registrarse = Button(self.frame_registrarse, text='Registrarse', command=registrar_usuario, cursor='hand2')

    posicionar_formulario(self.lista_label_registrarse, self.lista_entry_registrarse, self.button_registrarse)

    notebook_contenido.add(self.frame_registrarse, text='Registrarse')

class WidgetsUsuarios:
    def __init__(self):
        
        self.frame = Frame()
        self.frame.grid(column=0, row=0, sticky='nsew')
        self.frame.columnconfigure((0,1,2), weight=1)
        self.frame.rowconfigure(1, weight=1)

        self.label_titulo = Label(self.frame, style='titulo.TLabel', text='Usuarios')
        self.label_titulo.grid(column=0, row=0, columnspan=3)

        self.frame_treeview = Frame(self.frame)
        self.frame_treeview.grid(column=0, row=1, columnspan=3, padx=24, pady=(12,8), sticky='nsew')
        self.frame_treeview.columnconfigure(0, weight=1)
        self.frame_treeview.rowconfigure(0, weight=1)

        columnas = ('id', 'nombre', 'apellido', 'legajo', 'email', 'tipo_usuario', 'activo')

        self.treeview = Treeview(self.frame_treeview, columns=columnas, height=20, show='headings')

        self.treeview.heading('id', text='ID')
        self.treeview.heading('nombre', text='Nombre')
        self.treeview.heading('apellido', text='Apellido')
        self.treeview.heading('legajo', text='Legajo')
        self.treeview.heading('email', text='Email')
        self.treeview.heading('tipo_usuario', text='Tipo de usuario')
        self.treeview.heading('activo', text='Activo')

        self.treeview.column('id', minwidth=40, width=0)
        self.treeview.column('nombre', minwidth=40, width=0)
        self.treeview.column('apellido', minwidth=40, width=0)
        self.treeview.column('legajo', minwidth=40, width=0)
        self.treeview.column('email', minwidth=40, width=0)
        self.treeview.column('tipo_usuario', minwidth=40, width=0)
        self.treeview.column('activo', minwidth=40, width=0)

        self.treeview.grid(column=0, row=0, sticky='nsew')

        self.scrollbar = Scrollbar(self.frame_treeview, command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        
        self.button_eliminar = Button(self.frame, style='peligro.TButton', text='Eliminar', command=modificar_ticket, cursor='hand2')
        self.button_eliminar.grid(column=2, row=2, padx=24, pady=(12,8), ipadx=16, ipady=6, sticky='e')
        self.button_modificar = Button(self.frame, text='Modificar', command=modificar_ticket, cursor='hand2')
        self.button_modificar.grid(column=1, row=2, padx=24, pady=(12,8), ipadx=16, ipady=6, sticky='e')
        
        notebook_contenido.add(self.frame, text='usuarios')

class WidgetsAreas:
    def __init__(self):
        
        self.frame = Frame()
        self.frame.grid(column=0, row=0, sticky='nsew')
        self.frame.columnconfigure(0, weight=5)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure((1,2,3,4,7,8,9), weight=1)

        self.label_titulo = Label(self.frame, style='titulo.TLabel', text='Áreas')
        self.label_titulo.grid(column=0, row=0, columnspan=3)

        self.frame_treeview = Frame(self.frame)
        self.frame_treeview.grid(column=0, row=1, rowspan=10, padx=24, pady=(12,8), sticky='nsew')
        self.frame_treeview.columnconfigure(0, weight=1)
        self.frame_treeview.rowconfigure(0, weight=1)

        columnas = ('id', 'nombre', 'email', 'telefono')

        self.treeview = Treeview(self.frame_treeview, columns=columnas, height=20, show='headings')

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
            Entry(self.frame, textvariable=nombre_mod_area),
            Entry(self.frame, textvariable=email_mod_area),
            Entry(self.frame, textvariable=telefono_mod_area)
        ]

        self.frame_button = Frame(self.frame)
        self.frame_button.columnconfigure((0,1), weight=1)

        self.button_modificar = Button(self.frame_button, text='Modificar', command=modificar_area, cursor='hand2')
        self.button_modificar.grid(column=1, row=0, ipadx=16, ipady=6, sticky='e')
        self.button_eliminar = Button(self.frame_button, style='peligro.TButton', text='Eliminar', command= eliminar_area, cursor='hand2')
        self.button_eliminar.grid(column=0, row=0, ipadx=16, ipady=6, sticky='w')

        posicionar_formulario(self.lista_label_mod, self.lista_entry_mod, self.frame_button, column=1)

        self.label_nueva = Label(self.frame, style='titulo.TLabel', text='Nueva Área')
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

        actualizar_treeview(Area(), self.treeview)

        self.lista_variables_mod = [None, nombre_mod_area, email_mod_area, telefono_mod_area]

        def item_seleccionado(event):
            for i in self.treeview.selection():
                item = self.treeview.item(i)
                record = item['values']
                id_mod_area.set(record[0])
            for i in range(len(self.lista_variables_mod)):
                if self.lista_variables_mod[i] != None:
                    self.lista_variables_mod[i].set(record[i])

        self.treeview.bind('<<TreeviewSelect>>', item_seleccionado)

        self.button_agregar = Button(self.frame, text='Agregar', command=agregar_area, cursor='hand2')

        posicionar_formulario(self.lista_label, self.lista_entry, self.button_agregar, column=1, row=7)

        notebook_contenido.add(self.frame, text='Áreas')

def widgets_crear_ticket():

    frame_crear_ticket = Frame()
    frame_crear_ticket.grid(column=0, row=0, sticky='nsew')
    frame_crear_ticket.columnconfigure((1,2), weight=1)
    frame_crear_ticket.rowconfigure((1,2,3,4,5,6), weight=1)

    label_titulo = Label(frame_crear_ticket, style='titulo.TLabel', text='Nuevo Ticket')
    label_titulo.grid(column=0, row=0, columnspan=2)

    lista_label_crear_ticket = [
        Label(frame_crear_ticket, text='Asunto *'),
        Label(frame_crear_ticket, text='Área *'),
        Label(frame_crear_ticket, text='Prioridad *'),
        Label(frame_crear_ticket, text='Código Hardware  '),
        Label(frame_crear_ticket, text='Técnico  '),
        Label(frame_crear_ticket, text='Detalle *')
    ]

    lista_entry_crear_ticket = [
        Entry(frame_crear_ticket),
        Combobox(frame_crear_ticket,values=lista_areas, state='readonly'),
        Combobox(frame_crear_ticket,values=lista_prioridades, state='readonly'),
        Entry(frame_crear_ticket),
        Combobox(frame_crear_ticket, values=lista_tecnicos, state='readonly'),
        text_con_scrollbar(frame_crear_ticket)
    ]

    button_crear_ticket = Button(frame_crear_ticket, text='Crear', command=crear_ticket, cursor='hand2')

    posicionar_formulario(lista_label_crear_ticket, lista_entry_crear_ticket, button_crear_ticket)

    notebook_contenido.add(frame_crear_ticket, text='Crear Ticket')

def widgets_mostrar_tickets():

    frame_mostrar_tickets = Frame()
    frame_mostrar_tickets.grid(column=0, row=0, sticky='nsew')
    frame_mostrar_tickets.columnconfigure(0, weight=1)
    frame_mostrar_tickets.rowconfigure(1, weight=1)

    label_titulo = Label(frame_mostrar_tickets, style='titulo.TLabel', text='Tickets')
    label_titulo.grid(column=0, row=0, columnspan=2)

    frame_treeview_tickets = Frame(frame_mostrar_tickets)
    frame_treeview_tickets.grid(column=0, row=1, padx=24, pady=(12,8), sticky='nsew')
    frame_treeview_tickets.columnconfigure(0, weight=1)
    frame_treeview_tickets.rowconfigure(0, weight=1)

    columnas = ('numero', 'nombre', 'area', 'asunto', 'estado', 'fecha_inicio', 'ultima_respuesta')

    treeview_tickets = Treeview(frame_treeview_tickets, columns=columnas, height=20, show='headings')

    treeview_tickets.heading('numero', text='Nº')
    treeview_tickets.heading('nombre', text='Nombre')
    treeview_tickets.heading('area', text='Área')
    treeview_tickets.heading('asunto', text='Asunto')
    treeview_tickets.heading('estado', text='Estado')
    treeview_tickets.heading('fecha_inicio', text='Fecha Inicio')
    treeview_tickets.heading('ultima_respuesta', text='Última Respuesta')

    treeview_tickets.column('numero', minwidth=40, width=0)
    treeview_tickets.column('nombre', minwidth=40, width=0)
    treeview_tickets.column('area', minwidth=40, width=0)
    treeview_tickets.column('asunto', minwidth=40)
    treeview_tickets.column('estado', minwidth=40, width=0)
    treeview_tickets.column('fecha_inicio', minwidth=40, width=0)
    treeview_tickets.column('ultima_respuesta', minwidth=40, width=0)

    # datos ejemplo
    ejemplos_tickets = []
    for i in range(1, 101):
        ejemplos_tickets.append((f'#{i}', f'Nombre {i}', f'Área {i}', f'Asunto {i}', f'Estado {i}', f'Fecha Inicio {i}', f'Última Modificación {i}'))
    for i in ejemplos_tickets:
        treeview_tickets.insert('', 'end', values=i)

    def item_seleccionado(event):
        for i in treeview_tickets.selection():
            item = treeview_tickets.item(i)
            record = item['values']
            print(', '.join(record))
    

    treeview_tickets.bind('<<TreeviewSelect>>', item_seleccionado)

    treeview_tickets.grid(column=0, row=0, sticky='nsew')

    scrollbar_tickets = Scrollbar(frame_treeview_tickets, command=treeview_tickets.yview)
    treeview_tickets.configure(yscrollcommand=scrollbar_tickets.set)
    scrollbar_tickets.grid(row=0, column=1, rowspan=5, sticky='ns')

    button_modificar_ticket = Button(frame_mostrar_tickets, text='Modificar', command=modificar_ticket, cursor='hand2')
    button_modificar_ticket.grid(column=0, row=2, padx=24, pady=(12,8), ipadx=16, ipady=6, sticky='e')

    notebook_contenido.add(frame_mostrar_tickets, text='Mostrar Tickets')

def widgets_crear_pedido():

    frame_crear_pedido = Frame()
    frame_crear_pedido.grid(column=0, row=0, sticky='nsew')
    frame_crear_pedido.columnconfigure((1,3), weight=1)
    frame_crear_pedido.rowconfigure((1,2,3,4,5,6), weight=1)

    label_titulo = Label(frame_crear_pedido, style='titulo.TLabel', text='Nuevo Pedido de Abastecimiento')
    label_titulo.grid(column=0, row=0, columnspan=4)

    lista_label_crear_pedido = [
        Label(frame_crear_pedido, text='Artículo *'),
        Label(frame_crear_pedido, text='Modelo *'),
        Label(frame_crear_pedido, text='Cantidad *'),
        Label(frame_crear_pedido, text='Descripción  ')
    ]

    frame_descripcion = Frame(frame_crear_pedido)
    frame_descripcion.columnconfigure(0, weight=1)

    lista_entry_crear_pedido = [
        Combobox(frame_crear_pedido, values=lista_articulos, state='readonly'),
        Entry(frame_crear_pedido),
        Spinbox(frame_crear_pedido, from_=1, to=9999),
        text_con_scrollbar(frame_crear_pedido)
    ]

    button_agregar_detalle = Button(frame_crear_pedido, text='Agregar', command=agregar_detalle_pedido, cursor='hand2')

    posicionar_formulario(lista_label_crear_pedido, lista_entry_crear_pedido, button_agregar_detalle, row=3)

    # 2ª columna

    lista_label_detalle_pedido = [
        Label(frame_crear_pedido, text='Ticket Nº'),
        Label(frame_crear_pedido, text='Código de Pedido *')
    ]

    lista_entry_detalle_pedido = [
        Entry(frame_crear_pedido, state='readonly'),
        Entry(frame_crear_pedido)
    ]

    posicionar_formulario(lista_label_detalle_pedido, lista_entry_detalle_pedido, column=2, row=1)

    frame_detalle_pedido = Frame(frame_crear_pedido)
    frame_detalle_pedido.grid(column=2, row=3, columnspan=2, rowspan=4, padx=24, pady=(12,8), sticky='nsew')
    frame_detalle_pedido.columnconfigure(0, weight=1)
    frame_detalle_pedido.rowconfigure(0, weight=1)

    columnas = ('articulo', 'modelo', 'cantidad', 'descripcion')

    treeview_pedidos = Treeview(frame_detalle_pedido, columns=columnas, height=0, show='headings')

    treeview_pedidos.heading('articulo', text='Artículo')
    treeview_pedidos.heading('modelo', text='Modelo')
    treeview_pedidos.heading('cantidad', text='Cantidad')
    treeview_pedidos.heading('descripcion', text='Descripción')

    treeview_pedidos.column('articulo', minwidth=40, width=0)
    treeview_pedidos.column('modelo', minwidth=40, width=0)
    treeview_pedidos.column('cantidad', minwidth=40, width=0)
    treeview_pedidos.column('descripcion', minwidth=40)

    def item_seleccionado(event):
        for i in treeview_pedidos.selection():
            item = treeview_pedidos.item(i)
            record = item['values']
            print(', '.join(record))

    treeview_pedidos.bind('<<TreeviewSelect>>', item_seleccionado)

    treeview_pedidos.grid(column=0, row=0, sticky='nsew')

    scrollbar_pedidos = Scrollbar(frame_detalle_pedido, command=treeview_pedidos.yview)
    treeview_pedidos.configure(yscrollcommand=scrollbar_pedidos.set)
    scrollbar_pedidos.grid(row=0, column=1, sticky='ns')

    button_crear_pedido = Button(frame_crear_pedido, text='Crear', command=crear_pedido, cursor='hand2')
    button_crear_pedido.grid(column=3, row=7, padx=24, pady=(12,8), ipadx=16, ipady=6, sticky='e')

    notebook_contenido.add(frame_crear_pedido, text='Crear Pedido')

#endregion

widgets_registrarse()
widgets_areas = WidgetsAreas()
widgets_crear_ticket()
widgets_mostrar_tickets()
widgets_crear_pedido()
widgets_usuarios = WidgetsUsuarios()
ventana.mainloop()
