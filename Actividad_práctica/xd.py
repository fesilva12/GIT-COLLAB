from os import system
system("cls")

interes = 0.03
comprando = True
            # numerodecompras #totaldecompras #deudaactual #cupototal
datos_cliente = [0, 0, 0, 800000]

def procesar_compra():
    compra = float(input("Ingrese el valor de la compra: "))
    compra_con_interes = compra + compra*interes
    if (datos_cliente[3]-datos_cliente[2])- compra_con_interes > 0:
        datos_cliente[0] = datos_cliente[0] + 1
        datos_cliente[1] = datos_cliente[1] + compra_con_interes
        datos_cliente[2] = datos_cliente[2] + compra_con_interes
        print('''
                Compra procesada satisfactoriamente
              ''')
    else:
        print('''
                Compra sobrepasa el cupo...
              ''')

def pagar_deuda():
    monto_de_pago = float(input(f"Ingrese el monto del pago que desea realizar, su deuda actual es de ${datos_cliente[2]}: "))
    if monto_de_pago <= datos_cliente[2] and monto_de_pago > 0:
        datos_cliente[2] = datos_cliente[2] - monto_de_pago
        print(f'''
                Pago realizado con exito, su deuda actual es de ${datos_cliente[2]}
            ''')
    elif monto_de_pago == 0:
        print('''
                El monto del pago debe ser distinto de 0
            ''')
    else:
        print('''
                El monto del pago no puede ser mayor a la deuda actual
            ''')
    
def consultar_detalles():
    print(f'''  Cupo total: {datos_cliente[3]}
                Deuda:      {datos_cliente[2]}
                Disponible: {datos_cliente[3] - datos_cliente[2]}
          ''')
    
def compras_totales():
    print(f'''
                Compras totales:        {datos_cliente[1]} 
                N° de compras:          {datos_cliente[0]}
        ''')
    if datos_cliente[0] == 0:
        print(f'''
                Promedio de compras: $0
        ''')
    else:
        print(f'''
                Promedio de compras: ${datos_cliente[1]/datos_cliente[0]}
        ''')

while comprando:
    print('''
                1.-Comprar
                2.-Pagar Deuda
                3.-Consultar detalles
                4.-Compras Totales
                0.-Salir
    ''')
    op = input("Seleccione una opción: ")
    match op:
        case "1":
            procesar_compra()
            pass
        case "2":
            pagar_deuda()
            pass
        case "3":
            consultar_detalles()
            pass
        case "4":
            compras_totales()
            pass
        case "0":
            comprando = False