from sys import exit
from random import randint


class Scene(object):
    
    def enter(self):
        print ("This is not finished.  Subclass it and imp. enter()."
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        print "Engine __init__ has scene_map", scene_map
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        print "Plays first scene", current_scene

        while True:
            print "\n--------"
            next_scene_name = current_scene.enter()
            print "next scene", next_scene_name
            current_scene = self.scene_map.next_scene(next_scene_name)
            print "map returns new scene", current_scene

class Death(Scene):
    
    def play(self):
        pass

class Corridor(Scene):

    def play(self):
        pass

class Armory(Scene):

    def play(self):
        pass

class Bridge(Scene):

    def play(self):
        pass

class EscapePod(Scene):

    def play(self):
        pass


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
