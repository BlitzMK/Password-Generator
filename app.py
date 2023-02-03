from flask import Flask, render_template, request, url_for, redirect, session
from genPassword import *
app = Flask(__name__)


@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "POST":
        param = {
            "len": request.form["length"],
            "upper": request.form.get('uppercase'),
            "spChar": request.form.get('specialChar')
        }
        return redirect(url_for("generatedPassword", par = param))
    else:
        return render_template('index.html')

@app.route("/generatedPassword/<par>", methods = ["POST","GET"])
def generatedPassword(par):
    return render_template("generatedPassword.html", password = generatePassword(par) )

if __name__ == "__main__":
    app.run(debug=True)