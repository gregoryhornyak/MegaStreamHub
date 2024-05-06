from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("menu.html")

@app.route('/the_egg')
def the_egg():
    return render_template('the_egg.html')

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

@app.route('/feast')
def feast():
    return render_template('feast.html')

@app.route('/map')
def map_finder():
    return render_template('budapest_map.html')

@app.route('/fideszcoin')
def fideszcoin():
    return render_template('fideszcoin.html')




if __name__ == "__main__":
    app.run()


