from RPLCD.i2c import CharLCD
import RPi.GPIO as GPIO
from time import sleep, time

# LCD Setup 
print("Initializing LCD...")
lcd = CharLCD('PCF8574', 0x27)
lcd.clear()

# GPIO Setup 
print("Setting up GPIO...")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

TRIG = 23       # GPIO pin 23 → HC-SR04 TRIG
ECHO = 24       # GPIO pin 24 → HC-SR04 ECHO (via voltage divider)
BUZZER = 18     # GPIO pin 18 → buzzer

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(BUZZER, GPIO.OUT)

GPIO.output(TRIG, False)
sleep(0.5)

# Distance Reading Function 
def get_distance():
    GPIO.output(TRIG, False)
    sleep(0.05)

    GPIO.output(TRIG, True)
    sleep(0.00001)
    GPIO.output(TRIG, False)

    timeout = time() + 0.02
    while GPIO.input(ECHO) == 0:
        if time() > timeout:
            return -1
    pulse_start = time()

    timeout = time() + 0.02
    while GPIO.input(ECHO) == 1:
        if time() > timeout:
            return -1
    pulse_end = time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # in cm
    return round(distance, 2)

# Main Loop
try:
    print("Running sensor loop...")
    while True:
        distance = get_distance()
        print(f"Measured distance: {distance} cm")

        lcd.clear()

        if distance == -1 or distance > 150:
            lcd.write_string("No object")
            GPIO.output(BUZZER, False)
            sleep(0.5)
            continue

        if distance < 5:
            lcd.write_string("TOO CLOSE!")
            for _ in range(3):
                GPIO.output(BUZZER, True)
                sleep(0.05)
                GPIO.output(BUZZER, False)
                sleep(0.05)

        elif distance < 8:
            lcd.write_string("CAUTION")
            for _ in range(2):
                GPIO.output(BUZZER, True)
                sleep(0.1)
                GPIO.output(BUZZER, False)
                sleep(0.1)

        elif distance < 12:
            lcd.write_string("Getting Close")
            GPIO.output(BUZZER, True)
            sleep(0.1)
            GPIO.output(BUZZER, False)
            sleep(0.3)

        elif distance < 30:
            lcd.write_string("SAFE")
            GPIO.output(BUZZER, False)
            sleep(0.5)

        else:
            lcd.write_string("SAFE")
            GPIO.output(BUZZER, False)
            sleep(0.5)

except KeyboardInterrupt:
    print("Shutting down gracefully...")
    lcd.clear()
    GPIO.cleanup()
