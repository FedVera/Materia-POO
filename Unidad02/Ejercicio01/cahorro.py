class CAhorro:
    def __init__(self, num_cuenta, nombre, apellido, sexo, cuil, saldo):
        self.__num_cuenta = num_cuenta
        self.__nombre = nombre
        self.__apellido = apellido
        self.__sexo = sexo
        self.__cuil = cuil
        self.__saldo = saldo

    def mostrarDatos(self):
        print("Número de Cuenta:", self.__num_cuenta)
        print("Nombre:", self.__nombre)
        print("Apellido:", self.__apellido)
        print("Sexo:", self.__sexo)
        print("CUIL:", self.__cuil)
        print("Saldo:", self.__saldo)

    def extraer(self, importe):
        if importe > self.__saldo:
            print("Saldo insuficiente.")
            return -1
        else:
            self.__saldo -= importe
            print("Extracción exitosa. Nuevo saldo:", self.__saldo)
            return self.__saldo

    def depositar(self, importe):
        if importe <= 0:
            print("El importe a depositar debe ser positivo.")
        else:
            self.__saldo += importe
            print("Depósito exitoso. Nuevo saldo:", self.__saldo)
