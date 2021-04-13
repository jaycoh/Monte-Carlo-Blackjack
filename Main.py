from Game import Game
from Player import Player
import numpy as np
import math

NUM_PLAYERS = 500
WIN_ODDS = 0.45
winnings = np.zeros(NUM_PLAYERS)
for i in range(NUM_PLAYERS):
    next_player = Player(100, WIN_ODDS)
    strategy_iterations = 0
    while next_player.money > 0 and strategy_iterations < 5:
        initial_bet = 5
        cur_iter = 1
        cur_iter = 0
        while next_player.money > 0 and cur_iter < 4:
            bet = initial_bet * (2 ** cur_iter)  # 5,10,20,40
            result = next_player.play(bet)
            if result == Game.WIN:
                break
            cur_iter = cur_iter + 1

        strategy_iterations = strategy_iterations + 1
    winnings[i] = next_player.money
    print("player " + str(i) + " finished in " + str(strategy_iterations) + " iterations with a final sum of " + str(next_player.money))
print("average: " + str(np.mean(winnings)))
print("median: " + str(np.median(winnings)))