from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/users")
def users():
    res = requests.get("http://user-service:8001")
    return jsonify(res.json())

@app.route("/orders")
def orders():
    res = requests.get("http://order-service:8002")
    return jsonify(res.json())

@app.route("/payments")
def payments():
    res = requests.get("http://payment-service:8003")
    return jsonify(res.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
