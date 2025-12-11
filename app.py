from flask import Flask, render_template, send_file, redirect, request
import json
app = Flask(__name__)

from dotenv import load_dotenv
import os

load_dotenv()

BASE_PATH = os.getenv("BASE_PATH")
DATA_PATH = os.getenv("DATA_PATH")

def redi_parse(text: str):
    split_text = text.split()
    if len(split_text) >= 2 and split_text[0] == "$redi":
        return split_text[1]
    return None

def is_it_true(value):
    return value.lower() == 'true'

def safe_redirect(url):
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    return redirect(url)

@app.route("/<just_url>")
@app.route("/")
def root(just_url=None):
    with open(DATA_PATH, "r") as file: # read data
        data = json.loads(file.read())
    
    if not just_url:
        return render_template("index.html") # defalt

    if just_url not in data:
        return render_template("file_not_found.html"), 404 # not found

    file_path = f"{BASE_PATH}{data[just_url]['path']}"
    
    with open(file_path, "r") as file: # read file
        parse_result = redi_parse(file.read())
        if parse_result:
            return safe_redirect(parse_result) # redirect
        
    is_download = request.args.get('download', default="true", type=str)

    return send_file(file_path, as_attachment=is_it_true(is_download)) # send file