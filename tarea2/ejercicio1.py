estudiantes = [("Ana", 20), ("Carlos", 22), ("Luis", 19), ("Sofía", 23), ("María", 21)]

def mayor_y_menor_edad(estudiantes):

    estudiantes_ordenados = sorted(estudiantes, key=lambda x: x[1])
    
    estudiante_menor = estudiantes_ordenados[0]
    estudiante_mayor = estudiantes_ordenados[-1]
    
    return estudiante_menor, estudiante_mayor

menor, mayor = mayor_y_menor_edad(estudiantes)
print(f"Estudiante con menor edad: {menor[0]}, Edad: {menor[1]}")
print(f"Estudiante con mayor edad: {mayor[0]}, Edad: {mayor[1]}")