<br> <br>

------------------------------------------------------------------------

# Network Terminology

------------------------------------------------------------------------

#### Introduction

My motivation behind this markdown file was that when I was searching for malware development of RATs in python (in order to better understand how they work), <br>
I barley found any guides that explain the use of libraries they used in their code or certain network terminologies that were given.

I put this here in order to help me and other viewers of this project to have a better understanding of whats going on and how a RAT functions with networks. 

This way, it wont be as confusing to understand for most first-time programmers who want to learn how to make projects like these.

I shall include this in most of my projects that involve networking, so I hope you enjoy. 

Support my Github Account Here - [lin8x](www.github.com/lin8x)

------------------------------------------------------------------------

#### Table of Contents

<!-- vim-markdown-toc GFM -->

* [Remote Access Trojans](#RATS)
* * [What is a RAT](#WIAR)
* * [How the RAT Works](#HTRW)
* * * [Hiding the RAT](#HTR)
* * * [Accessing the Victim's System](#ATVS)
* * * [Allowing Attacker's Use](#AAU)
* * [What do RATs allow for attackers](#WDRAFA)
* * [This Specific RAT Project](#TSRP)
* [Python and Libraries](#Python_&_Libraries)
* * [Python](#PYTHON)
* * [Python Libraries](#PYTHON_LIBRARIES)
* * [How to Install and Use pip](#HTIAUP)
* [Networking](#Networking)
* * [IP Addresses](#IP_Addresses)
* * * [IP Addresses](#IPA)
* * * [Types of IP Traffic](#TOIT)
* * [Network Ports](#Network_Ports)
* * * [Ports](#PORTS)
* * * [Open and Closed Ports](#OACP) 
* * * [How Malicious Hackers can Abuse Ports](#HMHCAP)
* * * [Types of Protocols](#TOP)
* * * [What are Port Protocols](#WAPP)
* * * [Types of Network Communication Protocols](#TONCP)
* * [Nodes and Hosts](#Nodes_&_Hosts)
* * * [Nodes](#NODES)
* * * [Hosts](#HOSTS)
* * * [Comparison](#COMPARISON)
* * * [Examples of Both](#EOB)
* * [Network Sockets](#Network_Sockets)
* [Socket Library in Python](#Socket_Python)
* * [Socket Library Variables](#SLV)
* * [Socket Library Functions](#SLF)
* * * [Accepting Connections](#AC)
* * * [Binding Sockets to Addresses](#BSTA)
* * * [Marking Sockets as Closed](#MSAC)
* * * [Connecting to Addresses](#CTA)
* * * [Connecting to Addresses With an Error Indicator](#CTAWAEI)
* * * [Put Sockets in a 'Closed State'](#PSIACS)
* * * [Duplicate the Socket](#DTS)
* * * [Socket File Descripting](#SFD)
* * * [Get Inheritable flag of Socket](#GIFOS)
* * * [Return Remote Address of Socket](#RRAOS)
* * * [Return Socket's Own Address](#RSOA)
* * * [Return Values on Socket Options](#RVOSO)
* * * [Check if Socket is in Blocking Mode](#CISIIBM)
* * * [Return the Timeout with Socket Operations](#RTTWSO)
* * * [Limited Interface to the WSAIoctl System Interface](#LITTWSI)
* * * [Enable a server to accept connections](#EASTAC)
* * * [Return a FileObject with the Socket](#RAFWTS)
* * * [Receive Data from Sockets](#RDFS)
* * * [Receive Data from Sockets in a Pair (bytes, address)](#RDFSIAP)
* * * [Receive Normal and Ancillary Data from Socket](#RNAADFS)
* * * [Send Data to the Socket](#SDTTS)
* * * [Specialized message sending for the AF_ALG Socket](#SMSFTAS)
* * * [Send a file until EOF is reached](#SAFUEIR)
* * * [Setting Inheritable Flags](#SIF)
* * * [Set Blocking/Non-Blocking Mode](#SBNBM)
* * * [Set a Timeout on Blocking Socket Operations](#SATOBSO)
* * * [Set Values of Given Socket Options](#SVOGSO)
* * * [Shutting Down Socket Connections](#SDSC)
* * * [Duplicate Sockets and Share with a Target Process](#DSASWATP)
* [Supporting Me](#Support)
* [Resource Links](#Links)

<!-- vim-markdown-toc -->

------------------------------------------------------------------------

###### RATS
### Remote Access Trojans (RATs)?

###### WIAR
#### **{-} What is a RAT? {-}**
A RAT is a piece of malware that is made to be fundamentally hidden (like throguh the instllation of a game or an email message) in order to let an attacker get full or administrative controls of a victim.

###### HTRW

#### **{-} How the RAT Works {-}**

###### HTR
***-- Hiding the RAT --***
1. The attacker can utilize a system to join the RAT with genuine  
   executable projects so that the RAT executes out of sight while the real projects run.

   This makes the RAT almost completley hidden from the victim who runs the real application it's combined with.

   (ex: Combining my RAT with an application like Steam. Once Steam runs/installs, my RAT is activated)

   RATs can be difficult to detect because they usually don't show up in lists of running programs or tasks. 

   The actions they perform can be similar to those of legitimate programs.

   Furthermore, an intruder will often manage the level of resource use so that a drop in performance doesn't alert the user that something's amiss.

###### ATVS
***-- Accessing the Victim's System --***
2. Once a victim (the client) runs the executable records unconsciously,
   this RAT introduces itself in the framework memory. 

   (A backdoor is a means to access a computer system or encrypted data that bypasses the system's customary security mechanisms.)

###### AAU
***-- Allowing Attacker's Use --***
3. The RAT abuses the use of Backdoors to gain administrative access of the 
   victim's system. These are normally activated with the use of a payload.
   
   (In the context of a computer virus or worm, the payload is the portion of the malware which performs malicious action.)

4. At that point, they may begin to set IP port numbers and characterizing the project's 
   practices.

5. In the wake of being dispatched, the RAT can specifically speak with the attacker by 
   utilizing a predefined TCP port and get orders from them.

   This allows the attacker to send commands/instructions for the RAT to perform actions on the computer 

   (Ex: Attacker sending a command to make the computer open up google)

###### WDRAFA
#### **{-} What do RATs allow for attackers? {-}**
A RAT can do a variety of things like:
* Monitoring user behavior through keyloggers or other spyware.
* Accessing confidential information, such as credit card and social security numbers.
* Activating a system's webcam and recording video.
* Taking screenshots.
* Distributing viruses and other malware.
* Formatting drives.
* Deleting, downloading or altering files and file systems.

###### TSRP
#### {-} This Specific RAT Project {-}

This is the description on our specific RAT that we have in our code.

The RAT works with 2 different parts. 

***--- The Server ---***

**The Server Code** - The other one will control the victims computer.

**1.** The code sets the port as 80. <br>
**2.** Defines clear() as the function that clears the screen. <br>
**3.** Defines the specific socket. <br>
**4.** Gets the hostname of the attacker. <br>
**5.** Binds the hostname to the port. <br>
**6.** Starts up a TCP listener. <br>
**7.** Accepts TCP connections from the Client. <br>
**8.** Messages/Commands can now be sent from the Server to the Client with an encoding of UCF-8. <br>
**9.** If the command is 'help', print the help list. <br>
**10.** If the command is anything else, send it to the client and get the data from it. <br>

***--- The Client ---***

**The Client Code** - The malicious one, which you have to put on the victims computer 

**1.** Defines the LHOST. <br>
**2.** The code sets the port as 80 (it has to be the same as the server's port). <br>
**3.** Defines getInstructions() as the function that makes the client wait for the any of the server's commands. Specific commands can perform specific things. <br>
**4.** Defines the specific socket. <br>
**5.** Gets the hostname of the client. <br>
**6.** If the connection is false, connect to the host and port until the connection is true. <br>
**7.** If the connection doesn't work, wait 2-3 seconds and then try to connect again. <br>
**8.** Perform getInstructions(). <br>
<br>

------------------------------------------------------------------------

###### Python_&_Libraries
### Python and Libraries

###### PYTHON
#### **{-} Python {-}**
> Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.

In this case, we shall be using the version of python which is Python3.
The reason for using python3 is that (as the time of making this) it is upcomming and future of python programming. 

*The other option is python2, but because it is soon to be outdated (as the time of making this) and there is less and less support, we shall be using python3.*

###### PYTHON_LIBRARIES
#### **{-} Python Libraries {-}**
Python library is a collection of functions and methods that allows you to perform many actions without writing your code. 

To use them in python, all you need to do is:
```python
import libraryname

libraryname.function()
```

###### USING_PIP
#### **{-} Using pip {-}**
To use libraries, you first have to install them with the use of the application called "pip".

> *pip* is a package-management system used to install and manage software packages written in Python.

###### HTIAUP
#### **{-} How to Install and Use pip {-}**
To install pip you can do:
1. Download it from their site (Windows OS Users)
2. Download it from the terminal with "apt-get" or "brew" (MacOS or Linux/Unix Users)

| Operating System      | Operation             | Link/Command                         |
| --------------------- | --------------------- | ------------------------------------ |
| Windows               | Download get-pip.py   | download get-pip.py and run          |
| Mac OS                | Terminal & Brew       | `brew install pip3`                  |
| Linux (Debian/Ubuntu) | Terminal              | `apt install python3-pip`            |
| Linux (CentOS/RHEL)   | Terminal              | `yum install epel-release`           |
| Linux (Fedora)        | Terminal              | `dnf install python3`	               |
| Linux (Arch)          | Terminal              | `pacman -S python-pip`	           |
| Linux (OpenSUSE)      | Terminal              | `zypper install python3-pip`         |

To use pip, you just type in the terminal/cmd-line:
`pip install {name of package/library}`

*If you are using repl.it to program, it already installs pip packages to do stuff for you.* 
*So you don't HAVE TO follow this installation if you're only going to program on repl.it.* 
*Still though, it is recommended!*

------------------------------------------------------------------------
###### Networking
------------------------------------------------------------------------

###### IP_Addresses
### IP Addresses

###### IPA
#### **{-} IP Addresses {-}**
An IP Address is the address assigned to any system that is connected to the internet. 
This is so that computers can be able to tell who is who and where to send packets of information to. 

Think if IP Addresses like a Home Address and sending packets like Mail. 
To send mail to someone specifically, I need to send it to their address. 

###### TOIT
#### **{-} Types of IP Traffic (TCP vs UDP) {-}**
There are two types of Internet Protocol (IP) traffic. 

They are TCP or Transmission Control Protocol and UDP or User Datagram Protocol. TCP is connection oriented – once a connection is established, data can be sent bidirectional.
With TCP, packets are 

UDP is a simpler, connectionless Internet protocol.

------------------------------------------------------------------------

###### Network_Ports
### Network Ports

###### PORTS
#### **{-} Ports {-}**
At the software level, within an operating system, a port is a logical construct that identifies a specific process or a type of network service.

Ports allow a single host with a single IP address to run network services.

Ports are an integral part of the Internet's communication model, as they are the channel through which applications on the client computer can reach the software on the server. 

###### OACP
#### **{-} Open and Closed Ports {-}**

Services, such as web pages or FTP, require their respective ports to be "open" on the server in order to be publicly reachable. 

**Open Port** - a TCP or UDP port number that is configured to accept packets.

**Closed Port** - A Port which rejects connections or ignores all packets directed at it.

In order for a port to be "open", there needs to be an application (service) listening on that port, accepting the incoming packets and processing them. 

If there is no application listening on a port, incoming packets to that port will simply be rejected by the computer's operating system, which makes them "closed"

It is common security practice to close unused ports in personal computers, so as to block public access to any services which might be running on the computer without the user's knowledge, whether due to legitimate services being misconfigured, or the presence of malicious software. 

This is the reason as to why many people say you should use a Firewall, (at its most basic definition), it blocks certain connections to get in the way of outsiders trying to access open ports.

###### HMHCAP
#### **{-} How Malicious Hackers can Abuse Ports {-}**

Many Malicious Hackers abuse the use of certain protocols for ports on a network in order to gain remote access or spread malware easily.

Hackers can abuse the function of certain ports to spread any malware across devices or a network.
Some malicious software acts as a service, waiting for connections from a remote attacker in order to give him information or control over the machine. 

Hackers also scan for open ports in order to see ports that are publically reachable.

**Hackers scan for open ports in order to:**
* To run an exploit, an attacker needs a vulnerability.
* To find a vulnerability, the attacker needs to fingerprint all services which run on the machine (find out which protocol they use, which programs implement them and preferably the versions of those programs).
* To fingerprint a service, the attacker needs to know that there is one running on a publicly accessible port.
* To find out which publicly accessible ports run services, the attacker needs to run a port scan.

More information on how open-ports are used as an advantage for hackers:<br>
[watchguard.com](https://www.watchguard.com/wgrd-resource-center/security-fundamentals/what-is-a-port)

###### TOP
#### **{-} Types of Protocols {-}**

###### WAPP
***--- What are Port Protocols --***

Ports are given a specific number for their protocol (ex: 443)

Port numbers are used to determine what protocol incoming traffic should be directed to. <br>
A port number is a way to identify a specific process to which an Internet or other network message is to be forwarded when it arrives at a server.

**While protocols can vary greatly in purpose and sophistication, most specify one or more of the following properties:**

* Detection of the underlying physical connection (wired or wireless), or the existence of the other endpoint or node
* Handshaking (dynamically setting parameters of a communications channel).
* Negotiation of various connection characteristics.
* How to start and end a message.
* How to format a message.
* What to do with corrupted or improperly formatted messages (error correction).
* How to detect unexpected loss of the connection, and what to do next.
* Termination of the session and or connection.

###### TONCP
***--- Types of Network Communication Protocols --***

| Protocol | TCP/UDP | Port Number | Description | 
| -------- | ------- | ----------- | ----------- |
| ARP (Address Resolution Protocol) | <br> ARP requests are not sent using ports, they are broadcast traffic and it could not work else way, since ARP traffic is used by IP protocol to find out relationship between MAC address (data link layer) and IP address (network layer), not TCP/UDP (which is transport layer). <br> <br> | No Ports | A network layer protocol used to convert an IP address (from the link layer address) into a physical address (from a link layer address), such as an Ethernet address. For instance, it can be used for discovering MAC addresses associated with the given IPv4 Address. More information about the ARP Protocol can be found [here](https://www.tummy.com/articles/networking-basics-how-arp-works/) |
| ICMP (Internet Control Message Protocol) | The ICMP packet does not have source and destination port numbers because it was designed to communicate network-layer information between hosts and routers, not between application layer processes. | No Ports | <br> ICMP is an error-reporting protocol. Network devices like routers use to generate error messages to the source IP address when network problems prevent delivery of IP packets provides feedback that you can use for diagnostics or to report logical errors. The most common ICMP type is the ping. The designers of ICMP envisioned a protocol that would be helpful and informative. Unfortunately, hackers have a different vision; they use ICMP to send the ping of death, craft Smurf DoS packets, query the timestamp of a system or its netmask, or even send ICMP type 5 packets to redirect traffic. <br><br> |
| Telnet | TCP | 23 | <br> Telnet is a protocol that allows you to connect to remote computers (called hosts) over a TCP/IP network (such as the internet). Using telnet client software on your computer, you can make a connection to a telnet server (that is, the remote host). <br> <br> |
| DNS (Domain Name System) | TCP / UDP | 53 | <br> DNS is a protocol that assists the users by helping to link between common usernames/works to an IP address and back, e.g. instead of cramming the IP address for Google, the user can easily type [www.google.com](www.google.com) to be able to access the content from there. <br> <br>
| HTTP (Hyper Text Transfer Protocol) | TCP | 80 / 8080 | <br> HTTP was the initial protocol that were used to access web content, because of its security vulnerabilities it was replaced by HTTPS. <br> <br> |
| HTTPS (Hypertext Transfer Protocol Secure) | TCP | 443 | <br> HTTPS is the secure version of HTTP that is now commonly used to access website content. HTTPS strengthens HTTP by incorporating SSL or TLS. This protocol allow for the use of encryption. You can see when they are in use because the URL begins with HTTPS and a padlock icon appears in the status bar or browser bar in the browser window. HTTPS is the worldwide standard that is used for payment transactions and for other data-sensitive Internet transactions. <br> <br> |
| SSL (Secure Sockets Layer | TCP | 465 | <br> SSL is the standard security technology for establishing an encrypted link between a web server and a browser. This link ensures that all data passed between the web server and browsers remain private and integral. To be able to create an SSL connection a web server requires an SSL Certificate. <br> <br> |
| TLS (Transport Layer Security) | TCP | 25 / 2525 / 587 | <br> TLS (which is an updated, more secure, version of SSL) is a cryptographic protocol designed to provide communications security over a computer network. <br> <br> |
| FTP (File Transfer Protocol) | TCP | 20/21 | <br> FTP is a standard internet protocol for transmitting files between computers on the internet over TCP/IP connections. It is a client server protocol that relies on two communications channels between client and server; a command channel for controlling the conversation and a data channel for transmitting files content. Clients initiate conversations with servers by requesting to download a file. <br> <br> |
| SMTP (Simple Mail Transfer Protocol) | TCP | 25 | <br> SMTP is a protocol for sending e-mail messages between servers. Most e-mail systems that send mail over the Internet use SMTP to send messages from one server to another; the messages can then be retrieved with an e-mail client using either POP or IMAP. <br> <br> |
| SSH (Secure Socket Shell) | TCP | 22 | <br> Provides secure access to remote desktops. (Also refers to the suite of utilities that implement the protocol) <br> <br> |
| DHCP (Dynamic Host Configuration Protocol) | UDP | 67 / 68 | <br> DHCP is a protocol that is used to assist users to configure multiple network devices from a single source. This protocol is used to assist a user in configuring multiple networks. <br> <br> |

<br> <br>

**More IP Protocols (as there are MANY MORE) can be found [here](http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xml)**

<br> <br>

------------------------------------------------------------------------

###### Nodes_&_Hosts
### Nodes and Hosts

###### NODES
#### **{-} Nodes {-}**
In a network, a node is a connection point, either a redistribution point or an end point for data transmissions. 
A node is also a broader term that includes anything connected to a network or a specific processing location. 

Nodes aren't hosts, but a node has programmed or engineered capability to recognize and process or forward transmissions to other nodes.

###### HOSTS
#### **{-} Hosts {-}**
A host on the other hand is a computer connected to a computer network. 
A host may offer information resources, services, and applications to users or other nodes (connection points) on the network.

###### COMPARISON
#### **{-} Comparison {-}**
Hosts are computers whereas nodes are all devices that have network addresses assigned (IP addresses). So, a router is not a host but is a node.

###### EOB
#### **{-} Examples of Both {-}**
Examples of Hosts (all of which are connected on the network):
* A CellPhone (Not Traditional Landline Phones, which is its own topic)
* A Computer
* A Laptop
* Any Type of Computer System

Examples of Nodes:
* Modems
* Switches
* Hubs
* Bridges
* Servers
* Printers

------------------------------------------------------------------------

###### Network_Sockets
### Network Sockets

> A network socket is an internal endpoint for sending or receiving data within a node on a computer network. 

------------------------------------------------------------------------

###### Socket_Python
### Socket Library in Python

*Almost everything here can be accessed in your program after importing it with the use of*
```python
import socket

socket.{name of word/term}
```

<br>

###### SLV
#### **{-} Socket Library Variables {-}**

AF_INET refers to addresses from the internet, IP addresses specifically.

AF_INET6 is the address family for IPV6

SOCK_STREAM means that it is a TCP socket.

SOCK_DGRAM means that it is a UDP socket.

socket.family is the socket family.

socket.type is the socket type.

socket.proto

    The socket protocol.

<br>

###### SLF
#### {-} Socket Library Functions {-}

###### AC
***-- Accepting Connections --***

`socket.accept()`

> Accept a connection. 
> The socket must be bound to an address and listening for connections. 
> The return value is a pair (conn, address) where conn is a new socket object usable to 
> send and receive data on the connection, and address is the address bound to the socket 
> on the other end of the connection.

The newly created socket is non-inheritable.

    Changed in version 3.4: 
    The socket is now non-inheritable.

    Changed in version 3.5: 
    If the system call is interrupted and the signal handler does not raise an exception, the method now retries the system call instead of raising an InterruptedError exception (see PEP 475 for the rationale).

<br><br>

###### BSTA
***-- Binding Sockets to Addresses --***

`socket.bind(address)`

> Bind the socket to address. The socket must not already be bound. (The format of address depends on the address family — see above.)

<br><br>

###### MSAC
***-- Marking Sockets as Closed--***

`socket.close()`

> Mark the socket closed. 
> The underlying system resource (e.g. a file descriptor) is also closed when all file objects from makefile() are closed. 
> Once that happens, all future operations on the socket object will fail. 
> The remote end will receive no more data (after queued data is flushed).

Sockets are automatically closed when they are garbage-collected, but it is recommended to close() them explicitly, or to use a with statement around them.

    Changed in version 3.6: OSError is now raised if an error occurs when the underlying close() call is made.

:warning: Note :warning:
close() releases the resource associated with a connection but does not necessarily close the connection immediately. If you want to close the connection in a timely fashion, call shutdown() before close().

<br><br>

###### CTA
***-- Connecting to Addresses --***

`socket.connect(address)`

> Connect to a remote socket at address. 
> (The format of address depends on the address family — see above.)

If the connection is interrupted by a signal, the method waits until the connection completes, or raise a socket.timeout on timeout, if the signal handler doesn’t raise an exception and the socket is blocking or has a timeout. For non-blocking sockets, the method raises an InterruptedError exception if the connection is interrupted by a signal (or the exception raised by the signal handler).

    Changed in version 3.5: The method now waits until the connection completes instead of raising an InterruptedError exception if the connection is interrupted by a signal, the signal handler doesn’t raise an exception and the socket is blocking or has a timeout (see the PEP 475 for the rationale).
    
<br> <br>    
    
###### CTAWEI
***-- Connecting to Addresses With an Error Indicator --***

`socket.connect_ex(address)`

    Like connect(address), but return an error indicator instead of raising an exception for errors returned by the C-level connect() call (other problems, such as “host not found,” can still raise exceptions). The error indicator is 0 if the operation succeeded, otherwise the value of the error variable. This is useful to support, for example, asynchronous connects.

<br> <br>

###### PSIACS
 ***-- Put Sockets in a 'Closed State' --***

`socket.detach()`

Put the socket object into closed state without actually closing the underlying file descriptor. 
The file descriptor is returned, and can be reused for other purposes.

    New in version 3.2.

<br> <br>

###### DTS
 ***-- Duplicate the Socket --***

`socket.dup()`

Duplicate the socket.

The newly created socket is non-inheritable.

Changed in version 3.4: The socket is now non-inheritable.

<br> <br>

###### SFD
 ***-- Socket File Descripting --***

`socket.fileno()`

Return the socket’s file descriptor (a small integer), or -1 on failure. This is useful with select.select().

    Under Windows the small integer returned by this method cannot be used where a file descriptor can be used (such as os.fdopen()). Unix does not have this limitation.

<br> <br>

###### GIFOS
 ***-- Get Inheritable flag of Socket --***

`socket.get_inheritable()`

    Get the inheritable flag of the socket’s file descriptor or socket’s handle: True if the socket can be inherited in child processes, False if it cannot.

    New in version 3.4.

<br> <br>

###### RRAOS
 ***-- Return Remote Address of Socket --***

`socket.getpeername()`

Return the remote address to which the socket is connected. 
This is useful to find out the port number of a remote IPv4/v6 socket, for instance. (The format of the address returned depends on the address family — see above.) 
On some systems this function is not supported.

<br> <br>

###### RSOA
 ***-- Return Socket's Own Address --***

`socket.getsockname()`

Return the socket’s own address. This is useful to find out the port number of an IPv4/v6 socket, for instance. 

(The format of the address returned depends on the address family — see above.)

<br> <br>

###### RVOSO
 ***-- Return Values on Socket Options --***

`socket.getsockopt(level, optname[, buflen])`

Return the value of the given socket option (see the Unix man page getsockopt(2)). 
<br><br>
The needed symbolic constants (SO_* etc.) are defined in this module. <br><br>
If buflen is absent, an integer option is assumed and its integer value is returned by the function.

If buflen is present, it specifies the maximum length of the buffer used to receive the option in, and this buffer is returned as a bytes object. 

It is up to the caller to decode the contents of the buffer (see the optional built-in module struct for a way to decode C structures encoded as byte strings).

<br> <br>

###### CISIIBM
 ***-- Check if Socket is in Blocking Mode --***

`socket.getblocking()`

    Return True if socket is in blocking mode, False if in non-blocking.

    This is equivalent to checking socket.gettimeout() == 0.

    New in version 3.7.

<br> <br>

###### RTTWSO
 ***-- Return the Timeout with Socket Operations --***

`socket.gettimeout()`

Return the timeout in seconds (float) associated with socket operations, or None if no timeout is set. <br>
This reflects the last call to setblocking() or settimeout().

<br> <br>

###### LITTWSI
 ***-- Limited Interface to the WSAIoctl System Interface --***

`socket.ioctl(control, option)
    Platform:	Windows`

The ioctl() method is a limited interface to the WSAIoctl system interface. <br>
Please refer to the Win32 documentation for more information.

    On other platforms, the generic fcntl.fcntl() and fcntl.ioctl() functions 
    may be used; they accept a socket object as their first argument.

    Currently only the following control codes are supported: 
    • SIO_RCVALL
    • SIO_KEEPALIVE_VALS
    and
    • SIO_LOOPBACK_FAST_PATH.

    Changed in version 3.6: SIO_LOOPBACK_FAST_PATH was added.

<br> <br>

###### EASTAC
 ***-- Enable a server to accept connections --***

`socket.listen([backlog])`

Enable a server to accept connections. 
If backlog is specified, it must be at least 0 (if it is lower, it is set to 0); it specifies the number of unaccepted connections that the system will allow before refusing new connections. 
If not specified, a default reasonable value is chosen.

    Changed in version 3.5: The backlog parameter is now optional.

<br> <br>

###### RAFWTS
 ***-- Return a FileObject with the Socket --***

`socket.makefile(mode='r', buffering=None, *, encoding=None, errors=None, newline=None)`

Return a file object associated with the socket. The exact returned type depends on the arguments given to makefile(). These arguments are interpreted the same way as by the built-in open() function, except the only supported mode values are 'r' (default), 'w' and 'b'.

The socket must be in blocking mode; it can have a timeout, but the file object’s internal buffer may end up in an inconsistent state if a timeout occurs.

Closing the file object returned by makefile() won’t close the original socket unless all other file objects have been closed and socket.close() has been called on the socket object.

: Warning: &nbsp; Note &nbsp; : Warning:

On Windows, the file-like object created by makefile() cannot be used where a file object with a file descriptor is expected, such as the stream arguments of subprocess.
Popen().

<br> <br>

###### RDFS
 ***-- Receive Data from Sockets --***

`socket.recv(bufsize[, flags])`

Receive data from the socket. The return value is a bytes object representing the data received. The maximum amount of data to be received at once is specified by bufsize. See the Unix manual page recv(2) for the meaning of the optional argument flags; it defaults to zero.

:warning: Note :warning:

For best match with hardware and network realities, the value of bufsize should be a relatively small power of 2, for example, 4096.

    Changed in version 3.5: 
    If the system call is interrupted and the signal handler does not raise 
    an exception, the method now retries the system call instead of raising 
    an InterruptedError exception (see PEP 475 for the rationale).

<br> <br>

###### RDFSIAP
 ***-- Receive Data from Sockets in a Pair (bytes, address) --***

`socket.recvfrom(bufsize[, flags])`

    Receive data from the socket. The return value is a pair (bytes, address) where 
    bytes is a bytes object representing the data received and address is the 
    address of the socket sending the data. 
    
    See the Unix manual page recv(2) for the meaning of the optional argument 
    flags; it defaults to zero. 
    (The format of address depends on the address family — see above.)

    Changed in version 3.5: 
    If the system call is interrupted and the signal handler does not raise 
    an exception, the method now retries the system call instead of raising 
    an InterruptedError exception (see PEP 475 for the rationale).

    Changed in version 3.7: 
    For multicast IPv6 address, first item of address does not contain %scope 
    part anymore. 
    In order to get full IPv6 address use getnameinfo().

<br> <br>

###### RNAADFS
 ***-- Receive Normal and Ancillary Data from Socket --***
 
`socket.recvmsg(bufsize[, ancbufsize[, flags]])`

Receive normal data (up to bufsize bytes) and ancillary data from the socket. <br> 
The ancbufsize argument sets the size in bytes of the internal buffer used to receive the ancillary data; it defaults to 0, meaning that no ancillary data will be received.
<br><br>
Appropriate buffer sizes for ancillary data can be calculated using CMSG_SPACE() or CMSG_LEN(), and items which do not fit into the buffer might be truncated or discarded. <br>
The flags argument defaults to 0 and has the same meaning as for recv().
    
<br> <br>    

###### SDTTS
 ***-- Send Data to the Socket --***    

`socket.sendmsg(buffers[, ancdata[, flags[, address]]])`

Send normal and ancillary data to the socket, gathering the non-ancillary data from a series of buffers and concatenating it into a single message.

The buffers argument specifies the non-ancillary data as an iterable of bytes-like objects (e.g. bytes objects); the operating system may set a limit (sysconf() value SC_IOV_MAX) on the number of buffers that can be used. 

The ancdata argument specifies the ancillary data (control messages) as an iterable of zero or more tuples <br><br>
(cmsg_level, cmsg_type, cmsg_data), <br><br>
where cmsg_level and cmsg_type are integers specifying the protocol level and protocol-specific type respectively, and cmsg_data is a bytes-like object holding the associated data.

Note that some systems (in particular, systems without CMSG_SPACE()) might support sending only one control message per call. <br>
The flags argument defaults to 0 and has the same meaning as for send(). 

If address is supplied and not None, it sets a destination address for the message. The return value is the number of bytes of non-ancillary data sent.

The following function sends the list of file descriptors fds over an AF_UNIX socket, on systems which support the SCM_RIGHTS mechanism. See also recvmsg().

```python
import socket, array

def send_fds(sock, msg, fds):
    return sock.sendmsg([msg], [(socket.SOL_SOCKET, socket.SCM_RIGHTS, array.array("i", fds))])

Availability: most Unix platforms, possibly others.
```

    New in version 3.3.

    Changed in version 3.5: If the system call is interrupted and the signal handler 
    does not raise an exception, the method now retries the system call instead of 
    raising an InterruptedError exception (see PEP 475 for the rationale).

<br> <br>

###### SMSFTAS
 ***-- Specialized message sending for the AF_ALG Socket --***

`socket.sendmsg_afalg([msg, ]*, op[, iv[, assoclen[, flags]]])`

Specialized version of sendmsg() for AF_ALG socket. <br>
Set mode, IV, AEAD associated data length and flags for AF_ALG socket.

Availability: Linux >= 2.6.38.

    New in version 3.6.

<br> <br>

###### SAFUEIR
 ***-- Send a file until EOF is reached --***

`socket.sendfile(file, offset=0, count=None)`

Send a file until EOF is reached by using high-performance os.sendfile and return the total number of bytes which were sent. file must be a regular file object opened in binary mode. 

If os.sendfile is not available (e.g. Windows) or file is not a regular file send() will be used instead. offset tells from where to start reading the file. 

If specified, count is the total number of bytes to transmit as opposed to sending the file until EOF is reached. 

File position is updated on return or also in case of error in which case file.tell() can be used to figure out the number of bytes which were sent. 

The socket must be of SOCK_STREAM type. Non-blocking sockets are not supported.

    New in version 3.5.

<br> <br>

###### SIF
 ***-- Setting Inheritable Flags --***

`socket.set_inheritable(inheritable)`

 Set the inheritable flag of the socket’s file descriptor or socket’s handle.

    New in version 3.4.

<br> <br>

###### SBNBM
 ***-- Set Blocking/Non-Blocking Mode --***

`socket.setblocking(flag)`

Set blocking or non-blocking mode of the socket: if flag is false, the socket is set to non-blocking, else to blocking mode.

This method is a shorthand for certain settimeout() calls:

`sock.setblocking(True) is equivalent to sock.settimeout(None)`
`sock.setblocking(False) is equivalent to sock.settimeout(0.0)`
<br><br>

    Changed in version 3.7: 
    The method no longer applies SOCK_NONBLOCK flag on socket.type.

<br> <br>

###### SATOBSO
 ***-- Set a Timeout on Blocking Socket Operations --***

`socket.settimeout(value)`

Set a timeout on blocking socket operations. 

The value argument can be a nonnegative floating point number expressing seconds, or None. 

If a non-zero value is given, subsequent socket operations will raise a timeout exception if the timeout period value has elapsed before the operation has completed. 

If zero is given, the socket is put in non-blocking mode. <br>
If none is given, the socket is put in blocking mode.

    For further information, please consult the notes on socket timeouts.

    Changed in version 3.7: The method no longer toggles SOCK_NONBLOCK flag on socket.type.

<br> <br>

###### SVOGSO
 ***-- Set Values of Given Socket Options --***

`socket.setsockopt(level, optname, value: int)`

`socket.setsockopt(level, optname, value: buffer)`

`socket.setsockopt(level, optname, None, optlen: int)`

Set the value of the given socket option (see the Unix manual page setsockopt(2)). 

The needed symbolic constants are defined in the socket module (SO_* etc.). 

The value can be an integer, None or a bytes-like object representing a buffer.

In the later case it is up to the caller to ensure that the bytestring contains the  proper bits <br> 
(see the optional built-in module struct for a way to encode C structures as bytestrings). 
    
When value is set to None, optlen argument is required. <br>
It’s equivalent to call setsockopt C function with optval=NULL and optlen=optlen.

    Changed in version 3.5: 
    Writable bytes-like object is now accepted.

    Changed in version 3.6: 
    setsockopt(level, optname, None, optlen: int) form added.

<br> <br>

###### SDSC
 ***-- Shutting Down Socket Connections --***

`socket.shutdown(how)`

 Shut down one or both halves of the connection. <br>
 If how is SHUT_RD, further receives are disallowed. <br>
 If how is SHUT_WR, further sends are disallowed. <br>
 If how is SHUT_RDWR, further sends and receives are disallowed.

<br> <br>

###### DSASWATP
 ***-- Duplicate Sockets and Share with a Target Process --***

`socket.share(process_id)`

Duplicate a socket and prepare it for sharing with a target process. 

The target process must be provided with process_id. <br>
The resulting bytes object can then be passed to the target process using some form of interprocess communication and the socket can be recreated there using fromshare(). 

Once this method has been called, it is safe to close the socket since the operating system has already duplicated it for the target process.

    Availability: Windows.

    New in version 3.3.

Note that there are no methods read() or write(); <br>
use recv() and send() without flags argument instead.

Socket objects also have these (read-only) attributes that correspond to the values given to the socket constructor.

<br> <br>

**All Socket Objects/Functions can be found [here](https://docs.python.org/3/library/socket.html#socket-objects)**

<br>

------------------------------------------------------------------------

###### Support
### Supporting Me

***--- Want to support me? ---*** <br><br>
***1. Make a pull-request for anything you think should be improved in this markdown file.***
* **Fix any grammar for this markdown file**. There must be at least a couple of grammar mistakes or things that should be updated in here, so feel free to make a pull request for any of them. 
* **Add any images or visuals** you think I should add for this markdown file.
* **Add any improvement for descriptions** of terminologies. I am NOT a master at networking and just did a couple of searches for each terminology. Feel free to let me know or fix any problems or errors in what I said.
* **Add any structural setups** for terminologies! There has to be *some* better setups for major parts of this markdown file. (ex: You think that the description of the RAT should be after the Network Terminoligies? Why? How can I improve it? Let me know!)

***2. Make a pull-request of anything you think should be improved in the code.***
* **Fix any of my code performance**. There can be an easier way of performing my code, let me know what I should change or fix to make it perform better!
* **Fix any commenting for my code**. I know there might be easier ways to comment for parts of code than what I already put. I'd be glad to see any improvements you think should be made for them!

***3. Spread the word of this project!***
* The more people looking at this and reading through this, means the more this project can improve. I love the idea of community support and would love to see it! As they say, "The More the Merrier!"

***4. Follow my Social Media!***
* [Github](https://www.github.com/lin8x)
* [Instagram](https://www.instagram.com/lin8x/)

<br>

------------------------------------------------------------------------

###### Links
### Resource Links

These are the links to websites and guides I looked at to help me with making this project and markdown file. <br>
* [Socket Server in Python](https://docs.python.org/2/library/socketserver.html)
* [Tutorial to Python3 Networking](https://www.tutorialspoint.com/python3/python_networking.htm)
* [Tutorial to Python Networking](https://www.tutorialspoint.com/python/python_networking.htm)
* [Example of Python RAT for Powershell on Github](https://github.com/0xIslamTaha/Python-Rootkit)
* [Example of Python Rootkit on Github](https://github.com/0xIslamTaha/Python-Rootkit)
* [Nullbyte Guide to make RATs (Part 1)](https://null-byte.wonderhowto.com/how-to/program-your-own-little-rat-part-1-getting-server-working-0167490/)
* [Nullbyte Guide to make RATs (Part 2)](https://null-byte.wonderhowto.com/how-to/program-your-own-little-rat-part-2-getting-client-working-0167527/)
<br><br>

------------------------------------------------------------------------

<br> <br>