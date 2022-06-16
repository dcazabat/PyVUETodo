from flask import Flask
from flask import render_template
from flask import url_for

app=Flask(__name__)

@app.route('/')
def index():
    title = 'PyVUEFlask'
    return render_template('index.html', title=title)


if __name__ == '__main__':
    app.run(debug=True)