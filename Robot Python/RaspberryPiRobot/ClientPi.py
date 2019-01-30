'''
imports
'''
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
import socket, os #added an os import
import setMotors
import robotControllerMethods
import pygame
import pygame.camera
from multiprocessing import Process
from PIL import *

#inits pygame with the correct video configs
pygame.init()
pygame.camera.init()


#This section uses UDP for a socket connection
'''
cam = pygame.camera.Camera("/dev/video0",(300,300),'RGB')
cam.start()
#creates a video feed
image = cam.get_image()
#print = cam.get_size()
img_str = pygame.image.tostring(image,"RGB")
'''

UDP_IP = "192.168.1.125" #Home ip 192.168.1.30
UDP_PORT = 5005
address = UDP_IP,UDP_PORT

#creates a video server and attempts to send it over UDP
def startCamServer(UDP_IP, UDP_PORT):           #startCamServer(UDP_IP, UDP_PORT)

    #Create server:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((UDP_IP,UDP_PORT))
    server.listen(5)

    screen = pygame.display.set_mode((320,240))

    cam = pygame.camera.Camera("/dev/video0",(320,240),"RGB")
    cam.start()

    '''
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((UDP_IP,UDP_PORT))
    s.listen(1)
    conn, addr = s.accept()
    string = bytes('','UTF-8')
    screen = pygame.display.set_mode((320,240))
    '''

    while True:
        s,add = server.accept()
        print "Connected from",add
        image = cam.get_image()
        screen.blit(image,(0,0))
        data = cam.get_raw()
        s.sendall(data)
        pygame.display.update()

#Interupt
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

'''
    while True:
        d = conn.recv(640*480)

        if not d:
            print ("break")
            break

        else:

            string += d

            pil_image = Image.fromstring("RGB",(352,288),string)
    #(352,288) is the return of cam.get_size()
'''
#new section added above test if this works later!

#gets controls over UDP from client
def startCommandServer(UDP_IP, UDP_PORT):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))
    while True:
        move, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        move = move.decode(encoding='UTF-8',errors='strict')
        setMotors.getDriveCommand(move)

p1 = process(target=startCamServer)
p1.start()
p2 = process(target=startCommandServer)
p2.start()
p1.join(UDP_IP, UDP_PORT)
p2.join(UDP_IP, UDP_PORT)
