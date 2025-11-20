#ejercicio 53

repetir = 's'
total = 0
repeticiones = 0

while repetir.lower() == 's':
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    suma = int(num1) + int(num2)
    total += suma
    repeticiones += 1
    print(f"El resultado de la suma es: {suma}")
    repetir = input("Deseas repetir la operación s/n: ")

print("Resumen:")
print(f"La suma total es: {total} y el número de repeticiones es: {repeticiones}")