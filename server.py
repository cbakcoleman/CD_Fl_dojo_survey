from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'commit often'

@app.route('/')
def home():
    return render_template("index.html", session = session)

@app.route('/store', methods=['POST'])
def store():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/results')

@app.route('/results')
def show_results():
    return render_template('results.html')

if __name__=="__main__":
    app.run(debug=True)