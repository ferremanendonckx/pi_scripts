import time
import wiringpi
import sys

def blink(_pin):
    wiringpi.digitalWrite(_pin, 1)  # Write 1 (HIGH) to pin
    time.sleep(0.005)
    wiringpi.digitalWrite(_pin, 0)  # Write 0 (LOW) to pin
    time.sleep(0.005)


print("Start")
pin4 = 3   # GPIO pin numbering for Orange Pi may differ, adjust pin numbers accordingly
pin8 = 4   # GPIO pin numbering for Orange Pi may differ, adjust pin numbers accordingly
pin10 = 6  # GPIO pin numbering for Orange Pi may differ, adjust pin numbers accordingly
pin12 = 9 # GPIO pin numbering for Orange Pi may differ, adjust pin numbers accordingly

wiringpi.wiringPiSetup()
wiringpi.pinMode(pin4, 1)   # Set pin to mode 1 (OUTPUT)
wiringpi.pinMode(pin8, 1)   # Set pin to mode 1 (OUTPUT)
wiringpi.pinMode(pin10, 1)  # Set pin to mode 1 (OUTPUT)
wiringpi.pinMode(pin12, 1)  # Set pin to mode 1 (OUTPUT)


for i in range(0, 1000):
    blink(pin4)
    blink(pin8)
    blink(pin10)
    blink(pin12)

print("Done")