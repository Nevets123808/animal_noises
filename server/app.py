from flask import Flask
import requests

app = Flask(__name__)
api = "http://api:5000"

# home route here
# must query the animal API for an animal and a noise – the noise should be based on the animal
@app.route("/")
def home():
    animal = requests.get(api + "/getanimal")
    
    noise = requests.post(api + "/getnoise", json = animal.json())
    return f"The {animal.json()['data']} goes {noise.json()['data']}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)