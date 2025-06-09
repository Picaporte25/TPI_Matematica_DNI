# def diversidad_numerica(dni_usuario):
#     cantidad_digitos_dni=set(str(dni_usuario))

#     if len(cantidad_digitos_dni) > 5:
#         return "Alta diversidad numerica"
#     else:
#         return "Baja diversidad numerica"


# def tipos_de_conjuntos(primer,segundo):
#     conjunto_de_digitos_uno = set(str(primer))
#     conjunto_de_digitos_dos = set(str(segundo))
#     conjunto_uno_ordenado=sorted(conjunto_de_digitos_uno)
#     conjunto_dos_ordenado=sorted(conjunto_de_digitos_dos)
#     print("Conjunto de digitos A ", conjunto_uno_ordenado, "Conjunto de digitos B ",  conjunto_dos_ordenado)

#     conjuntos_AyB = conjunto_de_digitos_uno | conjunto_de_digitos_dos
#     conjutos_AyB_ordenados=sorted(conjuntos_AyB)
#     print(f"La union de los conjuntos A Y B es: {conjutos_AyB_ordenados}")

# dni_usuario = int(input("Escriba su DNI: "))
# dni_usuario_dos = int(input("Escriba su DNI: "))

# print(tipos_de_conjuntos(dni_usuario, dni_usuario_dos))

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
                                # ESTAS RAYAS SON  PARA SEPARAR LA PRACTICA DE ARRIBA ^^^^^^^^^^^
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
                                # ESTAS RAYAS SON  PARA SEPARAR LA PRACTICA DE ARRIBA ||||||||||| 
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# FUNCION PARA CREAR LOS COJUNTOS A,B,C,D,E
def crear_conjuntos(dnis):
    conjuntos = [] # ASIGNAMOS UNA VARIABLE QUE TIENE UNA LISTA VACIA QUE VA A ALMACENAR LOS CONJUNTOS
    nombres = ["A","B","C","D","E"] # ASIGNAMOS LOS NOMBRES DE LOS CONJUNTOS
    i=0 # CONTADOR PARA INDICAR EL INDICE DE LA LISTA ( DE LOS NOMBRES A,B,C,D,E)
    print("\n----------   LOS CONJUNTOS   ----------\n")
    for dni in dnis: # Este for recorre la lista de DNIs
        conjuntos.append(set(dni)) # .append nos permite agregar al final de la lista "Conjuntos" los conjuntos ( que son convertidos en conjuntos gracias al set() )
    for  conjunto in conjuntos: # Este ciclo recorre los conjuntos  para poder escribirlos en pantalla con su letra " A=123456 ", "B=23456", etc
        print(f"Conjunto {nombres[i]} = {conjunto} ")
        i=i+1
    return conjuntos,nombres


# FUNCION UNION DE LOS CONJUNTOS
def union_conjuntos(dnis):
    print("\n----------   UNION DE CONJUNTOS   ----------\n")
    union_total_dnis=set() # CREACION DE VARIABLE UNION_TOTAL PARA ALMACENAR LOS NUMEROS DE LOS DNIS SIN REPETIR
    for dni in dnis:
        union_total_dnis.update(dni) #ACA USAMOS LA FUNCION .UPDATE()  QUE AGREGA LOS ELEMENTOS AL CONJUNTO SIN REPETIR , IDEAL PARA CALCULAR LA UNION
    print(f"\nLa union de los conjuntos es: {union_total_dnis}") #MENSAJE FINAL
    return union_total_dnis
# Funcion Calcular Diferencias
def calcular_diferencias(conjuntos,nombres): # Se  le pasan de parametros a calcular diferencias ( conjuntos que tiene almacenado los numeros de cada conjunto) y nombres que tiene almacenadas las letras "A","B","C",etc 
    print("\n----------   DIFERENCIA DE CONJUNTOS   ----------\n")
    for x in range(len(conjuntos)):# Creamos un ciclo que tiene como parametros recorrer la lista CONJUNTOS que tiene en su interior a los conjuntos 
        for y in range(len(conjuntos)): # Creamos un ciclo que tiene como parametros recorrer la lista CONJUNTOS que tiene en su interior a los conjuntos.
            if x != y: # Esta comparacion sirve para evitar que nos haga la diferencia de A - A, es seria irrelevante.
                diferencia=conjuntos[x] - conjuntos[y] # Resta de conjuntos
                if diferencia ==set(): # Condicional para  evitar que  aparezca un error de impresion
                    print(f"El conjunto {nombres[x]} Tiene los  mismos valores que el Conjunto {nombres[y]}")
                else:    
                    print(f"La diferencia entre ( {nombres[x]} - {nombres[y]} ) = {diferencia}") # Mensaje con el resultado
# Funcion calcular Diferencia Simetrica
def calcular_diferencia_simetrica(conjuntos,nombres):
    print("\n----------   DIFERENCIA SIMETRICA    ----------\n")
    for x in range(len(conjuntos)):
        for y in range(len(conjuntos)):
            if x != y:
                diferencia_simetrica= conjuntos[x] ^ conjuntos[y]
                if diferencia_simetrica ==set():
                    print(f"El conjunto {nombres[x]} Tiene los  mismos valores que el Conjunto {nombres[y]}")
                else:
                    print(f"La diferencia simetrica entre el conjunto {nombres[x]} y el conjunto {nombres[y]} es = {diferencia_simetrica}")# Mensaje con el resultado
# Funcion para calcular La Interseccion
def calcular_interseccion(conjuntos,nombres):
    print("\n----------   INTERSECCION    ----------\n")
    for x in range(len(conjuntos)):
        for y in range(len(conjuntos)):
            if x != y:
                interseccion= (conjuntos[x] & conjuntos[y])
                if interseccion ==set():
                    print(f"El conjunto {nombres[x]} Tiene los  mismos valores que el Conjunto {nombres[y]}")
                else:
                    print(f"La interseccion entre el conjunto {nombres[x]} y el conjunto {nombres[y]} es = {interseccion}")# Mensaje con el resultado