import tkinter as tk
from tkinter import font as tkFont
from tkinter import ttk
import data_base



def create_table(parent, headers, height=10):
    tree_view = ttk.Treeview(parent, columns=headers, show='headings', height=height)

    for header in headers:
        tree_view.heading(header, text=header.title())
        tree_view.column(header, stretch=True, width=tkFont.Font().measure(header.title()))

    return tree_view



# VENTANA  DE BUSQUEDA POR FECHA DESDE/HASTA
def search_by_date():
    # DEFINICIÓN DE VARIABLES DE CONTROL
    from_entry_control_var = tk.StringVar()
    to_entry_control_var = tk.StringVar()
    client_search_control_var = tk.StringVar()
    id_search_control_var = tk.StringVar()

    # FUNCIONES

    # DE BUSQUEDA
    def search(treeview):

        # ELIMINA LAS COLUMNAS PREVIAMENTE CARGADAS PARA QUE NO SE DUPLIQUEN
        items = treeview.get_children()
        for item in items:
            treeview.delete(item)


        print(from_entry_control_var.get(),
            to_entry_control_var.get())
            
        found_checks = data_base.search_check_date_in_db(from_entry_control_var.get(),
                                                            to_entry_control_var.get())

        for check in found_checks:
            treeview.insert('', 'end', values=check)


    window_date_search = tk.Toplevel()
    window_date_search.title('BUSCAR CHEQUES POR FECHA')
    window_date_search.geometry('800x400')
    window_date_search.resizable(False,False)
    # Foco automático sobre la ventana que se abre
    window_date_search.focus()
    # CON GRAB_SET NO PERMITe ACCEDER A LA VENTANA ANTERIOR MIENTRAS LA VENTANA ACTUAL SIGA ABIERTA
    window_date_search.grab_set()




    # FRAMES
    frame_labels_buttons = tk.Frame(window_date_search, width=700, height=100)
    frame_labels_buttons.pack(fill='x')

    frame_table = tk.Frame(window_date_search, width=700, height=300)
    frame_table.pack(fill='x')

    # CAMPOS DE ENTRADA

    from_label = tk.Label(frame_labels_buttons, text='Desde:').grid(row=1, column=0)
    to_label = tk.Label(frame_labels_buttons, text='Hasta:').grid(row=1, column=2)

    from_entry_date = tk.Entry(frame_labels_buttons, textvariable=from_entry_control_var)
    from_entry_date.grid(row=1, column=1)
    # PONEMOS EL FOCO SOBRE EL WIDGET DE ENTRADA
    from_entry_date.focus_set()

    to_entry_date = tk.Entry(frame_labels_buttons, textvariable=to_entry_control_var)
    to_entry_date.grid(row=1, column=3)
    

    # BOTONES
    button_close = tk.Button(frame_labels_buttons,
                        text='Cancelar',
                        command=window_date_search.destroy).grid(row=0, column=0, padx=10, pady=10)
    button_search = tk.Button(frame_labels_buttons,
                        text='Buscar',
                        command=lambda:search(tree_table_date)).grid(row=1, column=4, padx=10, pady=10)           

    # TABLE
    headers = ('Fecha de carga', 'ID', 'Cliente', 'Banco', 'N° cheque', 'Importe','Fecha de cobro', 'Destino')
    
    tree_table_date = create_table(frame_table, headers=headers, height=14)

    tree_table_date.pack(fill='both')

    all_checks_loaded = data_base.load_all_checks()

    for check in all_checks_loaded:
        tree_table_date.insert('', 'end', values=check)

        for i, item in enumerate(check):
            widht_col = tkFont.Font().measure(item)
            if tree_table_date.column(headers[i], width=None) < widht_col:
                tree_table_date.column(headers[i], width=widht_col)

def search_by_id():
    pass

def search_by_client():
    pass         

# VENTANA DE BUSQUEDA PRINCIPAL

def search_check():
    window_search = tk.Toplevel()
    window_search.title('BUSCAR CHEQUES')
    window_search.geometry('500x400')
    window_search.resizable(False,False)
    # Foco automático sobre la ventana que se abre
    window_search.focus()
    window_search.grab_set()

    # BOTONES PÁGINA PRINCIPAL DE BUSQUEDA
    button_return = tk.Button(window_search,
                        text='Volver',
                        command=window_search.destroy).grid(row=0, column=0, padx=10, pady=10)
    
    button_date = tk.Button(window_search,
                         text='Por fecha',
                         width=15,
                         height=3,
                         command=search_by_date).grid(row=1, column=5, padx=10, pady=10)
    
    button_id = tk.Button(window_search,
                       text='Por ID',
                       width=15,
                       height=3,
                       command=search_by_id).grid(row=2, column=5, padx=10, pady=10)
    
    button_client = tk.Button(window_search,
                           text='Por cliente',
                           width=15,
                           height=3,
                           command=search_by_client).grid(row=3, column=5, padx=10, pady=10)





