from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length, options):
    selected = []
    all_chars = ""

    if options.get("uppercase"):
        selected.append(random.choice(string.ascii_uppercase))
        all_chars += string.ascii_uppercase

    if options.get("lowercase"):
        selected.append(random.choice(string.ascii_lowercase))
        all_chars += string.ascii_lowercase

    if options.get("numbers"):
        selected.append(random.choice(string.digits))
        all_chars += string.digits

    if options.get("symbols"):
        selected.append(random.choice(string.punctuation))
        all_chars += string.punctuation

    if not all_chars:
        return "Select at least one option"

    if length < len(selected):
        return "Length too short for selected options"

    remaining = length - len(selected)
    selected += random.choices(all_chars, k=remaining)
    random.shuffle(selected)

    return "".join(selected)

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    length = ""
    options = {}

    if request.method == "POST":
        length = int(request.form["length"])
        options = {
            "uppercase": request.form.get("uppercase"),
            "lowercase": request.form.get("lowercase"),
            "numbers": request.form.get("numbers"),
            "symbols": request.form.get("symbols"),
        }
        password = generate_password(length, options)

    return render_template(
        "index.html",
        password=password,
        length=length,
        options=options
    )

if __name__ == "__main__":
    app.run(debug=True)
