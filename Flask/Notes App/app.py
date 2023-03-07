from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///note.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Notes(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        title = request.form["title"]
        desc = request.form["desc"]
        note = Notes(title=title, desc=desc)
        db.session.add(note)
        db.session.commit()

    allNotes = Notes.query.all()
    return render_template('index.html', allNotes=allNotes)

@app.route('/read/<int:sno>', methods=['GET', 'POST'])
def read(sno):
    note = Notes.query.filter_by(sno=sno).first()
    return render_template('read.html',note=note)

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method == "POST":
        title = request.form["title"]
        desc = request.form["desc"]
        note = Notes.query.filter_by(sno=sno).first()
        note.title = title
        note.desc = desc
        db.session.add(note)
        db.session.commit()
        return redirect('/')

    note = Notes.query.filter_by(sno=sno).first()
    return render_template('update.html',note=note)

@app.route('/delete/<int:sno>')
def delete(sno):
    note = Notes.query.filter_by(sno=sno).first()
    db.session.delete(note)
    db.session.commit()
    return redirect("/")

@app.route('/create')
def create():
    return render_template('create.html', redirect="/")


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True, port=8000)
