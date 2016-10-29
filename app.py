import RPi.GPIO as GPIO
import time
from random import randint

class Main():
	output_pins = [3,5,7]
	input_pins = []
	current_led = 3
	def __init__(self):
		GPIO.setmode(GPIO.BOARD)
		self.initLeds()
		self.randomRoutine()


	def randomRoutine(self):
		while True:
			GPIO.output(self.current_led, False)
			pos = randint(0, len(self.output_pins) - 1)
			print pos
			self.current_led = self.output_pins[pos]
			GPIO.output(self.current_led, True)
			time.sleep(0.05)
			

	def initLeds(self):	
		# inicializar pins de salida
		for i in range(0, len(self.output_pins)):
			print("Inicializando led: {} ".format(self.output_pins[i]))
			GPIO.setup(self.output_pins[i],GPIO.OUT)
		


# correr desde linea de commando
if __name__ == "__main__":
	reacciona = Main()
