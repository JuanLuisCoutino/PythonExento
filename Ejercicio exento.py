#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Juan Luis Couti?o
#
# Created:     03/03/2023
# Copyright:   (c) Juan Luis Couti?o 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
print("Calcula areas de figuras geometricas")

elegir = 0

while elegir not in [1, 2, 3, 4]:
    try:
        elegir = int(input("Por favor escribe 1 para trapecio, escribe 2 para circulo, escribe 3 para triangulo, escribe 4 para corona circular"))
    except KeyboardInterrupt:
        print("Se aborto la mision")
        break

if elegir == 1:
    print("Elegiste la opcion para calcular area de una figura")
    B = float(input("Introduce el valor de la base mayor: "))
    b = float(input("Introduce el valor de la base menor: "))
    a = float(input("Introduce el valor de la altura del trapecio: "))
    sumabases = b + B
    sumatotal = sumabases / 2
    altura = a
    area = sumatotal * altura
    print("El area del trapecio es:", area)

elif elegir == 2:
    print("Elegiste la opcion para calcular area de un circulo")
    r = float(input("Introduce el valor de radio: "))
    pi = 3.14159
    if r <= 0:
        print("El valor del radio debe ser mayor que cero.")
    else:
        rcuadrado = r * r
        area = pi * rcuadrado
        if area <= 0:
            print("Los datos estan mal, ingresa los datos de nuevo.")
        else:
            print("El area del circulo es:", area)

elif elegir == 3:
    print("Elegiste la opcion para calcular area de un triangulo")
    b = float(input("Introduce la base del triangulo"))
    a = float(input("Introduce la altura del triangulo"))
    areaTriangulo = (b * a)/2

    if areaTriangulo <= 0:
        print("Valores invalidos, verifica la base y/o altura")
    else:
        print("El area es", areaTriangulo)

elif elegir ==4:
    print("Elegiste la opcion de corona circular")
    rmayor = input("Introduce el radio del circulo mayor")
    rmenor = input("Introduce el radio del circulo menor")
    pi = 3.14
    rmayorCuadrado = rmayor * rmayor
    rmenorCuadrado = rmenor * rmenor
    areaCorona = pi * (rmayorCuadrado - rmenorCuadrado)
    if areaCorona <= 0:
        print("Valores invalidos, verifica los radios")
    else:
        print("El area es", areaCorona)

else:
    print("Opcion no valida. Por favor lee de nuevo y elige una opcion valida")
