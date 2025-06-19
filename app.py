from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Random correct button (or fixed for testing)
CORRECT_BUTTON = 2019
FLAG = "BNMIT_CTF{the_last_heartbeat_of_tony}"

@app.route("/")
def index():
    return render_template("index.html", correct_index=CORRECT_BUTTON)

@app.route("/jarvis_check_flag", methods=["POST"])
def fake_flag():
    data = request.get_json()
    index = data.get("index")
    return jsonify({"flag": f"BNMIT_CTF{{decoy_flag_triggered{index}}}"}), 200

# This is the real one — Unicode iota (U+03B9), not ASCII 'i'
@app.route("/jarvis_check_fιag", methods=["POST"])
def real_flag():
    data = request.get_json()
    index = data.get("index")
    if index == CORRECT_BUTTON:
        return jsonify({"flag": FLAG}), 200
    return jsonify({"flag": "ACCESS_DENIED"}), 403

@app.route("/health")
def health():
    return "OK", 200
