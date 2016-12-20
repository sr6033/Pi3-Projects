from gpiozero import LED
from time import sleep

red = LED(2)
orange = LED(3)
green = LED(4)

green.on()
orange.off()
red.off()

while True:
    sleep(5)
    green.off()
    orange.on()
    sleep(1)
    orange.off()
    red.on()
    sleep(5)
    orange.on()
    sleep(1)
    green.on()
    orange.off()
    red.off()
