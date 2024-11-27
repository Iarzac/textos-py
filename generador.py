import sqlite3
import random

def obtener_palabra(categoria):
    conn = sqlite3.connect("palabras.db")
    c = conn.cursor()
    c.execute("SELECT palabra FROM palabras WHERE categoria = ? ORDER BY RANDOM() LIMIT 1", (categoria,))
    resultado = c.fetchone()
    conn.close()
    return resultado[0] if resultado else None

def construir_oracion():
    sujeto = obtener_palabra("sujeto")
    verbo = obtener_palabra("verbo")
    adjetivo = obtener_palabra("adjetivo")
    complemento = obtener_palabra("complemento")
    conector = obtener_palabra("conector")

    if not all([sujeto, verbo, adjetivo, complemento, conector]):
        return None

    estructuras = [
        f"{sujeto} {verbo} una idea {adjetivo} hacia {complemento}.",
        f"{sujeto} {verbo} {complemento}, {conector} es una {adjetivo} perspectiva.",
        f"{sujeto} es {adjetivo} y siempre {verbo} {complemento}.",
        f"{complemento} se logra cuando {sujeto} {verbo} {adjetivo} objetivos."
    ]

    return random.choice(estructuras)

def generar_texto_aleatorio(num_oraciones):
    texto = []
    for _ in range(num_oraciones):
        oracion = construir_oracion()
        if oracion:
            texto.append(oracion)
    return " ".join(texto)
