r = "s"
total_a_pagar = 0
valorEntradas = 0
cantEntradasn = 0
cantEntradasj = 0
cantEntradasa = 0
cantTotal = 0
porcentajeNiños = 0
porcentajeJoven = 0
porcentajeAdulto = 0
pagar = 0
vuelto = 0
print("Bienvenido a cine moro")
while r == "s":
  print("Las entradas son las siguientes: \n")
  print("Categoria niño: 5500 \ de 1 a 13 años\n")
  print("Categoria joven: 7000 \ de 14 a 21 años\n")
  print("Categoria adulto: 9000 \ de 24 años en adelante\n")
  edad = int(input("Cual es su edad "))

  if edad <14:
   print("Entradas de categoria niño")
   cantEntradasn = int(input("Cuantas entradas de categoria niño desea?: "))
   valorEntradas = cantEntradasn * 5500
  elif edad > 13 and edad < 22:
    cantEntradasj = int(input("Cuantas entradas de categoria joven desea?: "))
    valorEntradas = cantEntradasj * 7000 
  else:
    cantEntradasa = int(input("Cuantas entradas de categoria adulto desea? "))  
    valorEntradas = cantEntradasa * 9000

  cantTotal = cantEntradasn + cantEntradasj + cantEntradasa
  total_a_pagar = total_a_pagar + valorEntradas  
  print(f"Tendra que pagar {total_a_pagar}")
  r = str(input("Desea seguir comprando Entradas? (s) or (n)"))  

print("----------------------------BOLETA----------------------------") 
print(f"El total a pagar es de: ${total_a_pagar}")
pagar = int(input("Cuanto dinero tiene para pagar? $"))
vuelto = pagar - total_a_pagar
if pagar < total_a_pagar:
   print("Dinero insuficiente")
else:
  print(f"Su vuelto es de ${vuelto}")
  print("Gracias por su compra, disfrute de la función")
 #Porcentaje de entras
print("--------------------------------------------------------------")
porcentajeNiños =(cantEntradasn * 100) /cantTotal
print("EL porcentaje de entradas de niño fue: ",porcentajeNiños,"%")

porcentajeJoven =(cantEntradasj * 100) /cantTotal
print("EL porcentaje de entradas de joven fue: ",porcentajeJoven,"%")

porcentajeAdulto =(cantEntradasa * 100) /cantTotal
print("EL porcentaje de entradas de adulto fue: ",porcentajeAdulto,"%")