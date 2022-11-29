

def cargar_cheque(f,id,cli,b,num,imp,fc):
    
    import sqlite3

    print('CREA DB')
    # CREA BASE DE DATOS PARA LOS CHEQUES
    conexion = sqlite3.connect('data/data_base_cheques.db')

    cursor = conexion.cursor()

    print('CREA TABLA')
    cursor.execute('''CREATE TABLE IF NOT EXISTS cheques(
                                    fecha_carga TEXT,
                                    id TEXT,
                                    ingreso_cliente TEXT,
                                    banco TEXT,
                                    num_cheque TEXT,
                                    importe REAL,
                                    fecha_cobro TEXT)''')
    conexion.commit()

    print('INSERTA REGISTRO')
    cursor.execute('INSERT INTO cheques VALUES(?,?,?,?,?,?,?)', (f,id,cli,b,num,imp,fc))
    conexion.commit()

    print('CIERRA DB')
    conexion.close()

