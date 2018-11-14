# Script for quickly spinning up an SSL webserver with a self-signed cert
# Stolen from here http://pankajmalhotra.com/Simple-HTTPS-Server-In-Python-Using-Self-Signed-Certs
# 
#create cert
#openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes

#!/usr/bin/python

import BaseHTTPServer, SimpleHTTPServer
import ssl

httpd = BaseHTTPServer.HTTPServer(('localhost', 4443), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='/path/to/server.pem', server_side=True)
httpd.serve_forever()
