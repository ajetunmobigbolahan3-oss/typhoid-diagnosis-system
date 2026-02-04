from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def diagnose():
    if request.method == "POST":
        score = 0

        if request.form.get("fever") == "yes":
            score += 3
        if request.form.get("headache") == "yes":
            score += 2
        if request.form.get("abdominal_pain") == "yes":
            score += 2
        if request.form.get("diarrhea") == "yes":
            score += 2

        if score >= 6:
            result = "Probable Typhoid Fever"
        else:
            result = "Typhoid unlikely"

        return render_template("result.html", result=result)

    return render_template("diagnosis.html")

if __name__ == "__main__":
    app.run()
