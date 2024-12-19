from http.server import SimpleHTTPRequestHandler, HTTPServer
import json

class MyHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/procesar_datos':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            print(data)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Page not found.")

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open('html/index.html', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/leer_csv':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"This is the about page.")
        elif self.path == '/app':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open('html/app.html', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/categorias':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            categories_json_file = 'json/categories.json'
            self.wfile.write(open(categories_json_file, 'rb').read())
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Page not found.")

def run(server_class=HTTPServer, handler_class=MyHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()