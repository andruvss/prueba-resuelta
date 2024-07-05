from funciones import *
import os , csv , msvcrt


while True:
    print("GAXEXPLOSIVE")
    print("1. Registrar pedido")
    print("2. Listar todos los pedidos")
    print("3. Buscar pedido por rut")
    print("4. Imprimir hoja de ruta")
    print("5. Salir del programa")
    opc = int(input("Ingrese opción: "))
    os.system('cls')

    if opc ==1:
        Registrar_pedidos()
    elif opc ==2:
        listar_pedidos()
    elif opc==3:
        buscar_pedido()
    elif opc ==4:
        imprimir_hoja_ruta()
    else:
        print("Adios hasta pronto")




