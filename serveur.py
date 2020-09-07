from flask import Flask
app=Flask(__name__)

@app.route("/")
def home():
    return "bonjour"

@app.route("/about")
def about():
    return ''' <h1> ABOUT </h1> '''

@app.route("/contain")
def contain():
    return ''' <h1> CONTAIN </h1> '''


if __name__== "__main__":
    app.run(debug=True)