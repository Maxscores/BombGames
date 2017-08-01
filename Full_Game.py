import sys
from random import randint
from modules.randombombgenerator import *
from modules.bomblist import bombs
from modules.BombRender import BombRender
import string


class Scene:
    def enter(self):
        pass


class Engine:
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self, scene_map):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        current_scene.enter()


class BombDiffuse:

    def __init__(self, room_number):
        self.room_number = room_number

    def enter(self, room_number):
        bomb_number = self.randombomb(room_number)
        bomb_layout = bombs[bomb_number]['Layout']
        bomb_solution = bombs[bomb_number]['Solution']
        bomb_render = BombRender(bomb_number)
        colored_bomb_layout = bomb_render.colorfixer(bomb_layout)
        bomb_sequence = bomb_render.buildsequence(colored_bomb_layout, 0)
        bomb_sequence_rendered = bomb_render.bombrender(bomb_sequence, 0)
        Instructions = bombs[bomb_number]['Instructions']
        print Instructions
        self.solvebomb(bomb_solution, bomb_sequence_rendered, Instructions)

    def solvebomb(self, bomb_solution, bomb_sequence_rendered, Instructions):
        self.bomb_solution = bomb_solution
        for i in bomb_solution:
            cut = raw_input("Which number wire do you cut?" )
            if int(cut) == (i + 1):
                print "Phew!"
                top_row_rendered = bomb_sequence_rendered.pop(0)
                bot_row_rendered = bomb_sequence_rendered.pop()
                top_row_rendered = string.replace(top_row_rendered,
                                                '|%r|' % cut,
                                                '|X|')
                bot_row_rendered = string.replace(bot_row_rendered,
                                                '|%r|' % cut,
                                                '|X|')
                bomb_sequence_rendered.insert(0, top_row_rendered)
                bomb_sequence_rendered.append(bot_row_rendered)
                print '\n'.join(bomb_sequence_rendered)
                print '\n' + Instructions
            else:
                an_explosion = Map('explosion')
                an_end = Engine(an_explosion)
                an_end.play(an_explosion)

    def printmanual(self, bomb_number):
        self.bomb_number = bomb_number
        print "-" * 72
        print BombDiffuse.bombs[bomb_number]['Instructions']


    def randombomb(self, room_number):
        bomb_choice = ((10*room_number) + randint(1,9))
        bomb_number = 'bomb' + str(bomb_choice)
        return bomb_number


class Explosion(Scene):

    descriptions = [
        "Your eye dialate while the bomb explodes in an inferno.",
        "A bomb releases an acidic slime that melts your skin.",
        "A firey tomb engulfs the room.",
        "The building crumbles as the shockwave destroys the walls.",
        "A mushroom cloud errupts out of the bomb casing."
    ]

    def enter(self):
        print '\n' + "-" * 72
        print Explosion.descriptions[randint(0, len(self.descriptions)-1)]
        print "You are dead"
        exit(1)


class EntryWay(Scene):
    def enter(self):
        print "-"*72
        print """
You enter the office to see that the receptionist is missing.
In the center of the desk is an egg timer with a note on it.
"The office has been rigged with bombs and your colleagues have been taken.."
Good Luck...
"""
        raw_input("")
        print "-"*72
        print "You remember that there might a bomb diffusal manual in the training room"
        print "Do you want to go to the training room? (Y/N)"
        choice = raw_input("> ")
        if choice.upper() == 'Y':
            return 'training_room'
        else:
            return 'explosion'


class TrainingRoom(Scene):
    def enter(self):
        room_number = 1
        print "Enter Training Room"
        print "On the table sits a thick textbook next to a ticking timebomb"
        raw_input("> ")
        print "-"*72
        print """
You took the textbook and rapidly began flipping to the diffusal Instructions
for the bomb sitting in front of you.
"""
        start_bomb = BombDiffuse(room_number)
        start_bomb.enter(room_number)
        print """
Breaking a light sweat you diffuse the first bomb
"Thank God" you think. "I probably deserve a coke for that effort!"
You head to the breakroom...
"""
        raw_input("> ")
        print "-"*72
        return 'break_room'



class BreakRoom(Scene):
    def enter(self):
        room_number = 2
        print "-"*72
        print """
Upon entering the breakroom and grabbing a soda from the vending machine you hear
a strange ticking coming from the microwave.
"I hope nobody forgot about their popcorn."
The microwave door is popped open and a dangerous looking bomb is ticking inside.
"""
        raw_input("> ")
        print "-"*72
        print "You open your bomb diffusal manual and turn to the bomb's instructions"
        start_bomb = BombDiffuse(room_number)
        start_bomb.enter(room_number)
        print "-"*72
        print "It has became clear that this whole place is rigged to blow and"
        print "that every room has a bomb in it.."
        print "You grab the diffusal manual and head down the hallway."
        raw_input("> ")
        return 'conference_room'

class ConferenceRoom(Scene):
    def enter(self):
        room_number = 3
        print "-"*72
        print "Ugh, the conference room, that is one room I wouldn't mind if it"
        print "blew up. I'm not sure whether this is just a test and if it is"
        print "then I don't want to fail."
        raw_input("> ")
        print "-"*72
        start_bomb = BombDiffuse(room_number)
        start_bomb.enter(room_number)
        print "-"*72
        print "A small tear drips from the corner of your eye as you realize"
        print "that this was the chance for you to gain revenge on all those"
        print "boring meetings that the suits put you though."
        print "I need to find my colleagues, maybe there is a clue in the"
        print "Boss\'s office."
        raw_input("> ")
        print "-"*72
        print "Between the conference room and the Boss's office is the dreaded"
        print "CUBICAL MAZE! They say that every man, woman or child to ever"
        print "enter here has been condemmed to 40 years of servitude to the"
        print "all powerful overlords, The Shareholders."
        print "Be WARNED, tread carefully here and avoid the comfortable chairs."
        raw_input("> ")
        print "-"*72
        return 'cube_maze'

class CubeMaze(Scene):
    def enter(self):
        room_number = 4
        print "-"*72
        print "Unluckily for you, you've been a resident of the Cubical Maze for"
        print "the last few years (who knows how long at this point). There are"
        print "no desks, nor deadends that surprise you."
        print "Today, however, there is a new organization. The direct route to"
        print "the Boss's office is blocked by a temporary cubical wall."
        print "This forces you to take the long route past your cell."
        print "You remember that you have a few granola bars in your desk, so"
        print "you decide to make a pit stop for some much needed rations."
        print "That's when you spot it. Sitting in your plush pnuematic pleather"
        print "desk chair is a bomb in the shape of a cat. Time to get to work..."
        raw_input("> ")
        print "-"*72
        start_bomb = BombDiffuse(room_number)
        start_bomb.enter(room_number)
        print "-"*72
        print "Now that the bomb has been diffused you can continue onto the"
        print "Boss's office."
        raw_input("> ")
        print "-"*72
        return 'boss_office'


class BossOffice(Scene):
    def enter(self):
        room_number = 5
        print "-"*72
        print "The Boss's Office, it is odd being in here alone. May as well"
        print "have a bit of a snoop before I get to looking for everyone else"
        print "Hmm, there is something making a pulsing vibrating sound in the"
        print "desk. I hope that's not a vibr... Oh damn, it another bomb."
        print "Atleast is isn't a sex toy..."
        raw_input("> ")
        print "-"*72
        start_bomb = BombDiffuse(room_number)
        start_bomb.enter(room_number)
        print "-"*72
        print "The bomb's diffusal revealed a hidden switch in the back of the"
        print "desk. I wonder what this does..."
        print "CRRREEAAKK! The bookshelves swing backwards revealing a secret"
        print "passageway. This must be where my colleagues are hiding."
        raw_input("> ")
        print "-"*72
        return 'explosive_storage'


class ExplosiveStorage(Scene):
    def enter(self):
        room_number = 6
        print "-"*72
        print "The concrete passageway wound it's way down and away from the"
        print "offices. I wonder if this is where we store our bombs. Around"
        print "the next corner was a heavy steel door that was labeled:"
        print "EXPLOSIVE STORAGE ~~ KEEP OUT!"
        print "At the foot of the door a ticking timebomb was resting..."
        raw_input("> ")
        print "-"*72
        start_bomb = BombDiffuse(room_number)
        start_bomb.enter(room_number)
        print "-"*72
        print "Upon disarming the bomb you here a mechanical click as the door"
        print "unlocked. You push the heavy door open to see..."
        raw_input("> ")
        print "-"*72
        return 'finished'


class Finished(Scene):
    def enter(self):
        print "-"*72
        print "\"CONTRATULATIONS!!!\" everyone shouts as you enter the room."
        print "This was your final test before receiving you official bomb"
        print "diffuser certification. You're now a certified bomb technician."


class Map:

    scenes = {
        'explosion': Explosion(),
        'entry_way': EntryWay(),
        'training_room': TrainingRoom(),
        'break_room': BreakRoom(),
        'conference_room': ConferenceRoom(),
        'cube_maze': CubeMaze(),
        'boss_office': BossOffice(),
        'explosive_storage': ExplosiveStorage(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

#create an instance of Map named a map
a_map = Map('entry_way')
#create an instance of Engine named a game
a_game = Engine(a_map)
#use the play function of a_game on a_map
a_game.play(a_map)
