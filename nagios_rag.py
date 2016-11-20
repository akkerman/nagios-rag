#!/usr/bin/python
import RPi.GPIO as GPIO
from cpu_usage import cpu_rag 
from nagios_status import nagios_rag

host_leds = [11,9,10]
serv_leds = [22,27,17]
cpu_leds  = [18,8,25]

def setup():
    GPIO.setmode(GPIO.BCM)
    for led in host_leds + serv_leds + cpu_leds:
        GPIO.setup(led, GPIO.OUT, initial=False)

def light(leds, state):
    for i in range(3):
       GPIO.output(leds[i], int(state[i])) 


if __name__ == '__main__':
    setup()
    try: 
        while True:
            cpu_state = cpu_rag()
            (host_state, serv_state) = nagios_rag()
            light(cpu_leds, cpu_state) 
            light(host_leds, host_state)
            light(serv_leds, serv_state)
        
    except KeyboardInterrupt:
        GPIO.cleanup()
