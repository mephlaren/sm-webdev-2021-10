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
       insert_victory(session['tipp'], session['nehezseg'])

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

@app.route('/stats')
def getStats():
    statbuilder = {}
    users = get_all_user_stats()
    #végigmegyünk az eredményen ami egy két elemü tuple: az első a user tábla adatai, a második a pontok tábláé
    for s_user in users:
        user = s_user[0]
        pont = s_user[1]
        #ha a user neve benne van a statbuilderbe, akkor hozzáfűzzük az adatait
        if user.name in statbuilder:
            statbuilder[user.name].append({'pontok':1,'tipp': pont.tippek, 'nehezseg': pont.nehezseg})
        #ha nincs benne, akkor kulcsként létrehozzuk
        else:
            statbuilder[user.name] = []
    print(statbuilder)
    stats = statBuilder(statbuilder)
    print(stats)
    return render_template("stats.html", data=stats)

#statBuilder: aggregáljuk a userek nyerési számait minden egyes nehézségen, hogy látjuk adott nehézségi szinteken hányszor nyertek
def statBuilder(stats):
    users = {}
    #létrehozzuk az usereket, mint kulcsokat
    for stat in stats:
        users[stat] = {}
    #végigmegyünk a compiled statisztikákon
    for ustat in stats:
        tmp_stat = stats[ustat]
        ret_stat = {}
        #a kiszedett useren átmegyünk
        for v in tmp_stat:
            #megkeressük a nehézségi szintjének az id-ját
            nehezseg = v['nehezseg']
            #majd a nehézségi szint friendly namejét
            nehezseg_lv = difficulties_names[nehezseg]
            #ha már szerepel ez a nehézség, akkor hozzáadunk 1-et az értékéhez
            if nehezseg_lv in ret_stat:
                ret_stat[nehezseg_lv] = ret_stat[nehezseg_lv]+1
            #ha nem létezik, létrehozzuk
            else:
                ret_stat[nehezseg_lv] = 1
        users[ustat] = ret_stat

    return users


# CRUD függvények: create, read, update, delete
def get_all_user_stats():
    stats = db.query(User, Pontok).filter(Pontok.user==User.id)
    return stats

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