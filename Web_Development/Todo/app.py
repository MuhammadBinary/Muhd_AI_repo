from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///register.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    title2 = db.Column(db.String(100))
    percentage = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

    def __repr__(self):
        return f'Todo("{self.title}", "{self.percentage}")'


with app.app_context():
    db.create_all()


# @app.route("/plus", methods=["POST"])
# def plus():
#     return render_template("index.html")


@app.route("/")
def home():
    todo_list = db.session.query(Todo).all()
    return render_template("index.html", todo_list=todo_list)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    percentage = request.form.get("percentage")
    new_todo = Todo(percentage=percentage, title=title, complete=False)
    db.session.add(new_todo)
    # db.session.add(new_percentage)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/home2")
def home2():
    return render_template("another.html")


@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = db.session.query(Todo).filter(Todo.id == todo_id).first()
    print(todo)
    percentage = request.form.get("percentage")
    ans = todo.percentage
    return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = db.session.query(Todo).filter(Todo.id == todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)