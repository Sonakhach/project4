from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Retrieve cookies from the 'Cookie' header
        cookie_header = self.headers.get('Cookie')
        if cookie_header:
            # Log the cookies to a file
            with open('cookies.txt', 'a') as file:
                file.write(f"Cookies from {self.client_address[0]}:{self.client_address[1]} - {cookie_header}\n")
            print(f"Logged cookies: {cookie_header}")
        else:
            print("No cookies found in the request.")

        # Send a simple response
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Cookie received and logged.")

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if name == 'main':
    run()
