#This manages the Pi from the server side
'''
imports
'''
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
'''
Setup of GPIO
'''

MotorLeftBackward = 17 #in pin 11 on RPI 3
MotorLeftForward = 27 #in pin 13 on RPI 3
MotorRightForward = 22 #in pin 15 on RPI 3
MotorRightBackward = 23 #in pin 16 on RPI 3

'''
Init the GPIO pins
'''
GPIO.setup(MotorLeftForward, GPIO.OUT)
GPIO.setup(MotorLeftBackward, GPIO.OUT)
GPIO.setup(MotorRightForward, GPIO.OUT)
GPIO.setup(MotorRightBackward, GPIO.OUT)

def init(): #sets all the motors to off
    GPIO.output(MotorLeftForward, False)
    GPIO.output(MotorRightForward, False)
    GPIO.output(MotorLeftBackward, False)
    GPIO.output(MotorRightBackward, False)

def Forward():#makes the robot go forward
    GPIO.output(MotorLeftForward, True)
    GPIO.output(MotorRightForward, True)
    GPIO.output(MotorLeftBackward, False)
    GPIO.output(MotorRightBackward, False)

def Backward():#makes the robot go backwards
    GPIO.output(MotorLeftForward, False)
    GPIO.output(MotorRightForward, False)
    GPIO.output(MotorLeftBackward, True)
    GPIO.output(MotorRightBackward, True)

def Right():#makes the robot go left
    GPIO.output(MotorLeftForward, True)
    GPIO.output(MotorRightForward, False)
    GPIO.output(MotorLeftBackward, False)
    GPIO.output(MotorRightBackward, False)

def Left():#makes the robot go right
    GPIO.output(MotorLeftForward, False)
    GPIO.output(MotorRightForward, True)
    GPIO.output(MotorLeftBackward, False)
    GPIO.output(MotorRightBackward, False)

def Stop():#makes the robot motors stop
    GPIO.output(MotorLeftForward, False)
    GPIO.output(MotorRightForward, False)
    GPIO.output(MotorLeftBackward, False)
    GPIO.output(MotorRightBackward, False)
