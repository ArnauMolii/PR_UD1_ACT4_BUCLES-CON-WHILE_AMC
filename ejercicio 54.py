#ejercicio 54

total = 0
operaciones = 0

while total <= 50:
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    suma = int(num1) + int(num2)
    total += suma
    operaciones += 1
    print(f"El resultado de la suma es: {suma}")
    if operaciones == 1:
        print(f"El total acumulado es: {total} y llevas {operaciones} operación realizada")
    else:
        print(f"El total acumulado es: {total} y llevas {operaciones} operaciones realizadas")

print("Fin del programa")