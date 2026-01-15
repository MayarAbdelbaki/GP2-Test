"""
Message Receiver for AIot Autocar Prime
Receives messages from PC and displays them in terminal.
Run this alongside face_capture.py
"""

import http.server
import socketserver
import json
import threading
from datetime import datetime

# Configuration
MESSAGE_PORT = 5001
HOST = "0.0.0.0"  # Listen on all interfaces


class MessageHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP request handler for receiving messages."""
    
    def do_POST(self):
        """Handle POST requests with messages."""
        if self.path == '/message':
            try:
                # Read request data
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                
                # Parse JSON
                data = json.loads(post_data.decode('utf-8'))
                message = data.get('message', '')
                timestamp = data.get('timestamp', '')
                source = data.get('source', 'PC')
                
                # Display message in terminal
                if timestamp:
                    try:
                        dt = datetime.fromtimestamp(timestamp)
                        time_str = dt.strftime('%Y-%m-%d %H:%M:%S')
                    except:
                        time_str = str(timestamp)
                else:
                    time_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                
                # Print message (this will appear in terminal)
                print(f"\n[{time_str}] Message from {source}:")
                print(f"  {message}\n")
                
                # Send success response
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {'status': 'success', 'message': 'Message received'}
                self.wfile.write(json.dumps(response).encode('utf-8'))
                
            except Exception as e:
                print(f"✗ Error processing message: {str(e)}")
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {'status': 'error', 'message': str(e)}
                self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_GET(self):
        """Handle GET requests (health check)."""
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {'status': 'healthy', 'service': 'Message Receiver'}
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
    
    def log_message(self, format, *args):
        """Override to reduce log noise."""
        # Only log errors, not every request
        if args[0].startswith('"GET') or args[0].startswith('"POST'):
            return  # Don't log normal requests
        super().log_message(format, *args)


def start_message_receiver():
    """Start the message receiver server in a separate thread."""
    try:
        with socketserver.TCPServer((HOST, MESSAGE_PORT), MessageHandler) as httpd:
            print(f"Message receiver started on port {MESSAGE_PORT}")
            print(f"Waiting for messages from PC...")
            httpd.serve_forever()
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"✗ Port {MESSAGE_PORT} is already in use")
            print(f"  Another instance might be running, or port is occupied")
        else:
            print(f"✗ Error starting message receiver: {str(e)}")
    except KeyboardInterrupt:
        print("\nMessage receiver stopped")


def run_in_background():
    """Run message receiver in background thread."""
    thread = threading.Thread(target=start_message_receiver, daemon=True)
    thread.start()
    return thread


if __name__ == '__main__':
    print("=" * 60)
    print("AIot Autocar Message Receiver")
    print("=" * 60)
    print(f"Listening on {HOST}:{MESSAGE_PORT}")
    print("Messages from PC will be displayed here")
    print("=" * 60)
    print("\nPress Ctrl+C to stop\n")
    
    start_message_receiver()
