#Implementar un generador de contraseñas seguras

import random
import string

def generar_contraseña(longitud, mayuscula, minuscula, numero, otro):
    caracteres = ""

if mayuscula:
    caracteres += string.ascii_uppercase  # Mayúsculas
if minuscula:
    caracteres += string.ascii_lowercase  # Minúsculas
if numero:
    caracteres += string.digits  # Números
if otro:
    caracteres += string.punctuation  # Símbolos

# Asegurar que la contraseña tenga al menos un carácter de cada tipo seleccionado
if mayusculas:
    caracteres += random.choice(string.ascii_uppercase)
if minusculas:
    caracteres += random.choice(string.ascii_lowercase)
if alfanumericos:
    caracteres += random.choice(string.digits)
if simbolos:
    caracteres += random.choice(string.punctuation)

# Si el número de caracteres es mayor que 4, se mezcla la longitud especificada
contraseña = ''.join(random.choice(caracteres) for i in range(longitud))

print(contraseña)


# Función principal

def menu():
    input("ingrese su nombre: ")
    
print("Bienvenido al generador de contraseñas seguras.")
print("Este generador permite crear contraseñas seguras con las configuraciones que elijas.")

while True:
    # Menú interactivo
    print("\\nMenú:")
    print("1. Especificar longitud de la contraseña.")
    print("2. Incluir mayúsculas.")
    print("3. Incluir minúsculas.")
    print("4. Incluir caracteres alfanuméricos.")
    print("5. Incluir símbolos.")
    print("6. Generar contraseña.")
    print("7. Salir.")

    opcion = input("Elige una opción (1-7): ")

    # Variables para las configuraciones
    longitud = 12  # Longitud por defecto
    mayusculas = False
    minusculas = False
    alfanumericos = False
    simbolos = False

    # Procesar opciones
    if opcion == "1":
        longitud = int(input("¿Qué longitud deseas para la contraseña? (ej. 12): "))
    elif opcion == "2":
        mayusculas = True
    elif opcion == "3":
        minusculas = True
    elif opcion == "4":
        alfanumericos = True
    elif opcion == "5":
        simbolos = True
    elif opcion == "6":
        if longitud < 4:
            print("La longitud debe ser al menos 4 para garantizar la seguridad.")
            continue
        contraseña = generar_contraseña(longitud, mayusculas, minusculas, alfanumericos, simbolos)
        print(f"Contraseña generada: {contraseña}")
        continuar = input("¿Quieres generar otra contraseña? (s/n): ")
        if continuar.lower() != 's':
            print("¡Hasta luego!")
            break
    elif opcion == "7":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida, por favor elige una opción entre 1 y 7.")