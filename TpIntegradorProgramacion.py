import timeit

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

def bubble_sort_por_nota(lista):
    """
    Ordena la lista de estudiantes de menor a mayor nota utilizando el algoritmo Bubble Sort.
    Devuelve una nueva lista ordenada.
    """
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j]["nota"] > lista[j + 1]["nota"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def quick_sort_por_nota(lista):
    """
    Ordena la lista de estudiantes de menor a mayor nota utilizando el algoritmo Quick Sort.
    Devuelve una nueva lista ordenada.
    """
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x["nota"] <= pivote["nota"]]
        mayores = [x for x in lista[1:] if x["nota"] > pivote["nota"]]
        return quick_sort_por_nota(menores) + [pivote] + quick_sort_por_nota(mayores)

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
    estudiantes = [
        {"nombre": "Paula", "nota": 8}, 
        {"nombre": "Pedro", "nota": 5.5}, 
        {"nombre": "Carlos", "nota": 3}, 
        {"nombre": "Juan", "nota": 10},
        {"nombre": "Andrea", "nota": 1},
        {"nombre": "Roberto", "nota": 4},
        {"nombre": "Matías", "nota": 6},
        {"nombre": "Ana", "nota": 2},
        {"nombre": "Lucas", "nota": 5},
        {"nombre": "Martín", "nota": 1.5},
        {"nombre": "Sol", "nota": 7}
    ]
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
            # Ejecutamos los algoritmos de ordenamiento y medimos el tiempo que demora cada uno
            start_time = timeit.default_timer()
            resultado_bubblesort = bubble_sort_por_nota(estudiantes.copy())
            end_time = timeit.default_timer()
            print("Tiempo Bubble Sort:", end_time - start_time, " segundos")
    
            start_time = timeit.default_timer()
            resultado_quicksort = quick_sort_por_nota(estudiantes.copy())
            end_time = timeit.default_timer()
            print("Tiempo Quick Sort:", end_time - start_time, " segundos")

            print("\n📊 Estudiantes ordenados por nota (de menor a mayor) - Bubble Sort:")
            for est in resultado_bubblesort:
                print(f"{est['nombre']} - Nota: {est['nota']}")

            print("\n📊 Estudiantes ordenados por nota (de menor a mayor) - Quick Sort:")
            for est in resultado_quicksort:
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