from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.secret_key="shshshs"

@app.route('/')
def index():
    if "contador" not in session:
        session["contador"] = 0
    else:
        session['contador'] += 1
    return render_template("index.html")

@app.route('/delete')
def delete():
    session.clear()
    return redirect('/')


@app.route('/2')
def clicks():
    if "contador" not in session:
        session["contador"] = 0
    else:
        session['contador'] += 2
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)