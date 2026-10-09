from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class TaskManagerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/health":
            response = {"status": "healthy"}
        else:
            response = {
                "application": "Task Manager",
                "message": "Welcome to our DevOps assessment project",
                "tasks": [
                    {"id": 1, "title": "Learn Docker"},
                    {"id": 2, "title": "Learn Kubernetes"},
                    {"id": 3, "title": "Build a CI/CD pipeline"}
                ]
            }

        body = json.dumps(response).encode()

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()

        self.wfile.write(body)


server = HTTPServer(("0.0.0.0", 8000), TaskManagerHandler)

print("Task Manager running on port 8000", flush=True)

server.serve_forever()
