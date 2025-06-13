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

def jugarCartas( carta, mazoUsuario):
    """
    El dar cartas sirve para cuando un jugador pone una carta 
    con funcion de dar ccartas al otro se le agrguega al jugador 
    las cartas debidas y eliminnar del maso
    """
    mazoUsuario.remove(carta)

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

while True:
    print(f"Cartas del Jugador 1 {Jugador1} : ")
    juego1=input("Jugador 1 tire una carta o saque del mazo : ")
    juego2=random.choice(Computadora)
    print(f"Computadora jugo {juego2}")
   
    if juego1 == "mazo":
        darCartas(1,mazo,Jugador1)
    else:
        jugarCartas(juego1,Jugador1)
    if juego1=='+4':
    #     print(mazo)
        darCartas(4,mazo,Computadora)
    
    if juego1=='+2':
    #     print(mazo)
        darCartas(2,mazo,Computadora)

    if juego2=='+2':
    #     print(mazo)
        darCartas(2,mazo,Jugador1)

    if juego2=='+4':
    #     print(mazo)
        darCartas(4,mazo,Jugador1)

    print(f"Cartas de la Computadora1 {Computadora} : ")
    jugarCartas(juego2,Computadora)


   
    #     darCartas(2, mazo, Computadora)
    #     print(mazo)
    #     print(f"Computadora {Computadora}")

   

    # if Computadora[0] == '+2':
    #     darCartas(2, mazo, Jugador1)
    #     print(mazo)
    #     print(f"jugador1 {Jugador1}")

    # if Computadora[0] == '+4':
    # darCartas(2, mazo, Jugador1)
    # print(mazo)
    # print(f"jugador1 {Jugador1}")



