from time import sleep
import RPi.GPIO as GPIO

# green - BCM 3 -> PWMA
# orange - BCM 6 -> AIN2
# blue - BCM 9 -> AIN1
# white - BCM 21 -> STBY
# (3v3 power -> VCC, Ground -> common GND)


PIN_PWMA = 3
PIN_AIN2 = 6
PIN_AIN1 = 9
PIN_STBY = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_PWMA, GPIO.OUT)
GPIO.setup(PIN_AIN2, GPIO.OUT)
GPIO.setup(PIN_AIN1, GPIO.OUT)
GPIO.setup(PIN_STBY, GPIO.OUT)

pwm_a = GPIO.PWM(PIN_PWMA, 50)

try:
  pwm_a.start(50)
  GPIO.output(PIN_STBY, 1);
  GPIO.output(PIN_AIN1, 1);
  sleep(0.5)

  GPIO.output(PIN_AIN1, 0);
  GPIO.output(PIN_STBY, 0);
  pwm_a.stop()
  

except KeyboardInterrupt:
  print "exiting..."

finally:
  print "cleaning up..."
  pwm_a.stop()
  GPIO.cleanup()

