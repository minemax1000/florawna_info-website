from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("main.html")

@app.route("/guide")
def guide():
    return render_template("guide.html")

@app.route("/map")
def map():
    return render_template("map.html")

@app.route("/story")
def map():
    return render_template("Exported Project.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
