from flask import Flask, render_template, send_file, redirect, request
import json
app = Flask(__name__)

from dotenv import load_dotenv
import os

load_dotenv()

BASE_PATH = os.getenv("BASE_PATH")
DATA_PATH = os.getenv("DATA_PATH")


data = {

}
with open(DATA_PATH, "r") as file: # read data
    data = json.loads(file.read())

latest_mtime = os.path.getmtime(DATA_PATH)


def is_it_true(value):
    return value.lower() == 'true'

def safe_redirect(url):
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    return redirect(url)

def cache_data():
    global latest_mtime, data

    try:
        mtime = os.path.getmtime(DATA_PATH)
    except FileNotFoundError:
        return

    if latest_mtime != mtime:
        with open(DATA_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
        latest_mtime = mtime


@app.route("/<just_url>")
@app.route("/")
def root(just_url=None):
    cache_data()

    if not just_url:
        return render_template("main.html") # defalt

    if just_url not in data:
        return render_template("file_not_found.html"), 404 # not found

    if "redirect" in data[just_url]:
        return safe_redirect(data[just_url]["redirect"])

    file_path = f"{BASE_PATH}{data[just_url]['path']}"

    is_download = request.args.get('download', default="true", type=str)

    return send_file(file_path, as_attachment=is_it_true(is_download)) # send file

@app.route("/index")
def index():
    cache_data()
    return render_template("index.html", data=data)
