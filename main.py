
import os

def limpiar_consola():
    os.system("cls")

def saludo_inicial():
    print("\n")
    print("="*60)
    print("   Bienvenido al sistema de gestión educativa - SchoolNet")
    print("="*60)
    print("\n")

def menu_numerico():
    print("Seleccione una de las siguientes opciones :)")
    print("1.- Agregar Colegio")
    print("2.- Agregar Curso")
    print("3.- Agregar Materia")
    print("4.- Agregar Estudiante")
    print("5.- Salir")

def main():
    limpiar_consola()
    saludo_inicial()
    while True:
        menu_numerico()
        opcion = input("Ingrese el número de la opción: ")
        if opcion == "5":
            print("¡Hasta luego! Recorda buscar el One Piece..")
            break
        elif opcion in ("1", "2", "3", "4"):
            print("Elegiste la opción", opcion, "(funcionalidad a programar)\n")
        else:
            print("Opción no válida, intente de nuevo.\n")

if __name__ == "__main__":
    main()
