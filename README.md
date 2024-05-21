# Pokemon-Warriors
Welcome to Pokemon Warriors, a Python-based card game where players compare Pokemon stats to determine the winner. This project was developed as part of the CFG Introduction to Python course.

Here's a brief overview of how the game works:
1. Number of Rounds: Each game consists of 5 rounds.
2. Turn-Based Gameplay: Players take turns starting with Player 1.
3. Choosing Stats: The current player selects a stat to compare from the displayed Pokemon details.
4. Validating Stats: If an invalid stat is chosen, players must select a valid stat before proceeding.
5. Comparing Stats: The player with the higher stat value wins the round and earns a point.
6. Draws: In case the round is draw, the players proceed to the next round.
7. Final Scores: After 5 rounds, the final scores for both players are displayed.
8. Data Storage: Game data is stored in a text file with details of all 5 rounds.
9. Determining Winner: The player with the higher score at the end of the game is declared the winner.
10. Continuation: Players have the option to play another game.
11. Tiebreaker: In case of a tie, the game is automatically played again.

To implement the game, the following required tasks were undertaken:
1. Generating a random number between 1 and 151 to use as the Pokemon ID.
2. Utilizing the Pokemon API to retrieve a Pokemon based on its ID.
3. Creating a dictionary containing the Pokemon's name, ID, height and weight.
4. Getting random Pokemon for the player and their opponent.
5. Prompting the user to select a stat (height or weight).
6. Comparing the player's and opponent's Pokemon based on the chosen stat to determine the winner.

Several extensions were applied to enhance the gameplay experience:
1. Added 'attack' to the Pokemon stats alongside height and weight.
2. Implemented a for loop for multiple rounds of the game (5 rounds).
3. Added a check to prevent the same Pokemon from being compared again.
4. Prompted the user to input a valid stat when an invalid stat is selected until a valid one is chosen.
5. Stored the Pokemon details from each round in a file.
6. Handled tie situations by replaying the game.
7. Provided an option for players to continue or exit the game.
8. Allowed the opponent to choose a stat for fair play.
