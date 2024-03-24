from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import time
import logging


logger = logging.getLogger(__name__)


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello, world!")

        # Parse query string from Url
        query_obj = parse_qs(self.path[2:])
        query = ['query']

        # Send query to GPT and wait for result.

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8090):
    """
    This is the web server runnning together with Selenium
    It receive query from RequestServer, post to ChatGPT 
    and return ChatGPT response.
    """
    
    server_address = ('0.0.0.0', port)
    httpd = server_class(driver, server_address, handler_class)
    print(f"Server running on port {port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
