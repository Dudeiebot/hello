from flask import Flask, render_template, request
#The purpose of the render_template function is to preprocess index.html such that, when we give it to the browser, it also includes the HTML it “inherits” from layout.html.

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        print("Form submitted!")
        color = request.form.get("color")
        return render_template("color.html", color=color)