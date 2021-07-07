from flask import Flask, jsonify, request
import random



app = Flask(__name__)

animals = {"pig":"oink", "cow":"moo", "sheep":"baa"}
# animal generator route here
@app.route("/getanimal")
def get_animal():
    animal = random.choice(list(animals.keys()))
    return jsonify({"data": animal})

@app.route("/getnoise", methods = ["POST"])
def get_noise():
    package = request.get_json()
    animal = package["data"]
    noise = animals[animal]
    return jsonify({"data": noise})
    

# animal noise generator route here

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)