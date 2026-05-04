import os
from flask import Flask, render_template, request

app = Flask(__name__)

# (هەمان function ـەکانت بمێنن)

@app.route("/", methods=["GET", "POST"])
def index():
    results = {}

    if request.method == "POST":
        c = float(request.form["c"])
        gamma = float(request.form["gamma"])
        Df = float(request.form["Df"])
        B = float(request.form["B"])
        Nc = float(request.form["Nc"])
        Nq = float(request.form["Nq"])
        Ngamma = float(request.form["Ngamma"])

        results["Terzaghi"] = c*Nc + gamma*Df*Nq + 0.5*gamma*B*Ngamma
        results["Meyerhof"] = results["Terzaghi"]
        results["Hansen"] = results["Terzaghi"]
        results["Vesic"] = results["Terzaghi"]

    return render_template("index.html", results=results)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)