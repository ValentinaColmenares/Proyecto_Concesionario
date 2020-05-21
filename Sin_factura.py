"""
PENDIENTE
-Facturas
-Ver informacion de contratos
-Actualizar status de contratos (pendiente/en proceso/terminado)
"""

import os
import json
## Solicita informacion del cliente


def infoCliente():
  datosClientes = {"ID-Cliente":12, "Nombre":10, "Apellido":10, "Dirección":20, "Telefono":10, "Ciudad":15}

  for dato in datosClientes:
    print(dato)
    nuevoDato = input()
    nuevoDato = nuevoDato.replace(" ", "")
    nuevoDato = nuevoDato.ljust(datosClientes[dato])
    datosClientes[dato] = nuevoDato

  diccionariojason = json.dumps(datosClientes)
  return diccionariojason

## Solicita informacion del Vehiculo
def infoVehiculo():
  datosVehiculos = {"Numero de placa":6, "ID-Cliente":12,"Marca":13, "Numero de modelo":4, "Cilindraje":5, "Color":25, "Tipo de servicio":10, "Tipo de combustible":10, "Capacidad de pasajeros":3, "Capacidad de carga":4, "Numero de chasis":20, "Numero de Motor":13}

  for dato in datosVehiculos:
    print(dato)
    nuevoDato = input()
    nuevoDato = nuevoDato.replace(" ", "-")
    nuevoDato = nuevoDato.ljust(datosVehiculos[dato])
    datosVehiculos[dato] = nuevoDato

  # Comprueba que el propietario este en la base de clientes. Si no, solicita que se agregue informacion
  verifCliente = leerBase("bClientes.txt", '1', datosVehiculos["ID-Cliente"], False) 
  if verifCliente == "No info":
    print("Cliente con id #", datosVehiculos["ID-Cliente"], "no esta en base de datos. Se debe ingresar informacion del cliente.")
    guardarInfo(infoCliente(),"bClientes.txt")

  diccionariojason = json.dumps(datosVehiculos)
  return diccionariojason

## Solicita informacón del servicio
def infoServicio():
  datosServicios = {"Codigo del servicio":4, "Nombre del servicio":15, "Precio/hora":10, "Horas del servicio":4}

  for dato in datosServicios:
    print(dato)
    nuevoDato = input()
    nuevoDato = nuevoDato.replace(" ", "")
    nuevoDato = nuevoDato.ljust(datosServicios[dato])
    datosServicios[dato] = nuevoDato

  diccionariojason = json.dumps(datosServicios)
  return diccionariojason

## Contratar servicio
def solServicio():
  datosContrato = {"ID-Cliente":12, "Placa":6, "Codigo del servicio":4, "Unidades contratadas":3, "Status":10}

  for dato in datosContrato:
    print(dato)
    nuevoDato = input()
    nuevoDato = nuevoDato.replace(" ", "")
    nuevoDato = nuevoDato.ljust(datosContrato[dato])
    datosContrato[dato] = nuevoDato

  # Comprueba que el vehiculo este en la base de datos. Si no, solicita que se agregue informacion
  if leerBase("bServicios.txt",'1',datosContrato["Codigo del servicio"])=="No info": 
    print("Servicio no existe, verifique base de datos.")
    return False
  else:
    if leerBase("bVehiculos.txt",'1',datosContrato["Placa"])=="No info": 
      print("Vehiculo con placa #", datosContrato["Placa"], "no esta en base de datos. Se debe ingresar informacion del vehiculo.")
      guardarInfo(infoVehiculo(),"bVehiculos.txt")

    diccionariojason = json.dumps(datosContrato)
    return diccionariojason

## Guarda informacion en base de datos
def guardarInfo(cad, base):
  with open(base, "a") as baseDatos:
    baseDatos.write(cad+"\n")

## función que comprueba si la entrada es un entero
def lee_entero():
  while True:
    try:
      valor = int(input())
      return valor

    except ValueError:
      print("ATENCIÓN: Debe ingresar un número entero.")

## función para comprobar una entrada del usuario dentro de un rango
def comprobar(a, b):
  while True:
    respuesta = lee_entero()

    if a <= respuesta <= b:
      return respuesta

    else:
      print("Debe ingresar un número entre ", a, "-", b, sep="")

## Organizar cualquier base de datos
def organizar(base, item):
  item -= 1
  lista2 = []

  for linea in base:
    diccionario = json.loads(linea)
    lista = [i for i in diccionario.values()]
    primero = lista[item]
    lista.remove(primero)
    lista.insert(0, primero)
    cadena = (" ".join(lista))+"\n"
    lista2.append(cadena)

  cadena = ""
  lista2.sort()

  for i in lista2:
    cadena += i

  if cadena == "":
    return "Base de datos vacía"

  else:
    return cadena

## Leer base
def leerBase(base, op, noid, Verif):
  if op == '1':
    c = ""

    with open(base, "r") as baseDatos:
      for linea in baseDatos:
        datos = json.loads(linea)
        info = [i for i in datos.values()]
        noid = noid.ljust(len(info[0]))

        
        
        if noid == info[0]:
          for dato in info:
            c += dato+" "
          c += "\n"
    
    if c == "": return "No info"
    else: return c

  elif op == '2':
    if base == "bClientes.txt":
      print("Ordenar información de clientes por:\n(1) Número de identificación\n(2) Nombre\n(3) Apellido\n(4) Dirección\n(5) Teléfono\n(6) Ciudad")
      item = comprobar(1, 6)

    elif base == "bVehiculos.txt":
      print("Organizar información de vehiculos por:\n(1) Número de placa\n(2) Número de identificación del cliente\n(3) Marca\n(4) Número de modelo\n(5) Cilindraje\n(6) Color\n(7) Tipo de servicio\n(8) Tipo de combustible\n(9) Capacidad de pasajeros\n(10) Numero de chasis\n(11) Número de motor")
      item = comprobar(1, 11)

    elif base == "bServicios.txt":
      print("Organizar información de servicios por:\n(1) Código del servicio\n(2) Nombre del servicio\n(3) Precios/hora\n(4) Horas de servicio")
      item = comprobar(1, 5)

    elif base=="bContratos.txt":
      print("Organizar informacion de contratos por:\n(1) Identificacion del cliente\n(2) Placa del vehiculo\n(3) Codigo del servicio\n(4) Unidades contratadas\n(5) Estatus del contrato")
      item=comprobar(1,5)

    with open(base,"r") as baseDatos:
      return (organizar(baseDatos,item))

  else: return "Opcion ingresada no es valida."

## Cambiar status de una base de datos
def cambioStatus(noid):
  contratos=[]
  op=''
  with open("bContratos.txt","r") as baseContratos:
    for linea in baseContratos:
      datos=json.loads(linea)
      contratos.append(datos)

  with open("bContratos.txt","w") as baseContratos:
    for contrato in contratos:
      if noid==contrato["ID-Cliente"]:
        while not op in ['1','2','3','4']:
          print("¿Que estatus desea establecer?\n(1) Pendiente\n(2) En taller\n(3) Finalizado\n(4) Entregado")
          op=input()
          if op=='1': contrato["Status"]="Pendiente"
          elif op=='2': contrato["Status"]="Entaller"
          elif op=='3': contrato["Status"]="Finalizado"
          elif op=='4': contrato["Status"]="Entregado"
          else: print("Opcion no valida.")

      datoGuardar=json.dumps(contrato)
      guardarInfo(datoGuardar,"bContratos.txt")
  
  print("Cambio de estatus exitoso.")

## Eliminar elemento en la base de datos
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
        baseDatos.write(datoGuardar)

## Limpia base de datos
def limpiarBase(base):
  conf = input("Seguro que desea eliminar base de datos? (s/n): \n").lower()

  if conf == 's':
    os.remove(base)
    print("Base de datos eliminada con exito! Volviendo al menu principal")
    return conf

  elif conf == 'n':
    print("Base de datos no eliminada.")

  else:
    print("Opcion no valida!")

## Base de Datos de Clientes
def clientes():
  op = ''

  while op != '0':
    print("(1) Ver clientes.\n(2) Agregar un cliente nuevo.\n(3) Eliminar un cliente.\n(4) Limpiar la base de datos.\n(0) Volver al menu principal.")
    op = input("Seleccione una opcion: \n")

    if op == '1':  # Lista de clientes
      sop = input("(1) Buscar un cliente.\n(2) Mostrar todos los clientes.\n")
      if sop == '1': noid = input("Inserte no. identificacion del cliente:\n")
      else: noid = ""
      result = leerBase("bClientes.txt", sop, noid, False)
      if result != "No info": print(result)
      else: print("Informacion no encontrada.")

    elif op == '2':  # Agregar cliente
      guardarInfo(infoCliente(), "bClientes.txt")
      print("Cliente agregado con exito!")

    elif op == '3':  # Elimina un cliente de la base de datos
      noid = input("Ingrese no. identificacion del cliente que desea eliminar:\n").ljust(12)
      eliminarElemento("bClientes.txt", noid, "ID-Cliente")
      eliminarElemento("bVehiculos.txt", noid, "ID-Cliente")
      print("Cliente eliminado con exito!")

    elif op == '4':  # Borra toda la informacion en la base de datos
      result = limpiarBase("bClientes.txt")
      if result == 's': break

    elif op == '0':  # Volver a menu principal
      print("Volviendo al menu principal.")

    else:
      print("Opcion no valida. Intente nuevamente!")

## Base de Datos de Vehiculos
def vehiculos():
  op = ''

  while op != '0':
    print("(1) Ver vehiculos en sistema.\n(2) Agregar un vehiculo nuevo.\n(3) Eliminar un vehiculo.\n(4) Limpiar la base de datos.\n(0) Volver al menu principal.")
    op = input("Seleccione una opcion: \n")

    if op == '1':  # Lista de vehiculos
      sop = input("(1) Buscar un vehiculo.\n(2) Mostrar todos los vehiculos.\n")
      if sop == '1': noid = input("Inserte placa del vehiculo:\n")
      else: noid = ""
      result = leerBase("bVehiculos.txt", sop, noid, False)
      if result != "No info": print(result)
      else: print("Informacion no encontrada.")

    elif op == '2':  # Agregar vehiculo
      guardarInfo(infoVehiculo(), "bVehiculos.txt")
      print("Vehiculo agregado con exito!")

    elif op == '3':  # Elimina un vehiculo
      placa=input("Ingrese placa del vehiculo que desea eliminar: \n").ljust(6)
      eliminarElemento("bVehiculos.txt", placa, "Numero de placa")
      print("Vehiculo eliminado con exito!")

    elif op == '4':  # Borra toda la informacion en la base de datos
      result = limpiarBase("bVehiculos.txt")
      if result == 's': break

    elif op == '0':  # Volver a menu principal
      print("Volviendo al menu principal.")

    else:
      print("Opcion no valida. Intente nuevamente!")

## Base de Datos de Servicios
def servicios():
  op = ''

  while op != '0':
    print("(1) Lista de servicios.\n(2) Crear un servicio nuevo.\n(3) Eliminar un servicio existente.\n(4) Limpiar base de datos.\n(0) Volver al menu principal.")
    op = input("Seleccione una opcion: \n")

    if op == '1':  # Lista de servicios
      sop = input("(1) Buscar un servicio.\n(2) Mostrar todos los servicios.\n")
      if sop == '1': noid = input("Inserte codigo del servicio:\n")
      else: noid = ""
      result = leerBase("bServicios.txt", sop, noid, False)
      if result != "No info": print(result)
      else: print("Informacion no encontrada.")

    elif op == '2':  # Agregar servicio
      guardarInfo(infoServicio(), "bServicios.txt")
      print("Servicio agregado con exito!")

    elif op == '3':  # Eliminar un servicio
      noid = input("Ingrese codigo del servicio: \n").ljust(4)
      eliminarElemento("bServicios.txt", noid, "Codigo del servicio")
      print("Servicio eliminado con exito!")

    elif op == '4':  # Borra toda la informacion en la base de datos
      result = limpiarBase("bServicios.txt")
      if result == 's': break

    
    elif op == '0':  # Volver a menu principal
      print("Volviendo al menu principal.")

    else:
      print("Opcion no valida. Intente nuevamente!")
      
## Base de Datos de Contratos
def contratos(): 
  op = ''

  while op!='0': ######Pendiente generar facturas#######
    print("(1) Ver contratos existentes\n(2) Nuevo contrato\n(3) Cambiar estatus de un contrato\n(4) Eliminar un contrato\n(5) Generar factura\n(6) Limpiar base de datos\n(0) Volver al menu principal")
    op=input("Seleccione una opcion:\n")

    if op=='1': #Lista contratos
      sop=input("(1) Buscar un contrato\n(2) Mostrar todos los contratos en sistema\n")
      if sop=='1': noid=input("Inserte ID-Cliente:\n")
      else: noid=""
      result=leerBase("bContratos.txt",sop,noid)
      if result!="No info": print(result)
      else: print("Informacion no encontrada.")

    elif op=='2': # Agregar Contrato
      contrato = solServicio()
      if contrato != False: guardarInfo(contrato,"bContratos.txt")

    elif op=='3': #Cambiar status de un contrato
      noid=input("Ingrese ID-Cliente\n").ljust(12)
      cambioStatus(noid)
    
    elif op=='4':
      noid=input("Ingrese ID-Cliente: \n").ljust(12)
      eliminarElemento("bContratos.txt", noid, "ID-Cliente")
      print("Contrato eliminado con exito!")

    elif op=='5':
      print("PENDIENTE GENERAR FACTURAS!!!!!")

    elif op=='6':
      result=limpiarBase("bContratos.txt")
      if result=='s': break

    elif op=='0':
      print("Volviendo al menu principal.")

    else:
      print("Opcion no valida. Intente nuevamente!")

## Menu Principal
def menu():
  op = '1'
  print("¡Bienvenido.\nIniciando sistema...")

  while op != '0':
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


menu()
