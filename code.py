"""
Created by Annwyn M. 
Created on Mar 3/2025 
this makes an LED blink every second on a breadboard 
"""

import time
import board 
import digitalio 

led = digitalio.DigitalInOut(board.GP5) 
led.direction = digitalio.Direction.OUTPUT

blink_time = 1 

# loop forever 
while True: 
  print(blink_time) 
  led.value = Ture #turnd LED on 
  time.sleep(blink_time) #wait for 1000ms 
  led.value = False #turns LED off 
  time.sleep(blink_time) #wait for 1000ms

  blink_time += 1 
