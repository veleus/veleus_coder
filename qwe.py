from flask import Flask
from flask import render_template


app=Flask(__name__)


@app.route("/home")
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/admin/<string:name>/<int:id>")
def about(name,id):
    return "Hello admin " +name+"/"+ str(id)

if __name__ == "__main__":
    app.run(debug=True)