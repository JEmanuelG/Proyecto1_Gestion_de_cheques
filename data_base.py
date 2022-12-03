import sqlite3

def insert_check_in_db(f,id,cli,b,num,imp,fc,des='En caja'):
    
    print('CREA DB')
    # CREA BASE DE DATOS PARA LOS CHEQUES
    conexion = sqlite3.connect('data/data_base_cheques.db')

    cursor = conexion.cursor()

    print('CREA TABLA')
    cursor.execute('''CREATE TABLE IF NOT EXISTS cheque(
                                    fecha_carga TEXT,
                                    id TEXT,
                                    ingreso_cliente TEXT,
                                    banco TEXT,
                                    num_cheque TEXT,
                                    importe REAL,
                                    fecha_cobro TEXT)
                                    destino TEXT''')
    conexion.commit()

    print('INSERTA REGISTRO')
    cursor.execute('INSERT INTO cheque VALUES(?,?,?,?,?,?,?,?)', (f,id,cli,b,num,imp,fc,des))
    conexion.commit()

    print('CIERRA DB')
    conexion.close()

def search_check_date_in_db(f, t):
    conexion = sqlite3.connect('data/data_base_cheques.db')

    cursor = conexion.cursor()

    print('REALIZA LA CONSULTA SEGÚN LAS FECHAS INGRESADAS')
    cursor.execute('SELECT * FROM cheque WHERE fecha_carga BETWEEN "{}" AND "{}" order by fecha_carga'.format(f, t))

    checks_from_to = cursor.fetchall()
    
    #print(checks_from_to)

    #for check in checks_from_to:
     #   print(check)
    
    conexion.close()

    return checks_from_to

# CARGA TODOS LOS CHEQUES DE LA BASE ORDENADOS POR FECHA DE CARGA MAS RECIENTE

def load_all_checks():
    conexion = sqlite3.connect('data/data_base_cheques.db')

    cursor = conexion.cursor()

    print('REALIZA LA CONSULTA DE TODOS LOS REGISTROS')
    cursor.execute('SELECT * FROM cheque ORDER BY fecha_carga DESC')

    all_checks = cursor.fetchall()
    
    
    
    conexion.close()

    return all_checks