# How the Pokemon card game is being played?
# There will be 5 rounds
# Players will take turns starting with Player 1
# The current player will pick a stat to compare from the Pokemon details displayed
# If it is an invalid stat, players will proceed to the next round only after selecting a valid stat
# The player with a higher stat value wins the round and earns a point
# If the round is a draw, players proceed to the next round
# At the end of the 5 rounds, final scores for the two players are displayed
# The game data is stored in a text file with details of the 5 rounds
# Depending on which player has a higher score at the end of the game, the final winner is displayed
# The players have the option to decide if they want to play another game
# In case of a tie, the game is played again automatically


# Required tasks:
# 1. Generate a random number between 1 and 151 to use as the Pokemon ID number
# 2. Using the Pokemon API get a Pokemon based on its ID number
# 3. Create a dictionary that contains the returned Pokemon's name, id, height and weight
# 4. Get a random Pokemon for the player and another for their opponent
# 5. Ask the user which stat they want to use (id, height or weight)
# 6. Compare the player's and opponent's Pokemon on the chosen stat to decide who wins

# Extensions applied:
# 1. Added 'attack' to the stats in the Pokemon dictionary in addition to height, weight and id
# 2. Applied for loop for multiple rounds of the game (5 rounds)
# 3. Added check to prevent the same Pokemon from being compared again
# 4. Ask user to input valid stat when an invalid stat is selected until a valid one is chosen
# 5. Stored the Pokemon details from each round in a file (write)
# 6. Handled a tie situation by playing game again
# 7. Added option for players to choose to continue or exit the game
# 8. Allow opponent to choose stat as well for fair play
import requests
from pprint import pprint

import random


def random_pokemon():
    pokemon_id = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_id)
    response = requests.get(url)
    data_pokemon = response.json()
    attack_stat = 0
    for stat in data_pokemon['stats']:
        if stat['stat']['name'] == 'attack':
            attack_stat = stat['base_stat']
    pokemon = {'name': data_pokemon['name'],
               'id': data_pokemon['id'],
               'height': data_pokemon['height'],
               'weight': data_pokemon['weight'],
               'attack': attack_stat
               }
    return pokemon


def game():
    print("Let's play Pokemon Warriors!")
    player1_score = 0
    player2_score = 0
    game_data = []
    selected_pokemon = []
    for number in range(1, 6):
        print('Round {} begins'.format(number))

        player_turn = "Player1" if number % 2 == 1 else "Player2"
        print("It is {}'s turn!".format(player_turn))

        current_player_pokemon = random_pokemon()
        print("Pokemon of {} is {}".format(player_turn, current_player_pokemon))

        while current_player_pokemon['id'] not in selected_pokemon:
            selected_pokemon.append(current_player_pokemon['id'])
            break
        opponent_pokemon = random_pokemon()
        if opponent_pokemon == current_player_pokemon:
            opponent_pokemon = random_pokemon()
            while opponent_pokemon['id'] not in selected_pokemon:
                selected_pokemon.append(opponent_pokemon['id'])
                break
        stat_choice = input(f'{player_turn}, which stat do you want to compare (id, height, weight or attack)?: ')

        while stat_choice not in ['id', 'height', 'weight', 'attack']:
            stat_choice = input(f'{player_turn}, please type a valid stat (id, height, weight or attack): ')

        if stat_choice in ['id', 'height', 'weight', 'attack']:
            current_player_stat = current_player_pokemon[stat_choice]
            print("Current player's pokemon: {}, stat {}".format(current_player_pokemon['name'], current_player_stat))
            opponent_stat = opponent_pokemon[stat_choice]
            print("Opponent's pokemon: {}, stat {}".format(opponent_pokemon['name'], opponent_stat))
            if current_player_stat > opponent_stat:
                winner = "current_player"
                print('You win')
                if player_turn == "Player1":
                    player1_score = player1_score + 1
                else:
                    player2_score = player2_score + 1
            elif current_player_stat < opponent_stat:
                winner = "opponent"
                print('Opponent wins')
                if player_turn == "Player1":
                    player2_score = player2_score + 1
                else:
                    player1_score = player1_score + 1
            else:
                winner = "Draw"
                print('The game is a draw')

            round_data = {'round': number,
                          'turn': player_turn,
                          'current_player_pokemonName': current_player_pokemon['name'],
                          'current_player_pokemonID': current_player_pokemon['id'],
                          'current_player_pokemonStat': current_player_stat,
                          'opponent_pokemonName': opponent_pokemon['name'],
                          'opponent_pokemonID': opponent_pokemon['id'],
                          'opponent_pokemonStat': opponent_stat,
                          'winner': winner
                          }
            print("Round data:")
            pprint(round_data)
            game_data.append(round_data)

    print("Final scores - Player1: {}, Player2: {}".format(player1_score, player2_score))
    data_file(game_data)
    print('The game data has been saved in text file game_score.txt')
    final_winner(player1_score, player2_score)


def data_file(game_data):
    with open('game_score.txt', 'w+') as text_file:
        for data in game_data:
            text_file.write(str(data) + '\n')


def final_winner(player1_score, player2_score):
    print("Game over!")
    if player1_score > player2_score:
        print('Player1 is the final winner')
    elif player2_score > player1_score:
        print('Player2 is the final winner')
    else:
        print('The game is a tie! Please play again!')
        game()
    players_choice = input('Do you want to play again (yes/no)?:')
    if players_choice == 'yes':
        game()
    else:
        print('Thank you for playing!')


game()
