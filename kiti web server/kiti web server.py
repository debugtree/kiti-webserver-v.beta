import time
import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer
import time


print("starting kiti web server")
time.sleep(1)
print("loading")
time.sleep(1)
print("loading.")
time.sleep(1)
print("loading..")
time.sleep(1)
print("loading...")
time.sleep(1)
print("loading....")


print("welcome to Kiti web server")
time.sleep(1)
print("launching web server")
time.sleep(1)

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>working</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>your web server is working.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
