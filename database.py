# database.py
import sqlite3

def crear_tablas():
    conn = sqlite3.connect('compras.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        DROP TABLE IF EXISTS categorias
    ''')
    
    cursor.execute('''
        DROP TABLE IF EXISTS articulos
    ''')
        

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS articulos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            valoracion REAL,
            categoria_id INTEGER NOT NULL,
            min INTEGER DEFAULT 0,
            max INTEGER DEFAULT 1,
            FOREIGN KEY (categoria_id) REFERENCES categorias (id)
        )
    ''')

    conn.commit()
    conn.close()

def insertar_categoria(nombre):
    conn = sqlite3.connect('compras.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM categorias WHERE nombre = ?', (nombre,))
    if cursor.fetchone()[0] > 0:
        conn.close()
        raise ValueError(f"La categoría '{nombre}' ya existe.")
    cursor.execute('INSERT INTO categorias (nombre) VALUES (?)', (nombre,))
    conn.commit()
    conn.close()

def insertar_articulo(nombre, precio, categoria_nombre, min=0, max=1, valoracion=None):
    conn = sqlite3.connect('compras.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM categorias WHERE nombre = ?', (categoria_nombre,))
    categoria_id = cursor.fetchone()
    if categoria_id is None:
        conn.close()
        raise ValueError(f"La categoría '{categoria_nombre}' no existe.")
    categoria_id = categoria_id[0]
    
    cursor.execute('''
        INSERT INTO articulos (nombre, precio, valoracion, categoria_id, min, max)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (nombre, precio, valoracion, categoria_id, min, max))
    conn.commit()
    conn.close()

def obtener_articulos_por_categoria(categoria_id):
    conn = sqlite3.connect('compras.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM articulos WHERE categoria_id = ?', (categoria_id,))
    articulos = cursor.fetchall()
    conn.close()
    return articulos

def get_categorias():
    conn = sqlite3.connect('compras.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM categorias')
    categorias = cursor.fetchall()
    conn.close()
    return {categoria[0]: categoria[1] for categoria in categorias}
