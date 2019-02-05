# Questo è un server python attaccato ad una presa (socket)
import socket                                         

# create a socket object
# AF_INET rappresenta la scelta del protocollo TCP/IP con indirizzo ip IPv4
presa_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
PC_ospitante = socket.gethostname()                           

porta = 9999                                           

# attacca la presa sul PC_ospitante e una sua porta
presa_server.bind((PC_ospitante, porta))                                  

# mette la presa server in ascolto,
# si ammette finoa 5 errori di ascolto.
presa_server.listen(5)
print('LeoServer in ascolto sulla porta ', porta, '\n', 'PC ospitante ', PC_ospitante)                                     

while True:
   # accetta di stabilire una connessione tra la sua presa ed una presa client
   # e restituisce l'oggetto presa_client collegata ed il suo indirizzo 
   presa_client, indirizzo_client = presa_server.accept()      

   print("Ho una connessione da:  %s" % str(indirizzo_client))
    
   messaggio_risposta = 'Grazie per la tua connnessione'+ "\r\n"
   presa_client.send(messaggio_risposta.encode('ascii'))
   presa_client.close()