from flask import Flask, jsonify, request


app = Flask(__name__)


def healthCheck():
    print("Checking healthCheck...")
    data = {"message": "The app is healthy"}
    return jsonify(data)



@app.route("/")
def inventory():
    print("Modern Inventory... ")
    products = [
        {"name": "oranges", "quantity": 10, "unit_price": 30, "available": True},
        {"name": "apples", "quantity": 20, "unit_price": 50, "available": False}
    ]
    return jsonify(products)

@app.route("/health")
def health():
    return healthCheck()


if __name__ == "__main__":
    app.run(debug=True, port=5003, host='0.0.0.0')