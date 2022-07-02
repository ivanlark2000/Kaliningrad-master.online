from flask import Flask
from flask import render_template, url_for

application = Flask(__name__)


@application.route("/")
def index():
    context = {
        "title": "Главная страница",
    }
    return render_template('index.html', context=context)


if __name__ == "__main__":
    application.run()