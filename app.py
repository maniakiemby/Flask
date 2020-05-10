"""stworzyć formularz, który po dodaniu wyświetla wpis,
 a później kolejny wpis"""

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post', methods=['POST'])
def post():
    title = request.form.get('title')
    description = request.form.get('description')
    return render_template('hello.html', title=title, description=description)
