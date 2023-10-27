import numpy as np

def encontrar_inversa_matriz():
    # Solicitar al usuario las dimensiones de la matriz
    filas = int(input("Introduce el número de filas de la matriz: "))
    columnas = int(input("Introduce el número de columnas de la matriz: "))

    # Solicitar al usuario los elementos de la matriz
    print("Introduce los elementos de la matriz (por fila):")
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = float(input(f"Elemento [{i + 1}][{j + 1}]: "))
            fila.append(elemento)
        matriz.append(fila)

    # Convertir la lista de listas en un array de NumPy
    matriz_np = np.array(matriz)

    # Verificar si la matriz es cuadrada (número de filas = número de columnas)
    if filas != columnas:
        print("La matriz no es cuadrada. No tiene inversa.")
    else:
        # Calcular la inversa de la matriz utilizando NumPy
        try:
            inversa = np.linalg.inv(matriz_np)
            print("Matriz Inversa:")
            print(inversa)
        except np.linalg.LinAlgError:
            print("La matriz no tiene inversa.")

def resolver_sistema_ecuaciones():
    print("Elija el tamaño del sistema de ecuaciones:")
    print("1. 2x2")
    print("2. 3x3")
    print("3. 4x4")
    tamaño_sistema = int(input("Ingrese el número de su elección: "))

    # Pedir al usuario los coeficientes de las ecuaciones
    matriz_coeficientes = []
    vector_resultados = []
    for i in range(tamaño_sistema):
        fila = []
        for j in range(tamaño_sistema):
            coeficiente = float(input(f"Ingrese el coeficiente para la ecuación {i + 1}, variable {j + 1}: "))
            fila.append(coeficiente)
        matriz_coeficientes.append(fila)
        resultado = float(input(f"Ingrese el resultado para la ecuación {i + 1}: "))
        vector_resultados.append(resultado)

    # Convertir las listas en matrices de NumPy
    matriz_coeficientes = np.array(matriz_coeficientes)
    vector_resultados = np.array(vector_resultados)

    print("Elija el método para resolver el sistema:")
    print("1. Método de Cramer")
    print("2. Método de Gauss-Jordan")
    metodo = int(input("Ingrese el número de su elección: "))

    # Resolver el sistema de ecuaciones
    if metodo == 1:
        try:
            # Método de Cramer
            solucion_cramer = []
            for i in range(tamaño_sistema):
                matriz_temporal = matriz_coeficientes.copy()
                matriz_temporal[:, i] = vector_resultados
                solucion_cramer.append(np.linalg.det(matriz_temporal) / np.linalg.det(matriz_coeficientes))

            print("\nSolución por Cramer:", solucion_cramer)

            # Verificar el tipo de solución
            if len(set(solucion_cramer)) == 1:
                print("El sistema tiene una solución única.")
            else:
                print("El sistema tiene soluciones infinitas.")

        except np.linalg.LinAlgError:
            print("\nEl sistema no tiene solución única.")

    elif metodo == 2:
        try:
            # Método de Gauss-Jordan
            solucion_gauss = np.linalg.solve(matriz_coeficientes, vector_resultados)
            print("\nSolución por Gauss-Jordan:", solucion_gauss)

            # Verificar el tipo de solución
            if len(set(solucion_gauss)) == 1:
                print("El sistema tiene una solución única.")
            else:
                print("El sistema tiene soluciones infinitas.")

        except np.linalg.LinAlgError:
            print("\nEl sistema no tiene solución única.")
    else:
        print("\nOpción inválida. Por favor, elija un método válido.")


def multiplicar_matrices():
    # Solicitar al usuario las dimensiones de la primera matriz
    filas_matriz1 = int(input("Introduce el número de filas de la primera matriz: "))
    columnas_matriz1 = int(input("Introduce el número de columnas de la primera matriz: "))

    # Solicitar al usuario las dimensiones de la segunda matriz
    filas_matriz2 = int(input("Introduce el número de filas de la segunda matriz: "))
    columnas_matriz2 = int(input("Introduce el número de columnas de la segunda matriz: "))

    # Verificar si las matrices pueden ser multiplicadas
    if columnas_matriz1 != filas_matriz2:
        print("Las matrices no pueden ser multiplicadas. El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")
    else:
        # Solicitar al usuario los elementos de la primera matriz
        print("Introduce los elementos de la primera matriz (por fila):")
        matriz1 = []
        for i in range(filas_matriz1):
            fila = []
            for j in range(columnas_matriz1):
                elemento = float(input(f"Elemento [{i + 1}][{j + 1}]: "))
                fila.append(elemento)
            matriz1.append(fila)

        # Solicitar al usuario los elementos de la segunda matriz
        print("Introduce los elementos de la segunda matriz (por fila):")
        matriz2 = []
        for i in range(filas_matriz2):
            fila = []
            for j in range(columnas_matriz2):
                elemento = float(input(f"Elemento [{i + 1}][{j + 1}]: "))
                fila.append(elemento)
            matriz2.append(fila)

        # Convertir las listas de listas en arrays de NumPy
        matriz1_np = np.array(matriz1)
        matriz2_np = np.array(matriz2)

        # Realizar la multiplicación de las matrices utilizando NumPy
        resultado = np.dot(matriz1_np, matriz2_np)

        # Mostrar el resultado de la multiplicación de las matrices
        print("Resultado de la multiplicación de las matrices:")
        print(resultado)

# Menú principal
while True:
    print("\nMenú Principal:")
    print("1. Encontrar la inversa de una matriz")
    print("2. Resolver un sistema de ecuaciones lineales")
    print("3. Multiplicar matrices")
    print("4. Salir")
    opcion = int(input("Ingrese el número de su elección: "))

    if opcion == 1:
        encontrar_inversa_matriz()
    elif opcion == 2:
        resolver_sistema_ecuaciones()
    elif opcion == 3:
        multiplicar_matrices()
    elif opcion == 4:
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, elija una opción válida.")
