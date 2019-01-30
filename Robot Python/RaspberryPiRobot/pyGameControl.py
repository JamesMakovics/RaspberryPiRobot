#simple control using pygame

'''
imports
'''
import pygame
import socket, sys #added a sys import for connection
import pygame.camera
from PIL import Image
from multiprocessing import Process

pygame.init()
screen = pygame.display.set_mode((480,320))
pygame.display.set_caption("Robot Driverstation")
font = pygame.font.SysFont("Arial",14)
clock = pygame.time.Clock()
timer = 0
previousImage = ""
image = ""
print('Welcome to the test Driverstation')
print("Controls:")
print("Up Arrow -> moves robot forward")
print("Down Arrow -> moves robot backward")
print("Left Arrow -> moves robot left")
print("Right Arrow -> moves robot right")
UDP_IP = "192.168.1.125" #This is the ip of the Pi School ip: 10.120.98.209
UDP_PORT = 5005 #This is the port it connects over
address = UDP_IP, UDP_PORT

#new camera stream
def startCamClient(UDP_IP, UDP_PORT):
    '''
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((UDP_IP,UDP_PORT))
    s.listen(1)
    '''
    #Receive data
  if timer < 1:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((str(ip),UDP_PORT))
    data = client_socket.recv(1024000)
    timer = 30

  else:
    timer -= 1
  previousImage = image

#Convert image
  try:
    image = Image.fromstring("RGB",(320,240),data)
    image = image.resize((320,240))
    image = pygame.image.frombuffer(image.tostring(),(320,240),"RGB")

#Interupt
  except:
    image = previousImage
  output = image
  screen.blit(output,(0,0))
  clock.tick(60)
  pygame.display.flip()

    '''
    conn, addr = s.accept()

    string = bytes('','UTF-8')
    #new part between the comments come back and test later

    sock = socket.socket(socket.AF_INET, # Internet
                 socket.SOCK_DGRAM) # UDP
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

def startCommandClient(UDP_IP, UDP_PORT):
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
                        move = "Forward"
                        sock.sendto(str(move).encode('utf-8'), address)
                    elif event.key == pygame.K_DOWN: #Moves Robot Backwards
                        move = "Backward"
                        sock.sendto(str(move).encode('utf-8'), address)
                    elif event.key == pygame.K_LEFT:
                        move = "Right"
                        sock.sendto(str(move).encode('utf-8'), address)
                    elif event.key == pygame.K_RIGHT:
                        move = "Left"
                        sock.sendto(str(move).encode('utf-8'), address)
                else:
                    move = "Stop"
                    sock.sendto(str(move).encode('utf-8'), address)
    finally:
        GPIO.cleanup()

p1 = Process(target=startCamClient)
p1.start()
p2 = Process(target=startCommandClient)
p2.start()
p1.join(UDP_IP, UDP_PORT)
p2.join(UDP_IP, UDP_PORT)
