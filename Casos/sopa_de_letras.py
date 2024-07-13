import random
import string

def contiene_caracteres_especiales(palabra):
    caracteres_especiales = {'{', '}', '[', ']', '@', ',', '.', '#', '$', '%', '^', '&', '*', '(', ')'}
    return any(char in caracteres_especiales for char in palabra)

def contiene_numeros(palabra):
    return any(char.isdigit() for char in palabra)

def validar_palabras(n, palabras):
    for palabra in palabras:
        if len(palabra) > n:
            return False
        if contiene_numeros(palabra):
            return False
        if contiene_caracteres_especiales(palabra):
            return False
    return True

def validar_numero(n):
    try:
        n = int(n)
        if n <= 0:
            raise ValueError("El tamaño de la sopa de letras debe ser un número entero positivo.")
        return n
    except ValueError:
        raise ValueError("Ingrese un número entero válido para el tamaño de la sopa de letras.")

def crear_sopa_de_letras(n, palabras):
    
    # Verificar si las palabras son válidas
    if not validar_palabras(n, palabras):
        raise ValueError("Las palabras no deben contener números, caracteres especiales y deben caber en la sopa de letras.")
    
    # Inicializa la sopa de letras con celdas vacías
    sopa = [[' ' for _ in range(n)] for _ in range(n)]

    # Función para colocar una palabra en la sopa de letras
    def colocar_palabra(palabra, x, y, dx, dy):
        for i, letra in enumerate(palabra):
            nx, ny = x + i * dx, y + i * dy
            if sopa[nx][ny] != ' ' and sopa[nx][ny] != letra:
                return False
        for i, letra in enumerate(palabra):
            nx, ny = x + i * dx, y + i * dy
            sopa[nx][ny] = letra
        return True

    # Intenta colocar todas las palabras en la sopa de letras
    # Horizontal, Vertical, Diagonal positiva, Diagonal negativa
    direcciones = [(1, 0), (0, 1), (1, 1), (-1, 1)] 
    for palabra in palabras:
        colocada = False
        while not colocada:
            x = random.randint(0, n-1)
            y = random.randint(0, n-1)
            dx, dy = random.choice(direcciones)
            if 0 <= x + (len(palabra) - 1) * dx < n and 0 <= y + (len(palabra) - 1) * dy < n:
                colocada = colocar_palabra(palabra, x, y, dx, dy)

    # Rellena los espacios en blanco con letras aleatorias
    for i in range(n):
        for j in range(n):
            if sopa[i][j] == ' ':
                sopa[i][j] = random.choice(string.ascii_uppercase)

    # Muestra la sopa de letras
    print("\nSOPA DE LETRAS :")
    print("\n")
    for fila in sopa:
        print(' '.join(fila))

    # Muestra las palabras a encontrar
    print("\nLas palabras a encontrar son:", ", ".join(palabras))
    print("\n")

if __name__ == "__main__":
    while True:
        try:
            n = input("Ingrese el tamaño de la sopa de letras (N): ")
            n = validar_numero(n)
            palabras = input("Ingrese las palabras separadas por comas: ").split(',')
            palabras = [palabra.strip().upper() for palabra in palabras]
            
            crear_sopa_de_letras(n, palabras)
            break
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"Error inesperado: {e}")
