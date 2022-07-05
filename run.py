import os
from flask import Flask, render_template
#if os.path.exists('env.py'):
#    import env


# Create an instance of Flask, and store it in a variable called "app"
app = Flask(__name__)

# This url ("/") should trigger the function that follows ("hello")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html", page_title="About")


@app.route('/contact')
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route('/careers')
def careers():
    return render_template("careers.html", page_title="Careers")


# If that is the name, then run the app with the following arguments
if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),  # Get IP if it exists, if not use default (0.0.0.0)
            port=int(os.environ.get('PORT', '5000')),
            debug=True)
