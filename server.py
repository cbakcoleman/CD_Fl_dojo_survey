from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'commit often'

@app.route('/')
def home():
    return render_template("index.html", session = session)

if __name__=="__main__":
    app.run(debug=True)