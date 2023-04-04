# a = 45 % 10
# print(a)

# b = 5 == 5
# print(b)

# FUNCION PARA SABER SI UN NUMERO ES PAR
# def imprime_pariedad(x):
#     if x % 2 == 0:
#         print(f"el numero {x} es par")

#     else:
#         print(f"el numero {x} es impar")


# print(imprime_pariedad(857829057823))

# COMPARAR DOS NUMEROS:

# def compara(x, y):
#     if x < y:
#         print(f"{x} es menor que {y}")
#     elif x > y:
#         print(f"{x} es mayor que {y}")
#     else:
#         print(f"{x} y {y} son iguales")


# print(compara(5, 6))
# print(compara(7, 6))
# print(compara(6, 6))

# FUNCION RESUELVE

# def resuelve(eleccion):
#     if eleccion == "A":
#         print("funcionA")
#     elif eleccion == "B":
#         print("funcionB")
#     elif eleccion == "C":
#         print("funcionC")
#     else:
#         print("Eleccion incorrecta")


# print(resuelve("A"))
# print(resuelve("B"))
# print(resuelve("N"))

# FUNCION COMPARA CON CONDICIONALES ANIDADOS

# def compara2(x, y):
#     if x == y:
#         print(f"{x} y {y} son iguales")
#     else:
#         if x > y:
#             print(f"{x} es mayor que {y} ")
#         else:
#             print(f"{x} es menor que {y}")


# print(compara2(6, 6))
# print(compara2(8, 6))
# print(compara2(5, 6))


# IDENTIFICAR NUMEROS POSITIVOS DE UN DIGITO

# def numero_un_digito(x):
#     if x >= 0 or x >= -9:
#         if x <= 9:
#             print(f"el numero {x} es de un digito")


# print(numero_un_digito(5))
# print(numero_un_digito(10))
# print(numero_un_digito(-5))
# print(numero_un_digito(-15))

# FUNCION RETURN

# import math


# def imprimeLogaritmo(x):
#     if x < 0:
#         print("solo numeros positivos")
#         #La funcion return tambien es como un break termina el programa
#         return
#     result = math.log(x)
#     print(f"el logaritmo de {x} es {result}")


# print(imprimeLogaritmo(7))
# print(imprimeLogaritmo(-7))
# print(imprimeLogaritmo(89))

# LLAMAAR FUNCION DENTRO DE LA MISMA FUNCION

# def cuentaAtras(x):
#     if x == 0:
#         print("!!despegando")
#     else:
#         print(x)
#         cuentaAtras(x-1)


# print(cuentaAtras(6))

# NUEVA LINEA CON FUNCIONES
# def nuevalinea():
#     print()


# print("linea 1")
# nuevalinea()
# print("linea 2")

# TRES LINEAS DENTRO DE NUEVE LLINEAS

# def tresLineas():
#     print()
#     print()
#     print()


# def nueveLineas():
#     tresLineas()
#     tresLineas()
#     tresLineas()


# print("lineas 1")
# nueveLineas()
# print("lineas 2")

# ESTA ES UNA MANERA DE SIMPLIFICAR EL ANTERIOR CODIGO

# def nlineas(n):
#     if n > 0:
#         print()
#         nlineas(n-1)


# print("lin1")
# nlineas(25)
# print("lin2")

# FUNCIONES ´PRODUCTIVAS,
# Calcular el area de un circulo

# Esta es una forma larga de hacerlo

# import math


# def area(radio):
#     area_ciculo = math.pi * radio**2
#     return area_ciculo


# print(area(4))

# Una forma mas corta es asi

# import math


# def area(radio):
#     return math.pi * radio**2


# print(area(5))

# AQUI HAY VARIOS RETURNS

# def valor_absoluto(x):
#     if x < 0:
#         return abs(x)
#     else:
#         return x


# print(valor_absoluto(98))

# Ejercicio 1.
# si x>y que de 1 si son iguales 0 y si y es mayor -1con una funcion

# def comparar(x, y):
#     if x > y:
#         return 1
#     elif x == y:
#         return 0
#     else:
#         return -1


# print(comparar(8, 6))
# print(comparar(8, 8))
# print(comparar(8, 9))

# Ejercicio 2. Hallar la hipotenusa
# import math


# def hipotenusa(x1, y1, x2, y2):
#     dx = x2-x1
#     dy = y2-y1
#     distancia = dx**2 + dy**2
#     return math.sqrt(distancia)


# print(hipotenusa(2, 3, 6, 6))

# Ejercicio 3. Hallar la pendiente
# def pendiente(x1, y1, x2, y2):
#     return (y2-y1)/(x2-x1)


# print(pendiente(2, 3, 4, 5))

# EJERCICO 4. Hallar el harea del circulo teniendo las cordenadas

# formula para hallar la distancia entre dos puntos
# import math


# def distancia(x1, y1, x2, y2):
#     dx = x2-x1
#     dy = y2-y1
#     distancia = dx**2 + dy**2
#     return math.sqrt(distancia)

# #Aqui se llama a la funcion distancia dentro de la funcion area_circulo
# #Y esta funcion calcula el area
# def area_circulo():
#     radio = distancia(4, 5, 6, 7)
#     return math.pi*radio**2


# print(area_circulo())

# Ejercicio 5.
# def estaEntre(x, y, z):
#     if y <= x <= z:
#         return True
#     else:
#         return False


# print(estaEntre(8, 4, 9))
# print(estaEntre(8, 8, 8))
# print(estaEntre(7, 4, 2))

# Ejercicio 5. Hallar el factorial de un numero. MIO
# def factorial(n):
#     if n == 0:
#         return 1
#     elif n > 0:
#         return n * factorial(n-1)
#     else:
#         return "El numero deve ser positivo"


# print(factorial(-3))
# print(factorial(5))
# print(factorial(0))

# Del computador
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         recursivo = factorial(n-1)
#         resultado = n * recursivo
#         return resultado


# print(factorial(5))

# FUNCION PARA SABER SI UN NUMERO ES DIVISIBLE POR OTRO

# def NuDivisible(x, y):
#     if x % y == 0:
#         return True
#     else:
#         return False

# print(NuDivisible(45,5))
# print(NuDivisible(45,3))
# print(NuDivisible(45,2))

# HALLAR FIBONACI
# formula= fibonacci(n) = fibonacci(n − 1) + fibonacci(n − 2);

# ------------------------------------
# ESTE ES EL MIO
# def fibonaci(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
# Este esta mal ya que el fibonaci no es sumar por los numero anteriores si no es sumar
# los numeros en sequencia asi:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1.597, 2.584,
# 4.181, 6.765, 10.946, 17.711, 28.#657, 46.368, …
#         fibonaci2 = fibonaci(n-1)
#         return n + fibonaci2


# print(fibonaci(4))
# print(fibonaci(3))
# print(fibonaci(8))
# print(fibonaci(2))
# --------------------------------------------
# ESTE ES DEL COMPUTADOR

# def fibonaci(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return fibonaci(n-1)+fibonaci(n-2)


# print(fibonaci(5))
