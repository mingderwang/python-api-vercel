#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler,HTTPServer
from datetime import datetime
import json
import random
import api.hello as hello

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser 

try:
  #Create a web server and define the handler to manage the
  #incoming request
  server = HTTPServer(('', PORT_NUMBER), hello.handler)
  print('Started httpserver on port ' , PORT_NUMBER)

  #Wait forever for incoming htto requests
  server.serve_forever()

except KeyboardInterrupt:
  print('^C received, shutting down the web server')
  server.socket.close()

