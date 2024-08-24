import random

numero = random.choice(range(1,10))

intentos = 0

while intentos <= 5 :

    usuario = int(input("Escoge un número del 1 al 10:"))

    if usuario == numero :
        print ("Has ganado")
        break

    elif usuario < numero :
        print ("Te has quedado corto")
        intentos += 1
    
    else:
        print ("Te has pasado")
        intentos += 1
    
    if intentos == 5 :
        print ("Te has quedado sin intentos, prueba de nuevo")
        break
