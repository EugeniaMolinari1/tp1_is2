"""
Calculadora RPN que evalúa expresiones usando una pila.
Soporta operaciones, funciones, constantes y memoria.
"""

#!/usr/bin/env python3
import math
import sys


class RPNError(Exception):
    pass


# Evalúa una expresión en notación polaca inversa


def evaluate(expr):
    """Evalúa una expresión en notación polaca inversa."""
    st, mem = [], [0.0] * 10
    # Extrae el último valor de la pila o lanza error
    pop = lambda: (
        st.pop() if st else (_ for _ in ()).throw(RPNError("Pila insuficiente"))
    )
    # Inserta un valor en la pila
    push = lambda x: st.append(float(x))

    # Operaciones aritméticas básicas
    ops = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: (
            a / b if b else (_ for _ in ()).throw(RPNError("División por cero"))
        ),
    }
    # Funciones matemáticas disponibles
    funcs = {
        "sqrt": math.sqrt,
        "log": math.log10,
        "ln": math.log,
        "exp": math.exp,
        "10x": lambda x: 10**x,
        "1/x": lambda x: (
            1 / x if x else (_ for _ in ()).throw(RPNError("División por cero"))
        ),
        "chs": lambda x: -x,
        "sin": lambda x: math.sin(math.radians(x)),
        "cos": lambda x: math.cos(math.radians(x)),
        "tg": lambda x: math.tan(math.radians(x)),
        "asin": lambda x: math.degrees(math.asin(x)),
        "acos": lambda x: math.degrees(math.acos(x)),
        "atg": lambda x: math.degrees(math.atan(x)),
    }
    # Constantes matemáticas
    const = {"p": math.pi, "e": math.e, "j": (1 + math.sqrt(5)) / 2}
    # Procesa cada token de la expresión
    for t in expr.split():
        # Detecta si el token es un número (entero o real)
        if t.replace(".", "", 1).lstrip("-").isdigit():
            push(t)
        # Inserta constantes matemáticas en la pila
        elif t in const:
            push(const[t])
        # Aplica operación binaria usando los dos últimos valores de la pila
        elif t in ops:
            if len(st) < 2:
                raise RPNError("Pila insuficiente")
            b, a = pop(), pop()
            push(ops[t](a, b))
        # Duplica el último valor de la pila
        elif t == "dup":
            push(st[-1]) if st else (_ for _ in ()).throw(RPNError("Pila vacía"))
        # Intercambia los dos últimos valores de la pila
        elif t == "swap":
            if len(st) < 2:
                raise RPNError("Pila insuficiente")
            st[-1], st[-2] = st[-2], st[-1]
        # Elimina el último valor de la pila
        elif t == "drop":
            pop()
        # Limpia completamente la pila
        elif t == "clear":
            st.clear()
        # Calcula potencia: base^exponente usando la pila
        elif t == "yx":
            if len(st) < 2:
                raise RPNError("Pila insuficiente")
            b, a = pop(), pop()
            push(a**b)
        # Ejecuta función matemática sobre el último valor
        elif t in funcs:
            push(funcs[t](pop()))
        # Maneja almacenamiento (STO) y recuperación (RCL) de memoria
        elif t[:3] in ("STO", "RCL"):
            i = int(t[3:])
            if i not in range(10):
                raise RPNError("Memoria inválida")
            (mem.__setitem__(i, pop()) if t[0] == "S" else push(mem[i]))
        # Error si el token no es reconocido
        else:
            raise RPNError(f"Token inválido: {t}")
    # Verifica que quede un único resultado en la pila
    if len(st) != 1:
        raise RPNError("La pila no terminó con 1 valor")
    return st[0]


# Punto de entrada del programa
def main():
    print(evaluate(" ".join(sys.argv[1:]) or input("RPN> ")))


if __name__ == "__main__":
    try:
        main()
    # Captura errores y muestra mensaje sin romper el programa
    except RPNError as e:
        print("Error:", e)
