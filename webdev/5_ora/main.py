from flask import Flask,request, render_template, make_response,redirect, url_for, session
import random as r
from model import User, Pontok, db
import hashlib

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = 'Gabor'
db.create_all()

difficulties = { '0': [1,5], '1':[1,10], '2':[1,20]}
difficulties_names = {
                      '0': "Könnyű",
                      '1': "Közepes",
                      '2': "Nehéz"
                      }

def hash(str):
    return hashlib.md5(str.encode('utf-8')).hexdigest()

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/new")
def new_user():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("user-name")
    email = request.form.get("user-email")
    password = request.form.get("user-pw")
    try:
        create_user(name,password,email)
        return redirect(url_for("login"))
    except:
        return "Szerveroldali hiba történt"

@app.route("/login", methods=["POST", "GET"])
def log_user_in():
    if session.get('logged_in'):
        if session['logged_in']:
            return redirect("start")
    else:
        user = request.form.get("user-name")
        password = request.form.get("user-pw")
        check_login = check_user_login(user, password)
        if check_login is not None:
            session['logged_in'] = True
            session['userid'] = check_login.id

            return redirect('start')
    return render_template('login.html')

@app.route("/start", methods=["POST", "GET"])
def start():
    try:
        if session['logged_in'] == True:
            return render_template("index.html")
        else:
            return redirect("/")
    except:
        return redirect("/")

@app.route("/game", methods=["POST", "GET"])
def game():
    # mindegy hányat jelöl be, ha több lesz mindig a legkönnyebbel indítunk játékot.
    new_game = False
    if request.args.get('newGame') is not None:
        new_game = True

    if session.get('logged_in') == True:
        #ternary operator
        error = True if request.args.get('error') is not None else False
        difficulty = None
        try:
            difficulty = request.form.getlist('nehezseg')[0]
            session['nehezseg'] = difficulty
        except:
            if session.get('nehezseg'):
                if session['nehezseg'] != None:
                    difficulty = session['nehezseg']
            else:
                redirect(url_for('start'))

        print(difficulty)
        calc_range = difficulties[difficulty]
        actual_secret = None
        if session.get('secret_number'):
            actual_secret = session['secret_number']

        resp = make_response(render_template("game.html",
                                              error=error,
                                              nehezseg=difficulties_names[difficulty]))

        if new_game is True or actual_secret is None or difficulty != session.get('nehezseg'):
            secret_number = r.randint(calc_range[0], calc_range[1])
            session['secret_number'] = str(secret_number)
            session['difficulty'] = difficulty
        return resp
    else:
        return redirect(url_for('login'))

@app.route("/result", methods=["POST", "GET"])
def result():
   guess = None
   try:
       guess = int(request.form.get("guess_data"))
   except:
       return redirect(url_for('game', error=True))

   if session.get('tipp') is None:
       session['tipp'] = 0


   secret_number = int(session['secret_number'])
   print(session)
   if guess == secret_number:
       session['tipp'] = session['tipp'] + 1
       insert_victory(session['tipp'], session['difficulty'])

       session['tipp'] = 0

       message = f"Talált, a titkos szám valóban {guess}!"
       return render_template("result.html", msg=message, win=True)
   elif guess < secret_number:
       session['tipp'] = session['tipp'] + 1
       message = f"Sajnos a titkos szám nagyobb, mint {guess}"
       return render_template("result.html", msg=message)
   else:
       session['tipp'] = session['tipp'] + 1
       message = f"Sajnos a titkos szám ksiebb, mint {guess}"
       return render_template("result.html", msg=message)


# CRUD függvények: create, read, update, delete
def insert_victory(tippek, nehezseg):
    user = int(session['userid'])
    trans = Pontok(tippek=tippek, nehezseg=nehezseg, user=user)
    db.add(trans)
    db.commit()

def create_user(name,password, email):
    hash_pw = hash(password)
    add_user = User(name=name, email=email, password=hash_pw)
    db.add(add_user)
    db.commit()

def check_user_login(user,password):
    login = db.query(User).filter_by(name=user, password=hash(password)).first()
    return login


if __name__=='__main__':
    app.run()