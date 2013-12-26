# internal
from . import gamegrid

# external
import mangoengine

class Move(mangoengine.Model):
    pos_x = mangoengine.IntegralField()
    pos_y = mangoengine.IntegralField()
    word = StringField()

class GameState(mangoengine.Model):
    moves = mangoengine.ListField(of = Move)

class Game:
    def __init__(self):
        self.moves = []

