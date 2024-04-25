from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("menu.html")

@app.route('/barber')
def barber():
    return render_template('barber.html')

@app.route('/cosmos')
def cosmos():
    return render_template('cosmos.html')

@app.route('/sprite')
def sprite():
    return render_template('sprite.html')

@app.route('/chuchotage')
def chuchotage():
    return render_template('chuchotage.html')

@app.route('/neighbours')
def neighbours():
    return render_template('neighbours.html')

@app.route('/assassin')
def assassin():
    return render_template('assassin.html')


if __name__ == "__main__":
    app.run()


