from http.server import BaseHTTPRequestHandler
from datetime import datetime
import json
import random

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    json_str=json.dumps({"可能中獎號碼": random.sample(range(10),3)}, ensure_ascii=False)
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    self.wfile.write(json_str.encode(encoding='utf_8'))
    return
