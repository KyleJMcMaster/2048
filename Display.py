# contains abstract class for display type
# also contains instances for text and windowed displays


from abc import ABC, abstractmethod
import tkinter as tk
from Board import Board
import colr


class Display(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def displayBoard(self, board: Board):
        pass


class WindowDisplay(Display):

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("2048 Game")
        self.tiles = [None for _ in range(16)]
        self.score_label = tk.Label(self.window, text="Score: 0")
        self.score_label.grid(row=0)

        for i in range(16):
            self.tiles[i] = tk.Canvas(self.window, width=100, height=100)
            self.tiles[i].grid(row=int(i / 4) + 1, column=(i % 4) + 1)

    def displayBoard(self, board: Board):
        tile_colours = {
            65536: "569BE0",
            32768: "#6BAED5",
            16384: "#F0513B",
            8192: "#27B053",
            4096: "#FB736D",
            2048: "#EDC22E",
            1024: "#EDC23F",
            512: "#EDC850",
            256: "#EDCC61",
            128: "#EDCF72",
            64: "#F65E3B",
            32: "#F67C5F",
            16: "#F59563",
            8: "#F2B179",
            4: "#EDE0C8",
            2: "#EEE4DA",
            0: "#CCC0B3"
        }

        for i in range(len(board.values)):
            tile = board.values[i]
            if tile not in tile_colours:
                colour = "#2E2C26"
            else:
                colour = tile_colours[tile]
            text_colour = "#000000" if tile > 0 else "#FFFFFF"
            self.tiles[i].create_rectangle(10, 10, 90, 90, fill=colour)
            self.tiles[i].create_text(50, 50, text=str(tile) if tile != 0 else '', fill=text_colour,
                                      font=("Helvetica", 24))
        self.score_label.config(text="Score: " + str(board.get_score()))
        self.window.update_idletasks()
        self.window.update()


class TextDisplay(Display):

    def __init__(self):
        pass

    def displayBoard(self, board: Board):
        tile_colours = {
            2048: "EDC22E",
            1024: "#EDC23F",
            512: "#EDC850",
            256: "#EDCC61",
            128: "#EDCF72",
            64: "#F65E3B",
            32: "#F67C5F",
            16: "#F59563",
            8: "#F2B179",
            4: "#EDE0C8",
            2: "#EEE4DA",
            0: "#3e403f"
        }
        print("score: %d" % (board.get_score()))
        for i in range(len(board.values)):
            tile = board.values[i]
            print(colr.color(f"{tile}\t".expandtabs(6), back=tile_colours[tile], fore="000000"),
                  end=" ")
            if i % 4 == 3:
                print("\n")

