from flask import Flask, request, jsonify
import requests
from data.data import products

app = Flask(__name__)


def get_data(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    print("Fetching URL:", url)

    try:
        headers = {
            "User-Agent": "Inventory-App/1.0 (student project)"
        }

        response = requests.get(url, headers=headers)
        print("Status Code:", response.status_code)

        if response.status_code != 200:
            print("Bad response:", response.text)
            return None

        data = response.json()
        print("Response Data:", data)

        if data.get("status") != 1:
            return None

        return {
            "code": barcode,
            "name": data["product"].get("product_name"),
            "brand": data["product"].get("brands"),
        }

    except Exception as e:
        print("ERROR:", e)
        return None

# GET ALL PRODUCTS
@app.route("/inventory", methods=["GET"])
def get_items():
    return jsonify(products)


# ADD PRODUCT
@app.route("/inventory", methods=["POST"])
def add_item():
    data = request.json
    code = data.get("code")

    if code in [p["code"] for p in products]:
        return jsonify({"error": "Product already exists"}), 400

    product = get_data(code)

    if not product:
        return jsonify({"error": "Invalid product"}), 400

    products.append(product)
    return jsonify(product), 201


# GET SINGLE PRODUCT
@app.route("/inventory/<code>", methods=["GET"])
def get_item(code):
    for p in products:
        if p["code"] == code:
            return jsonify(p)

    return jsonify({"error": "Product not found"}), 404


# UPDATE PRODUCT
@app.route("/inventory/<code>", methods=["PATCH"])
def update_item(code):
    data = request.json

    for p in products:
        if p["code"] == code:
            p.update(data)
            return jsonify(p)

    return jsonify({"error": "Product not found"}), 404


# DELETE PRODUCT
@app.route("/inventory/<code>", methods=["DELETE"])
def delete_item(code):
    for p in products:
        if p["code"] == code:
            products.remove(p)
            return jsonify({"message": "Product deleted"})

    return jsonify({"error": "Product not found"}), 404


if __name__ == "__main__":
    app.run(port=5555, debug=True)