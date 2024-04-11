import RPi.GPIO as GPIO
import time

left = 4
middle = 27
right = 22

def setup():
  GPIO.setmode(GPIO.BCM)  # Numbers GPIOs by physical location
  GPIO.setup(left, GPIO.OUT)
  GPIO.setup(middle, GPIO.OUT)
  GPIO.setup(right, GPIO.OUT)
  GPIO.output(left, GPIO.LOW)
  GPIO.output(middle, GPIO.LOW)
  GPIO.output(right, GPIO.LOW)


def loop():
  while True:
    print('...left on')
    GPIO.output(left, GPIO.HIGH)
    time.sleep(10)
    print('left off...')
    GPIO.output(left, GPIO.LOW)
    
    print('...middle on')
    GPIO.output(middle, GPIO.HIGH)
    time.sleep(10)
    print('middle off...')
    GPIO.output(left, GPIO.LOW)
    
    print('...right on')
    GPIO.output(right, GPIO.HIGH)
    time.sleep(10)
    print('right off...')
    GPIO.output(left, GPIO.LOW)

    print('...all on')
    GPIO.output(right, GPIO.HIGH)
    GPIO.output(left, GPIO.HIGH)
    GPIO.output(middle, GPIO.HIGH)
    time.sleep(10)
    print('all off...')
    GPIO.output(left, GPIO.LOW)
    GPIO.output(middle, GPIO.LOW)
    GPIO.output(right, GPIO.LOW)

def destroy():
  GPIO.output(left, GPIO.HIGH)
  GPIO.output(middle, GPIO.HIGH)
  GPIO.output(right, GPIO.HIGH)
  GPIO.cleanup()  # Release resource


if __name__ == '__main__':  # Program start from here
  setup()
  try:
    loop()
  except KeyboardInterrupt:
    destroy()
