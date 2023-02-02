import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
import upload_check
import search_check
import data_base
import sys

# CREA BASE DE DATOS
data_base.insert_check_in_db()

def proximamente():
        window_proximamente = tk.Toplevel()
        window_proximamente.title('PROXIMAMENTE')
        window_proximamente.geometry('350x200')
        window_proximamente.resizable(False,False)
        # Foco automático sobre la ventana que se abre
        window_proximamente.focus()
        tk.Label(window_proximamente, text='PROXIMAMENTE', font=30).pack(pady=20)
        button_return = tk.Button(window_proximamente,
                        text='Volver',
                        command=window_proximamente.destroy).pack(pady=20)


def create_table(parent, headers, height=10):
    tree_view = ttk.Treeview(parent, columns=headers, show='headings', height=height)

    for header in headers:
        tree_view.heading(header, text=header.title())
        tree_view.column(header, stretch=True, width=tkFont.Font().measure(header.title()))

    return tree_view



# VENTANA PRINCIPAL - RAÍZ
root = tk.Tk()
root.title('Gestor de cheques')
# INICIA LA VENTANA MIXIMIZADA
root.state('zoomed')
root.geometry('800x600')

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=3)


# FRAMES
frame_header = tk.Frame(root, bg='blue',width=800, height=50)
frame_header.grid(row=0, column=0, columnspan=2, sticky='nsew')
frame_header.columnconfigure(0, weight=1)

frame_buttons = tk.Frame(root, bg='green', width=300, height=550)
frame_buttons.grid(row=1, column=0, sticky='nsew')
frame_buttons.columnconfigure(0, weight=1)

frame_ad = tk.Frame(root, bg='red', width=500, height=550)
frame_ad.grid(row=1, column=1, sticky='nsew')
frame_ad.columnconfigure(0, weight=1)
frame_ad.rowconfigure(0, weight=1)
frame_ad.rowconfigure(1, weight=1)

# ETIQUETA
label_header = tk.Label(frame_header, text='GESTOR DE CHEQUES', font=('arial',30, 'bold'))
label_header.grid(row=0, column=0, rowspan=2, sticky='nsew', pady=20)

label_ad = tk.Label(frame_ad, text='CHEQUES AL DÍA', font=('arial',20, 'bold'))
label_ad.grid(row=0, column=0, sticky='ew')

# BOTONES
# CARGAR UN NUEVO CHEQUE
button_load = tk.Button(frame_buttons, command=upload_check.upload_check)
button_load.config(text='Cargar cheque', width=15, height=2, font=('arial', 20))
button_load.grid(row=0, column=0, pady=10, padx=10, sticky='nsew')

# BUSCAR CHEQUE
button_search = tk.Button(frame_buttons, command=search_check.search_check)
button_search.config(text='Buscar cheque', width=15, height=2, font=('arial', 20))
button_search.grid(row=1, column=0, padx=10, sticky='nsew')

# OPCIONES
button_option = tk.Button(frame_buttons, command=proximamente, state='disabled')
button_option.config(text='Opciones', width=15, height=2, font=('arial', 20))
button_option.grid(row=2, column=0, pady=10, padx=10, sticky='nsew')

# SALIR DEL PROGRAMA
button_exit = tk.Button(frame_buttons, command=sys.exit)
button_exit.config(text='Salir', width=15, height=2, font=('arial', 20))
button_exit.grid(row=3, column=0, padx=10, sticky='nsew')

# CREA TABLA CON LOS REGISTROSDE LOS CHEQUES
headers = ('Fecha de carga', 'ID', 'Cliente', 'Banco', 'N° cheque', 'Importe','Fecha de cobro', 'Destino')
    
tree_table_date = create_table(frame_ad, headers=headers)
tree_table_date.grid(row=1, column=0, sticky='new', padx=10, pady=10)

all_checks_loaded = data_base.load_all_checks()

#print(all_checks_loaded)
for check in all_checks_loaded:
    tree_table_date.insert('', 'end', values=check)

    for i, item in enumerate(check):
        widht_col = tkFont.Font().measure(item)
        if tree_table_date.column(headers[i], width=None) < widht_col:
            tree_table_date.column(headers[i], width=widht_col)

# para eliminar fila usar np.delete(arreglo, indice, axis= 0 p/filas, 1 p/columnas)

root.mainloop()