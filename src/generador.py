import random
import string

print("=== GENERADOR DE CONTRASEÑAS ===")

longitud = int(input("Ingrese la longitud de la contraseña: "))

caracteres = string.ascii_letters + string.digits + string.punctuation

contrasena = ""

for i in range(longitud):
    contrasena += random.choice(caracteres)

print("\nContraseña generada:")
print(contrasena)
