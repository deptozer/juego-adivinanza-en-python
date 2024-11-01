import random


numero_secreto = random.randint(0,100)
cant_intentos = 0
cant_maxima = 5
adivinado = False

print("bienvenido")

while not adivinado and cant_intentos < cant_maxima:
    entrada = input("introduce ") 
    numero = int(entrada)
    


    if numero == numero_secreto:
        print("felicidades")
        adivinado = True
    elif numero < numero_secreto:
        print("mayor")
    else:
        print("menor")
        
    cant_intentos += 1
    
    if not cant_intentos < cant_maxima:
        print("perdiste")