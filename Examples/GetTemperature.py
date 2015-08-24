import serial
import Petduino
from time import sleep
import sys

def main():
	try:
		pet = Petduino.Petduino('COM4', 9600)
	except Petduino.UnhappyPetduino as sadness:
		print "There is a disturbance in the force: %s" % sadness
		sys.stdin.read()
		sys.exit()

	while True:
		pet.getTemperature()
		sleep(1)


if __name__ == "__main__":
  main()