'''
imports
'''
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
import socket
import setMotors
import robotControllerMethods
import pygame
import pygame.camera

#inits pygame with the correct video configs
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(300,300),'RGB')
cam.start()

#creates a video feed
image = cam.get_image()
print = cam.get_size()
img_str = pygame.image.tostring(image,"RGB")

UDP_IP = "192.168.1.125" #Home ip 192.168.1.30
UDP_PORT = 5005
address = UDP_IP,UDP_PORT

p1 = Process(target=startCamServer)
  p1.start(UDP_IP, UDP_PORT)
  p2 = Process(target=startCommandServer)
  p2.start(UDP_IP, UDP_PORT)
  p1.join(UDP_IP, UDP_PORT)
  p2.join(UDP_IP, UDP_PORT)

#creates a video server and attempts to send it over UDP
def startCamServer(UDP_IP, UDP_PORT):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((UDP_IP,UDP_PORT))
    s.listen(1)
    conn, addr = s.accept()

    string = bytes('','UTF-8')


    while True:

        d = conn.recv(640*480)

        if not d:
            print ("break")
            break

        else:

            string += d

            pil_image = Image.fromstring("RGB",(352,288),string)
    #(352,288) is the return of cam.get_size()
#new section added above test if this works later!

#gets controls over UDP from client
def startCommandServer(UDP_IP, UDP_PORT):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))
        while True:
            move, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
            move = move.decode(encoding='UTF-8',errors='strict')
            setMotors.getDriveCommand(move)
