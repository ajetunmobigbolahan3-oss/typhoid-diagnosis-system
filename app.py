from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diagnose', methods=['POST'])
def diagnose():
    fever = request.form.get('fever')
    abdominal_pain = request.form.get('abdominal_pain')
    bleeding = request.form.get('bleeding')

    if bleeding == "yes":
        level = "Severe Typhoid"
        treatment = "Hospital admission, IV antibiotics (e.g. Ceftriaxone)."
    elif abdominal_pain == "yes":
        level = "Moderate Typhoid"
        treatment = "Oral antibiotics, hydration, medical supervision."
    else:
        level = "Mild Typhoid"
        treatment = "Early antibiotics, rest, fluids."

    return render_template('result.html', level=level, treatment=treatment)

if __name__ == '__main__':
    app.run(debug=True)
