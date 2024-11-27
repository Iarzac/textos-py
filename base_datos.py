import sqlite3
from datetime import datetime

def inicializar_bd():
    conn = sqlite3.connect('palabras.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS palabras (
            categoria TEXT,
            palabra TEXT UNIQUE
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS textos_generados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texto TEXT,
            timestamp TEXT
        )
    ''')
    palabras_predefinidas = [
        ('sujeto', 'La tecnología'),
        ('sujeto', 'El ser humano'),
        ('sujeto', 'La creatividad'),
        ('verbo', 'impulsa'),
        ('verbo', 'crea'),
        ('verbo', 'representa'),
        ('adjetivo', 'revolucionaria'),
        ('adjetivo', 'nueva'),
        ('adjetivo', 'esencial'),
        ('complemento', 'el futuro'),
        ('complemento', 'la innovación'),
        ('complemento', 'nuevas ideas'),
        ('conector', 'y'),
        ('conector', 'pero'),
        ('conector', 'además')
    ]
    for categoria, palabra in palabras_predefinidas:
        c.execute('''
            INSERT OR IGNORE INTO palabras (categoria, palabra) VALUES (?, ?)
        ''', (categoria, palabra))
    conn.commit()
    conn.close()

def agregar_texto_generado(texto):
    conn = sqlite3.connect('palabras.db')
    c = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute('''
        INSERT INTO textos_generados (texto, timestamp) VALUES (?, ?)
    ''', (texto, timestamp))
    conn.commit()
    conn.close()

def obtener_historial_textos():
    conn = sqlite3.connect('palabras.db')
    c = conn.cursor()
    c.execute('SELECT texto, timestamp FROM textos_generados ORDER BY timestamp DESC')
    historial = c.fetchall()
    conn.close()
    return historial
