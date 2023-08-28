print("Bienvenidos al calculo de Iones")
print(" Ingrese los datos requeridos\n")
while True:
    #Ingreso de datos
    nombre = str(input("Ingrese el nombre del elemento: "))
    gramos = float(input("Ingrese los gramos a calcular: "))
    masa_molar = float(input("Ingrese la masa molar del elemento: "))
    carga = float(input("Ingrese la forma común del elemento: "))

    #Calculo de datos
    moles = gramos / masa_molar
    moles2 = moles * carga
    total = moles2 * 6.022

    #Muestreo de datos
    print("\nEl calculo del " + str(nombre) + " a Iones es aproximado: " + str(round(total, 2)) + " x 10^23 \n")

    # Mostrar el procedimiento de cálculo
    if input("¿Desea ver el procedimiento del cálculo? (s/n) \n").lower() == "s":
        print("                                    Proceso")
        print("\n-Calcular los moles de los gramos = " + str(round(gramos , 2)) + "g dividido entre " + str(round(masa_molar , 3)) + "g/mol = " + str(round(moles , 3)))
        print("\n-Luego se tiene que multiplicar " + str(round(moles , 3)) + " por " + str(round(carga , 3)) +" que el resultado es = " +str(round(moles2 , 3)) )
        print("\n-Por ultimo se tiene que multiplica " +str(round(moles2 , 3))+ " por 6.022 x 10^23 cuyo resultado es = " + str(round(total , 2)))

    #Decision
    if input("\n¿Desea hacer un cambio? (s/n) \n").lower() == "n":
        break

print("Programa finalizado.\n")