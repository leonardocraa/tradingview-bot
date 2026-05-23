from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("SIGNAL RECEIVED:", data)
    return "OK", 200
