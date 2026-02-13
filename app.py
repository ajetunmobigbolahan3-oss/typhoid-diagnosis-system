from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diagnose', methods=['POST'])
def diagnose():
    fever = int(request.form['fever'])
    abdominal_pain = int(request.form['abdominal_pain'])
    vomiting = int(request.form['vomiting'])

    score = fever + abdominal_pain + vomiting

    if score <= 2:
        level = "Mild Typhoid"
        advice = "Oral antibiotics and rest. Consult a doctor."
    elif score <= 4:
        level = "Moderate Typhoid"
        advice = "Visit hospital for proper medical supervision."
    else:
        level = "Severe Typhoid"
        advice = "EMERGENCY! Go to hospital immediately."

    return render_template('result.html', level=level, advice=advice)

if __name__ == '__main__':
    app.run(debug=True)
