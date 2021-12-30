from flask import Blueprint, render_template

from pybo.models import Question
bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    question_list = Question.query.order_by(Question.create_date.desc())
    #질문 목록 데이터를 쿼리로 받아오는 것
    return render_template('question/question_list.html', question_list=question_list)

