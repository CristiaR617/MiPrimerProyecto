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

# def multiplicar(n):
#     if n == 0:

#     elif n > 0:
#         return multiplicar(n-1)


# print(multiplicar(5))

# def cuentaAtras(x):
#     if x == 0:
#         print("!!despegando")
#     else:
#         print(x)
#         cuentaAtras(x-1)


# cuentaAtras(5)

v ="git config - -list
diff.astextplain.textconv = astextplain
filter.lfs.clean = git-lfs clean - - % f
filter.lfs.smudge = git-lfs smudge - - % f
filter.lfs.process = git-lfs filter-process
filter.lfs.required = true
http.sslbackend = openssl
http.sslcainfo = C: / Program Files/Git/mingw64/etc/ssl/certs/ca-bundle.crt
core.autocrlf = true
core.fscache = true
core.symlinks = false
pull.rebase = false
credential.helper = manager
credential.https: // dev.azure.com.usehttppath = true
init.defaultbranch = master
core.repositoryformatversion = 0
core.filemode = false
core.bare = false
core.logallrefupdates = true
core.symlinks = false
core.ignorecase = true
remote.origin.url = https: // github.com/CristiaR617/MiPrimerProyecto.git
remote.origin.fetch = +refs/heads/*: refs/remotes/origin/*
"
