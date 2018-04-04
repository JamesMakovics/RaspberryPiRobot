#simple control using pygame

'''
imports
'''
import curses
import RPi.GPIO as GPIO
import pygame
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

pygame.init()
screen = pygame.display.set_mode((480,320))
pygame.display.set_caption("Robot Driverstation")
init() #turns motors off from previous run
print('Welcome to the test Driverstation')
print("Controls:")
print("Up Arrow -> moves robot forward")
print("Down Arrow -> moves robot backward")
print("Left Arrow -> moves robot left")
print("Right Arrow -> moves robot right")

try:
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                GPIO.cleanup()
                pygame.display.quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: #Quits the program
                    break
                elif event.key == pygame.K_UP: #Moves Robot forward
                    Forward()
                elif event.key == pygame.K_DOWN: #Moves Robot Backwards
                    Backward()
                elif event.key == pygame.K_LEFT:
                    Left()
                elif event.key == pygame.K_RIGHT:
                    Right()
            else:
                Stop()
finally:
    GPIO.cleanup()
