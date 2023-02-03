from flask import Flask, render_template, request, url_for, redirect, session
app = Flask(__name__)


@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "POST":
        return redirect(url_for("generatedPassword", len = request.form["length"]))
    else:
        return render_template('index.html')

@app.route("/generatedPassword/<len>", methods = ["POST","GET"])
def generatedPassword(len):
    return render_template("generatedPassword.html", password = len )

if __name__ == "__main__":
    app.run(debug=True)