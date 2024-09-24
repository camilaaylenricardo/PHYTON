# Lista de empleados inicial
companeros = [
    {'nombre': 'Nataly', 'edad': 19, 'ocupacion': 'Estudiante', 'especialidad': 'Informatica'},
    {'nombre': 'Alan', 'edad': 18, 'ocupacion': 'Desocupado', 'especialidad': 'Ninguna'},
    {'nombre': 'Facundo', 'edad': 18, 'ocupacion': 'Salir con menores', 'especialidad': 'Enganchar menores'},
    {'nombre': 'Tomas', 'edad': 19, 'ocupacion': 'Estudiante', 'especialidad': 'Informatica'},
    {'nombre': 'Matias', 'edad': 19, 'ocupacion': 'Desocupado', 'especialidad': 'Ninguna'},
    {'nombre': 'Luca', 'edad': 19, 'ocupacion': 'Estudiante', 'especialidad': 'Informatica'},
    {'nombre': 'Federico', 'edad': 19, 'ocupacion': 'Barbero', 'especialidad': 'Todo lo que sea barberia'},
    {'nombre': 'Alan alias alita', 'edad': 18, 'ocupacion': 'Estudiante', 'especialidad': 'Informatica'},
    {'nombre': 'Natalia', 'edad': 35, 'ocupacion': 'No hacer nada', 'especialidad': 'Hacer pestañas'},
    {'nombre': 'Juan', 'edad': 19, 'ocupacion': 'Estudiante', 'especialidad': 'Informatica'}
]

# Función para agregar empleados
def agregar_companero(nombre, edad, ocupacion, especialidad):
    nuevo_companero = {'nombre': nombre, 'edad': edad, 'ocupacion': ocupacion, 'especialidad': especialidad}
    companeros.append(nuevo_companero)

# Función para listar empleados
def listar_companeros():
    for com in companeros:
        print(f"Nombre: {com['nombre']}, Edad: {com['edad']}, Ocupacion: {com['ocupacion']}, Especialidad: {com['especialidad']}")

# Función para actualizar empleado
def actualizar_companero(nombre, nueva_edad=None, nueva_ocupacion=None, nueva_especialidad=None):
    for com in companeros:
        if com['nombre'] == nombre:
            if nueva_edad:
                com['edad'] = nueva_edad
            if nueva_ocupacion:
                com['ocupacion'] = nueva_ocupacion
            if nueva_especialidad:
                com['especialidad'] = nueva_especialidad
            print(f"Companero actualizado: {com}")
            return
    print(f"Companero con nombre {nombre} no encontrado.")

# Ejemplos de uso
# Agregar un empleado
agregar_companero('Sofia', 22, 'Becaria', 'Ninguna')

# Listar todos los empleados
listar_companeros()

# Actualizar información de un empleado
actualizar_companero('Juan', nueva_edad=31, nueva_ocupacion='Director')