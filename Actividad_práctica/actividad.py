cupo_total = 800000
sueldo_inicial = 800000
recargo = 0.03
deuda_total = 0
compras = []
suma = 0

while True:
    print("""
1.- Comprar
2.- Pagar Deuda
3.- Consultar detalles
4.- Compras Totales
5.- Salir""")
    
    op = input("Ingrese una opción: ")
    match op:
        case "1":
            while True:
                #Agregar función de compra
                monto_compra = int(input("Ingrese el monto de la compra: "))
                nombre_compra = input("Ingrese nombre producto")
                interes = monto_compra * recargo
                pago_total = interes + monto_compra
                compras.append(nombre_compra)
                suma +=1
                if pago_total > sueldo_inicial:
                    deuda_total = sueldo_inicial- pago_total
                    sueldo_inicial -= pago_total
                    if sueldo_inicial < 0:
                        sueldo_inicial = 0
                else:
                    sueldo_inicial -= pago_total
                print(sueldo_inicial)
                print(deuda_total)
                print(compras)
                break
        case "2":
            while True:
                #Agregar funcion deuda
                pago_deuda = int(input("Ingrese el monto a pagar de la deuda: "))
                if pago_deuda > -(deuda_total):
                    print(f"Su deuda es de {-(deuda_total)}, no puede pagar más que eso")
                if deuda_total == 0:
                    print("usted no tiene deudas pendientes")
                elif deuda_total < 0:
                    deuda_total += pago_deuda
                    print(deuda_total)
        case "3":
            print(f""" 
Cupo total: ${cupo_total}
deuda: ${deuda_total}
disponible: ${sueldo_inicial}""")
        case "4":
            print(f""" 
compras totales: {compras}
cantidad compras: {suma}""")
        case "5":
            print("adios")
            break

    