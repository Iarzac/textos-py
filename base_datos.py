import sqlite3

def inicializar_bd():
    conn = sqlite3.connect('palabras.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS palabras (
            categoria TEXT,
            palabra TEXT UNIQUE
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

def agregar_palabra(categoria, palabra):
    conn = sqlite3.connect('palabras.db')
    c = conn.cursor()
    try:
        c.execute('''
            INSERT INTO palabras (categoria, palabra) VALUES (?, ?)
        ''', (categoria, palabra))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        conn.close()
        return False

def eliminar_palabra(palabra):
    conn = sqlite3.connect('palabras.db')
    c = conn.cursor()
    c.execute('DELETE FROM palabras WHERE palabra = ?', (palabra,))
    conn.commit()
    conn.close()
