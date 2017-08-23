import Adafruit_BBIO.PWM as PWM
from time import sleep

myPWM="P9_14"
PWM.start(myPWM, 4, 100)
sleep(1)
PWM.stop(myPWM)
PWM.cleanup()
