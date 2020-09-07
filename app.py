from flask import Flask ,render_template
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return '''<h3> about </h3> '''

@app.route("/contain")
def contain():
    return '''<h3> contain </h3> '''

if __name__=="__main__":
    app.run(debug=True)