from flask import Flask, render_template
import requests
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URI")
app.config['SECRET_KEY'] = getenv("SECRET_KEY")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

api = "http://api:5000"

class animals(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(50))

db.create_all()
#home route here
#must query the animal API for an animal and a noise – the noise should be based on the animal
@app.route("/")
def home():
    animal = requests.get(api + "/getanimal")
    print(animal.json()['data'])
    noise = requests.post(api + "/getnoise", json = animal.json())
    text = f"The {animal.json()['data']} goes {noise.json()['data']}"
    previous = animals.query.order_by(animals.id.desc()).limit(5).all()
    new = animals(text = text)
    db.session.add(new)
    db.session.commit()
    return render_template("index.html", text = text, previous = previous)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)