import sqlite3
import random

def obtener_palabra(categoria):
    conn = sqlite3.connect("palabras.db")
    c = conn.cursor()
    c.execute("SELECT palabra FROM palabras WHERE categoria = ? ORDER BY RANDOM() LIMIT 1", (categoria,))
    resultado = c.fetchone()
    conn.close()
    return resultado[0] if resultado else None

def construir_oracion(tipo_texto):
    sujeto = obtener_palabra("sujeto")
    verbo = obtener_palabra("verbo")
    adjetivo = obtener_palabra("adjetivo")
    complemento = obtener_palabra("complemento")
    conector = obtener_palabra("conector")

    if not all([sujeto, verbo, adjetivo, complemento, conector]):
        return None

    # Variación en las estructuras de las oraciones según el tipo de texto
    if tipo_texto == "Poético":
        estructuras = [
            f"{sujeto} {verbo} una idea {adjetivo} hacia {complemento}, como un suspiro en la brisa.",
            f"En la quietud, {sujeto} {verbo} {complemento}, mientras {conector} se disuelve en el aire {adjetivo}.",
            f"{sujeto} se convierte en {adjetivo}, y en su camino, {verbo} {complemento} en un mar de emociones.",
        ]
    elif tipo_texto == "Coloquial":
        estructuras = [
            f"{sujeto} {verbo} algo {adjetivo}, como siempre, hacia {complemento}.",
            f"¿Sabías que {sujeto} {verbo} {complemento}? {conector} es {adjetivo}.",
            f"Pues nada, {sujeto} {verbo} {complemento}, y es bastante {adjetivo}.",
        ]
    elif tipo_texto == "Formal":
        estructuras = [
            f"{sujeto} {verbo} una {adjetivo} solución en relación con {complemento}.",
            f"De acuerdo con el análisis, {sujeto} {verbo} {complemento}, {conector} se espera que sea una {adjetivo} propuesta.",
            f"En el futuro, {sujeto} tiene la intención de {verbo} {complemento} bajo una perspectiva {adjetivo}.",
        ]
    else:  # Tipo de texto Informal
        estructuras = [
            f"{sujeto} {verbo} algo {adjetivo}, así que {complemento} es genial.",
            f"{sujeto} {verbo} {complemento}, {conector} es simplemente {adjetivo}.",
            f"{sujeto} {verbo} de manera {adjetivo}, y {complemento} tiene algo especial.",
        ]

    return random.choice(estructuras)

def generar_texto_aleatorio(num_oraciones, tipo_texto):
    texto = []
    for _ in range(num_oraciones):
        oracion = construir_oracion(tipo_texto)
        if oracion:
            texto.append(oracion)
    return " ".join(texto)
