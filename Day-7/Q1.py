# flask
# Question-16:
# Sharing of content 
# @app.route("/updatefortoday", methods=['GET','POST'])#http://localhost:5000/updatefortoday
# @app.route("/share", methods=['GET'])#http://localhost:5000/share
# @app.route("/clearnotepadtxt", methods=['GET'])#http://localhost:5000/clearnotepadtxt
from flask import Flask
from flask import render_template,request
import os
app = Flask(__name__)

@app.route("/")        
def index():
    return """
    <html><head>
    <title>My webserver</title>
    <style>
    .some {
        color: pink;
    }
    </style></head>
    <body>
        <h1 id="some" class="some">welcome to geetha notepad!!!</h1>
        <h1 id="some1" class="some">1)add /updatefortoday for updating the notes</h1>
        <h1 id="some1" class="some">2)add /share for seeing the notes</h1>
        <h1 id="some1" class="some">3)add /clearnotepadtxt for clearing the notes</h1>
    </body>
    </html>
    """

@app.route("/updatefortoday",methods = ["GET","POST"])  
def update_for_today():
    if request.method =='POST':
        updated_msg = request.form.get("data","")
        with open(path,"wt") as f1:
            for data in updated_msg:
                f1.writelines(data)
        return  """
        <h1>updation completed</h1>
        <a href="http://localhost:5000">home page</a>
        """
    else:
        with open(path,"rt") as f1:
            msg = f1.readlines()
        return render_template("update.html",msg=[i for i in msg])
        
        
@app.route("/share",methods = ["GET"])  
def share_notes():
    with open(path,"rt") as f1:
            msg = f1.readlines()
    return render_template("share.html",msg = [i for i in msg])


@app.route("/clearnotepadtxt",methods = ["GET"]) 
def clear_notes():
    with open(path,"rt") as f1:
        msg = [i for i in f1.readlines()]
        
    if msg: 
        with open(path,"wt") as f2:
            f2.write("")
    else:
        return """<h1><h1>Nothing to clear</h1>
                    <h1>notepad is already empty</h1>
                    <a href="http://localhost:5000">home page</a>
                   """
    return  """
        <h1>notepad is cleared</h1>
        <a href="http://localhost:5000">home page</a> 
        """

path = r"C:\Users\Geetha\handson\assignments\day7\geethanotes.txt"
app.run()
