player = {"location":"jail"}
game_map = {
	"jail": {"south": "sewers"},
	"sewers":{"west": "exit1", "south": "exit2"},
	"exit1":{"south":"exit3","west": "bankvault", 
	"north":"alleyway"},
	"alleyway":{"west":"home"}
}
descriptions = {"jail":"At the jailcell","sewers":"The sewers, main way to escape jail.","alleyway":"Dark and spooky, you cannot be spotted."}