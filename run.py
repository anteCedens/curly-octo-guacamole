import os
from flask import Flask
if os.path.exists('env.py'):
    import env


# Create an instance of Flask, and store it in a variable called "app"
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
