#simple control using pygame

'''
imports
'''
import pygame
import socket

pygame.init()
screen = pygame.display.set_mode((480,320))
pygame.display.set_caption("Robot Driverstation")
print('Welcome to the test Driverstation')
print("Controls:")
print("Up Arrow -> moves robot forward")
print("Down Arrow -> moves robot backward")
print("Left Arrow -> moves robot left")
print("Right Arrow -> moves robot right")
UDP_IP = "10.120.100.0" #This is the ip of the Pi School ip: 10.120.98.209
UDP_PORT = 5005 #This is the port it connects over
address = UDP_IP, UDP_PORT
#new camera stream
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
conn, addr = s.accept()

string = bytes('','UTF-8')
#new part between the comments come back and test later

sock = socket.socket(socket.AF_INET, # Internet
                 socket.SOCK_DGRAM) # UDP

try:
    while True:
        events = pygame.event.get()

        #gets camera feed must test later
        d = conn.recv(640*480)

        if not d:
            print ("break")
            break

        else:

            string += d

        pil_image = Image.fromstring("RGB",(352,288),string)
        #(352,288) is the return of cam.get_size()
        #gets camera feed and displays it must test later

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
