#UNE
import random

def darCartas(cantidad, mazo, usuario):
    """
    El dar cartas sirve para cuando un jugador pone una carta 
    con funcion de dar ccartas al otro se le agrguega al jugador 
    las cartas debidas y eliminnar del maso
    """
    contador=0
    while contador < cantidad:
        carta = random.choice  (list(mazo.keys()))
        usuario.append(carta)
        mazo[carta] -= 1
        contador +=1

mazo = {
    '0' :4,
    '1' : 4,
    '2' : 4,
    '3' : 4,
    '4' : 4,
    '5' : 4,
    '6' : 4,
    '7' : 4,
    '8' : 4,
    '9' : 4,
    '+2' : 4,
    '+4' : 5,
    'reversa' : 4,
    'comodin' : 3,
}
print(mazo)

Jugador1 = []
Computadora = []


#Repartir cartas
darCartas(7, mazo, Jugador1)
darCartas(7, mazo, Computadora)


print(Jugador1)
juego1=input("tire una carta ")

print(Computadora)
juego2=input("tire una carta ")

print(Jugador1)
juego1=input("tire una carta ")

print(Computadora)
juego2=input("tire una carta ")

print(Jugador1)
juego1=input("tire una carta ")

print(Computadora)
juego2=input("tire una carta ")

print(Jugador1)
juego1=input("tire una carta ")

print(Computadora)
juego2=input("tire una carta ")

print(Jugador1)
juego1=input("tire una carta ")

print(Computadora)
juego2=input("tire una carta ")

print(Jugador1)
juego1=input("tire una carta ")

print(Computadora)
juego2=input("tire una carta ")

print(Jugador1)
juego1=input("tire una carta ")

print(Computadora)
juego2=input("tire una carta ")

if Jugador1[0] == '+2':
    darCartas(2, mazo, Computadora)
    print(mazo)
    print(f"Computadora {Computadora}")

if Jugador1[0]=='+4':
    print(mazo)
    print(f"Computadora {Computadora}")

if Computadora[0] == '+2':
    darCartas(2, mazo, Jugador1)
    print(mazo)
    print(f"jugador1 {Jugador1}")

if Computadora[0] == '+4':
    darCartas(2, mazo, Jugador1)
    print(mazo)
    print(f"jugador1 {Jugador1}")



