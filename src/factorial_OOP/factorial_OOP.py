#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

class Factorial:

    def __init__(self):
        pass

    def calcular(self, num):
        if num < 0:
            print("Factorial de un número negativo no existe")
            return 0
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact

    def run(self, minimo, maximo):
        for i in range(minimo, maximo + 1):
            print("Factorial ", i, "! es ", self.calcular(i))


if __name__ == "__main__":
    f = Factorial()

    # Entrada desde argumento o teclado
    if len(sys.argv) > 1:
        entrada = sys.argv[1]
    else:
        entrada = input("Ingrese un número o rango: ")

    if "-" in entrada:
        partes = entrada.split("-")

        if partes[0] == "":
            desde = 1
            hasta = int(partes[1])
        elif partes[1] == "":
            desde = int(partes[0])
            hasta = 60
        else:
            desde = int(partes[0])
            hasta = int(partes[1])

        f.run(desde, hasta)

    else:
        num = int(entrada)
        print("Factorial ", num, "! es ", f.calcular(num))