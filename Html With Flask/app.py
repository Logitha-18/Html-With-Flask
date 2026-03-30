from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple in-memory "database"
users = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        age = request.form['age']
        email = request.form['email']

        if email in users:
            return "User already exists! Try login."

        users[email] = {
            "name": name,
            "password": password,
            "age": age
        }

        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email in users and users[email]['password'] == password:
            return render_template('welcome.html', user=users[email])
        else:
            return "Invalid email or password!"

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)