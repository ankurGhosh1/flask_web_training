from flask_restful import Resource
from flask import request
from marshmallow import ValidationError

from models.users import UserModel
from schema.user import UserSchema


user_schema = UserSchema()

class UserRegister(Resource):
    @classmethod
    def post(cls):
        try:
            user = user_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400

        if UserModel.find_by_username(user.username):
            return {"message": "A user with that username already exists"}, 400

        user.save_to_db()

        return {"message": "User created successfully."}, 201