from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route('/')
def hello():
    hostname = socket.gethostname()
    return f"""
    <html>
        <body>
            <h1>Hello from Krishna!</h1>
            <p><strong>Container ID:</strong> {hostname}</p>
            <p><strong>Service:</strong> Web App</p>
            <p><strong>Replica:</strong> {os.environ.get('HOSTNAME', 'unknown')}</p>
        </body>
    </html>
    """

@app.route('/health')
def health():
    return {'status': 'healthy', 'service': 'web-app'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)