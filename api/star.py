from http.server import BaseHTTPRequestHandler
from datetime import datetime
import json
import random
import uuid
import time

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    result = json.dumps(
        {
            "id": str(uuid.uuid4()),
            "選號日期": time.strftime("%m/%d/%Y", time.localtime()) ,
            "可能中獎號碼": random.sample(range(10),3),
            "猜中機率": 0
        }, ensure_ascii=False)
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    self.wfile.write(result.encode(encoding='utf_8'))
    return
