from pickletools import read_uint1
import re
from flask import Flask, session
from flask import render_template
from flask import url_for
from flask import jsonify
from flask import request
from flask import redirect

from config import Config
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

import models # Se importa aca porque sino genera un error al depender de la variable 'db'
from forms import TaskForm

@app.route('/')
def index():
    title = 'PyVUEFlask Todo App'
    tasks = models.Task.query.all()

    # Si es un Get que pide los datos retorna un JSON, sino rederiza el Index.html
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(tasks)
    
    return render_template('index.html', title=title)


@app.route('/add', methods=['POST'])
def add():
    user_input = request.get_json()

    form = TaskForm(data=user_input)

    if form.validate():
        task = models.Task(title=form.title.data)
        db.session.add(task)
        db.session.commit()

        return jsonify(task)

    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete():
    id = request.get_json().get('id')
    task = models.Task.query.filter_by(id=id).first()

    db.session.delete(task)
    db.session.commit()

    return jsonify({'result': 'Ok'}), 200


@app.route('/complete', methods=['POST'])
def complete():
    id = request.get_json().get('id')
    task = models.Task.query.filter_by(id=id).first()

    db.session.add(task)
    db.session.commit()

    return jsonify({'result': 'Ok'}), 200

if __name__ == '__main__':
    app.run(debug=True)