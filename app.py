from flask import Flask, render_template, request, url_for, redirect, session
app = Flask(__name__)


@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "POST":
        return redirect(url_for("generatedPassword", nam = request.form["nm"]))
    else:
        return render_template('index.html')

@app.route("/generatedPassword/<nam>", methods = ["POST","GET"])
def generatedPassword(nam):
    return render_template("generatedPassword.html", password = nam )

if __name__ == "__main__":
    app.run(debug=True)