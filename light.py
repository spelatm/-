#!/usr/bin/python
# encoding:utf-8
import RPi.GPIO as GPIO
import time
 
pin_pqrs=22
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_pqrs, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
try:
    while True:
        status = GPIO.input(pin_pqrs)
        if status == False:
            print('能见度正常')
        else:
            print('哇塞，好黑')
        time.sleep(0.5)
except KeyboradInterrupt:
    GPIO.cleanup()
