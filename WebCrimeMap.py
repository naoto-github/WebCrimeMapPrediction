from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():

    template = render_template("template.html")
    
    return template

if __name__ == "__main__":
    app.run(debug=True)
