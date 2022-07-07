import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists('env.py'):
    import env


# Create an instance of Flask, and store it in a variable called "app"
app = Flask(__name__)

# This url ("/") should trigger the function that follows ("hello")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


# Whenever we get an 'about' url with something after it, that will be passed into this view
@app.route('/about/<member_name>')
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


# Any method allowed beyond POST needs to be explicitly stated
@app.route('/contact', methods=["GET", "POST"])
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route('/careers')
def careers():
    return render_template("careers.html", page_title="Careers")


# If that is the name, then run the app with the following arguments
if __name__ == '__main__':
    # Get IP if it exists, if not use default (0.0.0.0)
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)
