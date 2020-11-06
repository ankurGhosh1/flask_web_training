from flask_restful import Resource
from flask import g
from oa import github

from models.users import UserModel


class GithubLogin(Resource):
    @classmethod
    def get(cls):
        return github.authorize(callback="http://localhost:5000/login/github/authorized")


class GithubAuthorize(Resource):
    @classmethod
    def get(cls): 
        response = github.authorized_response()
        g.access_token = response['access_token']
        github_user = github.get('user')
        github_username = github_user.data['login']
        return github_username

        user = UserModel.find_by_username(github_username)

        if not User:
            user = UserModel(username= github_username, password= None)
            user.save_to_db

        access_token = create_access_token(identity = user.id,fresh = True)

        return {"access_token": access_token}, 200

