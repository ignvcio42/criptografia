# Abre el archivo modificado en modo lectura
with open('processed_rockyou.dic', 'r') as archivo_modificado:
    # Lee todas las líneas del archivo en una lista
    contraseñas_modificadas = archivo_modificado.readlines()

# Cuenta la cantidad de contraseñas en la lista
cantidad_contraseñas = len(contraseñas_modificadas)

# Imprime la cantidad de contraseñas
print(f"El archivo modificado contiene {cantidad_contraseñas} contraseñas finales.")
