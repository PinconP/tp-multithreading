#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer

from src.manager import QueueClient


class Proxy(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.client = QueueClient()
        super().__init__(*args, **kwargs)

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        t = self.client.tasks.get()
        self.wfile.write(bytes(t.to_json(), "utf-8"))


def run(server_class=HTTPServer, handler_class=Proxy):
    server_address = ("127.0.0.1", 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
