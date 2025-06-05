# Función para cargar estudiantes desde la consola
def cargar_estudiantes():
    """
    Permite ingresar estudiantes por teclado.
    Retorna una lista de diccionarios con nombre y nota.
    """
    estudiantes = []

    # Validación para cantidad de estudiantes
    while True:
        try:
            cantidad = int(input("¿Cuántos estudiantes desea ingresar?: "))
            if cantidad > 0:
                break
            else:
                print("Debe ingresar un número entero positivo.")
        except ValueError:
            print("Por favor ingrese un número válido (entero).")

    for i in range(cantidad):
        print(f"\nEstudiante #{i + 1}")
        nombre = input("Nombre: ").strip()

        while True:
            try:
                nota = float(input("Nota: "))
                if 0 <= nota <= 10:
                    break
                else:
                    print("La nota debe estar entre 0 y 10.")
            except ValueError:
                print("Por favor ingrese una nota válida (número decimal).")

        estudiantes.append({"nombre": nombre, "nota": nota})

    return estudiantes

# Algoritmo de ordenamiento: Bubble Sort por nota
def bubble_sort_por_nota(lista):
    """
    Ordena la lista de estudiantes de menor a mayor nota.
    """
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j]["nota"] > lista[j + 1]["nota"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Algoritmo de búsqueda lineal por nombre
def buscar_estudiante_por_nombre(lista, nombre_buscado):
    """
    Busca un estudiante por su nombre usando búsqueda lineal.
    Devuelve el diccionario del estudiante si lo encuentra, o None.
    """
    for estudiante in lista:
        if estudiante["nombre"].lower() == nombre_buscado.lower():
            return estudiante
    return None

# ---------- Programa principal ----------
if __name__ == "__main__":
    print("📋 Bienvenido al sistema de gestión de estudiantes")
    estudiantes = []
    opcion = 0
    while opcion != '4':
        print("\nAcciones disponibles:")
        print("1. Cargar estudiantes")
        print("2. Ordenar estudiantes por nota")
        print("3. Buscar estudiante por nombre")
        print("4. Salir")
        opcion = input("Ingrese su opción: ")
        print("---------------------------------")
        if opcion == '1':
            estudiantes = cargar_estudiantes()
            print("\n📚 Listado original de estudiantes:")
            for est in estudiantes:
                print(f"{est['nombre']} - Nota: {est['nota']}")
        elif opcion == '2':
            # Ordenar por nota
            bubble_sort_por_nota(estudiantes)
            print("\n📊 Estudiantes ordenados por nota (de menor a mayor):")
            for est in estudiantes:
                print(f"{est['nombre']} - Nota: {est['nota']}")
        elif opcion == '3':
            # Buscar estudiante
            nombre_buscado = input("\n🔍 Ingrese el nombre del estudiante que desea buscar: ").strip()
            resultado = buscar_estudiante_por_nombre(estudiantes, nombre_buscado)
            print(f"\n🔎 Resultado de búsqueda para '{nombre_buscado}':")
            if resultado:
                print(f"✅ Nombre: {resultado['nombre']} - Nota: {resultado['nota']}")
            else:
                print("❌ Estudiante no encontrado.")

    print("Fin del programa!")