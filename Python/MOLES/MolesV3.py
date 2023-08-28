from tkinter import *
#Accion cerrar programa
def cierre():
    raiz.destroy()

#Listados de elementos con sus masas molares
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

def calcular():
    # Obtener los valores de los cuadros de texto
    nombre = str(cuadroNombre.get())
    gramos = float(cuadroGramos.get())
    masa_molar = elementos[nombre][1]

    # Cálculo
    moles = gramos / masa_molar

    # Mostrar el resultado en la etiqueta de resultado
    resultado.config(text="El calculo de " +str(gramos)+ "g de " + str(elementos[nombre][0]) + " a moles es = " + str(round( + moles , 3)) + " g/mol")

    #Mensaje de procedimiento
    mensaje_procedimiento.config(text="Procedimiento")
    
    #Muestreo del procedimiento  
    Proceso.config(text="Divide " +str(gramos)+ " entre " +str(masa_molar)+ " cuyo resultado es =" +str(round(moles , 3)) +" g/mol")
    
#Raiz de la interfaz
raiz = Tk()
raiz.title("Cálculo")
raiz.resizable(0, 0)
raiz.geometry("450x450")
raiz.config(bg="#869AA2")

#Interfaz
inicio = Frame(raiz)
inicio.pack(fill="both", expand="true")
inicio.config(bg="#869AA2")
inicio.config(width="450", height="450")
inicio.config(cursor="hand2")

#Cuadros de ingresos de datos
cuadroNombre = Entry(inicio)
cuadroNombre.grid(row=2, column=1, padx=10, pady=10)
cuadroNombre.config(bg="#B0C7D0", fg="black")

cuadroGramos = Entry(inicio)
cuadroGramos.grid(row=3, column=1, padx=10, pady=10)
cuadroGramos.config(bg="#B0C7D0", fg="black")

#Lo que ve el usuario
TituloLAL=Label(inicio,bg="#9C5CF3",fg="white", width=50,height=2, text="Calculo de gramos a moles")
TituloLAL.grid(row=0,column=0,columnspan=2,padx=0, pady=0,)

NombreLAL = Label(inicio,font=("Arial",12), bg="#869AA2",fg="white", width=25,height=2, text="Ingrese el símbolo químico:")
NombreLAL.grid(row=2, column=0, sticky="nsew", padx=5, pady=10)

GramosLAL = Label(inicio,font=("Arial",12),bg="#869AA2",fg="white", width=25, height=2, text="Ingrese los gramos a calcular:")
GramosLAL.grid(row=3, column=0, padx=5, pady=10)

#Boton calcular
Boton_calcular = Button(inicio,bg="#74D2E5",width=15,height=1, text="Calcular", command=calcular)
Boton_calcular.grid(row=4, column=0,columnspan=2, padx=10,pady=10)

#cuadro del resultado
resultado = Label(inicio,bg="#869AA2", width=45, height=1, text="", padx=10, pady=10)
resultado.grid(row=5, column=0, columnspan=2)

#Texto de procedimiento
mensaje_procedimiento = Label(inicio,font=("Arial",12), bg="#869AA2",fg="white", width=25,height=2, text="")
mensaje_procedimiento.grid(row=6,column=0,columnspan=2 )

#Proceso
Proceso = Label(inicio, bg="#869AA2", width=45, height=1, padx=10, pady=10, text="")
Proceso.grid(row=8,column=0,columnspan=2,padx=10,pady=10)

#boton cerrar
cierre =Button(raiz, bg="#9C5CF3",width=15, height=1, fg="white", padx="5", pady="5", text="Cerrar", command=cierre)
cierre.pack()

raiz.mainloop()
