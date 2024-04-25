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

@app.route('/coffee')
def coffee():
    return render_template('coffee.html')

if __name__ == "__main__":
    app.run()


