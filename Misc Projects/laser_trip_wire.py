import RPi.GPIO as gpio
from gpiozero import LightSensor
import time.sleep
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

gpio.setup(3, gpio.OUT) #Use pin number accordingly (for Buzer)
ldr = LightSensor(17)

while True:
    if ldr.value < 0.5:
        for i in range(10):
            gpio.output(3, gpio.HIGH)
            sleep(.2)
            gpio.output(3, gpio.LOW)
            sleep(.2)
    else:
        gpio.output(3, gpio.LOW)


        
