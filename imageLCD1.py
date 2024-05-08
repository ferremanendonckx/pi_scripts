import time
import wiringpi
from PIL import Image
from ClassLCD import LCD

def ActivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 0)  # Activated LCD using CS
    time.sleep(0.000005)

def DeactivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 1)  # Deactivated LCD using CS
    time.sleep(0.000005)

# Load image
image_path = "your_image.bmp"  # Replace "your_image.bmp" with the path to your image
image = Image.open(image_path)

# Resize image to fit LCD screen
lcd_width = 84  # Adjust according to your LCD resolution
lcd_height = 48  # Adjust according to your LCD resolution
image = image.resize((lcd_width, lcd_height))

# Convert image to monochrome (1-bit) mode
image = image.convert("1")

# Convert image to bytes
image_bytes = image.tobytes()

# Pin configuration
PIN_OUT = {
    'SCLK': 14,
    'DIN': 11,
    'DC': 9,
    'CS': 15,  # We will not connect this pin! --> we use w13
    'RST': 10,
    'LED': 6,  # backlight
}

# In this code, we use w13 (pin 22) as chip select
pin_CS_lcd = 13

# Setup WiringPi
wiringpi.wiringPiSetup()
wiringpi.wiringPiSPISetupMode(1, 0, 400000, 0)  # (channel, port, speed, mode)
wiringpi.pinMode(pin_CS_lcd, 1)  # Set pin to mode 1 (OUTPUT)

# Initialize LCD
ActivateLCD()
lcd_1 = LCD(PIN_OUT)

try:
    lcd_1.clear()
    lcd_1.set_backlight(1)

    while True:
        ActivateLCD()
        lcd_1.display_image(image_bytes)  # Display the image
        DeactivateLCD()
        time.sleep(5)  # Adjust delay as needed

except KeyboardInterrupt:
    ActivateLCD()
    lcd_1.clear()
    lcd_1.refresh()
    lcd_1.set_backlight(0)
    DeactivateLCD()
    print("\nProgram terminated")
