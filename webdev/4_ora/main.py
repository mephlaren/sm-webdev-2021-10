from flask import Flask, request,render_template, make_response
import random as r
from model import User,Secret, db


app = Flask(__name__)
min = 1
max = 30

db.create_all()

@app.route("/")
def index():
    sn = request.cookies.get("secret_number")
    response = make_response(render_template("index.html", min=min, max=max))
    if not sn:
        secret = r.randint(min,max)
        response.set_cookie("secret_number", str(secret))

    return response


@app.route("/result", methods=["POST"])
def result():
    guess = 0#int(request.form.get("gtsn_tipp"))
    try:
        guess = int(request.form.get("gtsn_tipp"))
    except:
        return "Kérlek, számot adj meg."
    name = request.form.get("gtsn_name")
    sn = int(request.cookies.get("secret_number"))

    if guess == sn:
        save_user_data(name, guess)
        message = "Eltaláltad!"
        response = make_response(render_template("result.html", message = message))
        response.set_cookie("secret_number", str(r.randint(min,max)))
        return response
    elif guess < sn:
        save_user_data(name, guess)
        message = "Ennél nagyobb számra gondoltam."
        return render_template("result.html", message=message)
    else:
        save_user_data(name,guess)
        message = "Ennél kisebb számra gondoltam."
        return render_template("result.html", message=message)

def save_user_data(name,guess):
    trans = User(name=name, guess=guess)
    db.add(trans)
    db.commit()

if __name__=="__main__":
    app.run()