import http.server
import socketserver
import os
import sys

PORT = 8080
DIRECTORY = os.path.dirname(__file__)

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Disable caching for metrics.json so multi-device dynamic fetches are always fresh
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

if __name__ == "__main__":
    print(f"Starting SPCX Dashboard local web server on port {PORT}...")
    print(f"Local URL: http://localhost:{PORT}")
    print(f"To expose to public web for multi-device access, use: cloudflared tunnel --url http://localhost:{PORT}")
    
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped cleanly.")
            sys.exit(0)
