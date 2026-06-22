import random
import string

# Función para generar la contraseña
def generar_contrasena(palabra_base, longitud, incluir_numeros, incluir_simbolos):

    caracteres = string.ascii_letters

    # Agregar números si el usuario lo desea
    if incluir_numeros == "SI":
        caracteres += string.digits

    # Agregar símbolos si el usuario lo desea
    if incluir_simbolos == "SI":
        caracteres += string.punctuation

    # Calcular cuántos caracteres faltan
    faltantes = longitud - len(palabra_base)

    # Si la palabra es más larga que la longitud solicitada
    if faltantes < 0:
        return palabra_base[:longitud]

    contrasena = palabra_base

    # Completar la contraseña con caracteres aleatorios
    for i in range(faltantes):
        contrasena += random.choice(caracteres)

    return contrasena


# Función para evaluar la seguridad
def evaluar_seguridad(longitud, incluir_numeros, incluir_simbolos):

    if longitud < 8:
        return "BAJA"

    elif longitud < 12:
        if incluir_numeros == "SI" or incluir_simbolos == "SI":
            return "MEDIA"
        else:
            return "BAJA"

    else:
        if incluir_numeros == "SI" and incluir_simbolos == "SI":
            return "ALTA"
        else:
            return "MEDIA"


# Programa principal
print("====================================")
print(" GENERADOR SEGURO DE CONTRASEÑAS ")
print("====================================")

palabra_base = input("Ingrese una palabra o nombre para la contraseña: ")

longitud = int(input("Ingrese la longitud total deseada: "))

incluir_numeros = input("¿Desea incluir números? (SI/NO): ").upper()

incluir_simbolos = input("¿Desea incluir símbolos? (SI/NO): ").upper()

# Generar contraseña
contrasena = generar_contrasena(
    palabra_base,
    longitud,
    incluir_numeros,
    incluir_simbolos
)

# Evaluar seguridad
nivel_seguridad = evaluar_seguridad(
    longitud,
    incluir_numeros,
    incluir_simbolos
)

# Mostrar resultados
print("\n====================================")
print("Contraseña generada:")
print(contrasena)
print("Nivel de seguridad:", nivel_seguridad)
print("====================================")
