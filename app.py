from flask import Flask ,render_template
app=Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contain")
def contain():
    return render_template("contain.html")

if __name__=="__main__":
    app.run(debug=True)