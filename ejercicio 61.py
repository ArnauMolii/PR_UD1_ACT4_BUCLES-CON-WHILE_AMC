#ejercicio 61

numero = int(input("Introduce un número: "))
contador = 1

while contador <= 10:
    resultado = int(numero) * int(contador)
    print(resultado)
    if resultado >= 40:
        print("Fin de programa")
        break
contador += 1