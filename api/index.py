from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        message = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>AI Career Guidance</title>
            <meta charset="utf-8">
            <style>
                body {
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
                    max-width: 800px;
                    margin: 50px auto;
                    padding: 20px;
                    background-color: #F7F6F3;
                    color: #2E2E2E;
                }
                h1 {
                    color: #5B6C8F;
                }
                .info {
                    background-color: #E8DFD8;
                    padding: 20px;
                    border-radius: 12px;
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <h1>🎓 AI Career Guidance Platform</h1>
            <div class="info">
                <p>This is a Streamlit application for AI-powered career guidance.</p>
                <p><strong>Note:</strong> Streamlit applications require a persistent WebSocket connection and are best deployed on platforms like:</p>
                <ul>
                    <li>Streamlit Cloud (recommended)</li>
                    <li>Heroku</li>
                    <li>AWS EC2</li>
                    <li>Google Cloud Run</li>
                </ul>
                <p>For local development, run: <code>streamlit run main.py</code></p>
            </div>
        </body>
        </html>
        """
        
        self.wfile.write(message.encode())
        return
