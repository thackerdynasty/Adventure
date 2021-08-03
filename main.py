inventory = []
player = {"location":"jail"}
tpicked = False
gt = False
dyn = False
game_map = {
	"jail": {"south": "sewers"},
	"sewers":{"west": "exit1", "south": "exit2"},
	"exit1":{"south":"exit3","west": "bankvault", 
	"north":"alleyway","southwest":"rcon2"},
	"alleyway":{"west":"home"},
	"bankvault":{"east":"exit1", "southeast":"rcon", "northwest":"fcon"}
}
descriptions = {"jail":"the jailcell","sewers":"The main way to escape jail.","alleyway":"Dark and spooky, you cannot be spotted.","home":"Escaped!","bankvault":"with MONEY!", "exit1":"_","exit2":"_","exit3":"_"}
directions = ["north", "south", "east", "west", "southeast", "northwest","southwest"]
game_over = False
def look(location):
	return descriptions[location]
def main():
	global dyn
	global inventory
	global game_over
	while not game_over:
		inputt = input("Which way do you want to go?")
			#print("hello!")
		if inputt == "look":
			print(look(player["location"]))
		elif inputt == "quit":
			print("Goodbye")
		elif inputt=="help":
			print("enter north, south, east, west to move.")
		elif inputt=="pickup":
			if player["location"] == "rcon":
				gt = True
				print("Got the money!")
				inventory.append("Money")
			elif player["location"] == "rcon2":
				dyn = True
				print("Got the dynamite!")
				inventory.append("Dynamite")
		elif inputt in directions and inputt in game_map[player["location"]]:
			player["location"] = game_map[player["location"]][inputt]
			print("You just moved to {}".format(player["location"]), ",", look(player["location"]))
			if player["location"] == "exit2" or player["location"] == "exit3":
				print("YOU...HAVE...BEEN...ARRESTED.")
				break
			if player["location"] == "bankvault":
				'''add in the use dynamite code'''
			if player["location"] == "home":
				if gt:
					print("You got away with the money!")
					break
				else:
					print("You escaped, but you forgot the money...")
					break
		elif inputt=="inventory":
			print(inventory)
		else:
			print("I'm afraid that this game cannot reconize that.")
if __name__ == "__main__":
	main()
