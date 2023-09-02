import sys

def cifrar_cesar(mensaje, corrimiento):
    mensaje_cifrado = ""
    for caracter in mensaje:
        if caracter.isalpha():
            mayuscula = caracter.isupper()
            caracter = caracter.upper()
            codigo = ord(caracter)
            codigo_cifrado = ((codigo - 65 + corrimiento) % 26) + 65
            if not mayuscula:
                mensaje_cifrado += chr(codigo_cifrado).lower()
            else:
                mensaje_cifrado += chr(codigo_cifrado)
        else:
            mensaje_cifrado += caracter
    return mensaje_cifrado

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 cesar.py <mensaje> <corrimiento>")
        sys.exit(1)

    mensaje = sys.argv[1]
    corrimiento = int(sys.argv[2])

    mensaje_cifrado = cifrar_cesar(mensaje, corrimiento)
    print("Mensaje cifrado:", mensaje_cifrado)
