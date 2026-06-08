#!/usr/bin/env python3
"""fleet-midi-voicing — HTTP server on :2162

Roles: note, velocity
Port: 2162
"""

import json
import http.server
import sys

PORT = 2162
AGENT = "fleet-midi-voicing"

class AgentHandler(http.server.BaseHTTPRequestHandler):
    def _json(self, code, data):
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        if self.path in ("/", "/health", "/agent"):
            self._json(200, {"status": "ok", "agent": AGENT, "port": PORT, "roles": ["note", "velocity"]})

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)
        data = json.loads(body) if body else {}

        if data.get("type") == "probe":
            self._json(200, {"status": "ok", "agent": AGENT})
            return

        result = self._analyze(data)
        self._json(200, result)

    def _analyze(self, data):
        """Override in subclass for per-agent analysis."""
        return {"status": "ok", "agent": AGENT, "ternary_vector": [0,0,0], "ternary_invariant": 0, "closed_gesture": True}

    def log_message(self, fmt, *args):
        if "probe" in str(args) or "health" in str(args): return
        print(f"  [{AGENT}] {fmt}".format(*args))

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else PORT
    server = http.server.HTTPServer(("0.0.0.0", port), AgentHandler)
    print(f"{AGENT} on :{port}")
    server.serve_forever()