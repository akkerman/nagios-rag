#!/usr/bin/python
import RPi.GPIO as GPIO
from nagios_rag import *
import time
from multiprocessing import Process

def test_cpu():
    light(cpu_leds, "001")
    time.sleep(1)
    light(cpu_leds, "011")
    time.sleep(1)
    light(cpu_leds, "010")
    time.sleep(1)
    light(cpu_leds, "110")
    time.sleep(1)
    light(cpu_leds, "100")
    time.sleep(1)
    light(cpu_leds, "000")

def test_hs(leds):
    light(leds, "001")
    time.sleep(2)
    light(leds, "010")
    time.sleep(2)
    light(leds, "100")
    time.sleep(1)
    light(leds, "000")

def test_host():
    test_hs(host_leds)

def test_serv():
    test_hs(serv_leds)
 
if __name__ == '__main__':
    setup()
    try: 
        while True:
            c = Process(target=test_cpu)
            h = Process(target=test_host)
            s = Process(target=test_serv)

            c.start()
            h.start()
            s.start()
            c.join()
            h.join()
            s.join()
    except KeyboardInterrupt:
        GPIO.cleanup()
