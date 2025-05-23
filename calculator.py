def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: División por cero"
    return x / y

def main():
    print("Calculadora básica en Python")
    print("Opciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    try:
        choice = input("Elige una opción (1/2/3/4): ")
        if choice not in ('1', '2', '3', '4'):
            print("Opción inválida.")
            return

        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if choice == '1':
            print("Resultado:", add(num1, num2))
        elif choice == '2':
            print("Resultado:", subtract(num1, num2))
        elif choice == '3':
            print("Resultado:", multiply(num1, num2))
        elif choice == '4':
            print("Resultado:", divide(num1, num2))
    except ValueError:
        print("Por favor, ingresa valores numéricos válidos.")
    except KeyboardInterrupt:
        print("\nPrograma terminado por el usuario.")

if __name__ == "__main__":
    main()