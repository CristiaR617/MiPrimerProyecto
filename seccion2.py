import math
# Ejercicio 1. funcion nLineas con bucle while

# def nLineas(n):
#     while n != 0:
#         print(" ")
#         n = n-1


# print("hola 1")
# nLineas(1)
# print("hola 2")

# TABLAS

# x = 1.0
# while x < 10.0:
#     print(f"{x},   {math.log(x)/math.log(2.0)}")
#     x = x + 1.0

# EJERCICIO 2.Hacer que imprima una tabla de multiplicar
# def multiplicaciones(a, b):
#     x = 0
#     n = 1
#     c = b
#     while x < a:
#         print(f"{b} x {n} = {c}")
#         c = c+b
#         n = n+1
#         x = x+1


# print(multiplicaciones(10, 67))

# El ejercicio del computador

# def imprimeMultiplos(n):
#     i = 1
#     while i <= 6:
#         print(n*i, end="    ")
#         i = i + 1


# i = 1
# while i < 6:
#     print(imprimeMultiplos(i))
#     i = i+1

def multiplicar(n):
    if n < 0:
        print("Deve agregar un numero positivo")
    elif n > 0:
        resultado = multiplicar(n-1)


print(multiplicar(5))
