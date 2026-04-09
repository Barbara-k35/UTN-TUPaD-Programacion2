#Ejercicio 1: "Caja del Kiosco"
nombre = input("Cliente: ").strip()

while nombre == "" or not nombre .isalpha():
    print("Error. Ingresa un nombre")
    nombre = input("Ingrese el nombre del cliente: ").strip()

cantidad_productos_str = (input("Ingrese la cantidad de productos a comprar: ")).strip()

while not cantidad_productos_str.isdigit() or int(cantidad_productos_str) == 0:
    print("Error. Ingresa un numero entero positivo que no sea cero")
    cantidad_productos_str = (input("Ingrese la cantidad de productos a comprar: ")).strip()

cantidad_productos_int = int(cantidad_productos_str)  

total_sin_descuento = 0
total_con_descuento = 0

for i in range(1, cantidad_productos_int + 1):
    precio_producto_str = input(f"Producto {i} - Precio: ").strip() 
    
    while not precio_producto_str.isdigit() or int(precio_producto_str) == 0:
        print("Error. El precio tiene que ser entero positivo")
        precio_producto_str = input(f"Producto {i} - Precio: ").strip()
        
    precio_producto_int = int(precio_producto_str)

    descuento = input("¿Tiene descuento?. Ingres (s por si) o (n por no)").strip().lower()
    while descuento != "s" and descuento != "n":
        print("Error. Ingrese la letra s o n")
        descuento = input("Descuento (S/N): ").strip().lower()

    total_sin_descuento += precio_producto_int

    if descuento == "s":
        precio_final = precio_producto_int * 0.9
    else:
        precio_final = precio_producto_int
    total_con_descuento += precio_final  

print(f"Producto {i} - Precio: {precio_final} Descuento (S/N): {descuento}") 
ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad_productos_int

print()
print(f"Cliente: {nombre}")
print(f"Cantidad de productos: {cantidad_productos_int:.2f}")
print(f"Total sin descuento: ${total_sin_descuento:.2f}")
print(f"Total con descuento: ${total_con_descuento:.2f}")
print(f"Ahorro total: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

#Ejercicio 2: "Acceso al Campus y Menu Seguro".
usuario_correcto = "alumno"
clave_correcta = "python123"
intento_maximo = 3
intentos = 0
cuenta_desbloqueada = False


while intentos < intento_maximo:
    intentos = intentos + 1
    print(f"Intento {intentos}/{intento_maximo}")
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if clave == clave_correcta and usuario == usuario_correcto:
        print("Cuenta desbloqueada")
        cuenta_desbloqueada = True
        break
    else:
        print("Error. usuario y clave incorrrecta.")
if not cuenta_desbloqueada:
    print("Cuenta bloqueda")
else:

    while True:
        print("Eija una opcion:") 

        opcion = input("1.Estado de inscripcion 2.Cambiar Clave 3. Una frase 4. Salir: ")

        if not opcion.isdigit(): 
            print("Error. Ingrese un numero valido") 
        else:
            opcion_numero = int(opcion)
            if opcion_numero == 1:
                print("Inscripto")  
            elif opcion_numero == 2:
                while True:
                    clave_nueva = input("Ingrese clave nueva: ")       
                    if len(clave_nueva) <6:
                        print("Error. La clave debe tener minimo 6 caracteres.")
                    else:
                        clave_confirmar = input("confirme la clave nueva: ")
                        if clave_nueva == clave_confirmar:
                            print("Clave cambiada correctamente.")
                            break
                        else:
                            print("Error. Las claves no coinciden")
            elif opcion_numero == 3:
                print("No te desanimes sigue luchando por lo que te gusta.")
            elif opcion_numero == 4:
                print("Salir")
                break
                
            else:
                print("Error. opcion fuera de rango ")

#Ejercicio 3:Agenda de Turnos con Nombres (Sin listas).
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = "" 
martes2 = ""
martes3 = ""
operador = input("Ingrese el nombre del operador: ").isalpha()
print(f"Buena jornada {operador}")
def validar_nombre(nombre):
   return len(nombre) > 0 and nombre.isalpha()       


while True:
   menu = """ 
    MENU DE OPCIONES
   1) RESERVAR TURNO
   2) CANCELAR TURNO
   3) VER AGENDE DEL NUMERO
   4) VER RESUMEN GENERAL
   5) CERRAR SISTEMA

Elija una opcion del 1 al 5: """   
   opcion = input(menu).strip()
   
   if opcion not in ["1", "2", "3", "4", "5"]:
        print("Error. Elija un numeno del 1 al 5")
        continue
   opcion = int(opcion)

   if opcion == 1:
    print("Reservar un turno")
    
    while True:
       nombre = input("Nombre del paciente: ").strip()
       if validar_nombre (nombre):
          break
       print("Error")
             
    while True:
       dia = input("Ingrese el dia (1-Lunes, 2-Martes): ").strip()
       if dia in ["1", "2"]:
          dia = int(dia)
          break
       print("Error. Elija 1 0 2")
    if dia == 1:
        turno_dia = [lunes1, lunes2, lunes3, lunes4]
    else:
        turno_dia = [martes1, martes2, martes3]    
    if nombre in turno_dia:
       print(f"Error {nombre} ya tiene reserva")
    else:
       asignado = False

    if dia == 1:
       if lunes1 == "":
          lunes1 = nombre
          asignado = True
       elif lunes2 == "":
          lunes2 = nombre
          asignado = True 
       elif lunes3 == "":
          lunes3 = nombre
          asignado = True    
       elif lunes4 == "":
          lunes4 = nombre
          asignado = True
        
    else:
       if martes1 == "":
          martes1 = nombre
          asignado = True
       elif martes2 == "":
          martes2 = nombre
          asignado = True
       elif martes3 == "":
          martes3 = nombre
          asignado = True
    if asignado:
      print(f"Reserva guardada correctamente a nombre de {nombre}")     
    else:
      print("Error no hay turnos disponibles para ese dia")                                     
                   
    
   if opcion == 2:
      print("Cancelar turno(Por nombre)")
   while True:
      dia = input("Elija dia (1=Lunes 2= Martes): ").strip()
      if dia in ("1", "2"):
         if dia == "1":
            dia_selec = "Lunes"
         else:
            dia_selec = "Martes"   
         break
      else:
         print("Error. Solo se permite 1 o 2")
   while True:
      nombre_paciente = input(f"Ingrese el nombre del paciente del {dia_selec}: ").strip()
      if nombre_paciente.isalpha():
         break
      else:
         print("Error. Solo ingresar letras")
   encontrado = False
   if dia == 1:
       if lunes1 == nombre_paciente:
          lunes1 = ""
          encontrado = True
       elif lunes2 == nombre_paciente:
          lunes2 = ""
          encontrado = True 
       elif lunes3 == nombre_paciente:
          lunes3 = ""
          encontrado = True    
       elif lunes4 == nombre_paciente:
          lunes4 = ""
          encontrado = True
        
   else:
       if martes1 == nombre_paciente:
          martes1 = ""
          encontrado = True
       elif martes2 == nombre_paciente:
          martes2 = ""
          encontrado = True
       elif martes3 == nombre_paciente:
          martes3 = ""
          encontrado = True
   if encontrado:
      print(f"Turno de {nombre} cancelado")
   else:
      print("No se encontro el nombre")   

             
   if opcion == 3:
      print("Ver agenda del Dia")
   while True:
      dia = input("Elija dia (1=Lunes  2=Martes): ").strip()
      if dia == "1":
         print("Agenda del Dia Lunes")
         print(f"Turno 1: {lunes1}")
         print(f"Turno 2: {lunes2}")
         print(f"Turno 3: {lunes3}")
         print(f"Turno 4: {lunes4}")
      elif dia == "2":
         print("Agenda del Dia Martes")
         print(f"Turno 1: {martes1}")
         print(f"Turno 2: {martes2}")
         print(f"Turno 3: {martes3}")
         break       
      else:
         print("Error. Solo 1 o 2")
   if opcion == 4:
      print("Ver resumen general") 
      print("Agenda del Lunes: ")
      print(f"Turno 1: {lunes1 if lunes1 != "" else "Vacio"}")
      print(f"Turno 2: {lunes2 if lunes2 != "" else "Vacio"}")
      print(f"Turno 3: {lunes3 if lunes3 != "" else "Vacio"}")
      print(f"Turno 4: {lunes4 if lunes4 != "" else "Vacio"}")

      print ("Agenda del Martes: ")
      print(f"Turno 1: {martes1 if martes1 != "" else "Vacio"}")
      print(f"Turno 2: {martes2 if martes2 != "" else "Vacio"}")
      print(f"Turno 3: {martes3 if martes3 != "" else "Vacio"}")

   if opcion == 5:
      print("Sistema cerrado")
      break

#Ejercicio 4:"Escape Room: La Boveda"   
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
contador_forzar = 0


while True:
    nombre_agente = input("Ingrese el nombre del agente: ").strip()
    if nombre_agente.isalpha():
        break
    else:
        print("Error. Solo letras")


while energia > 0 and cerraduras_abiertas < 3 and not alarma:
    print(f"ESTADO")
    print(f"Energia: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
    print("----------")

    print("MENU DE ACCIONES") 
    print("1-Forzar cerradura")
    print("2-Hackear panel")
    print("3-Descansar")

    while True:
        opcion = input("Elija una opcion: ").strip()
        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= 3:
               break
            else:
                print("Error. La opcion debe ser 1, 2 o 3")
        else:
            print("Error. Solo numeros") 

    if opcion == 1:
        energia -= 20
        tiempo -= 2
        contador_forzar += 1
        if contador_forzar >= 3:
            print("ALARMA ACTIVADA - La carradura se trabo")
            alarma = True
        else:
            if energia < 40:
                print("Riesgo de alarma")
                while True:
                    num= input("Ingrese un numero del 1 al 3: ").strip()
                    if num.isdigit():
                        num = int(num)
                        if 1 <= num <= 3:
                            break
                        else:
                            print("Error. 1 al 3")
                    else:
                        print("Error. Solo numeros")
                if num == 3:
                    print("ALARMA ACTIVADA")
                    alarma = True
                else:
                    print("Cerradura abierta")
                    cerraduras_abiertas += 1 
            else:
                print("Cerradura abierta")
                cerraduras_abiertas += 1    
    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        print("Hackeando...", end=" ")
        for i in range(4):
            codigo_parcial += "A"
            print(".", end=" ")
        print(f"Codigo parcial: {codigo_parcial}")
        if len(codigo_parcial) >= 8:
            print("Cerradura abierta automaticamente")
            cerraduras_abiertas += 1
        else:
            print("Todavia faltan caracteres...")
    elif opcion == 3:
        print("DESCANSANDO")
        energia += 15
        if energia > 100:
            energia= 100
        tiempo -= 1
        if alarma:
            energia -= 10
            print("Alarma activada: -10 energia")
        print(f"Energia: {energia} - Tiempo {tiempo}")
        contador_forzar = 0
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("SIATEMA BLOQUEADO - Perdiste")
        break
print("---JUEGO TERMINADO---")
if cerraduras_abiertas >= 3:
    print(f"VICTORIA {nombre_agente}! Abriste todas las cerraduras")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA. Se termino la energio y/o tiempo")
elif alarma:
    print("DERROTA. Activaste la alarma")  

#Ejercicio 5: Escape Room:"La Arena del Gladiador"  

nombre = input("Nombre del Gladiador: ").strip()

while nombre == "" or not nombre .isalpha():
    print("Error. Solo se permiten letras")
    nombre = input("Ingrese el nombre del Gladiador: ").strip()

vida_gladiador = 100
vida_enemigo = 100 
pociones_vida = 3
daño_base_ataque_pesado = 15
daño_base_enemigo = 12 
turno_gladiador = True 

print("BIENVENIDO")
print(f"Nombre del Gladiador {nombre}")
print("INICIA EL COMBATE")

while vida_gladiador > 0 and vida_enemigo > 0:
    if turno_gladiador:
        print(f"{nombre} (Vida Gladiador: {vida_gladiador} vs Vida Enemigo: {vida_enemigo}) - Pociones: {pociones_vida}")
        print("Elije una opcion")
        print("1-Ataque pesado")
        print("2-Rafaga veloz")
        print("3-Curar")
        opcion = ""
        while True:
            opcion = input("Opcion: ").strip()
            if not opcion.isdigit():
                print("Error. Ingrese un numero")
            else:
                opcion = int(opcion)
                if 1 <= opcion <= 3:
                    break
                else:
                    print("Error. Ingrese un numero del 1 al 3.")
        if opcion == 1:
            daño_final = daño_base_ataque_pesado
            if vida_enemigo < 20:
                daño_final = daño_base_ataque_pesado * 1.5
                print('"Golpe Critico"')  

            vida_enemigo -= daño_final
            if vida_enemigo < 0:
                vida_enemigo = 0
            print(f"Atacaste al enemigo por {daño_final} puntos de daño")
        elif opcion == 2:
            print("Inicias una rafaga Veloz")
            for _ in range(3):
                daño_golpe = 5
                vida_enemigo -= daño_golpe
                if vida_enemigo < 0:
                    vida_enemigo = 0
                print(f"Golpe conectado por {daño_golpe} de daño ") 
        elif opcion == 3:
            if pociones_vida > 0:
                vida_gladiador += 30
                pociones_vida -= 1

                if vida_gladiador > 100:
                    vida_gladiador = 100
                print(f"Sumas 30 puntos de vida. Te quedan {pociones_vida} pociones")
            else:
                print("¡No quedan pociones!")          
        turno_gladiador = False
    else:
        if vida_gladiador > 0:
            print(f"El enemigo contraataca  por {daño_base_enemigo} puntos")
            vida_gladiador -= daño_base_enemigo
            if vida_gladiador < 0:
                vida_gladiador = 0
            print(f"¡El enemigo ataco por {daño_base_enemigo} puntos de daño!")
        turno_gladiador = True
print("FIN DEL JUEGO")
if vida_gladiador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla")
elif vida_gladiador <= 0:
    print("DERROTA. Has caidoen combate") 