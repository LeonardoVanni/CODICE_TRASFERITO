import http.server
import socketserver
 
PORT = 3333
GestoreRichieste = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), GestoreRichieste)
print("In ascolto sulla porta", PORT)
httpd.serve_forever()