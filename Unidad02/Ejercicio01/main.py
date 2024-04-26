# En el archivo main.py
from cahorro import CAhorro

def test():
    cuentas = []
    for i in range(3):
        print("\nIngrese los datos para la cuenta", i+1)
        numero_cuenta = input("Número de cuenta: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        sexo = input("Sexo:(f para femenino y m para masculino)")
        cuil = input("CUIL: ")
        saldo = float(input("Saldo inicial: "))

        cuenta = CAhorro(numero_cuenta, nombre, apellido,sexo, cuil, saldo)
        cuentas.append(cuenta)

    for i, cuenta in enumerate(cuentas, start=1):
        print("\nDatos de la cuenta", i)
        cuenta.mostrarDatos()

        print("\nRealizando operaciones en la cuenta", i)
        monto_extraer = float(input("Monto a extraer: "))
        cuenta.extraer(monto_extraer)

        monto_depositar = float(input("Monto a depositar: "))
        cuenta.depositar(monto_depositar)

if __name__ == "__main__":
    test()

