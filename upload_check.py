from tkinter import *
import data_base

def upload_check_gui():    

    # VARIABLES DE CONTROL
    date_variable = StringVar()
    check_number_variable = StringVar()
    bank_variable = StringVar()
    client_variable = StringVar()
    amount_variable = DoubleVar()
    payment_date_variable = StringVar()
    id_variable = StringVar()


    window_load = Toplevel()
    window_load.title('Cargar cheque')
    window_load.geometry('350x400')
    window_load.resizable(False,False)
    # Foco automático sobre la ventana que se abre
    window_load.focus()



#    ************** PROCESOS ******************

    def upload_check():
        data_base.cargar_cheque(date_variable.get(),
                                id_variable.get(),
                                client_variable.get(),
                                bank_variable.get(),
                                check_number_variable.get(),
                                amount_variable.get(),
                                payment_date_variable.get()
                                )
        window_load.destroy()


#       *********** INTERFAZ *************


    # ETIQUETAS
    Label(window_load,
          text='Fecha:').grid(row=1,
                            column=0,
                            padx=10,
                            pady=10)

    Label(window_load,text='Cheque N°:').grid(row=2, column=0, padx=10, pady=10)
    Label(window_load,text='Banco:').grid(row=3, column=0, padx=10, pady=10)
    Label(window_load,text='Entregó cliente:').grid(row=4, column=0, padx=10, pady=10)
    Label(window_load,text='Importe:').grid(row=5, column=0, padx=10, pady=10)
    Label(window_load,text='Fecha de Cobro:').grid(row=6, column=0, padx=10, pady=10)
    Label(window_load,text='ID de la empresa:').grid(row=7, column=0, padx=10, pady=10)



    # BOTONES
    button_close = Button(window_load,
                        text='Cancelar',
                        command=window_load.destroy).grid(row=8, column=0, padx=10, pady=10)
    
    button_save = Button(window_load,
                         text='Cargar',
                         command=lambda:upload_check()).grid(row=8,
                                                             column=5,
                                                             padx=10,
                                                             pady=10)
    

    # CAMPOS DE ENTRADA
    date_data = Entry(window_load, justify='center', textvariable=date_variable).grid(row=1, column=1)
    check_number_data = Entry(window_load, justify='center', textvariable=check_number_variable).grid(row=2, column=1)
    bank_data = Entry(window_load, justify='center', textvariable=bank_variable).grid(row=3, column=1)
    client_data = Entry(window_load, justify='center', textvariable=client_variable).grid(row=4, column=1)
    amount_data = Entry(window_load, justify='center', textvariable=amount_variable).grid(row=5, column=1)
    payment_date_data = Entry(window_load, justify='center', textvariable=payment_date_variable).grid(row=6, column=1)
    id_data = Entry(window_load, justify='center', textvariable=id_variable).grid(row=7, column=1)

