empleados = [
    {'nombre': 'Juan', 'edad': 30, 'puesto': 'Gerente'},
    {'nombre': 'Maria', 'edad': 25, 'puesto': 'Asistente'},
    {'nombre': 'Carlos', 'edad': 40, 'puesto': 'Desarrollador'},
    {'nombre': 'Ana', 'edad': 28, 'puesto': 'Contadora'},
    {'nombre': 'Luis', 'edad': 35, 'puesto': 'Marketing'},
    {'nombre': 'Elena', 'edad': 32, 'puesto': 'RRHH'},
    {'nombre': 'Jose', 'edad': 29, 'puesto': 'Ventas'},
    {'nombre': 'Laura', 'edad': 33, 'puesto': 'Desarrollador'},
    {'nombre': 'Andres', 'edad': 45, 'puesto': 'Supervisor'},
    {'nombre': 'Gabriela', 'edad': 27, 'puesto': 'Diseñadora'}
]

def agregar_empleado(nombre, edad, puesto):
    nuevo_empleado = {'nombre': nombre, 'edad': edad, 'puesto': puesto}
    empleados.append(nuevo_empleado)
    print(f"Empleado {nombre} agregado exitosamente.")

def listar_empleados():
    for emp in empleados:
        print(f"Nombre: {emp['nombre']}, Edad: {emp['edad']}, Puesto: {emp['puesto']}")

def actualizar_empleado(nombre, nueva_edad=None, nuevo_puesto=None):
    for emp in empleados:
        if emp['nombre'] == nombre:
            if nueva_edad:
                emp['edad'] = nueva_edad
            if nuevo_puesto:
                emp['puesto'] = nuevo_puesto
            print(f"Empleado {nombre} actualizado: {emp}")
            return
    print(f"Empleado con nombre {nombre} no encontrado.")

def eliminar_empleado(nombre):
    for emp in empleados:
        if emp['nombre'] == nombre:
            empleados.remove(emp)
            print(f"Empleado {nombre} eliminado.")
            return
    print(f"Empleado con nombre {nombre} no encontrado.")

def calcular_edad_promedio():
    total_edad = sum(emp['edad'] for emp in empleados)
    promedio = total_edad / len(empleados)
    print(f"La edad promedio de los empleados es: {promedio:.2f} años.")
    return promedio

def agregar_empleado_interactivo():
    print("Agregar un nuevo empleado")
    nombre = input("Ingrese el nombre del empleado: ")
    edad = int(input("Ingrese la edad del empleado: "))
    puesto = input("Ingrese el puesto del empleado: ")
    agregar_empleado(nombre, edad, puesto)

listar_empleados()

agregar_empleado_interactivo()

listar_empleados()

actualizar_empleado('Juan', nueva_edad=31, nuevo_puesto='Director')

eliminar_empleado('Carlos')

calcular_edad_promedio()