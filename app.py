import os
from flask import Flask, render_template, request, redirect, url_for, flash, Markup
from main import MelanJournal
import datetime
import save_text
from werkzeug.utils import secure_filename
from get_txt import fetch
import jinja2


template_dir = os.path.join(os.path.dirname(__file__), '/')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)


app = Flask(__name__)
journal = MelanJournal()
app.config['UPLOAD_FOLDER'] = "/Diary_uploads"

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

@app.route("/write", methods=["POST", "GET"])
def write():
    if request.method == "POST":
        written = request.form["write"]
        try:
            save_text.save_text(written)
            journal.turn_into_data_frame({"Date": datetime.datetime.now(), "Text": written})
            return redirect('/')
        except:
            return "There was an error."
    else:
        return render_template("write.html")


@app.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        try:
            upload = request.files["filename"]
            upload.save(os.path.join("./Diary_uploads/", secure_filename(upload.filename)))
            journal.turn_into_data_frame(fetch(upload.filename))
            return redirect('/')
        except:
            return "There was an error."
    else:
        return render_template("upload.html")


@app.route("/visualize", methods=["POST", "GET"])
def visualize():
    all_visualizations = list()
    for filename in os.listdir("visualizations"):
        all_visualizations.append("css/visualizations/" + filename)
    
    return render_template("visualize.html", all_visualizations=all_visualizations)

if __name__ == "__main__":
    app.run(debug=True)