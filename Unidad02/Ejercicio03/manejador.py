# manejador.py
from gestor_ventas import GestorVentas

class Manejador:
    def __init__(self):
        self.gestor_ventas = GestorVentas()

    def leer_venta(self):
        dia = int(input("Ingrese el día de la semana (1-7): "))
        sucursal = int(input("Ingrese el número de sucursal (1-5): "))
        importe = float(input("Ingrese el importe de la factura: "))
        self.gestor_ventas.registrar_venta(dia, sucursal, importe)

    def total_facturacion_sucursal(self):
        sucursal = int(input("Ingrese el número de la sucursal para calcular la facturación total: "))
        total = self.gestor_ventas.total_facturacion_sucursal(sucursal)
        print(f"La facturación total de la sucursal {sucursal} es: {total}")

    def sucursal_mas_facturacion_dia(self):
        dia = int(input("Ingrese el día de la semana para encontrar la sucursal con más facturación: "))
        sucursal = self.gestor_ventas.sucursal_mas_facturacion_dia(dia)
        print(f"La sucursal con más facturación el día {dia} es la sucursal {sucursal}")

    def sucursal_menos_facturacion_semana(self):
        sucursal = self.gestor_ventas.sucursal_menos_facturacion_semana()
        print(f"La sucursal con menos facturación durante toda la semana es la sucursal {sucursal}")

    def total_facturacion_semana(self):
        total = self.gestor_ventas.total_facturacion_semana()
        print(f"La facturación total de todas las sucursales durante la semana es: {total}")
