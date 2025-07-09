from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from app.models.question import Question, Category
from app.schemas.questions import QuestionCreate, QuestionSchema, QuestionUpdate
from app.schemas.common import MessageResponse
from app.models import db


questions_bp = Blueprint('questions', __name__, url_prefix='/questions')


@questions_bp.route('/', methods=['GET'])
def get_questions():
    questions = Question.query.all()
    # model_dump() conversion to standard dictionary
    serialized = [QuestionSchema.model_validate(q).model_dump() for q in questions]

    if questions:
        return jsonify(MessageResponse(message=serialized).model_dump()), 200
    else:
        return jsonify(MessageResponse(message="No questions found").model_dump()), 404


# creating a function to create a question with method "POST"
@questions_bp.route('/', methods=['POST'])
def create_question():
    input_data = request.get_json()

    try:
        question_data = QuestionCreate(**input_data)
    except ValidationError as e:
        return jsonify({'error': e.errors}), 400 # 400 indicates that the user did something wrong

    # Check if a category with this ID exists
    category = Category.query.get(question_data.category_id)
    if not category:
        return jsonify({'error': f"Category with id {question_data.category_id} does not exist."}), 400

    question = Question(text=question_data.text, category_id=question_data.category_id)
    db.session.add(question)
    db.session.commit()

    return jsonify(MessageResponse(message="Your question was created!").model_dump()), 201


# creating a function to get question by ID
@questions_bp.route('/<int:id>', methods=['GET'])
def get_question(id):
    question = Question.query.get(id)

    if question:
        return jsonify(MessageResponse(message=QuestionSchema.model_validate(question).model_dump()).model_dump()), 200
    else:
        return jsonify(MessageResponse(message=f"No question with id {id} was found.").model_dump()), 404


# creating a function to update a question by ID
@questions_bp.route('/<int:id>', methods=['PUT'])
def update_question(id):
    question = Question.query.get(id)
    input_data = request.get_json()

    if question:
        try:
            updated_data = QuestionUpdate(**input_data)
            question.text = updated_data.text
            db.session.commit()
            return jsonify(MessageResponse(message=f"The question with id {id} was updated.").model_dump()), 200
        except ValidationError as e:
            return jsonify({'error': e.errors}), 400
    else:
        return jsonify(MessageResponse(message=f"No question with id {id} was found.").model_dump()), 404


# creating a function to delete a question by ID
@questions_bp.route('/<int:id>', methods=['DELETE'])
def delete_question(id):
    question = Question.query.get(id)

    if question:
        db.session.delete(question)
        db.session.commit()
        return jsonify(MessageResponse(message=f"The question with id {id} was deleted.").model_dump()), 200
    else:
        return jsonify(MessageResponse(message=f"No question with id {id} was found.").model_dump()), 404