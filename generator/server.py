import http.server
import socketserver
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import threading
from generator.builder import build_site

class ChangeHandler(FileSystemEventHandler):
    def __init__(self, project_name):
        self.project_name = project_name

    def on_modified(self, event):
        if event.src_path.endswith(".md") or event.src_path.endswith(".html"):
            print(f"Detected change in {event.src_path}. Rebuilding site...")
            build_site(self.project_name)

def start_server(project_name, port=8000):
    public_path = f"{project_name}/public"
    os.chdir(public_path)

    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Serving at http://localhost:{port}")
        httpd.serve_forever()

def watch_and_serve(project_name, port=8000):
    build_site(project_name)

    observer = Observer()
    handler = ChangeHandler(project_name)
    observer.schedule(handler, path=f"{project_name}/content", recursive=True)
    observer.schedule(handler, path=f"{project_name}/themes", recursive=True)

    observer.start()

    server_thread = threading.Thread(target=start_server, args=(project_name, port))
    server_thread.daemon = True
    server_thread.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
        print("\nStopping server...")

    observer.join()
