#!/usr/bin/env python

import mraa
import time

gpio_1 = mraa.Gpio(10)
gpio_2 = mraa.Gpio(11)

gpio_3 = mraa.Gpio(12)
gpio_4 = mraa.Gpio(13)

class Robot(object):
 gpio_1.dir(mraa.DIR_OUT)
 gpio_2.dir(mraa.DIR_OUT)
 gpio_3.dir(mraa.DIR_OUT)
 gpio_4.dir(mraa.DIR_OUT)

 def __init__(self,start):
     self.start = start

 def run(self):
    gpio_1.write(1)
    gpio_2.write(1)
    gpio_3.write(1)
    gpio_4.write(1)
    time.sleep(0.5)
    gpio_1.write(0)
    gpio_2.write(0)
    gpio_3.write(0)
    gpio_4.write(0)

 def stop(self):
    gpio_1.write(0)
    gpio_2.write(0)
    gpio_3.write(0)
    gpio_4.write(0)

 def left(self):
    gpio_1.write(1)
    gpio_2.write(1)
    gpio_3.write(0)
    gpio_4.write(1)

 def right(self):
    gpio_1.write(1)
    gpio_2.write(1)
    gpio_3.write(1)
    gpio_4.write(0)
 
 def back(self):
    gpio_1.write(0)
    gpio_2.write(0)
    gpio_3.write(0)
    gpio_4.write(1)



