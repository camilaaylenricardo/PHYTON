Explicación del Código para la Gestión de Empleados:

1. Lista inicial de empleados:
   Se crea una lista de diccionarios, donde cada diccionario representa a un empleado
   con tres claves: 'nombre', 'edad' y 'puesto'. Esta lista contiene inicialmente 10 empleados.

2. Función 'agregar_empleado':
   Esta función permite agregar un nuevo empleado a la lista. Recibe como parámetros
   el nombre, la edad y el puesto del empleado, y luego añade este nuevo empleado a la lista.

3. Función 'listar_empleados':
   Esta función recorre la lista de empleados y muestra la información de cada uno en
   formato de texto, incluyendo su nombre, edad y puesto.

4. Función 'actualizar_empleado':
   Esta función permite actualizar la edad o el puesto de un empleado. Recibe como parámetros
   el nombre del empleado que se quiere modificar, y opcionalmente la nueva edad y/o el nuevo puesto.
   Si se encuentra el empleado, actualiza la información. Si no, muestra un mensaje indicando que no se encontró.

5. Función 'eliminar_empleado':
   Esta función permite eliminar un empleado de la lista. Recibe como parámetro el nombre
   del empleado, busca en la lista y lo elimina si es encontrado.

6. Función 'calcular_edad_promedio':
   Esta función calcula la edad promedio de todos los empleados. Suma las edades de todos
   los empleados y luego divide esta suma entre la cantidad total de empleados.

7. Función 'agregar_empleado_interactivo':
   Esta función permite que el usuario agregue empleados de forma interactiva. Pide al usuario
   que ingrese el nombre, la edad y el puesto del nuevo empleado a través de la consola.

Uso del código:
   - El usuario puede usar las funciones para agregar empleados, listarlos, actualizar su información,
     eliminarlos, o calcular la edad promedio. Además, la función interactiva permite ingresar empleados directamente.