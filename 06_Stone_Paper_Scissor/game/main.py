from .entities import Rock, Paper, Scissor
from .characters import User, Computer

GAME_NAME = 'Rock 0  : Paper ___ : Scissor >8'
GREET_USER = 'Hello user, welcome to\n%s' % GAME_NAME


class Game:
    total_rounds = 3

    def start_game(self):
        print('========'*3)
        print(GREET_USER)
        print('========'*3)

        self.player = User()
        self.computer = Computer()

        self.player.name = input('Please enter your name:\n') or 'anonymous'

        start = input('Ready to play the game? (y/n)') or 'n'

        if start.lower() == 'n':
            print('Bye')
            exit(0)
        else:
            self.play_game()

    def play_game(self):
        self.rounds = 1
        while self.rounds <= self.total_rounds:
            self.play_round()
            self.rounds += 1
        quit = input('Quit? (y/n)') or 'n'
        if quit.lower() == 'y':
            print('Game finished with scores!')
            self.show_score()
            exit(0)
        print('You have completed %d rounds' % self.total_rounds)
        print('Game finished with scores!')
        self.show_score()

    def play_round(self):

        print('========')
        print('Round %s' % self.rounds)
        print('========')

        self.player.play_hand()
        self.computer.play_hand()
        self.apply_rules()
        self.show_score()

    def apply_rules(self):
        if self.player.hand == self.computer.hand.can_kill:
            # Player has lost this round
            self.computer.score += 1
        elif self.player.hand == self.computer.chosen_hand:
            print('DRAW')
        else:
            # Player has won this round
            self.player.score += 1

    def show_score(self):
        print('Your score: %d | Computer score: %d\n\n' %
              (self.player.score, self.computer.score))

        if self.rounds == self.total_rounds:

            if self.player.score > self.computer.score:
                print('Congratulations %s!!' % self.player.name)
                print('You have WON')
            elif self.player.score < self.computer.score:
                print('Better luck next time!!')
            else:
                print('Looks like we have a draw!\n')
