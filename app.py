from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json(silent=True)

        if data is None:
            data = request.data.decode("utf-8")

        print("SIGNAL RECEIVED:", data)

        return "OK", 200

    except Exception as e:
        print("ERROR:", e)
        return "ERROR", 400
