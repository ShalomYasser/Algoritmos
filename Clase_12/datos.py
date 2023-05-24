#ejemplos de uso github
print("Ingreso de datos")
print("----------------")
nombre = (input("Ingrese su nombre: "))
while False:
 try:
     edad = int((input("Ingrese su edad: ")))
     
 except:
    print("Error ingreso")    
print("-----------------------------")
print(f"Su nombre es: {nombre}")
print(f"Su edad es: {edad}")
print("Programa finalizado...")