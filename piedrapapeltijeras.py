import random

def jugar_adivina_numero():
    numero_oculto = random.randint(1, 50)
    intentos = 0

    while  intentos < 3:
        numero = int(input("Adivina el número oculto (entre 1 y 50): "))
        intentos += 1

        if numero < 1 or numero > 50:
            print("Error: Por favor, elige un número dentro del rango adecuado.")
            continue

        if numero == numero_oculto:
            print(f"¡Enhorabuena! Adivinaste el número oculto en {intentos} intentos.")
            break
        if intentos >= 3 and numero != numero_oculto:
            print("fin del turno")
            break
        respuesta = input("Incorrecto. ¿Quieres seguir jugando? (s/n): ")
        if respuesta.lower() != "s" :
            break
    
        

# Ejemplo de uso:
jugar_adivina_numero()
