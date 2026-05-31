from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    try:
        users = requests.get("http://api-gateway:8000/users").json()
        orders = requests.get("http://api-gateway:8000/orders").json()
        payments = requests.get("http://api-gateway:8000/payments").json()

        return f"""
        <h1>Microservices Dashboard</h1>

        <h2>User Service</h2>
        <p>{users}</p>

        <h2>Order Service</h2>
        <p>{orders}</p>

        <h2>Payment Service</h2>
        <p>{payments}</p>
        """

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
