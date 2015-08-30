import serial
import Petduino
from time import sleep
import sys

def printData(data):
	print "Printdata!"
	print data

def main():
	try:
		pet = Petduino.Petduino('.\petduino.cfg')
		pet.setCallback(1, printData)

	except Petduino.UnhappyPetduino as sadness:
		print "There is a disturbance in the force: %s" % sadness
		sys.stdin.read()
		sys.exit()

	while True:
		pet.setLed(1)
		sleep(1)
		pet.setLed(0)
		sleep(1)

if __name__ == "__main__":
  main()