#
from Display import *
from Input import *
from Game import *
from Board import *
from AI import *

if __name__ == '__main__':

    d = TextDisplay()
    i = MinMaxAI()
    g = Game(display=d, input=i)
    g.play_game()
