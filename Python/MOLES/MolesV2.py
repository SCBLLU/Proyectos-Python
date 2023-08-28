print("Convercion de gramos a moles\n")
print("     Ingrese los datos")

# Diccionario de elementos con sus masas MoLar
elementos = {
            "H": ("Hidrógeno", 1.008),
            "He": ("Helio", 4.003),
            "Li": ("Litio", 6.941),
            "Be": ("Berilio", 9.012),
            "B": ("Boro", 10.81),
            "C": ("Carbono", 12.011),
            "N": ("Nitrógeno", 14.007),
            "O": ("Oxígeno", 15.999),
            "F": ("Flúor", 18.998),
            "Ne": ("Neón", 20.180),
            "Na": ("Sodio", 22.990),
            "Mg": ("Magnesio", 24.305),
            "Al": ("Aluminio", 26.982),
            "Si": ("Silicio", 28.086),
            "P": ("Fósforo", 30.974),
            "S": ("Azufre", 32.066),
            "Cl": ("Cloro", 35.453),
            "Ar": ("Argón", 39.948),
            "K": ("Potasio", 39.098),
            "Ca": ("Calcio", 40.078),
            "Sc": ("Escandio", 44.956),
            "Ti": ("Titanio", 47.867),
            "V": ("Vanadio", 50.942),
            "Cr": ("Cromo", 52.000),
            "Mn": ("Manganeso", 54.938),
            "Fe": ("Hierro", 55.845),
            "Co": ("Cobalto", 58.933),
            "Ni": ("Níquel", 58.693),
            "Cu": ("Cobre", 63.546),
            "Zn": ("Zinc", 65.380),
            "Ga": ("Galio", 69.723),
            "Ge": ("Germanio", 72.630),
            "As": ("Arsénico", 74.922),
            "Se": ("Selenio", 78.960),
            "Br": ("Bromo", 79.904),
            "Kr": ("Kriptón", 83.798),
            "Rb": ("Rubidio", 85.468),
            "Sr": ("Estroncio", 87.620),
            "Y": ("Itrio", 88.906),
            "Zr": ("Zirconio", 91.224),
            "Nb": ("Niobio", 92.906),
            "Mo": ("Molibdeno", 95.940),
            "Tc": ("Tecnecio", 98),
            "Ru": ("Rutenio", 101.070),
            "Rh": ("Rodio", 102.905),
            "Pd": ("Paladio", 106.420),
            "Ag": ("Plata", 107.868),
            "Cd": ("Cadmio", 112.411),
            "In": ("Indio", 114.818),
            "Sn": ("Estaño", 118.710),
            "Sb": ("Antimonio", 121.760),
            "Te": ("Telurio", 127.600),
            "I": ("Yodo", 126.904),
            "Xe": ("Xenón", 131.293),
            "Cs": ("Cesio", 132.905),
            "Ba": ("Bario", 137.327),
            "Hf": ("Hafnio", 178.49),
            "Ta": ("Tántalo", 180.947),
            "W": ("Wolfra", 183.84),
            "R": ("Renio", 186.207),
            "O": ("Osmio", 190.23),
            "Ir": ("Iridio", 192.217),
            "Pt": ("Platino", 195.084),
            "A": ("Oro", 196.966),
            "Hg": ("Mercurio", 200.59),
            "TI": ("Talio", 204.383),
            "Pb": ("Plomo", 207.2),
            "Bi": ("Bismuto", 208.9804),
            "Po": ("Polonio", 208.9824),
            "At": ("Astato", 209.9871),
            "Rn": ("Radón", 222.0176),
            "Fr": ("Francio", 223.0197),
            "Ra": ("Radio", 226.0254),
            "Ac": ("Actinio", 227.0278),
            "Th": ("Torio", 232.0380),
            "Pa": ("Protactinio", 231.0358),
            "U": ("Uranio", 238.0289),
            "Np": ("Neptunio", 237.0482),
            "Pu": ("Plutonio", 244.0642),
            "Am": ("Americio", 243.0614),
            "Cm": ("Curio", 247.0703),
            "Bk": ("Berkelio", 247.0703),
            "Cf": ("Californio", 251.0796),
            "Es": ("Einstenio", 252.0829),
            "Fm": ("Fermio", 257.0951),
            "Md": ("Mendelevio", 258.0951),
            "No": ("Nobelio", 259.1009),
            "Lr": ("Lawrencio", 266.1193),
            "Ubu": ("Unbiunio", 320),
            "Ubb": ("Unbibio", 321),
            "Ubt": ("Unbitrio", 325),
            "Ubq": ("Unbiquadio", 330),
            "Ubp": ("Unbipentio", 332),
            "Ubh": ("Unbihexio", 334),
            "Ubs": ("Unbiseptium", 335),
            "La": ("Lantano", 138.905),
            "Ce": ("Cerio", 140.116),
}
while True:
    # Ingreso de datos
    Nombre = str(input("Ingrese el simbolo quimico: "))
    gramos = float(input("Ingrese los gramos a calcular: "))
    masa_molar = elementos[Nombre][1]

    #Confirmacion de datos
    confirmacion = input("Quiere hacer una modificacion? (s/n)\n").lower()
    while confirmacion == 's':
        Nombre = str(input("Ingrese el nuevo simbolo quimico: "))
        gramos = float(input("Ingrese los nuevos gramos a calcular: "))
        masa_molar = elementos[Nombre][1]
        confirmacion = input("Quiere hacer otra modificacion? (s/n)\n").lower()

    # Calculo
    MoLar = gramos / masa_molar

    # Muestro de datos
    print("\nEl calculo de " +str(gramos)+ "g de " + str(elementos[Nombre][0]) + " a moles es = " + str(round( + MoLar , 3)) + " g/mol")
    if input("\n¿Desea ver el procedimiento del cálculo? (s/n) ").lower() == "s":
        print("\n- Se divide " +str(gramos)+ " entre " +str(masa_molar)+ " y el resultado de la divicion es = " +str(round(MoLar , 3)) +" g/mol" )

    # Decision
    if input("\n¿Desea hacer un otro calculo? (s/n) ").lower() == "n":
        break

print("\nPrograma finalizado")