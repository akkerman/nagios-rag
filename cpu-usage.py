import RPi.GPIO as GPIO
import time
import psutil

GPIO.setmode(GPIO.BCM)

lights=[4,18,23]
for gpio in lights:
    GPIO.setup(gpio, GPIO.OUT, initial=False)

try:
    while True:
        cpu = psutil.cpu_percent(interval=1)
        print cpu

        state = "001"
        if cpu > 25:
            state = "011"
        if cpu > 50:
            state = "010"
        if cpu > 75:
            state = "110"
        if cpu > 99:
            state = "100"
            
        for i in range(3):
          GPIO.output(lights[i], int(state[i]))            
                
except KeyboardInterrupt:
    GPIO.cleanup()
