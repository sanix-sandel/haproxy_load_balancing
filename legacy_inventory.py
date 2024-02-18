from flask import Flask, jsonify


app = Flask(__name__)


def healthCheck():
    print("Checking healthCheck...")
    data = {"message": "The app is healthy"}
    return jsonify(data)


@app.route("/")
def inventory():
    products = [
        {"name": "oranges", "quantity": "10"},
        {"name": "apples", "quantity": "20"}
    ]
    return jsonify(products)


@app.route("/health")
def health():
    return healthCheck()


if __name__ == "__main__":
    app.run(debug=True, port=5001, host='0.0.0.0')