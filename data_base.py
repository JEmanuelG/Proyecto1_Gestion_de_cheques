import sqlite3

def insert_check_in_db(f='',i='',cli='',b='',num='',imp='',fc='',des='En caja'):
    
    # CREA BASE DE DATOS PARA LOS CHEQUES
    conexion = sqlite3.connect('data/data_base_cheques.db')
    cursor = conexion.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS cheque(
                                    fecha_carga TEXT,
                                    id INT,
                                    ingreso_cliente TEXT,
                                    banco TEXT,
                                    num_cheque TEXT,
                                    importe REAL,
                                    fecha_cobro TEXT,
                                    destino TEXT)''')
    
    
    conexion.commit()
    if f != '' and i != '' and cli  != '' and num  != '':
        cursor.execute('INSERT INTO cheque VALUES(?,?,?,?,?,?,?,?)', (f,i,cli,b,num,imp,fc,des))
        conexion.commit()

    conexion.close()

# FUNCION PARA MODIFICAR DATOS DE CHEQUE
def update_check(f, i, cli, b, num, imp, fc):
    conexion = sqlite3.connect('data/data_base_cheques.db')
    cursor = conexion.cursor()
    
    cursor.execute('UPDATE cheque SET fecha_carga = ? WHERE id = ?',(f, i))
    cursor.execute('UPDATE cheque SET ingreso_cliente = ? WHERE id = ?',(cli, i))
    cursor.execute('UPDATE cheque SET banco = ? WHERE id = ?',(b, i))
    cursor.execute('UPDATE cheque SET num_cheque = ? WHERE id = ?',(num, i))
    cursor.execute('UPDATE cheque SET importe = ? WHERE id = ?',(imp, i))
    cursor.execute('UPDATE cheque SET fecha_cobro = ? WHERE id = ?',(fc, i))

    conexion.commit()

    conexion.close()


def search_check_date_in_db(f, t):
    conexion = sqlite3.connect('data/data_base_cheques.db')
    cursor = conexion.cursor()

    cursor.execute('SELECT * FROM cheque WHERE fecha_carga BETWEEN "{}" AND "{}" order by fecha_carga'.format(f, t))

    checks_from_to = cursor.fetchall()
    
    conexion.close()

    return checks_from_to

# CARGA TODOS LOS CHEQUES DE LA BASE ORDENADOS POR FECHA DE CARGA MAS RECIENTE
def load_all_checks():
    conexion = sqlite3.connect('data/data_base_cheques.db')
    cursor = conexion.cursor()

    cursor.execute('SELECT * FROM cheque ORDER BY fecha_carga DESC')

    all_checks = cursor.fetchall()    
    
    conexion.close()

    return all_checks

# CARGA LOS CHEQUES SEGUN EL ID
def search_check_id_in_db(i):
    conexion = sqlite3.connect('data/data_base_cheques.db')
    cursor = conexion.cursor()

    cursor.execute('SELECT * FROM cheque WHERE id = "{}"'.format(i))

    checks_for_id = cursor.fetchall()
    
    conexion.close()

    return checks_for_id


# CARGA LOS CHEQUES SEGUN EL CLIENTE
def search_check_client_in_db(client):
    conexion = sqlite3.connect('data/data_base_cheques.db')
    cursor = conexion.cursor()

    cursor.execute('SELECT * FROM cheque WHERE ingreso_cliente = "{}"'.format(client))

    checks_for_client = cursor.fetchall()
    
    conexion.close()

    return checks_for_client