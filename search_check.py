from tkinter import *

# VENTANA  DE BUSQUEDA POR FECHA DESDE/HASTA
def date_search_gui():

    window_date_search = Toplevel()
    window_date_search.title('BUSCAR CHEQUES POR FECHA')
    window_date_search.geometry('500x400')
    window_date_search.resizable(False,False)
    # Foco automático sobre la ventana que se abre
    window_date_search.focus()

    # CAMPOS DE ENTRADA

    #data_search = Entry(window_search, textvariable=data_search).grid(row=1, column=0, columnspan=4)
    Label(window_date_search, text='Desde:').grid(row=1, column=0)
    Label(window_date_search, text='Hasta:').grid(row=1, column=2)

    data_search_to = Entry(window_date_search).grid(row=1, column=1)
    data_search_from = Entry(window_date_search).grid(row=1, column=3)

def search_check_gui():
    window_search = Toplevel()
    window_search.title('BUSCAR CHEQUES')
    window_search.geometry('500x400')
    window_search.resizable(False,False)
    # Foco automático sobre la ventana que se abre
    window_search.focus()

    # BOTONES PÁGINA PRINCIPAL DE BUSQUEDA
    button_return = Button(window_search,
                        text='Volver',
                        command=window_search.destroy).grid(row=0, column=0, padx=10, pady=10)
    
    button_date = Button(window_search,
                         text='Por fecha',
                         width=15, height=3,
                         command=date_search_gui).grid(row=1, column=5, padx=10, pady=10)
    
    button_id = Button(window_search,
                       text='Por ID',
                       width=15,
                       height=3).grid(row=2, column=5, padx=10, pady=10)
    
    button_client = Button(window_search,
                           text='Por cliente',
                           width=15,
                           height=3).grid(row=3, column=5, padx=10, pady=10)





