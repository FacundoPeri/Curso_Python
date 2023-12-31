# def holamundo(x, y, s):
#     for i in range(10):
#         print(f"{s}{i + 1} de la funcion.")
#         x += y
#         print(x)
#     return x

# x = 10
# y = 12

# fase = "Este es el bucle "

# resultado = holamundo(x,y,fase)
# print("El resultado de la funcion es: ", resultado)

# resultado += holamundo(x,y,fase)

# print(f"\nEl resultado es: {resultado}")
# nota1 = 10
# nota2 = 6

# notafinal = (nota1*0.4 + nota2*0.6)
# print(notafinal)

# cadena1 = "moderno"
# cadena2 = "Python"
# cadena3 = "de programacion"
# cadena4 = "es un lenguaje"

# cadena5 = cadena2 + " "+ cadena4 + " " + cadena3 + cadena1
# print(cadena5)


# cadena_corrupta = "airtosiH,6.7,aicraG nómaR"

# cadena_volteada =  cadena_corrupta[::-1]
# print(cadena_volteada)
# nombre = cadena_volteada[:12]
# print(nombre)
# nota = cadena_volteada[13:16]
# print(nota)
# materia = cadena_volteada[17:]
# print(materia)
# cadena_formateada = f"{nombre} ha sacado un {nota} en {materia}"
# print(cadena_formateada)

# lista1 = [1,12,123]
# lista2 = ["bye", "ciao","agur", "adieu"]

# lista1.append(1234)
# lista1.append("hola")

# lista2.append("adios")
# lista2.append(1234)

# lista3 = lista1[:-1]
# print(lista3)

# lista4 = lista2[1:-1]
# print(lista4)

# lista5 = lista4 + lista3
# print(lista5)


# valor  = int(input("Ingrese un valor: "))
# print("El numero ingresado es " + valor)

# nombre = input("Ingrese nombre: ")
# apellido = input("Ingrese apellido: ")
# edad = int(input("Ingrese la edad: "))
# numero_magico = float(input("Ingrese un numero de la suerte: "))
# print(f"{nombre} tu numero de la suerte es el {edad * numero_magico}")

# resultados = [False, True, True, True, True]

expresion = False
while not(expresion):
    nombre = input("Ingrese un nombre: ")
    edad = int(input("Ingrese una edad: "))
    expresion = ((nombre != "****") and ((edad > 10) and (edad < 18)) and ((len(nombre) >= 3) and (len(nombre) < 10)))
    print(expresion)