import random

def game():

    symbol = ["pierre","papier","ciseaux"];

    print(f"veuillez choisir un symbole")

    for i in range(len(symbol)):
        print(f"symbole {i} : " + symbol[i]);

    player = symbol[int(input("veuillez choisir un chiffre entre 0 et 2 pour choisir votre symbole : "))]
    bot = symbol[random.randint(0,2)]

    print(f"vous avez choisie : {player}")
    print(f"le bot a choisie : {bot}")
    listsymb = [player, bot];
    print(listsymb)
    return victory(listsymb);

def victory(gameplay):
    print("supersonic")
    victoryGamePlayer = 0;
    victoryGameBot = 0;

    if victoryGameBot == 3:
        return print("le bot a gagner")
        replay();
    elif victoryGamePlayer == 3:
        return print(f"vous avez gagner {playerName}")
        replay(playerName);
    else:
            if gameplay[0] == gameplay[1]:
                print("ceci est une manche nulle")
                game();
            elif gameplay[0] == "ciseaux" and gameplay[1] == "papier":
                print(f"vous avez gagner car le {gameplay[0]} bat le {gameplay[1]}")
                victoryGamePlayer +=1;
                game();
            elif gameplay[0] == "papier" and gameplay[1] == "ciseaux":
                print(f"je t'ai battu car le {gameplay[1]} bat le {gameplay[0]}")
                victoryGameBot +=1
                game();
            elif gameplay[0] == "pierre" and gameplay[1] == "ciseaux":
                print(f" vous avez gagner car le {gameplay[0]} bat le {gameplay[1]}")
                victoryGamePlayer +=1;
                game();
            elif gameplay[0] == "ciseaux" and gameplay[1] == "pierre":
                print(f"je t'ai battu car le {gameplay[1]} bat le {gameplay[0]}")
                victoryGameBot +=1
                game();
            elif gameplay[0] == "papier" and gameplay[1] == "pierre":
                print(f"vous avez gagner car le {gameplay[0]} bat le {gameplay[1]}")
                victoryGamePlayer +=1;
                game();
            elif gameplay[0] == "pierre" and gameplay[1] == "papier":
                print(f"je t'ai battu car le {gameplay[1]} bat le {gameplay[0]}")
                victoryGameBot +=1
                game();
        
       
def replay(playername):
    choice = input("Voulez vous rejouer ? (y/n)").upper();
    if choice == "Y":
        game();
        victory(playerName, game(playerName));
    else:
        return print(f"merci d'avoir jouer {playername} ;)")
    


def main():
    game()
    print(victory())
    #replay(playerName);


##main();
print(game())