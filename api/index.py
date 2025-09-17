from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response = {
            'message': 'Crypto ML API - Serverless Functions',
            'status': 'active',
            'version': '2.0',
            'platform': 'Vercel Serverless Functions',
            'endpoints': {
                '/api/health': 'Health check',
                '/api/predict/bitcoin': 'Get Bitcoin prediction', 
                '/api/predict/ethereum': 'Get Ethereum prediction',
                '/api/predict/cardano': 'Get Cardano prediction',
                '/api/train/bitcoin': 'Train Bitcoin model (POST)',
                '/api/model_info': 'Get model information'
            },
            'timestamp': datetime.now().isoformat()
        }
        
        self.wfile.write(json.dumps(response).encode())