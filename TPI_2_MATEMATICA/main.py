from conjuntos_DNI import crear_conjuntos, calcular_diferencias, union_conjuntos, calcular_diferencia_simetrica,calcular_interseccion # importar librerias personales
# Funcion Main o principal
def main(): 
    while True: 
        print("\n--- MENU PRINCIPAL ---")
        print("A. --- Ingresar DNI(s) ---")
        print("B. --- Ingresar Fechas ---")
        print("C. --- PARA SALIR ---")

        menu_principal=input("Elige  una opcion: ")
        if menu_principal.lower() == "a":
            sub_menu_principal_A()
        
        elif menu_principal.lower() == "b":
            print("hola")
        elif menu_principal.lower()== "c":
            print("Hasta la proxima!") 
            break    
        else:
            print("Opcion no valida, intentelo de nuevo")
# Funcion Sub menu principal
def sub_menu_principal_A():
    dnis = []
    respuesta=""
    while True:
        respuesta=input("\nPresione 1 para continuar con la operacion: \nPresione 2 para Salir de la operacion: \n")
        if respuesta=="1":
            for i in range(5):
                dni = input(f"Ingrese un número de DNI ({i + 1}/5): ") # Una vez ingresados los 5 DNI(s) llamamos a todas las funciones creadas posteriormente
                dnis.append(dni) # .append(dni) agrega cada conjunto del dni a la lista DNIS[]
            conjuntos,nombres=crear_conjuntos(dnis) # LLamada a la funcion
            calcular_diferencias(conjuntos,nombres) # LLamada a la funcion
            union_conjuntos(dnis) # LLamada a la funcion
            calcular_diferencia_simetrica(conjuntos,nombres) # LLamada a la funcion
            calcular_interseccion(conjuntos,nombres) # LLamada a la funcion
        elif respuesta=="2": # Cierre del while
            break 
        else:
            print("Ingrese un valor valido, deben ser numericos")
# Ejecucion del programa solo si estamos en main
if __name__=="__main__":
    main()
