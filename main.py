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
rango20 = (edad >= 20 and edad < 30)    #Estas expresiones gral. se encuentran dentro del if.
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
elif resp == "N":
    envio = False
else:
    print("Valor incorrecto.")

print(f'Nombre', nombre)
print(f'id:', id)
print(f'Precio:', precio)
if envio:
    print("Incluye envio gratis.")
else:
    print("No invluye envio gratis.")