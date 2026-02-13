from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"

# List of symptoms for Yes/No questions
SYMPTOMS = [
    "Fever",
    "Headache",
    "Abdominal Pain",
    "Diarrhea",
    "Constipation",
    "Rash"
]

# Symptom weights for scoring
SYMPTOM_WEIGHTS = {
    "Fever": 3,
    "Headache": 2,
    "Abdominal Pain": 3,
    "Diarrhea": 2,
    "Constipation": 2,
    "Rash": 1
}

# Function to diagnose severity and treatment
def diagnose_typhoid(responses):
    total_score = sum(SYMPTOM_WEIGHTS[sym] for sym, val in responses.items() if val == "Yes")
    max_score = sum(SYMPTOM_WEIGHTS.values())
    probability = (total_score / max_score) * 100

    if probability < 40:
        severity = "Mild"
        treatment = (
            "Oral Ciprofloxacin 500mg twice daily for 7-10 days or "
            "Azithromycin 500mg once daily for 5-7 days. Hydration, rest, and nutrition advised."
        )
    elif probability < 70:
        severity = "Moderate"
        treatment = (
            "Oral Ciprofloxacin 500-750mg twice daily or IV Ceftriaxone 1-2g daily for 10-14 days. "
            "Monitor symptoms and consult a healthcare provider regularly."
        )
    else:
        severity = "Severe"
        treatment = (
            "Hospitalization required. IV Ceftriaxone 2g once daily or IV Azithromycin 500mg once daily "
            "for 10-14 days. Monitor for complications such as intestinal perforation or sepsis."
        )

    return probability, severity, treatment

# Start page
@app.route("/")
def index():
    session.clear()
    return render_template("index.html")

# Symptom questions
@app.route("/symptom", methods=["GET", "POST"])
def symptom():
    if request.method == "POST":
        responses = {sym: request.form.get(sym) for sym in SYMPTOMS}
        session['responses'] = responses
        return redirect(url_for("result"))
    return render_template("symptom.html", symptoms=SYMPTOMS)

# Result page
@app.route("/result")
def result():
    responses = session.get('responses', {})
    probability, severity, treatment = diagnose_typhoid(responses)
    return render_template(
        "result.html",
        responses=responses,
        probability=probability,
        severity=severity,
        treatment=treatment
    )

if __name__ == "__main__":
    app.run(debug=True)
