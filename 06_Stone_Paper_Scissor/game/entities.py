ROCK = 'r'
PAPER = 'p'
SCISSOR = 's'

CHOICES = [ROCK, PAPER, SCISSOR]


class Rock:

    @property
    def can_kill(self):
        return SCISSOR


class Scissor:

    @property
    def can_kill(self):
        return PAPER


class Paper:

    @property
    def can_kill(self):
        return ROCK
