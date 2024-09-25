def busqueda_binaria(A, primero, ultimo, x):
    if primero > ultimo:
        return -1

    mitad = (primero + ultimo) // 2

    if x == A[mitad]:
        return mitad
    if x < A[mitad]:
        return busqueda_binaria(A, primero, mitad - 1, x)
    else:
        return busqueda_binaria(A, mitad + 1, ultimo, x)

A = [1, 3, 5, 7, 9, 11, 13]
primero = 0  # En Python, la indexación comienza en 0
ultimo = len(A) - 1
x = 2

resultado = busqueda_binaria(A, primero, ultimo, x)
if resultado != -1:
    print(f"El elemento {x} se encuentra en la posición {resultado}.")
else:
    print(f"El elemento {x} no se encuentra en la lista.")
