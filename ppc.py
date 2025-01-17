import random

def gamer(symbol):
    print(f"veuillez choisir un symbole")
    for i in range(len(symbol)):
        print(f"symbole {i} : " + symbol[i]);

    player = symbol[int(input("veuillez choisir un chiffre entre 0 et 2 pour choisir votre symbole : "))]
    bot = symbol[random.randint(0,2)]
    print(f"vous avez choisie : {player}")
    print(f"le bot a choisie : {bot}")

    return player, bot


def victory_one_game(gameplay, partie_player, partie_bot):
    player= gameplay[0]
    bot= gameplay[1]

    if player == "ciseaux" and bot == "papier":
        print("player 1 vous avez gagner une manche")
        partie_player.append("V")
        return partie_player
    elif player == "papier" and bot == "ciseaux":
        print("le bot a gagner la manche")
        partie_bot.append("V")
        return partie_bot 
    elif player == "papier" and bot == "pierre":
        print("player 1 vous avez gagner une manche")
        partie_player.append("V")
        return partie_player
    elif player == "pierre" and bot == "papier":
        print("le bot a gagner la manche")
        partie_bot.append("V")
        return partie_bot 
    elif player == "ciseaux" and bot == "pierre":
        print("player 1 vous avez gagner une manche")
        partie_player.append("V")
        return partie_player
    elif player == "pierre" and bot == "ciseaux":
        print("le bot a gagner la manche")
        partie_bot.append("V")
        return partie_bot 

    

def result():
    print("votre resultat")
    
def main():
    manche_player = []
    manche_bot = []
    while True:
        symbol = ["pierre","papier","ciseaux"];
        gamers = gamer(symbol)
        victory_one_game(gamers, manche_player, manche_bot)

        print(f"vous avez gagner {manche_player.count("V")} manche ")
        print(f"le bot a gagner {manche_bot.count("V")} manche ")


        print(gamers)


main()