import os 

# Ruta del archivo CSV
ruta_csv = 'listadoEmpleado.cvs'

# Guardar los nombres en un diccionario
nombres = {}

# Vamos a leer linea por linea los nombres
with open(ruta_csv, 'r') as empleado:
    for linea in empleado:
        campos = linea.strip().split(',')

        # ignora la columna nombre
        if campos[0] == 'Nombres':
             continue
        nombre = campos[0]
        if nombre in nombres:
            nombres[nombres] += 1
    else:
        nombres[nombre] = 1
        directorio_raiz = os.path.dirname(os.path.abspath(__file__))

        for nombre in nombres:
            #crear la carpeta si no existe
            carpeta = os.path.join(directorio_raiz, nombre)
            if not os.path.exists(carpeta):
                os.makedirs(carpeta)
                print(f"se ha creado la carpeta para {nombre}")
            else:
                print(f"La carpeta para {nombre} ya existe")


