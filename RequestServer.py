from http.server import HTTPServer, BaseHTTPRequestHandler
import json

import requests


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # self.send_response(200)
        # self.send_header('Content-type', 'text/html')
        # self.end_headers()
        # self.wfile.write(b"Hello, world!")
        self._handle()

    def _handle(self):
        # reqstr = self.rfile.read()
        # reqobj = json.loads(reqstr)
        # token = reqobj.token
        # query = reqobj.query
        
        # validate request
        # if token != '123':
        #     raise f'Invalid request token.'
        
        # send req to selenium bridge
        resp = requests.get('http://localhost:8090/', {'query': 'Hello GPT'})
        print(f'Response from GPT: {resp}')


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('0.0.0.0', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
