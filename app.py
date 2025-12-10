from flask import Flask, render_template, send_file, redirect
import json
app = Flask(__name__)

BASE_PATH = "/home/sinokadev/noka.moe/files/"

def redi_parse(text: str):
    split_text = text.split()
    if split_text[0] == "$redi":
        return split_text[1]
    else: return None

@app.route("/<just_url>")
@app.route("/")
def root(just_url=None):
    with open("data.json", "r") as file: # read data
        data = json.loads(file.read())
    
    if not just_url:
        return render_template("index.html") # defalt
    
    file_path = f"{BASE_PATH}{data[just_url]["path"]}"

    if just_url not in data:
        return render_template("file_not_found.html"), 404 # not found

    file_path = f"{BASE_PATH}{data[just_url]['path']}"
    
    with open(file_path, "r") as file: # read file
        parse_result = redi_parse(file.read())
        if parse_result:
            return redirect(parse_result) # redirect
    
    return send_file(file_path) # send file