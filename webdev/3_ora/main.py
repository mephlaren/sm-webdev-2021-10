from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def contact_form():

    if request.method == "GET":
        name = None
        email = None

        if request.cookies.get("name"):
            name = request.cookies.get("name")
        if request.cookies.get("email"):
            email = request.cookies.get("email")

        return render_template("contact.html",
                                name=name,
                                email=email)


    else:
        return "A kérést nem sikerült teljesíteni."

@app.route("/feldolgoz", methods=["POST"])
def feldolgozo():
    name = request.form.get("ugyfel_neve")
    email = request.form.get("ugyfel_email")
    msg = request.form.get("uzenet")
    response = make_response(
                render_template("success.html",
                           name=name,
                           email=email,
                           msg=msg,
                           source="feldolgozó v1.0")
                )
    response.set_cookie("name", name)
    response.set_cookie("email", email)

    return response

if __name__ == '__main__':
    app.run()

