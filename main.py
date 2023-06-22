#
from Display import *
from Input import *
from Game import *
from Board import *
from AI import *

if __name__ == '__main__':

    d = TextDisplay()
    i = RandomAI()
    g = Game(display=d, input=i)
    g.report_statistics(400)
