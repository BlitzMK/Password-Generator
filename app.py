from flask import Flask, render_template, request, url_for, redirect, session
from genPassword import *
app = Flask(__name__)


@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "POST":
        param = {
            "len": request.form.get("length",type=int),
            "upper": request.form.get("upperCase", type=bool),
            "spChar": request.form.get("specialChar", type=bool)
        }
        return redirect(url_for("generatedPassword", par = param))
    else:
        return render_template('index.html')

@app.route("/generatedPassword/<par>", methods = ["POST","GET"])
def generatedPassword(par):
    return render_template("generatedPassword.html", password = generatePassword(par) )

if __name__ == "__main__":
    app.run(debug=True)