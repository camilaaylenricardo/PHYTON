personas = {}

def registrar_persona(nombre, edad, correo):
    personas[nombre] = {"edad": edad, "correo": correo}

def filtrar_mayores_de_18(personas):
    mayores = {nombre: datos for nombre, datos in personas.items() if datos["edad"] > 18}
    return mayores

registrar_persona("Juan", 20, "juan@example.com")
registrar_persona("Ana", 17, "ana@example.com")
registrar_persona("Luis", 19, "luis@example.com")

mayores_de_18 = filtrar_mayores_de_18(personas)
print(f"Personas mayores de 18 años: {mayores_de_18}")