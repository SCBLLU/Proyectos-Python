print("Calculos de Moles\n")
print("Ingrese los datos")
while True:
    #Ingreso de datos
    Nombre = str(input("Ingrese el nombre del elemento: "))
    gramos = float(input("Ingrese los gramos a calcular: "))
    masa_molar = float(input("Ingrese los gramos mol: "))

    #Calculo
    moles = gramos / masa_molar

    #Muestro de datos
    print("\nEl calculo de " +str(gramos)+ "g de " +str(Nombre)+ " a moles es = " +str(round(moles , 3)) +" g/mol")
    if input("¿Desea ver el procedimiento del cálculo? (s/n) \n").lower() == "s":
        print("- Se divide " +str(gramos)+ " entre " +str(masa_molar)+ " y el resultado de la divicion es = " +str(round(moles , 3)) +" g/mol" )

    #Decision
    if input("\n¿Desea hacer un cambio? (s/n) \n").lower() == "n":
        break
print("Programa finalizado")