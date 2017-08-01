"""Bomb example image

/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\
\ |r|   |g|   |w|   |b|   |y|   |p| /
/ |r|   |g|   |w|   |b|   |y|   |p| \
\ |r|   |g|   |w|   |b|   |y|   |p| /
/ |r|   |g|   |w|   |b|   |y|   |p| \
\ |r|   |g|   |w|   |b|   |y|   |p| /
/ |r|   |g|   |w|   |b|   |y|   |p| \
\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/

Colors:
red_wire_colored = RW
green_wire_colored = GW
white_wire_colored = WW
blue_wire_colored = BW
cyan_wire_colored = CW
yellow_wire_colored = YW
purple_wire_colored = PW

    RW = "\033[1;30;41m |r|"
    GW = "\033[1;30;42m |g|"
    WW = "\033[1;30;47m |w|"
    BW = "\033[1;30;44m |b|"
    CW = "\033[1;30;46m |c|"
    OW = "\033[1;30;43m |o|"
    PW = "\033[1;30;45m |p|"

Dictionary:
   bombliost = {
        'bomb_11': {
            'layout': (RW, WW, CW, PW, YW),
            'solution': (),
            'clue': ()
            },

"""
from random import randint


class BombRender:


#bomb_layout is imported from bomb file. bomb_render is the string of wires
    def __init__(self, bomb_number):
        self.bomb_number = bomb_number

    def buildsequence(self, bomb_layout, number):
    #from bomb dictionary
        bomb_string = ""
        BL = 0
        top_row_sequence = "/~"
        bot_row_sequence = "\\~"
        while BL < len(bomb_layout):
            bomb_string = (bomb_string
                + bomb_layout[BL]
                + "\033[1;37;40m")
            top_row_sequence = top_row_sequence + "|" + str(BL+1) + "|"
            bot_row_sequence = bot_row_sequence + "|" + str(BL+1) + "|"
            if BL < (len(bomb_layout)-1):
                bomb_string = bomb_string + "   "
                top_row_sequence = top_row_sequence + "~~~"
                bot_row_sequence = bot_row_sequence + "~~~"
            BL += 1
        top_row_sequence = top_row_sequence + "~\\"
        bot_row_sequence = bot_row_sequence + "~/"
        bomb_sequence = (bomb_string, top_row_sequence, bot_row_sequence)
        return bomb_sequence

    def colorfixer(self,  bomb_layout):
        B = 0
        while B < len(bomb_layout):
            if bomb_layout[B] == "red":
                bomb_layout[B] = "\033[1;30;41m|r|"
            elif bomb_layout[B] == "green":
                bomb_layout[B] = "\033[1;30;42m|g|"
            elif bomb_layout[B] == "white":
                bomb_layout[B] = "\033[1;30;47m|w|"
            elif bomb_layout[B] == "blue":
                bomb_layout[B] = "\033[1;30;44m|b|"
            elif bomb_layout[B] == "cyan":
                bomb_layout[B] = "\033[1;30;46m|c|"
            elif bomb_layout[B] == "orange":
                bomb_layout[B] = "\033[1;30;43m|o|"
            elif bomb_layout[B] == "purple":
                bomb_layout[B] = "\033[1;30;45m|p|"
            else:
                print "Color Error"
            B += 1
        return bomb_layout

    def bombrender(self, bomb_sequence, number):
        bomb_string = bomb_sequence[0]
        top_row_sequence = bomb_sequence[1]
        bot_row_sequence = bomb_sequence[2]
        row1 = "\\~" + bomb_string + "~/"
        row2 = "/~" + bomb_string + "~\\"
        row3 = "\\~" + bomb_string + "~/"
        row4 = "/~" + bomb_string + "~\\"
        row5 = "\\~" + bomb_string + "~/"
        row6 = "/~"  + bomb_string + "~\\"
        bomb_sequence_rendered = [top_row_sequence,
                        row1,
                        row2,
                        row3,
                        row4,
                        row5,
                        row6,
                        bot_row_sequence
                        ]
        print "\n"
        print '\n'.join(bomb_sequence_rendered)
        print "\n"
        return bomb_sequence_rendered
