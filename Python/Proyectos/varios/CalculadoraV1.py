while True:
    operacion = input("\n¿Qué operación desea realizar? (suma/resta): ")
    
    if operacion.lower() == "suma":
        num1 = int(input("Ingrese un número entero: "))
        num2 = int(input("Ingrese otro número entero: "))
        resultado = num1 + num2
        print("El resultado de la suma es:", resultado)
    elif operacion.lower() == "resta":
        num1 = int(input("Ingrese un número entero: "))
        num2 = int(input("Ingrese otro número entero: "))
        resultado = num1 - num2
        print("El resultado de la resta es:", resultado)
    else:
        print("Operación no válida. Por favor, ingrese 'suma' o 'resta'.")

    opcion = input("\n¿Desea realizar otra operación? (s/n): ")
    if opcion.lower() == "n":
        break

print("\nGracias por preferirnos")
