import time
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler

NOME_HOST = 'esempio.net' # !!!REMEMBER TO CHANGE THIS!!!
NUMERO_PORTA = 80 # Maybe set this to 9000.


class MioGestore(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
    def do_GET(self):
        """Respond to a GET request."""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("<html><head><title>Titolo</title></head>")
        self.wfile.write("<body><p>Questo è un server Python.</p>")
        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
        self.wfile.write("<p>Hai avuto accesso al path: %self</p>" % self.path)
        self.wfile.write("</body></html>")

classe_server = HTTPServer
httpd = classe_server((NOME_HOST, NUMERO_PORTA), MioGestore)
print(time.asctime())

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()
print(time.asctime(), "Server Stops")
