from flask import Flask
app = Flask(__name__)

# The main flask app

@app.route("/")
def hello():
    return "<h1 style='color:green'>Hello There!</h1>"

if __name__ == "__main__":
    # app.run(host='0.0.0.0')

    # Dev server
    app.run(host='0.0.0.0', debug=True)
