import random
pinnar = random.randint(15, 25)
print(pinnar)

def playerTurn(namn):
    global pinnar
    print("\nDet är " + namn + "s tur...")
    print("|"*pinnar)
    taPinnar = int(input("Vill du ta 1 eller 2 pinnar? "))

    if (taPinnar == 1) or (taPinnar == 2):
        pinnar = pinnar - taPinnar
    else:
        playerTurn(namn)

def ai():
    global pinnar
    print("\nDatorns tur...")
    print("|"*pinnar)
    if pinnar % 3 == 0:
        pinnar = pinnar - 1
    elif pinnar % 3 == 1:
        pinnar = pinnar - 1
    else:
        pinnar = pinnar - 2

def spela(n):
    global pinnar
    if n == "1":
        namn = input("Skriv in ditt namn: ")
        for i in range(100):
            playerTurn(namn)
            if pinnar < 1:
                return(namn + "vinner!")
            ai()
            if pinnar < 1:
                return("\nBOOOM " + namn + ", Hugos och Bozons AI VANN!")

    elif n == "2":
        
        print("hejehej")

print(spela(input("1: Singleplayer \n2: Multiplayer\n" )))