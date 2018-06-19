import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import socket
import os
import pygame

    
def playSounds2():
    pygame.mixer.init()
    pygame.mixer.music.load("doorbell-1.wav")
    pygame.mixer.music.play()
    
    
    

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        currentTime = (time.strftime("%A %d. %B %Y  %H:%M:%S"))
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Fired and Event!')
        query = self.path
        
        if (query == "/sound1"):
            print("Doorbell Ring at: %r" % currentTime)
            #print(currentTime)
            playSounds2()
            time.sleep(2)
            playSounds2()
            time.sleep(2)
            playSounds2()
        print("Waiting")

print("Waiting at IP")
print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
