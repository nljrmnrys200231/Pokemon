import requests
import random

pokemon_list = ["pikachu",
                 "charmander",
                   "bulbasaur",
                     "squirtle",
                       "eevee"]
pokemon = random.choice(pokemon_list)

url = "https://pokeapi.co/api/v2/pokemon/" + pokemon

try:

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        name = data["name"]
        height = data["height"]
        weight = data["weight"]

        print("Guess the Pokemon!")
        print("Height:", height)
        print("Weight:", weight)

        guess = input("Guess 1: ")
        if guess.lower() == name:
            print("You win!")
        else:
            guess = input("Guess 2: ")
            if guess.lower() == name:
                print("You win!")
            else:
                guess = input("Guess 3: ")
                if guess.lower() == name:
                    print("You win!")
                else:
                    print("You lose. The Pokemon was", name)
    else:
        print("Pokemon not found.")

except:
    print("Network error.")