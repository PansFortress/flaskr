from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CsrfProtect
from forms import NameForm


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'some random string'
    Bootstrap(app)
    # CsrfProtect(app)

    return app

app = create_app()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("base.html")


@app.route('/form', methods=['GET', 'POST'])
def form():
    form = NameForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
        return render_template("base_form.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
