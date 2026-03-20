from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

def generate_password(length, upper, lower, numbers, symbols):
    chars = ""
    password = []

    if upper:
        chars += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))
    if lower:
        chars += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))
    if numbers:
        chars += string.digits
        password.append(random.choice(string.digits))
    if symbols:
        chars += string.punctuation
        password.append(random.choice(string.punctuation))

    if not chars:
        return ""

    while len(password) < length:
        password.append(random.choice(chars))

    random.shuffle(password)
    return ''.join(password)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()

    password = generate_password(
        int(data.get("length", 12)),
        data.get("upper", True),
        data.get("lower", True),
        data.get("numbers", True),
        data.get("symbols", False)
    )

    return jsonify({"password": password})

if __name__ == "__main__":
    app.run(debug=True)