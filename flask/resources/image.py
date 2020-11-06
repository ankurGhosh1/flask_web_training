from flask_restful import Resource
from flask import request
from flask_uploads import UploadNotAllowed
from flask_jwt import jwt_required

from libs import image_helper
from schema.image import ImageSchema

image_schema = ImageSchema()

class Image(Resource):
    @jwt_required
    def post(self): 
        data = image_schema.load(request.files)
        user_id = get_jwt_identity()
        folder = f"user_{user_id}"
        try: 
            image_path = image_helper.save(data['image'], folder=folder)
            print(image_path)
            return {"messages": "image uploaded successfully"}
        except UploadNotAllowed:
            return {"message": "not allowed"}, 400
