'''
imports
'''
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
import socket
import runMotors
import robotControlMethods
import pygame

#inits pygame with the correct video configs
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(300,300),'RGB')
cam.start()

#creates a video feed
image = cam.get_image()
print = cam.get_size()
img_str = pygame.image.tostring(img,"RGB")

UDP_IP = "10.120.100.0" #Home ip 192.168.1.30
UDP_PORT = 5005
address = UDP_IP,UDP_PORT

#creates a video server and attempts to send it over UDP
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((UDP_IP,UDP_PORT))
s.sendall(img_str)
s.close
#new section added above test if this works later!

#gets controls over UDP from client
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
    move, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    move = move.decode(encoding='UTF-8',errors='strict')
    setMotors.getDriveCommand(move)
