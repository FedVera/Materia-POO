# main.py
from manejador import Manejador

def main():
    manejador = Manejador()

    while True:
        print("\nMenu:")
        print("1. Registrar venta")
        print("2. Facturación total de una sucursal")
        print("3. Sucursal con más facturación en un día")
        print("4. Sucursal con menos facturación durante la semana")
        print("5. Facturación total de la semana")
        print("6. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            manejador.leer_venta()
        elif opcion == 2:
            manejador.total_facturacion_sucursal()
        elif opcion == 3:
            manejador.sucursal_mas_facturacion_dia()
        elif opcion == 4:
            manejador.sucursal_menos_facturacion_semana()
        elif opcion == 5:
            manejador.total_facturacion_semana()
        elif opcion == 6:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
