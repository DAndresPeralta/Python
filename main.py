# Ej1 - Valor dentro de rango.
print()
val = int(input("Ingrese un valor."))
valorMinimo = 0
valorMaximo = 5

dentroRango = (val >= valorMinimo) and (val <= valorMaximo)

if dentroRango:
    print("Valor dentro de rango.")
else:
    print("Valor fuera de rango.")

# Ej2 - Valor entre dos o mas rangos. Utilizaremos un if anidado.
print()

edad = int(input("Ingrese su edad."))
rango20 = (edad >= 20 and edad < 30)  # Estas expresiones gral. se encuentran dentro del if.
rango30 = (30 <= edad < 40)

if rango20 or rango30:
    print("Se encuentra dentro del rango etario.")
    if rango20:
        print("Dentro de los 20.")
    elif rango30:
        print("Dentro de los 30.")
else:
    print("Se encuentra fuera del rango etario.")

# Ej3 - Libro.

nombre = input("Ingrese el nombre del libro.")
id = int(input("Ingrese el id del libro."))
precio = float(input("Ingrese el precio."))
resp = input("Incluye envio gratis? S (SI) - N (NO).")
resp = resp.upper()

if resp == "S":
    envio = True
    envioC = "Incluye envio gratis."
elif resp == "N":
    envio = False
    envioC = "No incluye envio."
else:
    print("Valor incorrecto.")

print(f'''

    Nombre: {nombre}
    Id: {id}
    Precio: {precio}
    Envío: {envioC}

''')

# Ej4 - Número a texto.
print()
num = int(input("Ingrese un número de 1 a 3."))
numTexto = ''

if num == 1:
    numTexto = "Número uno."
elif num == 2:
    numTexto = "Número dos."
elif num == 3:
    numTexto = "Número tres."
else:
    numTexto = "Valor fuera de rango."

print(f'Número proporcionado: {num} - {numTexto}')

# Ej5 - Mes del año.

mes = int(input("Ingrese un mes del año."))
season = None

if (mes == 10) or (mes == 11) or (mes == 12):
    season = "primavera"
    print(f'Estamos en {season}! ')
elif (mes == 1) or (mes == 2) or (mes == 3):
    season = "verano"
    print(f'Estamos en {season}!')
elif (mes == 4) or (mes == 5) or (mes ==6):
    season = "otoño"
    print(f'Estamos en {season} :|')
elif (mes == 7) or (mes == 8) or (mes == 9):
    season = "invierno"
    print(f'Estamos en {season} :(')

# Ej6 - Etapa de edad.

edad = int(input("Ingrese su edad."))

if (edad > 0) and (edad <= 10):
    print("La infancia es increible.")
elif (edad > 10) and (edad <=20):
    print("Muchos cambios y mucho estudio...")
elif (edad > 20) and (edad <= 30):
    print("Amor y comienza el trabajo.")
else:
    print("Etapa de vida no reconocida.")
