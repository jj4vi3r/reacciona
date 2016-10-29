import RPi.GPIO as GPIO
import time
from random import random as rand

class Main():
	output_pins = [3,5,7,11,13]
	input_pins = []
	current_led = 0
	def __init__():
		GPIO.setMode(GPIO.BOARD)
		initLeds()
		randomRoutine()


	def randomRoutine():
		while True:
			GPIO.output(current_led, False)
			current_led = rand(0, output_pins.length)
			GPIO.output(current_led, True)
			time.delay(2)
			

	def initLeds():	
		# inicializar pins de salida
		for i in range(0,output_pins):
			GPIO.setup(output_pins[i],GPIO.OUT)
		


# correr desde linea de commando
if __name__ == "__main__":
	reacciona = Main()
