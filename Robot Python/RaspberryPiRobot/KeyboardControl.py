#Simple Keyboard control through the console
'''
imports
'''
import curses
import RPi.GPIO as GPIO
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

#Get the curses window, turn off echoing of keyboard to screen, turn on
#instant (no waiting) key response,  and use special values for cursor keys

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

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

def Left():#makes the robot go left
    GPIO.output(MotorLeftForward, True)
    GPIO.output(MotorRightForward, False)
    GPIO.output(MotorLeftBackward, False)
    GPIO.output(MotorRightBackward, False)

def Right():#makes the robot go right
    GPIO.output(MotorLeftForward, False)
    GPIO.output(MotorRightForward, True)
    GPIO.output(MotorLeftBackward, False)
    GPIO.output(MotorRightBackward, False)

def Stop():#makes the robot motors stop
    GPIO.output(MotorLeftForward, False)
    GPIO.output(MotorRightForward, False)
    GPIO.output(MotorLeftBackward, False)
    GPIO.output(MotorRightBackward, False)

init() #turns motors off from previous run
try:
    while True:
        char = screen.getch()
        if char == ord('q'): #Quits the program
            break
        elif char == curses.KEY_UP: #Moves Robot forward
            Forward()
            print("FORWARD")
        elif char == curses.KEY_DOWN:
            Backward()
            print("BACKWARD")
        elif char == curses.KEY_LEFT:
            Left()
            print("LEFT")
        elif char == curses.KEY_RIGHT:
            Right()
            print("RIGHT")
        elif char == ord('s'):
            Stop()
            print("STOP")
finally:
    #Close down curses properly,inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
