#UNE
import random
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