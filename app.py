"""stworzyć formularz, który po dodaniu wyświetla wpis,
 a później kolejny wpis"""

from flask import Flask, render_template, request


app = Flask(__name__)
list_items = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post', methods=['POST'])
def post():
    title = request.form.get('title')
    description = request.form.get('description')
    if len(title) and len(description) > 0:
        list_items.append([title, description])
    return render_template('index.html', list_items=list_items)

