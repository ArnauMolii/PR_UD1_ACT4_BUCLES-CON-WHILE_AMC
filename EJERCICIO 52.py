#EJERCICIO 52

repetir = 's'
while repetir.lower() == 's':
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    suma = int(num1) + int(num2)
    print(f"El resultado de la suma es: {suma}")
    repetir = input("Deseas repetir la operación s/n: ")

print("Programa finalizado")