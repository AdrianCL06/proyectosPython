
r = input("Quieres guardar o revisar?(g/r)")

if r == "g":



    gc = open('R:\contrs.txt', 'a', encoding='utf-8')

    while True:
        serv = input("introduce el servicio: \n")
        usr = input("introduce el usuario(o correo): \n")
        contr = input("introduce la contraseña: \n")
        cad = ("Servicio: " + serv + " Usuario: " + usr + " Contraseña: " + contr + "\n")
        gc.write(cad)

        a = input("Quieres guardar algo más?(s/n)")
        if a != "s":
            break
    gc.close()
elif r == "r":
    
    gc = open('R:\contrs.txt', 'r')
    lineas = gc.readlines()
    for i in range(len(lineas)):
        print(lineas[i])
    gc.close()
else:
    print("Respuesta no valida")

input("Enter para salir")