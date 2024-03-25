import json
import logging
from functools import partial
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

from GPTHandler import GPTHandler


logger = logging.getLogger(__name__)


class RequestServer(BaseHTTPRequestHandler):
    def __init__(self, gpt_handler: GPTHandler, *args, **kwargs):
        self.gpt_handler = gpt_handler
        # BaseHTTPRequestHandler calls do_GET **inside** __init__ !!!
        # So we have to call super().__init__ after setting attributes.
        super().__init__(*args, **kwargs)

    def do_GET(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-Type', 'text/html; charset=utf-8')

        query_obj = parse_qs(self.path[2:])
        resp = self.gpt_handler.do_query(query_obj['query'][0])
#         resp = """
# 123
# 456
# 789
# """
        resp_bytes = resp.encode('utf-8')
        self.send_header('Content-Length', len(resp_bytes))
        self.end_headers()
        self.wfile.write(resp_bytes)
        # self.wfile.write(b'123456')

    def do_POST(self):
        # self.send_response(200)
        # self.send_header('Content-type', 'text/html')
        # self.end_headers()
        # self.wfile.write(b"Hello, world!")
        self._handle_123()

    def _handle_123(self):
        req_str = self.rfile.read()
        req_obj = json.loads(req_str)
        token = req_obj.token
        query = req_obj.query
        
        # validate request
        # if token != '123':
        #     raise f'Invalid request token.'
        
        # send req to selenium bridge
        # resp = requests.get('http://localhost:8090/', {'query': 'Hello GPT'})
        # logger.debug(f'Response from GPT: {resp}')


def run(driver, server_class=HTTPServer, handler_class=RequestServer, port=8000):
    server_address = ('0.0.0.0', port)

    # Assign gpt_handler to the first argument of RequestServer constructor
    gpt_handler = GPTHandler(driver)
    handler_class = partial(handler_class, gpt_handler)
    httpd = server_class(server_address, handler_class)

    logger.debug(f"Server running on port {port}")
    httpd.serve_forever()

