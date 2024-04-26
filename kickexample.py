import RPi.GPIO as GPIO
import time

kickMotor = 27
snareMotor = 4
hatMotor = 23

kick_array = [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
snare_array = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
hat_array = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

lengthofkick = len(kick_array)

while (1==1):
    for x in kick_array:
        if (x==1):
            GPIO.output(kickMotor, GPIO.HIGH)
            time.sleep(.5)
        else:
            GPIO.output(kickMotor, GPIO.LOW)
            time.sleep(.5)

while (1==1):
    for x in snare_array:
        if (x==1):
            GPIO.output(snareMotor, GPIO.HIGH)
            time.sleep(.5)
        else:
            GPIO.output(snareMotor, GPIO.LOW)
            time.sleep(.5)

while (1==1):
    for x in hat_array:
        if (x==1):
            GPIO.output(hatMotor, GPIO.HIGH)
            time.sleep(.5)
        else:
            GPIO.output(hatMotor, GPIO.LOW)
            time.sleep(.5)
