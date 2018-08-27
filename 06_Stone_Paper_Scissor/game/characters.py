import random
from .entities import (
    CHOICES,
    Rock,
    Scissor,
    Paper
)


class User:
    score = 0
    name = ''

    def play_hand(self):
        self.hand = input('Rock (r) / Paper (p) / Stone (s)\n')
        print('You played : ', self.hand)


class Computer:
    score = 0

    def play_hand(self):
        self.chosen_hand = random.choice(CHOICES)
        print('Computer played : ', self.chosen_hand)
        if self.chosen_hand == 'r':
            self.hand = Rock()
        elif self.chosen_hand == 's':
            self.hand = Scissor()
        else:
            self.hand = Paper()
