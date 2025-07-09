from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from app.models.question import Category
from app.schemas.categories import CategorySchema, CategoryCreate, CategoryUpdate
from app.schemas.common import MessageResponse
from app.models import db


category_bp = Blueprint('categories', __name__, url_prefix='/categories')


@category_bp.route('/', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    # model_dump() conversion to standard dictionary
    serialized = [CategorySchema(id=c.id, name=c.name).model_dump() for c in categories]

    if categories:
        return jsonify(MessageResponse(message=serialized).model_dump()), 200
    else:
        return jsonify(MessageResponse(message="No categories found").model_dump()), 404


# creating a function to create a category with method "POST"
@category_bp.route('/', methods=['POST'])
def create_question():
    input_data = request.get_json() # get_json() returns dictionary

    try:
        category_data = CategoryCreate(**input_data)
        category = Category(name=category_data.name)
        db.session.add(category)
        db.session.commit()
        return jsonify(MessageResponse(message="Your category was created!").model_dump()), 201
    except ValidationError as e:
        return jsonify({'error': e.errors}), 400 # 400 indicates that the user did something wrong


# creating a function to get category by ID
@category_bp.route('/<int:id>', methods=['GET'])
def get_category(id):
    category = Category.query.get(id)

    if category:
        return jsonify(MessageResponse(message=CategorySchema(id=category.id,
                                                              name=category.name).model_dump()).model_dump())
    else:
        return jsonify(MessageResponse(message=f"No category with id {id} was found.").model_dump())


# creating a function to update a category by ID
@category_bp.route('/<int:id>', methods=['PUT'])
def update_category(id):
    category = Category.query.get(id)
    input_data = request.get_json()

    if category:
        try:
            updated_data = CategoryUpdate(**input_data)
            category.name = updated_data.name
            db.session.commit()
            return jsonify(MessageResponse(message=f"The category with id {id} was updated.").model_dump()), 200
        except ValidationError as e:
            return jsonify({'error': e.errors}), 400
    else:
        return jsonify(MessageResponse(message=f"No category with id {id} was found.").model_dump()), 404


# creating a function to delete a category by ID
@category_bp.route('/<int:id>', methods=['DELETE'])
def delete_category(id):
    category = Category.query.get(id)

    if category:
        db.session.delete(category)
        db.session.commit()
        return jsonify(MessageResponse(message=f"The category with id {id} was deleted.").model_dump()), 200
    else:
        return jsonify(MessageResponse(message=f"No category with id {id} was found.").model_dump()), 404