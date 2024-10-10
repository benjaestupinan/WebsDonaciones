import pymysql
import datetime

def getConnection():
    conn = pymysql.connect(
        db='tarea2',
        user='cc5002',
        passwd='programacionweb',
        host='localhost',
        charset='utf8',
    )
    return conn

def get_contact_by_id(id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, email, celular, comuna_id, fecha_creacion FROM contacto WHERE id = %s", (id,))
    user = cursor.fetchone()
    return user

def get_contact_by_mail(mail):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, email, celular, comuna_id, fecha_creacion FROM contacto WHERE email = %s", (mail,))
    user = cursor.fetchone()
    return user

def get_contact_by_username(username):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, email, celular, comuna_id, fecha_creacion FROM contacto WHERE nombre = %s", (username,))
    user = cursor.fetchone
    return user

def get_comuna_id_by_name(comuna):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM comuna WHERE nombre = %s", (comuna,))
    comuna_id = cursor.fetchone()
    return comuna_id

def get_comuna_by_id(id):

    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM comuna WHERE id = %s", (id,))
    comuna = cursor.fetchone()
    return comuna

def create_contact(nombre, mail, telefono, comuna):
    
    comuna_id = get_comuna_id_by_name(comuna)

    now = datetime.datetime.now()
    texto_fecha_hora = now.strftime('%Y-%m-%d %H:%M:%S')
    
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacto (nombre, email, celular, comuna_id, fecha_creacion) VALUES (%s, %s, %s, %s, %s)",(nombre, mail, telefono, comuna_id, texto_fecha_hora,))
    conn.commit()
    return True, None
    
def create_disp(contacto_mail, nombre, descripcion, tipo, anos_uso, estado):

    contacto_id = get_contact_by_mail(contacto_mail)
    # print(contacto_id)

    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO dispositivo (contacto_id, nombre, descripcion, tipo, anos_uso, estado) VALUES (%s,%s,%s,%s,%s,%s)", (contacto_id[0], nombre, descripcion, tipo, anos_uso, estado))
    conn.commit()
    return True, None

def get_disp_id(contacto_mail, nombre, descripcion, tipo, años_uso, estado):
    contacto_id = get_contact_by_mail(contacto_mail)
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM dispositivo WHERE contacto_id = %s AND nombre = %s AND descripcion = %s AND tipo = %s AND anos_uso = %s AND estado = %s", ((contacto_id[0], nombre, descripcion, tipo, años_uso, estado)))
    disp = cursor.fetchone()
    return disp

def create_img(ruta, nombre, disp_id):

    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO archivo (ruta_archivo, nombre_archivo, dispositivo_id) VALUES (%s,%s,%s)", (ruta, nombre, disp_id))
    conn.commit()
    return True, None

def get_disps(start,range):
    
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, contacto_id, nombre, descripcion, tipo, anos_uso, estado FROM dispositivo ORDER BY id DESC LIMIT %s, %s", (start, range))
    data = cursor.fetchall()
    return data

def get_disp_by_id(disp_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, contacto_id, nombre, descripcion, tipo, anos_uso, estado FROM dispositivo WHERE id=%s", (disp_id,))
    disp = cursor.fetchone()
    return disp

def get_files_by_disp_id(disp_id):
    
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT ruta_archivo FROM archivo WHERE dispositivo_id = %s", (disp_id,))
    files = cursor.fetchall()
    return files

def get_commentarios_by_disp_id(disp_id):
    
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM comentario WHERE dispositivo_id = %s", (disp_id,))
    comentarios = cursor.fetchall()
    return comentarios

def create_comment(autor, texto, disp_id):

    now = datetime.datetime.now()
    texto_fecha_hora = now.strftime('%Y-%m-%d %H:%M:%S')

    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO comentario (nombre, texto, fecha, dispositivo_id) VALUES (%s, %s, %s, %s)", (autor, texto, texto_fecha_hora, disp_id))
    conn.commit()
    return True, None