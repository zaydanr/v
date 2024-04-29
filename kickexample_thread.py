import RPi.GPIO as GPIO
import time
import threading

kickMotor = 27
snareMotor = 4
hatMotor = 23

kick_array = [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
snare_array = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
hat_array = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

def setup():
    GPIO.setmode(GPIO.BCM)  # Numbers GPIOs by physical location
    GPIO.setup(kickMotor, GPIO.OUT)
    GPIO.setup(snareMotor, GPIO.OUT)
    GPIO.setup(hatMotor, GPIO.OUT)
    GPIO.output(kickMotor, GPIO.LOW)
    GPIO.output(snareMotor, GPIO.LOW)
    GPIO.output(hatMotor, GPIO.LOW)

def kick_thread():
    while True:
        for x in kick_array:
            GPIO.output(kickMotor, GPIO.HIGH if x == 1 else GPIO.LOW)
            time.sleep(0.5)

def snare_thread():
    while True:
        for x in snare_array:
            GPIO.output(snareMotor, GPIO.HIGH if x == 1 else GPIO.LOW)
            time.sleep(0.5)

def hat_thread():
    while True:
        for x in hat_array:
            GPIO.output(hatMotor, GPIO.HIGH if x == 1 else GPIO.LOW)
            time.sleep(0.5)

def loop():
    # Create threads for each motor
    kick_thread_instance = threading.Thread(target=kick_thread)
    snare_thread_instance = threading.Thread(target=snare_thread)
    hat_thread_instance = threading.Thread(target=hat_thread)

    # Start all threads
    kick_thread_instance.start()
    snare_thread_instance.start()
    hat_thread_instance.start()

    # Join all threads
    kick_thread_instance.join()
    snare_thread_instance.join()
    hat_thread_instance.join()

def destroy():
    GPIO.output(kickMotor, GPIO.LOW)
    GPIO.output(snareMotor, GPIO.LOW)
    GPIO.output(hatMotor, GPIO.LOW)
    GPIO.cleanup()  # Release resource

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
