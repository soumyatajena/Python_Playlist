from flask import Flask, render_template

app = Flask(__name__)
print(__name__) # __main__   -> name of the app
@app.route("/") # decorator
def hello():
    return "<p>Hello, Soumyata!</p>"

@app.route("/renderHtml") 
def renderHtml():
    return render_template('index.html')

# @app.route("/favicon.ico") 
# def favicon():
#     return render_template('index.html')