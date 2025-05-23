#UNE
import random

def darCartas(cantidad, mazo, usuario):
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

carta = random.choice(list(mazo.keys()))
Jugador1.append(carta)
print(f"Jugador1 {Jugador1}")

mazo[carta] -= 1

Computadora = []
carta = random.choice(list(mazo.keys()))
Computadora.append(carta)
print(f"computadora {Computadora}")

mazo[carta] -= 1

print(mazo)

if Jugador1[0] == '+2':
    darCartas(2, mazo, Computadora)
    print(mazo)
    print(f"Computadora {Computadora}")

if Jugador1[0]=='+4':
    darCartas(4, mazo, Computadora)
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



