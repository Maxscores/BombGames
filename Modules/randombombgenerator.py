from sys import argv
from random import randint, shuffle
import json



"""
    RW = "\\" + "033[1;30;41m|r|" + "\\" + "033[1;37;40m"
    GW = "\\" - "\\" + "033[1;30;42m|g|" + "\\033[1;37;40m"
    WW = "\\" + "033[1;30;47m|w|" + "\\033[1;37;40m"
    BW = "\\" + "033[1;30;44m|b|" + "\\033[1;37;40m"
    CW = "\\" + "033[1;30;46m|c|" + "\\033[1;37;40m"
    OW = "\\" + "033[1;30;43m|o|" + "\\033[1;37;40m"
    PW = "\033[1;30;45m|p|\033[1;37;40m"


"""
class BombRandomizer:

    wire_colors = ["red", "green", "white", "blue", "cyan", "orange", "purple"]

    def __init__(self):
        wire_colors = self.wire_colors

    def randombomblayout(self, wire_count, wire_colors):
        w = 0
        layout = []
        for w in range(0, wire_count):
            wire = randint(0, len(wire_colors)-1)
            layout.append(wire_colors[wire])
        return layout

    def createbombsolution(self, layout):
        solution = []
        red_list = []
        green_list = []
        white_list = []
        blue_list = []
        cyan_list = []
        orange_list = []
        purple_list = []
        cut = []
        color_list = [
                    red_list,
                    green_list,
                    white_list,
                    blue_list,
                    cyan_list,
                    orange_list,
                    purple_list
                    ]
        for i, j in enumerate(layout):
            if j == "red":
                red_list.append(i)
            elif j == "green":
                green_list.append(i)
            elif j == "white":
                white_list.append(i)
            elif j == "blue":
                blue_list.append(i)
            elif j == "cyan":
                cyan_list.append(i)
            elif j == "orange":
                orange_list.append(i)
            elif j == "purple":
                purple_list.append(i)
        for entry in color_list:
            if len(entry) >= 1:
                cut = []
                if len(entry) == 1:
                    cut = [entry.pop(0)]
                elif len(entry) == 2:
                    cut = [entry.pop(0)]
                elif len(entry) == 3:
                    cut = [entry.pop(1)]
                elif len(entry) == 4:
                    cut1 = [entry.pop(0)]
                    cut2 = [entry.pop(2)]
                    cut = cut1 + cut2
                elif len(entry) == 5:
                    cut1 = [entry.pop(0)]
                    cut2 = [entry.pop(1)]
                    cut3 = [entry.pop(2)]
                    cut = cut1 + cut2 + cut3
                elif len(entry) == 6:
                    cut1 = [entry.pop(1)]
                    cut2 = [entry.pop(3)]
                    cut = cut1 + cut2
                elif len(entry) == 7:
                    cut = entry.pop(6)
                elif len(entry) == 8:
                    cut = entry.pop(7)
                solution = solution + cut
            elif len(entry) == 0:
                pass
        return solution

    def bomblistcreator(self, filename, wire_colors):
        target = open(filename, "w")
        target.truncate()
        target.write("bombs = {")
        for a in range(1,7):
            for b in range(1, 10):
                wire_count = a + 3
                layout = self.randombomblayout(wire_count, wire_colors)
                solution = self.createbombsolution(layout)
                instructions = """
Always cut wires in this order: R, G, W, B, C, O, P
If there are 2 wires alike, cut the first wire of that color
If there are 3 wires alike, cut the middle wire of that color
If there are 4 wires alike, cut the first and last wire of that color
If there are 5 wires alike, cut every other wire of that color
If there are 6 wires alike, cut the 2nd and 5th wire of that color
If there are 7 wires alike, you're so lucky! Cut the 7th wire
If there are 8 wires alike, you should buy a lotto ticket. Cut the 8th wire
"""
                bomb_number = str((10*a) + b)
                target.write("\n    'bomb")
                target.write(bomb_number)
                target.write("': {")
                target.write("\n        'Layout': ")
                json.dump(layout, target)
                target.write(",")
                target.write("\n        'Solution': ")
                json.dump(solution, target)
                target.write(",")
                target.write("\n        'Instructions': ")
                json.dump(instructions, target)
                if a != 6 or b != 9:
                    target.write("\n        },")
                else:
                    target.write("\n        }")
        target.write("\n}")
        target.close()
        print "bombs generated in %s" % filename
