from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index1():
    return render_template("index.html")


@app.route('/index')
def index2():
    return render_template("index.html")


@app.route('/visualization')
def visualization():
    return render_template("visualization.html")


@app.route('/csgokz')
def feature():
    return render_template("csgokz.html")


@app.route('/blog')
def blog():
    return render_template("blog.html")


@app.route('/elements')
def elements():
    return render_template("elements.html")


@app.route('/pricing')
def pricing():
    return render_template("pricing.html")


@app.route('/services')
def services():
    return render_template("services.html")


@app.route('/single-blog')
def single_blog():
    return render_template("single-blog.html")


if __name__ == '__main__':
    app.run()
