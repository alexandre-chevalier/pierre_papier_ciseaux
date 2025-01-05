import random

symbol = ["pierre","papier","ciseaux"];
print(symbol);

playerName = input("veuillez entrez votre nom :")
print("veuillez choisir un symbole")

for i in range(len(symbol)):
    print(f"symbole {i} : " + symbol[i]);


player1 = symbol[int(input("veuillez choisir un chiffre entre 0 et 2 pour choisir votre symbole : "))]
player2 = symbol[random.randint(0,2)]

print(f"{playerName}, vous avez choisie : {player1}")
print(f"le bot a choisie : {player2}")

if player1 == player2: 
    print("ceci est une manche nulle")
elif player1 == "ciseaux" and player2 == "papier":
    print(f"{playerName} vous avez gagner car le {player1} bat le {player2}")
elif player1 == "papier" and player2 == "ciseaux":
    print(f"je t'ai battu {playerName}car le {player2} bat le {player1}")
elif player1 == "pierre" and player2 == "ciseaux":
    print(f"{playerName} vous avez gagner car le {player1} bat le {player2}")
elif player1 == "ciseaux" and player2 == "pierre":
    print(f"je t'ai battu {playerName}car le {player2} bat le {player1}")
elif player1 == "papier" and player2 == "pierre":
    print(f"{playerName} vous avez gagner car le {player1} bat le {player2}")
elif player1 == "pierre" and player2 == "papier":
    print(f"je t'ai battu {playerName}car le {player2} bat le {player1}")


