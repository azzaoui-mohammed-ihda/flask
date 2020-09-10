from flask import Flask ,render_template, request
import datetime

app=Flask(__name__)
burger=[
    {
        "nom":"cheese burger",
        "prix":"200 DH",
        "image":"1.jpeg"
    },
    {
        "nom":"chicken burger",
        "prix":"298 DH",
        "image":"2.jpeg"
    },
    {
        "nom":"meal burger",
        "prix":"390 DH",
        "image":"3.jpeg"
    },
    {
        "nom":"hamburger",
        "prix":"25DH",
        "image":"4.jpeg"
    },
    {
        "nom":"cheese burger",
        "prix":"200 DH",
        "image":"1.jpeg"
    },
    {
        "nom":"cheese burger",
        "prix":"200 DH",
        "image":"2.jpeg"
    },
    {
        "nom":"cheese burger",
        "prix":"200 DH",
        "image":"3.jpeg"
    },
    {
        "nom":"cheese burger",
        "prix":"200 DH",
        "image":"2.jpeg"
    }
]
Message=[]
@app.route("/home")
@app.route("/")
def home():
    date=datetime.datetime.now().date()
    return render_template("index.html",today=date,title="Home",burgers=burger)

@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method=="POST":  
        nom=request.form.get("nom")
        email=request.form.get("email")
        mssg=request.form.get("message")
        messag={"nom":nom,"email":email,"message":mssg}
        Message.append(messag)
        print(Message)
    return render_template("contact.html",title="Contact")

if __name__=="__main__":
    app.run(debug=True)