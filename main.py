from tkinter import *
from tkinter import ttk
import upload_check
import search_check
import sys


def proximamente():
        window_proximamente = Toplevel()
        window_proximamente.title('PROXIMAMENTE')
        window_proximamente.geometry('350x200')
        window_proximamente.resizable(False,False)
        # Foco automático sobre la ventana que se abre
        window_proximamente.focus()
        Label(window_proximamente, text='PROXIMAMENTE', font=30).pack(pady=20)
        button_return = Button(window_proximamente,
                        text='Volver',
                        command=window_proximamente.destroy).pack(pady=20)


# VENTANA PRINCIPAL - RAÍZ
root = Tk()
root.title('Gestor de cheques')
# INICIA LA VENTANA MIXIMIZADA
root.state('zoomed')
root.geometry('1000x600')

# ETIQUETA
Label(root, text='GESTOR DE CHEQUES', font=('arial',30, 'bold')).pack(pady=20)

# BOTONES
# CARGAR UN NUEVO CHEQUE
button_load = Button(root, text='Cargar cheque', width=15, height=3, command=upload_check.upload_check).pack(pady=20)

# BUSCAR CHEQUES
button_search = Button(root, text='Buscar cheque', width=15, height=3, command=search_check.search_check).pack(pady=20)
# OPCIONES
button_opciones = Button(root, text='Opciones', width=15, height=3, command=proximamente, state='disabled').pack(pady=20)
# SALIR DEL PROGRAMA
button_exit = Button(root, text='Salir', width=15, height=3, command=sys.exit).pack(pady=20)


root.mainloop()