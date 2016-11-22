#!/usr/bin/python
import RPi.GPIO as GPIO
from cpu_usage import cpu_rag 
from nagios_status import nagios_rag

host_leds = [23,24,26] # 25 ground
serv_leds = [19,21,22] # 20 ground
cpu_leds  = [13,15,16] # 14 ground

def setup():
    GPIO.setmode(GPIO.BOARD)
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
