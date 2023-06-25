## TCP SYN Flood dos attack with python3
### Description
this script was made for the computer networking class n°1 as part of the final project for the course, which consisted in trying to take the university website out of service using a SYN flood attack.
### State
:ballot_box_with_check:finished:ballot_box_with_check:
### Requirements
- threading
- IP, TCP from scapy.layers.inet
- randint from random
- send from scapy.sendrecv
### How to use
- clone the repository
- write the target ip and the target port, please make sure the port is for tcp use, I recommend port 80 or 443.
- run: python3 script.py <Number of process> on the project folder (terminal)
- you can use wiresharsk to check the traffic
- To stop the attack just close the terminal.
### Contributors
- :beginner:Vicente Moya
- :floppy_disk:Ignacio González
