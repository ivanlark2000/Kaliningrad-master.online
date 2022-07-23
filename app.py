from flask import Flask
from flask import render_template, url_for

application = Flask(__name__)


@application.route("/")
def index():
    context = {
        "title": "Главная страница",
    }
    return render_template('index.html', context=context)


@application.route('/about')
def about():
    context = {
        "title": "О нас",
    }
    return render_template('test.html', context=context)


@application.route('/price')
def price():
    context = {
        "title": "Цены",
    }
    return render_template('test.html', context=context)


@application.route('/numbers')
def numbers():
    context = {
        "title": "Цены",
    }
    return render_template('test.html', context=context)


@application.route('/test')
def test():
    context = {
        "title": "Тестовая страница",
    }
    return render_template('test.html', context=context)


@application.route('/fridge')
def fridge():
    context = {
        "title": "Холодильники",
    }
    return render_template('fridge.html', context=context)


@application.route('/washing')
def washing():
    context = {
        "title": "Стиральная машины",
    }
    return render_template('test.html', context=context)


@application.route('/hobs')
def hobs():
    context = {
        "title": "Варочные поверхности",
    }
    return render_template('test.html', context=context)


@application.route('/ovens')
def ovens():
    context = {
        "title": "Духовые шкафы",
    }
    return render_template('test.html', context=context)


@application.route('/dishwasheres')
def dishwasheres():
    context = {
        "title": "Посудомоечные машины",
    }
    return render_template('test.html', context=context)


@application.route('/drying_machines')
def drying_machines():
    context = {
        "title": "Сушильные машины",
    }
    return render_template('test.html', context=context)


if __name__ == "__main__":
    application.run()