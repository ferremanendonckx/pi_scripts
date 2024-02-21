import wiringpi as wpi
import time

# Define GPIO pins for motor control
motor_pins = [17, 18, 27, 22]  # Example GPIO pins, adjust as per your setup

# Initialize WiringPi
wpi.wiringPiSetupGpio()

# Set motor pins as output
for pin in motor_pins:
    wpi.pinMode(pin, wpi.OUTPUT)

# Define sequences for wave drive and full step
wave_drive_seq = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]

full_step_seq = [
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 0, 1]
]

# Function to drive the motor
def drive_motor(sequence, delay):
    for step in sequence:
        for pin, value in zip(motor_pins, step):
            wpi.digitalWrite(pin, value)
        time.sleep(delay)

try:
    # Drive the motor using wave drive
    print("Driving motor with wave drive...")
    drive_motor(wave_drive_seq, 0.01)  # 10ms delay between steps
    
    # Drive the motor using full step
    print("Driving motor with full step...")
    drive_motor(full_step_seq, 0.01)  # 10ms delay between steps

except KeyboardInterrupt:
    print("\nProgram terminated by user")

finally:
    # Clean up GPIO
    wpi.digitalWrite(motor_pins, wpi.LOW)
    wpi.pinMode(motor_pins, wpi.INPUT)
