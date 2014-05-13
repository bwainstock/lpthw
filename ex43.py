from sys import exit
from random import randint

class Scene(object):

        def enter(self):
                print "Not yet configured.  Subclass it and implement enter()."
                exit(1)

class Engine(object):

        def __init__(self, scene_map):
                #print "Engine __init__ has scene_map", scene_map
                self.scene_map = scene_map

        def play(self):
                current_scene = self.scene_map.opening_scene()
                #print "Plays first scene", current_scene

                while True:
                        print "\n--------"
                        next_scene_name = current_scene.enter()
                        #print "next scene", next_scene_name
                        current_scene = self.scene_map.next_scene(next_scene_name)
                        #print "map returns new scene", current_scene

class Death(Scene):

        quips = ["You died.  You suck.", "Your mom is dumb.", "You are a loser.", "I have a small puppy that's better."]

        def enter(self):
                print Death.quips[randint(0, len(self.quips)-1)]
                exit(1)

class CentralCorridor(Scene):

        def enter(self):
                print "The Gothons of Planet PErcal have invaded your ship and destroyed"
                print "your entire crew.  You are the last surviving member and your last"
                print "mission is to get the neutron bomb from the Armory,"
                print "put it in the bridge, and blow the ship up after getting into an "
                print "escape pod."
                print "\n"
                print "You're running down the central corridor to the Armory when"
                print "a Gothon jumps out, red scaly skin, and evil clown costume"
                print "flowing around his gross body.  He's blocking the door to the"
                print "Armory and about to pull a weapon to blast you."

                action = raw_input("> ")

                if action == "shoot":
                        print "Quick on the draw, you shoot your blaster!"
                        print "His stupid clown costume is flowing and moving, which throws"
                        print "off your aim.  Your laser hits his costume only.  This"
                        print "ruins his costume which makes him mad and shoots you in the face."
                        print "You are dead.  he eats you."
                        return 'death'
                elif action == "dodge":
                        print "Duck, dodge, dive, dip, and dodge.  The five Ds of dodge ball."
                        print "Too bad this isn't dodgeball.  You die you idiot."
                        return 'death'
                elif action == "tell a joke":
                        print "You're fancy yourself a pretty funny guy.  You tell the ugly aliean"
                        print "a good joke.  It works and he falls on the floor laughing.  Quick, run"
                        print "to the ARmory before he figures out you're an idiot."
                        return 'laser_weapon_armory'
                else:
                        print "DOES NOT COMPUTER!"
                        return 'central_corridor'


class LaserWeaponArmory(Scene):

        def enter(self):
                
                print "You do a dive roll into the ARmory.  There's a keypad on the bomb's case."
                print "If you get the code wrong 10 times, the lock closes forever.  There appears"
                print " to be 3 digits in the code"
                        
                code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
                print "CODE: ", code
                guess = raw_input("[keypad]> ")
                guesses = 0

                while guess != code and guesses < 10:
                        print "BZZZZEDDDD!"
                        print guesses
                        guesses += 1
                        guess = raw_input("[keypad]> ")
                        print "GUESS: ", guess

                if guess == code:
                        print "The container pops open and you grab the bomb.  Get to the bridge!"
                        return 'the_bridge'
                else:
                        print "That was the last try buddy.  The bomb will blow up before you know it."
                        return 'death'


class TheBridge(Scene):

        def enter(self):
                print "You break out onto the Bridge and you've got the bomb!"
                print "There are five ugly ass alieans trying to take contorl of"
                print "the ship.  Thankfully, they see the bomb and don't draw"
                print "their weapons.  What now?"
                action = raw_input("> ")

                if action == "throw the bomb":
                        print "You panic and throw the bomb at the alieans."
                        print "The bomb starts its self destruct sequence and"
                        print "the whole ship blows.  Great job, you killed"
                        print "the aliens, but you also killed yourself."
                        return 'death'

                elif action == "place the bomb":
                        print "You point your gun at the bomb and caution"
                        print "the aliens.  You slowly place the bomb on the ground"
                        print "and make a mad dash for the escape pod.  Get out now!"
                        return 'escape_pod'
                else:
                        print "DOES NOT COMPUTE!"
                        return 'the_bridge'


class EscapePod(Scene):

        def enter(self):
                print "You rush through the halls trying to get to the escape pod."
                print "When you get to the airlock, there are five different pods."
                print "Some look like they've sustained some damage and might now work."
                print "Which one do you take?"

                good_pod = randint(1,5)
                print good_pod
                guess = raw_input("[pod #]")
                

                if int(guess) != good_pod:
                        print "You jump into pod %s and hit the eject button." % guess
                        print "The pod slowly breaks away from the ship and you're home free!"
                        print "But this is a damaged ship.  It is cracked and doesn't work."
                        print "You're doomed to float through space forever."
                        return 'death'
                else:
                        print "You jump into pod %s and hit the eject button." % guess
                        print "You did it! You're free.  Congrats!"


                return 'finished'

class EndGame(Scene):

        def enter(self):
                exit(1)

class Map(object):

        scenes = {
                'central_corridor': CentralCorridor(),
                'laser_weapon_armory': LaserWeaponArmory(),
                'the_bridge': TheBridge(),
                'escape_pod': EscapePod(),
                'death': Death(),
                'finished': EndGame()
                }

        def __init__(self, start_scene):
                self.start_scene = start_scene
                #print "start_scene in __init__", self.start_scene

        def next_scene(self, scene_name):
                #print "start_scene in next_scene"
                val = Map.scenes.get(scene_name,'CentralCorridor()')
                #print "next_scene returns", val
                return val

        def opening_scene(self):
                return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
