import os
import json

contador = 0


class clienteclass:
    def __init__(self):
        self.datos = ["ID-Cliente", "Nombre", "Apellido","Dirección", "Telefono", "Ciudad"]
    


#setters para poder  cambiar las variables privadas

    def setIdcliente(self, id_cliente):
        self.__IdCliente = id_cliente

    def setNombre(self, nombre):
        self.__Nombre = nombre

    def setapellid(self, apellido):
        self.__Apellido = apellido

    def setDireccion(self, Direccion):
        self.__Direccion = Direccion

    def setTelefono(self, Telefono):
        self.__Telefono = Telefono

    def setCiudad(self, Ciudad):
        self.__Ciudad = Ciudad

 #getters para obtener las variables privadas
    def getidcliente(self):
        return clienteclass.ajustar_dato(self.__IdCliente, 12)

    def getNombre(self):
        return clienteclass.ajustar_dato(self.__Nombre, 10)

    def getapellid(self):
        return clienteclass.ajustar_dato(self.__Apellido, 10)

    def getDireccion(self):
        return clienteclass.ajustar_dato(self.__Direccion, 15)

    def getTelefono(self):
        return clienteclass.ajustar_dato(self.__Telefono, 10)

    def getCiudad(self):
        return clienteclass.ajustar_dato(self.__Ciudad, 15)

    def ajustar_dato(dato, caracteres):
        return (((((dato).title()).replace(" ", "-")).ljust(caracteres))[0:caracteres])

    def creardiccionario(self, idcliente, nombre, apellido, direccion, telefono, ciudad):
        diccionario = {"ID-Cliente": idcliente, "Nombre": nombre, "Apellido": apellido,
            "Dirección": direccion, "Telefono": telefono, "Ciudad": ciudad}
        diccionariojason = json.dumps(diccionario)
        return diccionariojason

    # Guarda informacion en base de datos

    def guardarInfo(self, cad, base):
        with open(base, "a") as baseDatos:
            baseDatos.write(cad+"\n")

    # Organizar cualquier base de datos
    def organizar(base, item):

            contador = 0
            item -= 1
            lista2 = []
            diccionario = {}
            cadena = ""
            cabecera = "|"
            diccionario_vehiculo = {"#placa": "", "id-cliente": "", "marca": "", "#modelo": "", "cilindraje": "",
                "color": "", "servicio": "", "combustible": "", "pasajeros": "", "carga": "", "#chasis": "", "#motor": ""}
            diccionario_servicio = {
                "cod": "", "servicio": "", "precio/hora": "", "horas": ""}
            diccionario_contrato = {"id-cliente": "",
                "#placa": "", "cod": "", "uds": "", "#": ""}

            for linea in base:
                diccionario = json.loads(linea)
                lista = [i for i in diccionario.values()]
                val = len(lista[item])

                try:
                    lista[item] = int(lista[item])
                    lista2.append(lista)
                    lista2.sort(key=lambda list: list[item])
                except:
                    lista2.append(lista)
                    lista2.sort(key=lambda list: list[item])

            for i in range(len(lista2)):
                lista2[i][item] = str(lista2[i][item]).ljust(val)

            if len(diccionario) == 12:
                for i in diccionario_vehiculo:
                    diccionario_vehiculo[i] = lista[contador]
                    palabra = i.ljust(len(diccionario_vehiculo[i]))
                    cabecera += palabra+"|"
                    contador += 1

            elif len(diccionario) == 4:
                for i in diccionario_servicio:
                    diccionario_servicio[i] = lista[contador]
                    palabra = i.ljust(len(diccionario_servicio[i]))
                    cabecera += palabra+"|"
                    contador += 1

            elif len(diccionario) == 5:
                for i in diccionario_contrato:
                    diccionario_contrato[i] = lista[contador]
                    palabra = i.ljust(len(diccionario_contrato[i]))
                    cabecera += palabra+"|"
                    contador += 1
            else:
                for i in diccionario:
                    palabra = i.ljust(len(diccionario[i]))
                    cabecera += palabra+"|"

            for i in lista2:
                i = "|".join(i)
                formato = "-"*(len(i)+2)+"\n"
                cadena += formato + "|"+i+"|"+"\n"

            if cadena == "":
                return "Base de datos vacía"

            else:
                return lista2

        # Leer base

    def leerBase(base, op, noid, verif, item):
        global contador
        contador = 0
        if op == '1':
            c = ""

            with open(base, "r") as baseDatos:

                for linea in baseDatos:
                    if base == "bFacturas.txt":
                        c += linea
                        if "FACTURA NUMERO" in linea:
                            contador += 1
                        continue
                    datos = json.loads(linea)
                    info = [i for i in datos.values()]
                    noid = noid.ljust(len(info[0]))

                    if noid == info[0]:
                        for dato in info:
                            c += dato+" "
                        c += "\n"
                        if verif == True and c != "":
                            return datos

            if c == "":
                return "No info"
            else:
                return c

        if op == '2': 
            with open(base, "r") as baseDatos:
                return (clienteclass.organizar(baseDatos, item))

        else:
            return "Opcion ingresada no es valida."
# Eliminar elemento en la base de datos

    def eliminarElemento(base, noid, ident):
        elementos = []
        with open(base, "r") as baseDatos:
            for linea in baseDatos:
                datos = json.loads(linea)
                elementos.append(datos)

        with open(base, "w") as baseDatos:
            for elemento in elementos:
                if noid != elemento[ident]:
                    datoGuardar = json.dumps(elemento)
                    baseDatos.write(datoGuardar+"\n")
# Limpia base de datos

    def limpiarBase(base):
        conf = input(
            "Seguro que desea eliminar base de datos? (s/n): \n").lower()

        if conf == 's':
            os.remove(base)
            if base == "bContratos.txt":
                os.remove("bFacturas.txt")
            print("Base de datos eliminada con exito! Volviendo al menu principal")
            return conf

        elif conf == 'n':
            print("Base de datos no eliminada.")

        else:
            print("Opcion no valida!")


class vehiculoclass(clienteclass):
        def __init__(self):
            self.datos=["Numero de placa", "ID-Cliente", "Marca", "Numero de modelo", "Cilindraje", "Color", "Tipo de servicio","Tipo de combustible", "Capacidad de pasajeros", "Capacidad de carga", "Numero de chasis", "Numero de Motor"]
            
        def setPlaca (self, placa):
            self.__placa = placa
        def setid(self, id):
            self.__id = id
        def setmarca(self, marca):
            self.__marca = marca
        def setmodelo(self, modelo):
            self.__modelo = modelo

        def setcilindraje (self, cilindraje):
            self.__cilindraje = cilindraje

        def setcolor (self, color):
            self.__color = color

        def setservicio (self, servicio):
            self.__servicio = servicio
        def setcombustible (self, combustible):
            self.__combustible = combustible

        def setpasajeros (self, pasajeros):
            self.__pasajeros = pasajeros

        def setcarga (self, carga):
            self.__carga = carga

        def setchasis(self, chasis):
            self.__chasis = chasis
        def setmotor (self, motor):
            self.__motor = motor

        def getplaca(self):
            return vehiculoclass.ajustar_dato(self.__placa, 10)

        def getidcliente(self):
            return vehiculoclass.ajustar_dato(self.__id, 12)

        def getmarca(self):
            return vehiculoclass.ajustar_dato(self.__marca, 15)

        def getmodelo (self):
            return vehiculoclass.ajustar_dato(self.__modelo,  10)

        def getcilindraje (self):
            return vehiculoclass.ajustar_dato(self.__cilindraje, 10)

        def getcolor (self):
            return vehiculoclass.ajustar_dato(self.__color, 10)

        def getservicio (self):
            return vehiculoclass.ajustar_dato(self.__servicio, 10)

        def getcombustle (self):
            return vehiculoclass.ajustar_dato(self.__combustible, 15)

        def getpasajeros(self):
            return vehiculoclass.ajustar_dato(self.__pasajeros, 10)

        def getcarga (self):
            return vehiculoclass.ajustar_dato(self.__carga, 10)

        def getchasisi(self):
            return vehiculoclass.ajustar_dato(self.__chasis, 10)

        def getmotor (self):
            return vehiculoclass.ajustar_dato(self.__motor, 10)



        def creardiccionario(self, placa,idcliente,marca,modelo,cilindraje,color,servicio,combustible,pasajeros,carga,chasis,motor):
            diccionario ={"Numero de placa": placa, "ID-Cliente": idcliente, "Marca": marca, "Numero de modelo": modelo, "Cilindraje": cilindraje, "Color": color, "Tipo de servicio": servicio,
                         "Tipo de combustible": combustible, "Capacidad de pasajeros": pasajeros, "Capacidad de carga": carga, "Numero de chasis": chasis, "Numero de Motor": motor}
            diccionariojason = json.dumps(diccionario)
            return diccionariojason


class servicioclass(clienteclass):
    def __init__(self):
        self.datos=["Codigo del servicio", "Nombre del servicio","Precio/hora", "Horas del servicio"]
      
    def setCodigo(self, codigo):
        self.__Codigo = codigo
    def setNombre(self, nombre):
        self.__nombre = nombre
    def setPrecio(self, precio):
        self.__precio = precio
    def setHoras(self, horas):
        self.__horas = horas

    def getCodigo (self):
        return servicioclass.ajustar_dato(self.__Codigo, 4)

    def getNombre(self):
        return servicioclass.ajustar_dato(self.__nombre, 15)

    def getPrecio(self):
        return servicioclass.ajustar_dato(self.__precio, 15)

    def getHoras(self):
        return servicioclass.ajustar_dato(self.__horas, 5)


    def creardiccionario(self, codigo,nombre,precio,horas):
        diccionario ={"Codigo del servicio": codigo, "Nombre del servicio": nombre,
                     "Precio/hora": precio, "Horas del servicio": horas}
        diccionariojason = json.dumps(diccionario)
        return diccionariojason
        
    def solServicio (self,idcliente,placa,codigo,unidades):
        
        datosContrato ={"ID-Cliente": idcliente, "Placa": placa,
                         "Codigo del servicio": codigo, "Unidades contratadas": unidades}

        clienteclass.leerBase("bFacturas.txt", "1", "0000", False)
        datosContrato["No. factura"] = str(contador)

        # Comprueba que servicio solicitado existe
        if clienteclass.leerBase("bServicios.txt", '1', datosContrato["Codigo del servicio"], False) == "No info":
            print("Servicio no existe, verifique base de datos.")
            return False
        else:
            # Comprueba que el vehiculo este en la base de datos. Si no, solicita que se agregue informacion
            if clienteclass.leerBase("bClientes.txt", '1', datosContrato["ID-Cliente"], False) != "No info" and clienteclass.leerBase ("bVehiculos.txt", '1', datosContrato["Placa"], False) != "No info":
                diccionariojason = json.dumps(datosContrato)
                servicio = servicioclass()
                servicio.guardarInfo(
                    (facturasclass.imprimirfac(datosContrato)), "bFacturas.txt")
                return diccionariojason
            else:
                if clienteclass.leerBase("bClientes.txt", '1', datosContrato["ID-Cliente"], False) == "No info" and clienteclass.leerBase ("bVehiculos.txt", '1', datosContrato["Placa"], False) != "No info":
                    print("Cliente no existe, verifique la base de datos.")
                elif clienteclass.leerBase("bClientes.txt", '1', datosContrato["ID-Cliente"], False) != "No info" and clienteclass.leerBase ("bVehiculos.txt", '1', datosContrato["Placa"], False) == "No info":
                    print("vehículo no existe, verifique la base de datos.")
                else:
                    print(
                        "Cliente y vehículo no existen, verifique las bases de datos.")
                return False


    # Contratar servicio
class contratoclass(clienteclass):
    def __init__(self):
        self.datos=["ID-Cliente", "Placa", "Codigo del servicio", "Unidades contratadas", "No. factura"]

    def setIDCliente (self, idcliente):
        self.__idcliente= idcliente
    def setPlaca (self, Placa):
        self.__placa=Placa
    def setCodigo (self,Codigo):
        self.__codigo=Codigo
    def setunidades (self,unidades):
        self.__unidades=unidades
    
    def getIDcliente (self):
        return contratoclass.ajustar_dato(self.__idcliente, 12)
    def getPlaca (self):
        return contratoclass.ajustar_dato(self.__placa, 10)
    def getCodigo (self):
        return contratoclass.ajustar_dato(self.__codigo, 4)
    def getUnidades (self):
        return contratoclass.ajustar_dato(self.__unidades, 3)




class facturasclass(clienteclass):
    def __init__(self):
         pass
    # imprimir facturas

    def imprimirfac(contrato):
        global contador

        id_cliente = contrato["ID-Cliente"]
        placa = contrato["Placa"]
        codigo_servicio = contrato["Codigo del servicio"]
        unidades = int((contrato["Unidades contratadas"]).rstrip())

        infoCliente = clienteclass.leerBase(
            "bClientes.txt", "1", id_cliente, True)
        infoVehiculo = clienteclass.leerBase(
            "bVehiculos.txt", "1", placa, True)
        infoServicio = clienteclass.leerBase(
            "bServicios.txt", "1", codigo_servicio, True)
        clienteclass.leerBase("bFacturas.txt", "1", "0000", False)
        cadena_cliente, cadena_vehiculo, cadena_servicio = "INFORMACIÓN DE USUARIO\n", "INFORMACIÓN DE VEHICULO\n", "INFORMACIÓN DE SERVICIO\n"

        for i in infoCliente:
            cadena = infoCliente[i].rstrip()
            cadena_cliente += i+": "+cadena+"\t\t"

        cadena_vehiculo += "Numero de placa: " + infoVehiculo["Numero de placa"].rstrip() + "\t\t" + \
            "Marca: " + infoVehiculo["Marca"].rstrip() + "\t\t" + \
            "Numero de Modelo: " + infoVehiculo["Numero de modelo"].rstrip() + "\t\t" + \
            "Color: " + infoVehiculo["Color"].rstrip()

        for i in infoServicio:
            cadena = infoServicio[i].rstrip()
            cadena_servicio += i+": "+cadena+"\t\t"
        cadena_servicio += "\n"+"Unidades contratadas:"+str(unidades)


        Total = int(infoServicio["Precio/hora"]) * int(infoServicio["Horas del servicio"])*unidades
        factura = "FACTURA NUMERO "+str(contador)+"\n"*2+cadena_cliente+"\n"*2 + \
            cadena_vehiculo+"\n"*2+cadena_servicio + \
            "\n"*2+"TOTAL A PAGAR: $"+str(Total)+"\n"*3

        print(factura)
        nuevaFactura = {"consec": contador, "infoFac": factura}
        factura = json.dumps(nuevaFactura)
        return factura

#Limpia la consola

def borrarPantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


# función que comprueba si la entrada es un entero


def lee_entero():
    while True:
        try:
            valor = int(input())
            return valor

        except ValueError:
            print("ATENCIÓN: Debe ingresar un número entero.")

# función para comprobar una entrada del usuario dentro de un rango


def comprobar(a, b):
    while True:
        respuesta = lee_entero()

        if a <= respuesta <= b:
            return respuesta

        else:
            print("Debe ingresar un número entre ", a, "-", b, sep="")

# Base de Datos de Clientes


def clientes():
    op = ''

    while op != '0':
        borrarPantalla()
        print("(1) Ver clientes.\n(2) Agregar un cliente nuevo.\n(3) Eliminar un cliente.\n(4) Limpiar la base de datos.\n(0) Volver al menu principal.")
        op = input("Seleccione una opcion: \n")

        if op == '1':  # Lista de clientes
            borrarPantalla()
            sop = input(
                "(1) Buscar un cliente.\n(2) Mostrar todos los clientes.\n")
            if sop == '1':
                noid = input("Inserte no. identificacion del cliente:\n")
            else:
                noid = ""
            result = clienteclass.leerBase("bClientes.txt", sop, noid, False)
            if result != "No info":
                print(result)
            else:
                print("Informacion no encontrada.")

        elif op == '2':  # Agregar cliente
            cliente = clienteclass()
            cliente.setIdcliente(input("Id-cliente:"))
            cliente.setNombre(input("Nombre:"))
            cliente.setapellid(input("apellido:"))
            cliente.setDireccion(input("Dirección:"))
            cliente.setTelefono(input("Teléfono:"))
            cliente.setCiudad(input("Ciudad:"))
            diccionario = cliente.creardiccionario(cliente.getidcliente(),cliente.getNombre(), cliente.getapellid(),cliente.getDireccion(), cliente.getTelefono(), cliente.getCiudad())
            cliente.guardarInfo(diccionario, "bClientes.txt" )
            print("Cliente agregado con exito!")

        elif op == '3':  # Elimina un cliente de la base de datos
            noid = input(
                "Ingrese no. identificacion del cliente que desea eliminar:\n").ljust(12)
            clienteclass.eliminarElemento("bClientes.txt", noid, "ID-Cliente")
            clienteclass.eliminarElemento("bVehiculos.txt", noid, "ID-Cliente")
            print("Cliente eliminado con exito!")

        elif op == '4':  # Borra toda la informacion en la base de datos
            result = clienteclass.limpiarBase("bClientes.txt")
            if result == 's':
                break
            else:
                input("Presione ENTER para continuar...")
                continue

        elif op == '0':  # Volver a menu principal
            break

        else:
            print("Opcion no valida. Intente nuevamente!")
        input("Presione ENTER para continuar...")

# Base de Datos de Vehiculos


def vehiculos():
    op = ''

    while op != '0':
        borrarPantalla()
        print("(1) Ver vehiculos en sistema.\n(2) Agregar un vehiculo nuevo.\n(3) Eliminar un vehiculo.\n(4) Limpiar la base de datos.\n(0) Volver al menu principal.")
        op = input("Seleccione una opcion: \n")

        if op == '1':  # Lista de vehiculos
            borrarPantalla()
            sop = input(
                "(1) Buscar un vehiculo.\n(2) Mostrar todos los vehiculos.\n")
            if sop == '1':
                noid = input("Inserte placa del vehiculo:\n")
            else:
                noid = ""
            result = clienteclass.leerBase("bVehiculos.txt", sop, noid, False)
            if result != "No info":
                print(result)
            else:
                print("Informacion no encontrada.")

        elif op == '2':  # Agregar vehiculo
            vehiculo = vehiculoclass()
            vehiculo.setPlaca(input("Placa:"))
            vehiculo.setid(input("Id-Cliente:"))
            vehiculo.setmarca(input("Marca:"))
            vehiculo.setmodelo(input("Modelo:"))
            vehiculo.setcilindraje(input("Cilindraje:"))
            vehiculo.setcolor(input("Color:"))
            vehiculo.setservicio(input("Servicio:"))
            vehiculo.setcombustible(input("Combustible:"))
            vehiculo.setpasajeros(input("Pasajeros:"))
            vehiculo.setcarga(input("Carga:"))
            vehiculo.setchasis(input("Chasis:"))
            vehiculo.setmotor(input("Motor:"))
            diccionario = vehiculo.creardiccionario(vehiculo.getplaca(),vehiculo.getidcliente(),vehiculo.getmarca(),vehiculo.getmodelo(),vehiculo.getcilindraje(),vehiculo.getcolor(),vehiculo.getservicio(),vehiculo.getcombustle(), vehiculo.getpasajeros(),vehiculo.getcarga(),vehiculo.getchasisi(),vehiculo.getmotor())
            vehiculo.guardarInfo(diccionario, "bVehiculos.txt")
            print("Vehiculo agregado con exito!")

        elif op == '3':  # Elimina un vehiculo
            placa = input(
                "Ingrese placa del vehiculo que desea eliminar: \n").ljust(10)
            clienteclass.eliminarElemento(
                "bVehiculos.txt", placa, "Numero de placa")
            print("Vehiculo eliminado con exito!")

        elif op == '4':  # Borra toda la informacion en la base de datos
            result = clienteclass.limpiarBase("bVehiculos.txt")
            if result == 's':
                break
            else:
                input("Presione ENTER para continuar...")
                continue

        elif op == '0':  # Volver a menu principal
            break

        else:
            print("Opcion no valida. Intente nuevamente!")
        input("Presione ENTER para continuar...")

# Base de Datos de Servicios


def servicios():
    op = ''

    while op != '0':
        borrarPantalla()
        print("(1) Lista de servicios.\n(2) Crear un servicio nuevo.\n(3) Eliminar un servicio existente.\n(4) Limpiar base de datos.\n(0) Volver al menu principal.")
        op = input("Seleccione una opcion: \n")

        if op == '1':  # Lista de servicios
            borrarPantalla()
            sop = input(
                "(1) Buscar un servicio.\n(2) Mostrar todos los servicios.\n")
            if sop == '1':
                noid = input("Inserte codigo del servicio:\n")
            else:
                noid = ""
            result = clienteclass.leerBase("bServicios.txt", sop, noid, False)
            if result != "No info":
                print(result)
            else:
                print("Informacion no encontrada.")

        elif op == '2':  # Agregar servicio
            servicio = servicioclass()
            servicio.setCodigo(input("Código:"))
            servicio.setNombre(input("Nombre:"))
            servicio.setPrecio(input("Precio:"))
            servicio.setHoras(input("Horas:"))
            codigo, nombre, precio, horas = servicio.getCodigo(),servicio.getNombre(),servicio.getPrecio(), servicio.getHoras()
            diccionario = servicio.creardiccionario(codigo,nombre,precio,horas)
            servicio.guardarInfo(diccionario, "bServicios.txt")
            print("Servicio agregado con exito!")

        elif op == '3':  # Eliminar un servicio
            noid = input("Ingrese codigo del servicio: \n").ljust(4)
            clienteclass.eliminarElemento(
                "bServicios.txt", noid, "Codigo del servicio")
            print("Servicio eliminado con exito!")

        elif op == '4':  # Borra toda la informacion en la base de datos
            result = clienteclass.limpiarBase("bServicios.txt")
            if result == 's':
                break
            else:
                input("Presione ENTER para continuar...")
                continue

        elif op == '0':  # Volver a menu principal
            break

        else:
            print("Opcion no valida. Intente nuevamente!")
        input("Presione ENTER para continuar...")

# Base de Datos de Contratos


def contratos():
    op = ''

    while op != '0':  # Pendiente generar facturas#######
        borrarPantalla()
        print("(1) Ver contratos existentes\n(2) Nuevo contrato\n(3) Eliminar un contrato\n(4) Generar factura\n(5) Limpiar base de datos\n(0) Volver al menu principal")
        op = input("Seleccione una opcion:\n")

        if op == '1':  # Lista contratos
            borrarPantalla()
            sop = input(
                "(1) Buscar un contrato\n(2) Mostrar todos los contratos en sistema\n")
            if sop == '1':
                noid = input("Inserte ID-Cliente:\n")
            else:
                noid = ""
            result = clienteclass.leerBase("bContratos.txt", sop, noid, False)
            if result != "No info":
                print(result)
            else:
                print("Informacion no encontrada.")

        elif op == '2':  # Agregar Contrato
            contrato=contratoclass()
            serivicio=servicioclass()
            contrato.setIDCliente(input("id-Cliente:"))
            contrato.setPlaca(input("Placa:"))
            contrato.setCodigo(input("Codigo:"))
            contrato.setunidades(input("Unidades:"))
            contrato = serivicio.solServicio(contrato.getIDcliente(),contrato.getPlaca(),contrato.getCodigo(),contrato.getUnidades())
            if contrato != False:
                cliente = clienteclass()
                cliente.guardarInfo(contrato, "bContratos.txt")

        elif op == '3':
            noid = input("Ingrese ID-Cliente: \n").ljust(12)
            clienteclass.eliminarElemento("bContratos.txt", noid, "ID-Cliente")
            print("Contrato eliminado con exito!")

        elif op == '4':
            noFactura = int(input("Ingrese numero de factura:\n"))
            ex = False
            with open("bFacturas.txt", "r") as baseFacturas:
                for linea in baseFacturas:
                    factura = json.loads(linea)
                    if factura["consec"] ==noFactura:
                        print(factura["infoFac"])
                        ex = True
                if not ex:
                    print("Factura no encontrada.")

        elif op == '5':
            result = limpiarBase("bContratos.txt")
            if result == 's':
                break
            else:
                input("Presione ENTER para continuar...")
                continue

        elif op == '0':
            break

        else:
            print("Opcion no valida. Intente nuevamente!")
        input("Presione ENTER para continuar...")

# Menu Principal


def menu():
    op = '1'
    print("¡Bienvenido.\nIniciando sistema...")

    while op != '0':
        borrarPantalla()
        if not os.path.exists("bClientes.txt"):
            baseClientes = open("bClientes.txt", "x")
            baseClientes.close()

        if not os.path.exists("bVehiculos.txt"):
            baseVehiculos = open("bVehiculos.txt", "x")
            baseVehiculos.close()

        if not os.path.exists("bServicios.txt"):
            baseServicios = open("bServicios.txt", "x")
            baseServicios.close()

        if not os.path.exists("bContratos.txt"):
            baseServicios = open("bContratos.txt", "x")
            baseServicios.close()

        if not os.path.exists("bFacturas.txt"):
            baseServicios = open("bFacturas.txt", "x")
            baseServicios.close()

        print("MENU PRINCIPAL\n(1) Clientes.\n(2) Catalogo de vehiculos.\n(3) Catalogo de servicios.\n(4) Contratos y Facturas\n(0) Salir.")
        op = input("Ingrese a cual opcion desea ingresar: \n")

        if op == '1':  # Base de datos clientes
            clientes()

        elif op == '2':  # Base de datos de vehiculos
            vehiculos()

        elif op == '3':  # Catalogo de servicios
            servicios()

        elif op == '4':
            contratos()  # Informacion de contratos y generador de facturas

        elif op != '0':
            print("Opcion no valida. Intente nuevamente!")

    print("Hasta la proxima!")


#menu()
