import time
import board
import busio
import BH1750FVI
import bmp280
import RPi.GPIO as GPIO
import requests
from random import randint

# Define GPIO pins
LIGHT_PIN = 17
TEMP_CONTROL_PIN = 18
TEMP_SENSOR_PIN = 23

# Define ThingSpeak parameters
THINGSPEAK_API_KEY = "FMB47V059AA45KAZ"

# Initialize I2C bus and sensors
i2c = busio.I2C(board.SCL, board.SDA)
bh1750 = BH1750FVI.BH1750FVI(addr=0x23)
bmp280 = bmp280.BMP280(i2c)

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(LIGHT_PIN, GPIO.OUT)
GPIO.setup(TEMP_CONTROL_PIN, GPIO.OUT)
GPIO.setup(TEMP_SENSOR_PIN, GPIO.IN)

# Define predefined settings
TEMP_GOAL = 25  # Temperature goal in Celsius
LIGHT_GOAL = 500  # Light intensity goal in lux

def publish_to_thingspeak(payload):
    try:
        requests.post('https://api.thingspeak.com/update.json', params=payload)
    except Exception as e:
        print("Error publishing to ThingSpeak:", e)

def read_temperature():
    return bmp280.read_temperature()

def read_light_intensity():
    return bh1750.luminance(BH1750FVI.ONCE_HIRES_1)

def control_light_intensity(intensity):
    GPIO.output(LIGHT_PIN, intensity)

def control_temperature(temperature):
    # Placeholder for controlling temperature
    if temperature < TEMP_GOAL:
        GPIO.output(TEMP_CONTROL_PIN, GPIO.HIGH)  # Turn on heating
    else:
        GPIO.output(TEMP_CONTROL_PIN, GPIO.LOW)   # Turn off heating

def read_light_goal():
    return LIGHT_GOAL

def read_temp_goal():
    return TEMP_GOAL

# Main loop
while True:
    try:
        # Read sensor data
        temperature = read_temperature()
        light_intensity = read_light_intensity()

        # Publish sensor data to ThingSpeak
        payload = {
            'api_key': THINGSPEAK_API_KEY,
            'field1': temperature,
            'field2': light_intensity
        }
        publish_to_thingspeak(payload)

        # Control light intensity based on goal
        light_goal = read_light_goal()
        if light_intensity < light_goal:
            control_light_intensity(True)
        else:
            control_light_intensity(False)

        # Control temperature based on goal
        temp_goal = read_temp_goal()
        control_temperature(temperature)

        # Print sensor data to the terminal
        print("Temperature:", temperature, "C")
        print("Light Intensity:", light_intensity, "lux")

        time.sleep(15)  # Update ThingSpeak every 15 seconds

    except KeyboardInterrupt:
        break

# Cleanup GPIO
GPIO.cleanup()