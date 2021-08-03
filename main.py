player = {"location":"jail"}
gt = False
game_map = {
	"jail": {"south": "sewers"},
	"sewers":{"west": "exit1", "south": "exit2"},
	"exit1":{"south":"exit3","west": "bankvault", 
	"north":"alleyway"},
	"alleyway":{"west":"home"},
	"bankvault":{"east":"exit1"}
}
descriptions = {"jail":"the jailcell","sewers":"The main way to escape jail.","alleyway":"Dark and spooky, you cannot be spotted.","home":"Escaped!","bankvault":"with MONEY!", "exit1":"_","exit2":"_","exit3":"_"}
directions = ["north", "south", "east", "west"]
game_over = False
def look(location):
	return descriptions[location]
def main():
	global game_over
	while not game_over:
		inputt = input("Which way do you want to go?")
		if inputt in directions and inputt in game_map[player["location"]]:
			player["location"] = game_map[player["location"]][inputt]
			print("You just moved to {}".format(player["location"]), ",", look(player["location"]))
			if player["location"] == "bankvault":
				gt = True
			if player["location"] == "exit2" or player["location"] == "exit3":
				print("YOU...HAVE...BEEN...ARRESTED.")
				break
			if player["location"] == "home":
				if gt == True:
					  print("You got away with the money!")
				else:
					  print("You escaped, but you forgot the money...")
			#print("hello!")
		elif inputt == "look":
			print(look(player["location"]))
		elif inputt == "quit":
			print("Goodbye")
		elif inputt=="help":
			print("enter north, south, east, west to move.")
		else:
			print("I'm afraid that this game cannot reconize that.")
if __name__ == "__main__":
	main()
