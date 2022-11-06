from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

@app.route("/write")
def write():
    return render_template("write.html")

if __name__ == "__main__":
    app.run(debug=True)