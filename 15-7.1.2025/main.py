from flask import Flask,render_template

app = Flask (__name__,)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about_me():
    return render_template("about.html")


if __name__ == '__main__':

    app.run(use_reloader=True, port=5002)
