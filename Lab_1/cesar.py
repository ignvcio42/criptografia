def cifrar_cesar(texto, correccion):
    resultado = ""
    for letra in texto:
        if letra.isalpha():  # Solo cifrar letras del alfabeto
            ajuste = 65 if letra.isupper() else 97  # 65 es el valor ASCII de 'A', 97 de 'a'
            cifrado = (ord(letra) - ajuste + correccion) % 26
            resultado += chr(cifrado + ajuste)
        else:
            resultado += letra  # Conserva los caracteres que no son letras
    return resultado

def main():
    texto_original = input("Ingrese el texto a cifrar: ")
    correccion = int(input("Ingrese la corrección (número entero): "))

    texto_cifrado = cifrar_cesar(texto_original, correccion)

    print("Texto cifrado:", texto_cifrado)

if __name__ == "__main__":
    main()
