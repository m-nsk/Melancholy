from flask import Flask, render_template, request, redirect
import save_text

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

@app.route("/write", methods=["POST", "GET"])
def write():
    if request.method == "POST":
        written = request.form["write"]
        try:
            save_text.save_text(written)
            return redirect('/')
        except:
            return "There was an error."
    else:
        return render_template("write.html")

@app.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        upload = request.form["upload"]
        try:
            return redirect('/')
        except:
            return "There was an error."
    else:
        return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)