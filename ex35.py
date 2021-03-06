#http://learnpythonthehardway.org/book/ex35.html

from sys import exit

def gold_room():
	print("This room is full of gold. How much do you take?")
	while True:
		try:
			next = input("> ")
			how_much = int(next)
			break
		except ValueError:
		    print("That's not a number... try again!")

	if 50 > how_much:
		print("You're not greedy, you win!")
		exit(0)
	else:
		dead("You greedy bastard!")

def bear_room():
	print("There is a bear here.")
	print("The bear has a bunch of honey.")
	print("The fat bear is in front of another door.")
	print("How are you going to move the bear?")
	bear_moved = False

	while True:
		next = input("> ")

		if next == "take honey":
			dead("The bear looks at you and pimp slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print("The bear has moved from the door. You can go through it now.")
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your crotch off.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print("I got no idea what that means.")


def cthulu_room():
	print("Here you see the great evil Cthulu.")
	print("He, it, whatever, stares at you and you go insane.")
	print("Do you flee for your life or eat your head?")

	next = input("> ")

	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulu_room()

def dead(why):
	print(why, "Good job!")
	exit(0)

def start():
	print("You are in a dark room.")
	print("There is a door to you right and left.")
	print("Which one do you take?")

	next = input("> ")

	if next == "left":
		bear_room()
	elif next == "right":
		cthulu_room()
	else:
		dead("You stumble around the room until you starve.")

start()