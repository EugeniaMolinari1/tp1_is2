import matplotlib.pyplot as plt

# Función Collatz
def collatz_iteraciones(n):
    contador = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        contador += 1
    return contador

# Listas para datos
numeros = []
iteraciones = []

# Calcular para 1 a 10000
for i in range(1, 10001):
    numeros.append(i)
    iteraciones.append(collatz_iteraciones(i))

# Graficar
plt.scatter(iteraciones, numeros, s=1)

plt.xlabel("Cantidad de iteraciones")
plt.ylabel("Número inicial")
plt.title("Conjetura de Collatz (1 a 10000)")

plt.show()