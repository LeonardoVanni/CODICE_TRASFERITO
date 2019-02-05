# Questo è il client attaccato alla presa (socket)

import socket

# create a socket (presa) object
# A pair (host, port) is used for the AF_INET address family,
# where host is a string representing either a hostname in Internet domain notation
# like 'daring.cwi.nl' or an IPv4 address like '100.50.200.5', and port is an integer
presa = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# poiché faremo girare il server su questa stessa macchina, per individuarne l'hostname
# basta individuare il nome della macchina che sta ospitando (host) questo stesso programma
PC_ospitante_server = socket.gethostname()                           

porta = 9999

# connettiamo la nostra presa ad un'altra presa remota, identificata da host e porta.
# metodo specifico da client.
presa.connect(("www.polomagona.it", 80))                               

# Receive data from the socket. The return value is a bytes object representing the data received.
# The maximum amount of data to be received at once is specified by bufsize.
# Receive no more than 1024 bytes
messaggio = presa.recv(1024)                                     

presa.close()
print (messaggio.decode('ascii'))