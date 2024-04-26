import RPi.GPIO as GPIO
import time

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

def loop():
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

def destroy():
  GPIO.output(kickMotor, GPIO.LOW)
  GPIO.output(snareMotor, GPIO.LOW)
  GPIO.output(hatMotor, GPIO.LOW)
  GPIO.cleanup()  # Release resource


if __name__ == '__main__':  # Program start from here
  setup()
  try:
    loop()
  except KeyboardInterrupt:
    destroy()
