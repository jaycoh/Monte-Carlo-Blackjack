import random
from Game import Game


class Player:
    WIN_PROB = 0.45

    def __init__(self, money, win_prob):
        self.money = money
        self.win_prob = win_prob

    def play(self, bet):
        if bet < self.money:
          outcome = random.uniform(0,1)
          if outcome <= self.win_prob:
            self.money = self.money + bet
            return Game.WIN
          else:
            self.money = self.money - bet
            return Game.LOSE
