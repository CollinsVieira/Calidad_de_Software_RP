def validar_numero(num):
    if not isinstance(num, (int, float)) or num < 0:
        raise ValueError("Solo se permiten números positivos")
    return num

def suma(a, b):
    return validar_numero(a) + validar_numero(b)

def resta(a, b):
    return validar_numero(a) - validar_numero(b)

def multiplicacion(a, b):
    return validar_numero(a) * validar_numero(b)

def division(a, b):
    a, b = validar_numero(a), validar_numero(b)
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

def calculadora():
    opciones = {
        1: ("Sumar", suma),
        2: ("Restar", resta),
        3: ("Multiplicar", multiplicacion),
        4: ("Dividir", division)
    }
    
    while True:
        print("\n")
        print("\nIndique la operación que quiere realizar:")
        print("\n")
        for key, value in opciones.items():
            print(f"{key}) {value[0]}")
        print("5) Salir de la calculadora")
        
        try:
            print("\n")
            opcion = int(input("Seleccione una opción: "))
            print("\n")
            if opcion == 5:
                print("Saliste de la calculadora ")
                break
            if opcion not in opciones:
                raise ValueError("La opción que ingresaste no es válida")
            a = float(input("Ingrese el primer número: "))
            print("\n")
            b = float(input("Ingrese el segundo número: "))
            
            resultado = opciones[opcion][1](a, b)
            print(f"El resultado de {opciones[opcion][0].lower()} {a} y {b} es: {resultado}")
            print("\n")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    calculadora()
