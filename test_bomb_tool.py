import sys
sys.path.insert(0, sys.path[0]+'\modules')
from randombombgenerator import *
from bomblist import bombs
from BombRender import BombRender



"""
Build bomblist from nothing. You'll need to run the file and input the bomb instructions
"""
#script, filename = argv        #for creating bomblist

#bomb_randomizer = BombRandomizer()
#wire_colors = BombRandomizer.wire_colors
#bomb_list = bomb_randomizer.bomblistcreator(filename, wire_colors)

"""
Run bomb render
"""
###To cycle through ALL bombs
#for a in range(1,7):
#    for b in range(1,10):
#        bomb_number = 'bomb%d' % (a*10 + b)
#        bomb_layout = bombs[bomb_number]['Layout']
#        bomb_solution = bombs[bomb_number]['Solution']
#        bomb_render = BombRender(bomb_number)
#        colored_bomb_layout = bomb_render.colorfixer(bomb_layout)
#        bomb_sequence = bomb_render.buildsequence(colored_bomb_layout)
#        bomb_render.bombrender(bomb_sequence)
#        print bombs[bomb_number]['Instructions']
#        for i in bomb_solution:
#            choice = raw_input("Which wire do you cut?")
#            if int(choice) == (i + 1):
#                print "\nphew!\n"
#            else:
#                print "\nBOOM!"
#                print "Onto next bomb"

###To print specific bomb
a=6
b=9
bomb_number = 'bomb%d' % (a*10 + b)
bomb_layout = bombs[bomb_number]['Layout']
bomb_solution = bombs[bomb_number]['Solution']
bomb_render = BombRender(bomb_number)
colored_bomb_layout = bomb_render.colorfixer(bomb_layout)
bomb_sequence = bomb_render.buildsequence(colored_bomb_layout)
bomb_render.bombrender(bomb_sequence)
print bombs[bomb_number]['Instructions']
for i in bomb_solution:
    choice = raw_input("Which wire do you cut?")
    if int(choice) == (i + 1):
        print "phew!"
    else:
        print "\nBOOM!"
        exit()
