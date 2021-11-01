from __future__ import print_function
from pololu_drv8835_rpi import motors, MAX_SPEED
from gpiozero import DistanceSensor
import time

try:
   ultrasonic = DistanceSensor(echo=17, trigger=4)
   def obstacleahead ():
     motors.motor1.setSpeed(0)
     motors.motor2.setSpeed(0)
     print("Obstacle ahead")

   while (1>0):
     read = raw_input("")
     ultrasonic.when_in_range = obstacleahead
     if read == "n":
       motors.motor1.setSpeed(0)
       motors.motor2.setSpeed(0)
       print ("stop")
     elif read == "b":
       motors.motor2.setSpeed(-200)
       motors.motor1.setSpeed(-200)
       print ("Backward")
     elif read == "f":
       motors.motor1.setSpeed(200)
       motors.motor2.setSpeed(200)
       print ("Forward")
     elif read == "l":
       motors.motor1.setSpeed(-200)
       motors.motor2.setSpeed(200)
       print ("Left")
     elif read == "r":
       motors.motor1.setSpeed(200)
       motors.motor2.setSpeed(-200)
       print ("Right")

finally:
  # Stop the motors, even if there is an exception
  # or the user presses Ctrl+C to kill the process.
  motors.setSpeeds(0, 0)