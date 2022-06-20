from datetime import datetime
from flask import Flask
from flask import render_template
from flask import url_for
from flask import jsonify
from flask import request
from flask import redirect
from forms import TaskForm

from ast import stmt
from models import Task, engine

from sqlalchemy.orm import Session
from sqlalchemy import select

app=Flask(__name__)

@app.route('/')
def index():
    title = 'PyVUEFlask Todo App'

    with Session(engine) as session:
        stmt = select(Task).order_by(Task.date.desc())
        tasks = session.scalars(stmt)
        
        tasks_dict = {}
        format_data = "%d/%m/%y %H:%M:%S"
        for task in tasks:
            print(type(task.date))
            tasks_dict[str(task.id)] = {
                'id': task.id, 
                'title': task.title, 
                'date': task.date.strftime("%d/%m/%Y %H:%M:%S"), 
                'completed': task.completed
                }
        
        # Si es un Get que pide los datos retorna un JSON, sino rederiza el Index.html
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify(tasks_dict)
    
    return render_template('index.html', title=title)

@app.route('/add', methods=['POST'])
def add():
    user_input = request.get_json()

    form = TaskForm(data=user_input)

    if form.validate():
        with Session(engine) as session:
            task = Task(title=form.title.data)
            session.add(task)
            session.commit()

        return jsonify(task)

    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete():
    id_task = request.get_json().get('id')
    with Session(engine) as session:
        stmt = select(Task).where(Task.id == id_task)
        task_del = session.scalars(stmt).one()   
        session.delete(task_del)
        session.commit()

    return jsonify({'result': 'Ok'}), 200

@app.route('/complete', methods=['POST'])
def complete():
    id_task = request.get_json().get('id')
    with Session(engine) as session:
        stmt = select(Task).where(Task.id == id_task)
        task = session.scalars(stmt).one()   
        task.completed = not task.completed
        session.commit()

    return jsonify({'result': 'Ok'}), 200

if __name__ == '__main__':
    app.run(debug=True)