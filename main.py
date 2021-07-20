player = {"location":"jail"}
game_map = {
	"jail": {"south": "sewers"},
	"sewers":{"west": "exit1", "south": "exit2"},
	"exit1":{"south":"exit3","west": "bankvault", 
	"north":"alleyway"},
	"alleyway":{"west":"home"}
}
descriptions = {"jail":"At the jailcell","sewers":"The sewers, main way to escape jail.","alleyway":"Dark and spooky, you cannot be spotted.","home":"Escaped!"}
directions = [north, south, east, west]
game_over = False
def main():
	global game_over
	while not game_over:
		ask = input("Which way do you want to go?")
		if input is in directions:
			print("hello!")
		elif input == "look":
			print("Ok")
		elif input == "quit":
			print("Goodbye")
		elif input=="help":
			print("enter north, south, east, west to move.")
		else:
			print("I'm afraid that this game cannot reconize that.")
if __name__ == "__main__":
	main()
