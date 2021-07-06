from flask import Flask, jsonify, request
from random import choice


app = Flask(__name__)
animals = {"pig":"oink", "cow":"moo", "sheep":"baa"}
# animal generator route here
@app.route("/getanimal")
def get_animal():
    animal = choice(list(animals.keys()))
    print(animal)
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