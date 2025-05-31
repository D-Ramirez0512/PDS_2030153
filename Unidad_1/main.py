from src.actividad1 import graficar_senales

def main():
    actividad = input("Ingresa actividad (ej: actividad1): ").strip().lower()

    if actividad == 'actividad1':
        graficar_senales()
    else:
        print("invalid")

if __name__ == "__main__":
    main()
