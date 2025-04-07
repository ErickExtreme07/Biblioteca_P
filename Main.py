from Database import crear_tabla
from Biblioteca import agregar_libro, actualizar_libro, eliminar_libro, ver_libros, buscar_libros


def menu():
    print("\n--- Menú Biblioteca Personal ---")
    print("1. Agregar nuevo libro")
    print("2. Actualizar información de un libro")
    print("3. Eliminar libro existente")
    print("4. Ver listado de libros")
    print("5. Buscar libros")
    print("6. Salir")


def main():
    crear_tabla()
    while True:
        menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            genero = input("Género: ")
            estado = input("Estado (leído/no leído): ")
            agregar_libro(titulo, autor, genero, estado)
            print("Libro agregado correctamente.")

        elif opcion == "2":
            id_libro = input("ID del libro a actualizar: ")
            campo = input("Campo a modificar (titulo, autor, genero, estado): ")
            nuevo_valor = input("Nuevo valor: ")
            actualizar_libro(id_libro, campo, nuevo_valor)
            print("Libro actualizado correctamente.")

        elif opcion == "3":
            id_libro = input("ID del libro a eliminar: ")
            eliminar_libro(id_libro)
            print("Libro eliminado.")

        elif opcion == "4":
            libros = ver_libros()
            print("\nListado de libros:")
            for libro in libros:
                print(libro)

        elif opcion == "5":
            clave = input("Buscar por (titulo, autor, genero): ")
            valor = input("Valor a buscar: ")
            resultados = buscar_libros(clave, valor)
            print("\nResultados de la búsqueda:")
            for libro in resultados:
                print(libro)

        elif opcion == "6":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida, intenta nuevamente.")


if __name__ == "__main__":
    main()
