from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/sign-up")
def sign_up_page():
    return render_template('sign_up.html')
    
if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)

