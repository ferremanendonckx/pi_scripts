import time
import wiringpi
import sys

print("start")
pinLed = 2
pinSwitch = 1
wiringpi.wiringPiSetup()
wiringpi.pinMode(pinLed, 1) #set pin to mode 1 (output)
wiringpi.pinMode(pinLed, 0) #set pin to mode 0 (input)

while True:
    if(wiringpi.digitalRead(pinSwitch) == 0): #input is active low
        print("Button Pressed")
        time.sleep(0.3) #anti bouncing
        wiringpi.digitalWrite(pinLed, 1) #write 1 (HIGH) to LED
    else:
        print("Button released")
        time.sleep(0.3) #anti bouncing
        wiringpi.digitalWrite(pinLed, 0) #write 0 (LOW) to LED