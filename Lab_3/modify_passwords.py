# Abre el archivo de entrada (Rockyoulinks) en modo binario
with open('rockyou.txt', 'rb') as archivo_entrada, open('processed_rockyou.dic', 'w') as archivo_salida:
    # Itera a través de cada línea en el archivo de entrada
    for linea in archivo_entrada:
        # Decodifica la línea utilizando UTF-8 y elimina espacios en blanco al principio y al final
        linea = linea.decode('utf-8', errors='ignore').strip()
        
        # Verifica si la línea no está vacía
        if linea:
            # Reemplaza la primera letra por su versión en mayúscula
            primera_letra = linea[0].upper()
            resto_de_la_linea = linea[1:]
            nueva_linea = primera_letra + resto_de_la_linea + '0'
            
            # Escribe la nueva línea en el archivo de salida
            archivo_salida.write(nueva_linea + '\n')

print("Proceso completado. El diccionario modificado se ha guardado en 'processed_rockyou.dic'.")
