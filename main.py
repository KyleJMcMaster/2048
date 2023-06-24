#
from Display import *
from Input import *
from Game import *
from Board import *
from AI import *
from Reporter import *

if __name__ == '__main__':

    i = RandomAI()
    r = TextReporter(i, num_games=20, multithreaded=False)
    r.report_statistics()
