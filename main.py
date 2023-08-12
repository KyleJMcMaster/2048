#
from Display import *
from Input import *
from Game import *
from Board import *
from AI import *
from Reporter import *
from Decoder import PickleDecoder
from GameReplay import GameReplay
from Statistics import Statistics

if __name__ == '__main__':


    r = FileReporter(RandomAI(),PickleEncoder)
    r.generate_report(100)





