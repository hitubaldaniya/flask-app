from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False #To remove warnings
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["desc"]
        print(f'title: ' + title, f'description: ' + description)
        new_item = Todo(title=title, desc=description)
        db.session.add(new_item)
        db.session.commit()
    todo = Todo.query.all()
    return render_template('index.html', allTodo=todo)

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method == 'POST':
        title = request.form.get("title")
        desc = request.form.get("desc")
        # sno = int(request.form.get("id"))
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    else:
        todo = Todo.query.filter_by(sno=sno).first()
        return render_template('update.html', todo=todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    item = Todo.query.filter_by(sno=sno).first()
    db.session.delete(item)
    db.session.commit()
    return redirect('/')

@app.route('/about')
def products():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port= 8000)