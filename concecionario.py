
from Excepciones import ConsecionarioError
import random

from datetime import datetime,timedelta

import csv   


class Vehiculo:
    def __init__(self,color : str,placa : str,marca : str,modelo : str,precio : int,año : str):
        self.color : str = color
        self.placa : str = placa
        self.marca : str = marca
        self.modelo : str = modelo
        self.precio : int = precio
        año : str = año
        self.estado = False #esto guarda si esta vendido o no, al inicio no se encuentra vendido el auto, por tanto es false

    def informacion_del_vehiculo(self):#metodo para imprimir la informacion de un vehiculo
        print("Color:",self.color)
        print("Placa:",self.placa)
        print("Marca:",self.marca)
        print("Modelo:",self.modelo)
        print("Precio: $",self.precio)
        if(self.estado):
            print("Estado: vendido")
        else:
            print("Estado: sin vender")
    
    def asignarDatos(self,color,placa,marca,modelo,precio): #este metodo sirve por si alguien desea editar un vehiculo se reasignan los atributos
        self.color = color
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
    def venderVehiculo(self):
        self.estado = True




class Moto(Vehiculo):

    def __init__(self, color: str, placa: str, marca: str, modelo: str, precio: int, año: str):
        super().__init__(color, placa, marca, modelo, precio, año)

    
    def informacion_de_la_moto(self):

        super().informacion_del_vehiculo()

    def vendermoto(self):

        super().venderVehiculo()











    


class Piezas:

    

    producto = {
    "tipo":"",
    "pieza":"",
    "precio":0,
    "unidades disponibles":0}
        
    

class Test_drive:

    fecha = []

    def __init__(self,cedula:str,nombre:str,correo:str,numero:str,fecha):
        self.cedula : str = cedula
        self.nombre : str = nombre
        self.correo :str = correo
        self.numero:str = numero
        self.fechas = fecha

    def __str__(self) -> str:
        return f"{self.cedula} - {self.nombre} - {self.correo} - {self.numero} - {self.fecha}"
        
        

    def asignar_fecha():
        print("---------------------------------------")
        print("Agenda Tu Test Drive")
        try:
            cedula = input("Ingrese su cedula: ")
            nombre = input("Ingrese su nombre: ")
            correo = input("Ingrese su correo: ")
            numero = input("Ingrese su numero: ")
        except ValueError:
            print("Dato ingresado es incorrecto, ingreselo nuevamente")


        hoy = datetime.now()
        print(hoy)

        dirve = hoy + timedelta(days= random.randint(0,31), hours=random.randint(0,24),minutes=random.randint(0,60))
        Test_drive.fecha.append(Test_drive(cedula,nombre,correo,numero,dirve))

        print(f"Hola {nombre}, su test Drive fue asignado con la fecha {dirve}")
  

                       
class Agendar_citas(Test_drive):

    Citas = []

    def __init__(self, cedula: str, nombre: str, correo: str, numero: str, dia: str, mes: str,año):
        super().__init__(cedula, nombre, correo, numero)
        

    def asignar_fecha_cita():
        print("---------------------------------------")
        print("Agenda Tu cita")
        try:
            cedula = input("Ingrese su cedula: ")
            nombre = input("Ingrese su nombre: ")
            correo = input("Ingrese su correo: ")
            numero = input("Ingrese su numero: ")
            dia = input("Ingrese un dia para cita: ")
            mes = input("ingrese el mes de su cita: ")
            año = 2022
            print(f"su fecha de la cita es:{dia}/{mes}/{año}")

        except ValueError:
            print("Dato ingresado es incorrecto, ingreselo nuevamente")

            cita = (Test_drive(cedula,nombre,correo,numero,dia,mes,año))
            Agendar_citas.Citas.append(cita)
            

        

        

    


    
class Concesionario:

    concesionario_vehiculo = []#el concesionario es una lista de vehiculos
    
        
    concesionario_moto = []
    
    
    inventario = []
        
    


    def catalogo_de_vehiculos(concesionario_vehiculo):#metodo que recorre una lista de vehiculos e imprime la informacion de cada uno
        print("")
        for i in range(len(concesionario_vehiculo)):
            print("Vehiculo #",i+1)
            concesionario_vehiculo[i].informacion_del_vehiculo()
            print("--------------------")

    def catalogo_de_la_moto(concesionario_moto):#metodo que recorre una lista de vehiculos e imprime la informacion de cada uno
        print("")
        for i in range(len(concesionario_moto)):
            print("Moto #",i+1)
            concesionario_moto[i].informacion_de_la_moto()
            print("--------------------") 

    
    def catalogo_piezas():
        
        Concesionario.inventario.append( { "tipo":"llantas","pieza":"llantas michelin","precio" : 250000, "unidades disponibles":2 } )
        Concesionario.inventario.append( { "tipo":"frenos","pieza":"frenos racing","precio" : 3950000, "unidades disponibles":1} )
        Concesionario.inventario.append( { "tipo":"ventanas","pieza":"ventanas polarizadas","precio" : 1150000, "unidades disponibles":8} )

        for producto in Concesionario.inventario:

            print("---------------------")
            print("\t tipo:", producto["tipo"])
            print("\t pieza:", producto["pieza"])
            print("\t precio:", producto["precio"])
            print("\t unidaes disponibles:", producto["unidades disponibles"])
            

    def vender_producto():
        
        Concesionario.catalogo_piezas()

        buscar = input("ingrese el producto que quiere comprar....>")

        for producto in Concesionario.inventario:

            if buscar == producto["tipo"]:
                print("---------------------")
                print("\t tipo:", producto["tipo"])
                print("\t pieza:", producto["pieza"])
                print("\t precio:", producto["precio"])
                print("\t unidaes disponibles:", producto["unidades disponibles"])

            else:
                print("No hay un producto con ese nombre")

        print("vuelva pronto XD")

    def Cargar_catalogo():
        with open("carros/catalogoCarros.cw") as file:
            csv_carros = csv.reader(file, delimiter=";")
            carros = map(lambda carro : Vehiculo(carro[0], carro[1], carro[2], carro[3], float(carro[4]), carro[5]), csv_carros )
            Concesionario.concesionario_vehiculoa = carros

    def adicionar_carro(self, color,placa, marca, modelo,precio, año ):
        carro = Vehiculo(color,placa, marca, modelo,precio, año)
        return carro
    
    
    
    


class Menu:

    def menu():
    

        

        
    
        opc = 1
        while(opc != 0):
            print("------------------------------------------------")
            print()
            print("--------Bienvenido a tu Moto Sport--------")
            print()
            print("0. Salir")
            print("1. Registrar vehiculo")
            print("2. catalogo vehiculos")
            print("3. Vender vehiculo")
            print("4. Editar informacion de un vehiculo")
            print("5. registrar moto")
            print("6. catalogo de motos ")
            print("7. vender moto ")
            print("8. Comprar piezas ")
            print("9. Agendar test Drive ")
            print("10. Agendar cita")
            
            


            print()


            opc = int(input("Ingrese opcion: "))
            print()
            
            
            if(opc == 1):
                try:
                    color = str(input("Ingrese color: "))
                    placa = str(input("Ingrese placa: "))
                    marca = str(input("Ingrese marca: "))
                    modelo = str(input("Ingrese modelo: "))
                    precio = int(input("Ingrese precio: "))
                    año = str(input("Ingrese año: "))
                    Concesionario.concesionario_vehiculo.append(Vehiculo(color,placa,marca,modelo,precio,año))
                    
                
                except ValueError:
                    
                    print("El dato que ingreso esta incorrecto")
                    print("Vuelvalo a intentarlo")


            
            
            elif(opc == 2):
                Concesionario.catalogo_de_vehiculos(Concesionario.concesionario_vehiculo)
            elif(opc == 3):
                Concesionario.catalogo_de_vehiculos(Concesionario.concesionario_vehiculo)
                try:
                    numero = int(input("Ingrese # del vehiculo que desea vender: "))
                
                    if(numero >= 1 and numero <= len(Concesionario.concesionario_vehiculo)):
                        Concesionario.concesionario_vehiculo[numero-1].venderVehiculo()
                    else:
                        print("Ingrese # de vehiculo valido!")

                except ValueError:
                    print("El dato que ingreso no le corresponde un a carro")
                    print("vuelva intentarlo")
            
            elif(opc == 4):
                Concesionario.catalogo_de_vehiculos(Concesionario.concesionario_vehiculo)
                numero = int(input("Ingrese # del vehiculo que desea editar: "))
                color = input("Ingrese color: ")
                placa = input("Ingrese placa: ")
                marca = input("Ingrese marca: ")
                modelo = input("Ingrese modelo: ")
                precio = input("Ingrese precio: ")
                if(numero >= 1 and numero <= len(Concesionario.concesionario_vehiculo)):
                    Concesionario.concesionario_vehiculo[numero-1].asignarDatos(color,placa,marca,modelo,precio)
                else:
                    print("Ingrese # de vehiculo valido!")

            elif(opc == 5):
                try:
                    color = input("Ingrese color: ")
                    placa = input("Ingrese placa: ")
                    marca = input("Ingrese marca: ")
                    modelo = input("Ingrese modelo: ")
                    precio = input("Ingrese precio: ")
                    año = input("Ingrese año: ")
                    Concesionario.concesionario_moto.append(Moto(color,placa,marca,modelo,precio,año))
                except ValueError:
                    print("El dato que ingreso esta incorrecto")
                    print("Vuelvalo a intentarlo")


            elif(opc == 6):
                Concesionario.catalogo_de_la_moto(Concesionario.concesionario_moto) 

            elif(opc == 7):
                Concesionario.catalogo_de_la_moto(Concesionario.concesionario_moto)
                numero = int(input("Ingrese # de la moto que desea vender: "))
                if(numero >= 1 and numero <= len(Concesionario.concesionario_moto)):
                    Concesionario.concesionario_moto[numero-1].vendermoto()
                else:
                    print("Ingrese # de moto valido!")               

            elif(opc == 8):
                Concesionario.vender_producto()

            elif(opc == 9):
                Test_drive.asignar_fecha()
                

            elif(opc == 10):

                Agendar_citas.asignar_fecha_cita()
                

                
                

            
            else:
                print("Ingrese una opcion correcta y gracias")

         


            



Menu.menu()


