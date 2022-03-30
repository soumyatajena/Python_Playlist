from flask import Flask

app = Flask(__name__)
print(__name__) # __main__   -> name of the app
@app.route("/") # decorator
def hello_world():
    return "<p>Hello, Soumyata!</p>"