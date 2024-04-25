# gestor_ventas.py

class GestorVentas:
    def __init__(self):
        self.__ventas = [[0 for _ in range(7)] for _ in range(5)]

    def registrar_venta(self, dia, sucursal, importe):
        self.__ventas[sucursal - 1][dia - 1] += importe

    def total_facturacion_sucursal(self, sucursal):
        total = sum(self.__ventas[sucursal - 1])
        return total

    # def sucursal_mas_facturacion_dia(self, dia):
        max_venta = max((fila[dia - 1], i + 1) for i, fila in enumerate(self.__ventas))
        return max_venta[1]  #
    
    
    ### def sucursal_mas_facturacion_dia(self, dia):
    ###int max_facturacion = 0  # Inicializamos el valor máximo de facturación con un valor muy bajo
    ###sucursal_max_facturacion = None  # Inicializamos la sucursal con la máxima facturación como None
    
    # Iteramos sobre las filas de ventas para encontrar la sucursal con la máxima facturación en el día dado
    ###for i, fila in enumerate(self.__ventas):
        facturacion_sucursal = fila[dia - 1]  # Obtenemos la facturación de la sucursal para el día dado
        if facturacion_sucursal > max_facturacion:
            max_facturacion = facturacion_sucursal  # Actualizamos el máximo de facturación
            sucursal_max_facturacion = i + 1  # Actualizamos la sucursal con la máxima facturación

    ###return sucursal_max_facturacion  # Devolvemos la sucursal con la máxima facturación en el día dado ###
    

    def sucursal_menos_facturacion_semana(self):
        total_ventas = [sum(fila) for fila in self.__ventas]
        min_venta = min((total, i + 1) for i, total in enumerate(total_ventas))
        return min_venta[1]

    def total_facturacion_semana(self):
        total = sum(sum(fila) for fila in self.__ventas)
        return total
