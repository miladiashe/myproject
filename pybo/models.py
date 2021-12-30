from pybo import db

class Question(db.model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.string(200), nullable=False)
    contemt = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.Datetime(), nullable=False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Foreignkey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    contemt = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.Datetime(), nullable=False)