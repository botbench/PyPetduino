import serial
import Petduino
from time import sleep
import sys

def main():
	try:
		pet = Petduino.Petduino('.\petduino.cfg')
	except Petduino.UnhappyPetduino as sadness:
		print "There is a disturbance in the force: %s" % sadness
		sys.stdin.read()
		sys.exit()

	while True:
		pet.setData("0000001800000000")
		sleep(0.1)
		pet.setData("00003C243C000000")
		sleep(0.1)
		pet.setData("007E42665A7E0000")
		sleep(0.1)
		pet.setData("FF81C3A59981FF00")
		sleep(0.5)
		pet.setData("007E42665A7E0000")
		sleep(0.1)
		pet.setData("00003C243C000000")
		sleep(0.1)

if __name__ == "__main__":
  main()