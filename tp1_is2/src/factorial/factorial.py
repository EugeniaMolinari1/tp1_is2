#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

# Si se pasa argumento por consola
if len(sys.argv) > 1:
    entrada = sys.argv[1]
else:
    # Si no, pedir por teclado
    entrada = input("Ingrese un número o rango: ")

# Procesamiento de la entrada
if "-" in entrada:
    partes = entrada.split("-")

    # Caso "-hasta" (ej: -10)
    if partes[0] == "":
        desde = 1
        hasta = int(partes[1])

    # Caso "desde-" (ej: 4-)
    elif partes[1] == "":
        desde = int(partes[0])
        hasta = 60

    # Caso "desde-hasta" (ej: 4-8)
    else:
        desde = int(partes[0])
        hasta = int(partes[1])

    for i in range(desde, hasta + 1):
        print("Factorial ", i, "! es ", factorial(i))

else:
    num = int(entrada)
    print("Factorial ", num, "! es ", factorial(num))