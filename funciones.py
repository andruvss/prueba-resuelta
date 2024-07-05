import os ,csv , time , msvcrt
pedidos = []
def Registrar_pedidos():
    print("Registrar pedido\nCliente")
    rut = int(input("Ingrese rut: "))
    nombre = input("Ingrese nombre: ")
    direccion = input("Ingrese direccion")
    comuna = int(input("Indique el número de la comuna(1: puente alto , 2: Pirque, 3:La pintana)"))
    print("\nPEDIDO")
    cant_5k = int(input("Indique cantidad de cilindro de 5kg: "))
    cant_15k = int(input("Indique cantidad de cilindros de 15kg: "))
    total = cant_5k*12500 + cant_15k*25500
    #como almacenar 1 pedido:
    pedido = {"rut":rut, "nombre":nombre, "direccion":direccion, "comuna":comuna[comuna-1],"cant_5k":cant_5k, "cant_15k":cant_15k, "total":total}
    pedidos.append(pedido)
    print("Pedido agregado con exito!")





def listar_pedidos():
    if not pedidos:
        print("No existen pedidos!")
    else:
        print("LISTAR PEDIDODS")
        for p in pedidos:
            print("RUT",p["rut"])    
            print("NOMBRE",p["nombre"])    
            print("DIRECCIÓN",p["direccion"])    
            print("COMUNA",p["comuna"])    
            print("CANT 5K",p["cant_5k"])    
            print("CANT 15K",p["cant_15k"])    
            print("TOTAL",p["total"]) 
            print()


def buscar_pedido():
    if not pedidos:
        print("No existen pedidos!")
    else:
        print("BUSCAR PEDIDO POR RUT")
        rut_buscar = int(input("Ingrese rut a buscar"))
        rut_existe = False
        for p in pedidos:
            if rut_buscar== p["rut"]:
                print("RUT",p["rut"])    
                print("NOMBRE",p["nombre"])    
                print("DIRECCIÓN",p["direccion"])    
                print("COMUNA",p["comuna"])    
                print("CANT 5K",p["cant_5k"])    
                print("CANT 15K",p["cant_15k"])    
                print("TOTAL",p["total"]) 
                print()
        if rut_existe==False:
            print("RUT NO EXISTE")


def imprimir_hoja_ruta():
    if not pedidos:
        print("No existe pedido alguno!")
    else:
        comuna = int(input("Ingrese comuna  1. puente alto, 2. pirque, 3.la pintana"))
        nombre_archivo = input("Ingrese nombre del archivo")+".csv"
        with open(nombre_archivo,"w",newline="") as file:
            escritor = csv.DictWriter(file,["rut","nombre","direccion","comuna","cant_5k","cant_15k","total"])
            escritor.writerheader()
            for p in pedidos:
                if p["comuna"]==comuna[comuna-1]:
                    escritor.writerow(p)
        print("ARCHIVO GUARDADO CORRECTAMENTE")

        
                
    
