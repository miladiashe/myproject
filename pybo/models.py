from pybo import db

class Question(db.model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.string(200), nullable=False)
    contemt = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.Datetime(), nullable=False)