import serial
import sys
import ConfigParser

from time import sleep

class UnhappyPetduino(Exception):
	def __init__(self, reason):
		self.reason = reason

	def __str__(self):
		return repr(self.reason)

class Petduino(object):

	# For PC -> Petduino 
	SET_STATE_ACTION				= 0
	GET_STATE_ACTION				= 1
	SET_LED_ACTION					= 2
	TOGGLE_LED_ACTION				= 3
	GET_LED_ACTION					= 4
	GET_TEMPERATURE_ACTION	= 5
	GET_LIGHT_LEVEL_ACTION	= 6
	SET_DATA_ACTION					= 7

	# For Petduino -> PC
	STATE_EVENT							= 0
	LED_EVENT								= 1
	TEMPERATURE_EVENT				= 2
	LIGHT_LEVEL_EVENT				= 3
	BUTTON_1_EVENT					= 4
	BUTTON_2_EVENT					= 5

	#def __init__ (self, serialPort, baudrate):
	#	try:
	#		self.ser = serial.Serial(serialPort, baudrate, timeout=1)
	#	except IOError:
	#		raise UnhappyPetduino("Could not open %s" % serialPort)
	#		return
	#	# The sleep is necessary to allow the serial port to open and the Petduino to start up
	#	sleep(2)

	#	# Absorb the first line of garbage
	#	self.readReply()

	def __init__ (self, configfile):
		self.configfile = configfile

		cfgparser = ConfigParser.ConfigParser()
		cfgparser.readfp(open(configfile))

		if not cfgparser.has_section('Serial'):
			raise UnhappyPetduino("Config file %s has no Serial section" % configfile)

		if not cfgparser.has_option('Serial', 'port'):
			raise UnhappyPetduino("Config file %s has no port value" % configfile)
		else:
			port = cfgparser.get('Serial', 'port')

		if not cfgparser.has_option('Serial', 'baud'):
			raise UnhappyPetduino("Config file %s has no baud value" % configfile)
		else:
			baud = cfgparser.getint('Serial', 'baud')

		try:
			self.ser = serial.Serial(port, baud, timeout=1)
		except IOError:
			raise UnhappyPetduino("Could not open %s" % port)
			return
		# The sleep is necessary to allow the serial port to open and the Petduino to start up
		sleep(2)

		# Absorb the first line of garbage
		self.readReply()

	def flush(self):
		self.ser.flushInput()
		self.ser.flushOutput()

	def readReply(self):
		reply = []
		data = ""
		line = self.ser.readline()
		if len(line) > 0:
			line = line.rstrip(';\r\n')
			print line.split(',')
			return line.split(',')


	def setState(self, state):
		return

	def getState(self):
		return 

	def setLed(self, onoroff):
		if (onoroff == 0) or (onoroff == 1):
			self.ser.write("%d, %d;" % (self.SET_LED_ACTION, onoroff))
			data = self.readReply()
			if data[0] != '%d' % self.LED_EVENT:
				sys.stderr.write("Wrong event returned!\n");
			else:
				sys.stderr.write("Current state of LED: %s\n" % data[1])

	def toggleLed(self):
		data = "%d;" % (self.TOGGLE_LED_ACTION)
		print data

	def getLed(self):
		return

	def getTemperature(self):
		self.ser.write("%d;" % (self.GET_TEMPERATURE_ACTION))
		data = self.readReply()
		if data[0] != '%d' % self.TEMPERATURE_EVENT:
			sys.stderr.write("Wrong event returned!\n");
		else:
			sys.stderr.write("Current temp: %s\n" % data[1])

	def getLightLevel(self):
		self.ser.write("%d;" % (self.GET_LIGHT_LEVEL_ACTION))
		data = self.readReply()
		if data[0] != '%d' % self.LIGHT_LEVEL_EVENT:
			sys.stderr.write("Wrong event returned!\n");
		else:
			sys.stderr.write("Current light level: %s\n" % data[1])

	def setData(self, data):
		return

	def getButton(self, button):
		return

	def printData(farg, *args):
		print "formal arg:", farg
		for arg in args:
				print "another arg:", args
