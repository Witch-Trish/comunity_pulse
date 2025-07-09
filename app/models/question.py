from app.models import db


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    questions = db.relationship('Question', back_populates='category', lazy=True)

    def __repr__(self):
        return f'Category {self.name}'

class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=True)

    category = db.relationship('Category', back_populates='questions', lazy=True)
    responses = db.relationship('Response', back_populates='question', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'Question {self.text}'


# class Statistic(db.Model):
#     __tablename__ = 'statistics'
#
#     question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), primary_key=True)
#     agree_count = db.Column(db.Integer, nullable=False, default=0)
#     disagree_count = db.Column(db.Integer, nullable=False, default=0)
#
#     def __repr__(self):
#         return f'Statistic for question {self.question_id}: {self.agree_count} agree, {self.disagree_count} disagree'