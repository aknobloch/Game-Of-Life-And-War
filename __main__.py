from game_of_war import main
import sys

if(__name__ == "__main__") :

	width = None
	height = None

	if(len(sys.argv) >= 3) :
		# screen size was given
		try :
			width = int(sys.argv[1])
			height = int(sys.argv[2])
			print("Game board size set to", width, "x", height)

		except ValueError:
			width = None
			height = None
			print("Invalid argument parameters.")

	else :
		print("No game board size specified. Dynamically calculating from monitor size.")

	main(width, height)
