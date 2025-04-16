from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/profile/<username>')
def profile(username):
    return render_template("profile.html", username=username)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        if int(age) < 0:
            error = "Age cannot be less than 0. Please enter a valid age."
        else:
            return render_template("submit.html", name=name, age=age)
    return render_template("submit.html", error=error)

if __name__ == '__main__':
    app.run(debug=True)