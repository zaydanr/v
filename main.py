import RPi.GPIO as GPIO
import time

firstM = 4


def setup():
  GPIO.setmode(GPIO.BCM)  # Numbers GPIOs by physical location
  GPIO.setup(firstM, GPIO.OUT)
  GPIO.output(firstM, GPIO.HIGH)


def loop():
  while True:
    print('...relayd on')
    GPIO.output(firstM, GPIO.LOW)
    time.sleep(10)
    print('relay off...')
    GPIO.output(firstM, GPIO.HIGH)
    time.sleep(10)


def destroy():
  GPIO.output(firstM, GPIO.HIGH)
  GPIO.cleanup()  # Release resource


if __name__ == '__main__':  # Program start from here
  setup()
  try:
    loop()
  except KeyboardInterrupt:
    destroy()
